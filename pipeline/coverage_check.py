#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""coverage_check.py — 覆盖率核算（管线第 5 步）
按 translation_plan.json 统计：已产出译文的单元数 / 词数 / 覆盖率。
判定标准：输出文件存在且中文正文字数 >= 源词数 * 0.6 视为该单元已覆盖。
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLAN = os.path.join(ROOT, "pipeline", "translation_plan.json")
plan = json.load(open(PLAN, encoding="utf-8"))
units = plan.get("units", plan) if isinstance(plan, dict) else plan

CJK = re.compile(r"[\u4e00-\u9fff]")
total_w = sum(u["words"] for u in units)
done_w = 0
done_u = 0
rows = []
for u in units:
    out = u["out"]
    ok = False
    cjk = 0
    if os.path.exists(out):
        txt = open(out, encoding="utf-8").read()
        cjk = len(CJK.findall(txt))
        need = max(30, int(u["words"] * 0.6))
        ok = cjk >= need
    if ok:
        done_w += u["words"]; done_u += 1
    rows.append((u["id"], u["words"], cjk, "OK" if ok else "--"))

print("单元 %d/%d 已覆盖｜词数 %d/%d｜覆盖率 %.1f%%" % (
    done_u, len(units), done_w, total_w, 100.0 * done_w / total_w))
if "-v" in sys.argv:
    for r in rows:
        print("  %-52s %6d 词  %7d 汉字  %s" % r)
