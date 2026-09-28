#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_text.py — 课程资料正文抽取（管线第 2 步）
把 index.html / pages/*.html / *.pdf 抽取为「带结构标记」的纯文本，
供后续分段翻译使用。可复跑：换一门课的资料目录，同样流程可再次产出。

用法:
  python3 extract_text.py --src ../source --out ../extracted [--pdf]

输出:
  <out>/<slug>.en.md    正文（Markdown 化：标题/段落/列表/表格）
  <out>/_manifest.json  文件清单 + 字符数/词数统计
"""
import argparse
import json
import os
import re
import sys
from html.parser import HTMLParser

SKIP_TAGS = {"script", "style", "noscript", "svg", "head", "nav", "footer", "aside", "form", "button"}
BLOCK_TAGS = {"p", "li", "td", "th", "pre", "blockquote", "div", "section", "article", "tr"}
HEAD_LEVEL = {"h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### ", "h5": "##### ", "h6": "###### "}


class HtmlToMarkdown(HTMLParser):
    """轻量 HTML -> Markdown：只保留正文块，丢弃脚本/样式/导航。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.skip_depth = 0
        self.buf = []
        self.in_pre = False

    # --- helpers ---
    def _flush(self, prefix=""):
        text = re.sub(r"[ \t\u00a0]+", " ", " ".join(self.buf)).strip()
        self.buf = []
        if text:
            self.parts.append(prefix + text)

    # --- parser callbacks ---
    def handle_starttag(self, tag, attrs):
        if tag in SKIP_TAGS:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag in HEAD_LEVEL:
            self._flush()
            self._pending_head = tag
        elif tag in BLOCK_TAGS:
            self._flush()
        elif tag == "br":
            self.buf.append(" ")
        elif tag == "code":
            self.buf.append("`")
        elif tag == "pre":
            self.in_pre = True

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if self.skip_depth:
            return
        if tag in HEAD_LEVEL:
            self._flush(HEAD_LEVEL[tag])
        elif tag in BLOCK_TAGS:
            self._flush()
        elif tag == "code":
            self.buf.append("`")
        elif tag == "pre":
            self.in_pre = False
            self._flush()

    def handle_data(self, data):
        if self.skip_depth or not data.strip():
            return
        self.buf.append(data if self.in_pre else data.replace("\n", " "))

    def result(self):
        self._flush()
        text = "\n\n".join(self.parts)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()


def extract_html(path):
    with open(path, encoding="utf-8", errors="ignore") as fh:
        raw = fh.read()
    p = HtmlToMarkdown()
    p.feed(raw)
    return p.result()


def extract_pdf(path):
    try:
        from pypdf import PdfReader
    except ImportError:
        raise SystemExit("需要 pypdf：uv pip install --python $COGSEED_PYTHON pypdf")
    reader = PdfReader(path)
    chunks = []
    for i, page in enumerate(reader.pages, 1):
        txt = (page.extract_text() or "").strip()
        if txt:
            chunks.append(f"<!-- page {i} -->\n{txt}")
    return "\n\n".join(chunks)


def slugify(rel):
    base = rel.replace(os.sep, "__")
    base = re.sub(r"\.(html?|pdf|md)$", "", base, flags=re.I)
    base = re.sub(r"[^0-9A-Za-z._-]+", "-", base)
    return base.strip("-").lower()[:80] or "doc"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--pdf", action="store_true", help="同时抽取 PDF")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    targets = []
    for root, _dirs, files in os.walk(args.src):
        for name in sorted(files):
            ext = os.path.splitext(name)[1].lower()
            if ext in (".html", ".htm"):
                targets.append(os.path.join(root, name))
            elif ext == ".pdf" and args.pdf:
                targets.append(os.path.join(root, name))

    manifest = []
    for path in sorted(targets):
        rel = os.path.relpath(path, args.src)
        slug = slugify(rel)
        try:
            text = extract_pdf(path) if path.lower().endswith(".pdf") else extract_html(path)
        except Exception as exc:  # noqa: BLE001
            print(f"[ERR ] {rel}: {type(exc).__name__} {exc}", file=sys.stderr)
            continue
        out_path = os.path.join(args.out, slug + ".en.md")
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
        words = len(re.findall(r"[A-Za-z0-9'\-]+", text))
        manifest.append({"source": rel, "slug": slug, "chars": len(text), "words": words})
        print(f"[OK  ] {rel} -> {slug}.en.md  chars={len(text)} words={words}")

    with open(os.path.join(args.out, "_manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(
            {
                "source_root": os.path.abspath(args.src),
                "doc_count": len(manifest),
                "total_chars": sum(m["chars"] for m in manifest),
                "total_words": sum(m["words"] for m in manifest),
                "docs": manifest,
            },
            fh,
            ensure_ascii=False,
            indent=2,
        )
    print(f"\n合计 {len(manifest)} 篇，{sum(m['chars'] for m in manifest)} 字符 / {sum(m['words'] for m in manifest)} 词")


if __name__ == "__main__":
    main()
