#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_batches.py — 翻译分批（管线第 3 步）
把抽取后的正文按「词数上限」装箱，产出 batches.json：
每个批次是一组待翻译文档，交给一个翻译单元（AI 批量翻译 / MT 接口）处理。
装箱规则与文档数量无关 —— 换一门课的资料，同样流程可直接复用。

用法:
  python3 make_batches.py --extracted ../extracted --out ../batches.json --limit 8500
"""
import argparse
import json
import os


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--extracted", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int, default=8500, help="每批词数上限")
    args = ap.parse_args()

    with open(os.path.join(args.extracted, "_manifest.json"), encoding="utf-8") as fh:
        manifest = json.load(fh)

    docs = [d for d in manifest["docs"] if d["words"] > 0]
    docs.sort(key=lambda d: -d["words"])

    batches, cur, cur_words = [], [], 0
    for d in docs:
        if cur and cur_words + d["words"] > args.limit:
            batches.append(cur)
            cur, cur_words = [], 0
        cur.append(d)
        cur_words += d["words"]
    if cur:
        batches.append(cur)

    out = {
        "limit_words": args.limit,
        "source_total_words": sum(d["words"] for d in docs),
        "batch_count": len(batches),
        "batches": [
            {
                "batch_id": f"B{i:02d}",
                "words": sum(d["words"] for d in b),
                "docs": [{"slug": d["slug"], "words": d["words"], "source": d["source"]} for d in b],
            }
            for i, b in enumerate(batches, 1)
        ],
    }
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)

    for b in out["batches"]:
        print(f"{b['batch_id']}  words={b['words']:>6}  docs={len(b['docs'])}  "
              + ", ".join(d["slug"] for d in b["docs"]))
    print(f"\n共 {out['batch_count']} 批 / {out['source_total_words']} 词（上限 {args.limit} 词/批）")


if __name__ == "__main__":
    main()
