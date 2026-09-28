#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
split_plan.py — 翻译单元规划（管线第 3.5 步）
把抽取后的正文按词数上限切分为可独立翻译的单元；
超过 MAX_WORDS 的文档按空行段落切分，保证单单元不超过上限，
避免单次翻译输出被截断。产出 pipeline/translation_plan.json。
可复跑：换一门课的资料，同样流程可再次产出。
"""
import json, os, re

MAX_WORDS = 4200
BASE = os.path.abspath(os.path.dirname(__file__) + "/..")
SRC = os.path.join(BASE, "extracted")
PARTS = os.path.join(BASE, "extracted_parts")
OUT = os.path.join(BASE, "translated")
os.makedirs(PARTS, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

man = json.load(open(os.path.join(SRC, "_manifest.json"), encoding="utf-8"))
plan = []
for d in man["docs"]:
    slug, words = d["slug"], d.get("words", 0)
    p = os.path.join(SRC, slug + ".en.md")
    if not os.path.exists(p):
        continue
    text = open(p, encoding="utf-8").read()
    if words <= MAX_WORDS:
        plan.append({"id": slug, "src": p, "out": os.path.join(OUT, slug + ".zh.md"),
                     "words": words, "part": 1, "parts": 1})
        continue
    paras = re.split(r"\n\s*\n", text)
    chunks, cur, cw = [], [], 0
    for para in paras:
        w = len(para.split())
        if cw + w > MAX_WORDS and cur:
            chunks.append("\n\n".join(cur)); cur, cw = [para], w
        else:
            cur.append(para); cw += w
    if cur:
        chunks.append("\n\n".join(cur))
    for i, ch in enumerate(chunks, 1):
        sp = os.path.join(PARTS, f"{slug}.part{i:02d}.en.md")
        open(sp, "w", encoding="utf-8").write(ch)
        plan.append({"id": f"{slug}.part{i:02d}", "src": sp,
                     "out": os.path.join(OUT, f"{slug}.part{i:02d}.zh.md"),
                     "words": len(ch.split()), "part": i, "parts": len(chunks)})

json.dump(plan, open(os.path.join(BASE, "pipeline", "translation_plan.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(f"翻译单元：{len(plan)} 个｜总词数：{sum(u['words'] for u in plan)}")
for u in plan:
    print(f"  {u['id']:<58} {u['words']:>6} 词  {u['part']}/{u['parts']}")
