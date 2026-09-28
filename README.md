# Stanford CS146S「Vibe Coding」课程中文资料包

> 挑战 C1：课程资料获取与翻译 ｜ 资料包版本 v1.0 ｜ 更新日期 2026-09-28
> 一手来源：Stanford CS146S *The Modern Software Developer*（2025，公开课程站点 `themodernsoftware.dev`）

## 一、这个包是什么

一句话：把一门课的全部公开资料**抓取 → 归档 → 抽取 → 术语统一 → 机器翻译 → 人工校对**，产出可复用的中文课程资料包，并让下一个人能按本文零成本复跑。

覆盖两类一手来源：

- **课程站点正文**：`source/CS146S_offline/pages/`（31 个页面）与站点导出 `source/CS146S_offline/site/`
- **课程讲义 PDF**：`source/CS146S_offline/pdfs/`（3 份）

合计 **44 个翻译单元、96,551 英文词**；**全部 44 个单元已完成中译并通过覆盖率核算（`coverage_check.py` 全表 OK，覆盖率 100.0%）**。

## 二、目录结构

```
C1_课程资料翻译/
├── README.md              ← 本文件：资料包说明（交付物）
├── AI日志.md              ← AI 协作日志（交付物）
├── AAR.md                 ← 七维 AAR 复盘（交付物）
├── 拿来说明.md            ← ≥3 个「拿来说明」（交付物）
├── source/                ← 一手原始资料（原样归档，未改动）
│   ├── CS146S_offline/
│   │   ├── site/          站点静态导出（themodernsoftware.dev）
│   │   ├── pages/         页面正文（31 个页面）
│   │   ├── pdfs/          讲义 PDF（3 份）
│   │   ├── assets/        页面引用的图片与附件
│   │   └── slides_info/   讲义元信息
│   └── Vibe_Coding_Playbook.pdf
├── extracted/             ← 抽取出的英文 Markdown（每个来源一份）
├── extracted_parts/       ← 超长文档切分后的分片＝翻译单元
├── extracted_playbook/    ← Playbook 抽取结果
├── translated/            ← 【核心产物】中文译文 translated/<单元id>.zh.md
├── pipeline/              ← 可复跑流水线
│   ├── TRANSLATION_BRIEF.md   翻译规范（风格 / 格式 / 不译项）
│   ├── glossary.tsv           术语表（77 条）
│   ├── extract_text.py        抽取：原始资料 → 英文 Markdown
│   ├── split_plan.py          切分：长文 → 翻译单元（≤4000 词）+ translation_plan.json
│   ├── make_batches.py        打包：单元 → 批次 batches.json
│   └── coverage_check.py      质检：覆盖率 / 漏译核算
└── batches.json           ← 批次清单
```

## 三、翻译流水线（五步，可复跑）

| 步骤 | 命令 | 作用 |
|---|---|---|
| 1 抽取 | `python3 pipeline/extract_text.py` | PDF / 网页 → 纯英文 Markdown，保留标题层级与表格 |
| 2 规划 | `python3 pipeline/split_plan.py` | 超长文档按 4000 词切分为单元，生成 `translation_plan.json` |
| 3 打包 | `python3 pipeline/make_batches.py` | 单元聚合为批次，输出 `batches.json` |
| 4 翻译 | 按批次逐单元翻译 → `translated/<id>.zh.md` | 依据 `TRANSLATION_BRIEF.md` + `glossary.tsv` 执行 |
| 5 质检 | `python3 pipeline/coverage_check.py -v` | 逐单元核算译文汉字数，标出未覆盖 / 疑似漏译 |

**换一门课怎么复用**：把新课程资料放进 `source/`，依次执行步骤 1–3；术语表按新课程主题增补；重复步骤 4–5。脚本不包含本课程专有内容，换源可复用。

## 四、术语一致性

- 术语表 `pipeline/glossary.tsv` 共 **77 条**（验收要求 ≥50 条），覆盖 Vibe Coding、Scaffolding、Context Engineering、Prompt Engineering、MCP 系列、代码评审、应用安全、SRE 等主题。
- 规则：同一术语全文同一译法；标注「首现双写」的条目（如 `Vibe Coding → 氛围编程（Vibe Coding）`）首次出现写中文＋英文，其后统一用中文。
- 不译项：代码块内容、命令行、文件名、路径、URL、API 名与模型名、产品名（Claude Code / Cursor / Windsurf / Warp / Kubernetes / Pod 等），以及 `Token`、`KSTAR`。

## 五、覆盖率核算方法

`translation_plan.json` 记录每个单元的源词数；`coverage_check.py` 的判定线为 **译文汉字数 ≥ 源词数 × 0.6** 记为该单元已覆盖。翻译规范要求实际译到 **≥ 源词数 × 0.75** 留安全余量，因此核算通过即意味着没有大段省略。运行 `python3 pipeline/coverage_check.py -v` 可查看逐单元明细与总完成度；本包最终核算结果为 **44/44 单元、96,551/96,551 词、100.0%**，全表 OK。

## 六、怎么用这个包

1. **只要成品**：进 `translated/`，文件名与原文一一对应；`index.zh.md` 是总目录与导航页。
2. **要复核质量**：英文原文在 `extracted/`（或 `extracted_parts/`），可逐段对照。
3. **要复跑流水线**：按第三节表格顺序执行；修改术语表即全局生效。
4. **要续译**：`python3 pipeline/coverage_check.py -v` 会列出未完成单元，按第 4 步补译即可。

## 七、已知缺口

- **视频字幕**：本课程公开材料以站点正文与讲义 PDF 为主，未包含视频字幕文件；若后续取得字幕，按同一流程追加即可。
- **图片与附件**：`assets/` 内的资源按原样归档，未逐张译注图内文字。
- **动态页面**：站点交互组件以静态导出为准，个别动态数据不体现。
