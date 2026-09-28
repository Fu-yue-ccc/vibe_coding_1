# 翻译规范（TRANSLATION BRIEF）

本文件是 C1「课程资料获取与翻译」译文的**唯一规范**。任何单元译文都必须逐条遵守，
以保证「术语全文一致」这一验收项。

## 一、总体要求

1. **完整**：源文件里的每一段正文都要译出，不得省略、概括、跳段或写"略"。宁长不短。
2. **准确**：忠实原意，不增删观点、不改数字与专有名词；原文的列表、表格、代码块、引用块
   结构一律保留。
3. **术语一致**：技术术语一律按下方《术语表》统一译法；表中标注"首现双写"的，
   在文中**首次出现**处写成"中文（English）"，其后统一用中文。
4. **不译项**：代码块内容、命令、文件名、URL、路径、API 名、模型名、产品名
   （Claude Code / Cursor / Windsurf / Semgrep / Graphite / Vercel / Warp / Kubernetes / Pod 等）、
   `Token`、`KSTAR` 保持原样。
5. **文体**：技术说明文，书面简体中文；长句可断句，但不改逻辑关系。
6. **标题**：各级 Markdown 标题都要翻译，层级符号（# 的个数）保持不变。
7. **图片/链接**：`![alt](url)` 译 alt 文本，url 不动；链接文字翻译。

## 二、输出文件格式

每个输出文件以如下头部开始（把 `{原文}` 换成实际源文件名，`{来源}` 换成来源网址或"本地材料"）：

```
# {译名标题}

> 译自：{原文}　｜　来源：{来源}

<!-- machine-translated: zh-CN | unit: {单元id} -->
```

正文之后，若原文为长文（>1500 词），在末尾追加一段「**要点回顾**」（5–8 条 bullet），
概括该文的核心结论——这是中文读者的导航锚点。

## 三、汉字量红线（覆盖核算用）

覆盖率脚本判定：输出文件汉字数 ≥ 源词数 × 0.6 才算该单元已覆盖。
因此每个单元译文的中文字符数**必须 ≥ 源词数 × 0.75**（留安全余量）。
若译文明显偏短，说明有省略，必须补全。

## 四、术语表（77 条，必须严格遵守）

| 术语原文 | 统一译法 | 备注/首现译法 |
|---|---|---|
| Vibe Coding | 氛围编程（Vibe Coding） | 首现双写，后文统一用"氛围编程" |
| Scaffolding | 脚手架 | 指先让 AI 搭出可运行骨架 |
| Context Engineering | 上下文工程 | 区别于 Prompt Engineering |
| Prompt Engineering | 提示工程 | |
| Context Window | 上下文窗口 | |
| Long Context | 长上下文 | |
| Context Rot | 上下文腐化 | 指长上下文下模型质量衰减 |
| Coding Agent | 编程智能体 | 不译"编码代理" |
| Agentic | 智能体化的 | 如 agentic workflow → 智能体化工作流 |
| AI IDE | AI 集成开发环境（AI IDE） | 首现双写 |
| LLM | 大语言模型 | 首现 LLM（大语言模型），后文可用 LLM |
| Foundation Model | 基础模型 | |
| Model Context Protocol | 模型上下文协议（MCP） | 首现双写 |
| MCP Server | MCP 服务器 | |
| MCP Client | MCP 客户端 | |
| MCP Registry | MCP 注册表 | |
| Tool Use | 工具调用 | |
| Function Calling | 函数调用 | |
| System Prompt | 系统提示词 | |
| Few-shot | 少样本 | |
| Zero-shot | 零样本 | |
| Chain of Thought | 思维链 | |
| Token | Token | 不译；如"上下文长度 200K Token" |
| Temperature | 温度参数 | |
| Hallucination | 幻觉 | |
| Prompt Injection | 提示注入 | 安全语境 |
| Jailbreak | 越狱攻击 | |
| Sandbox | 沙箱 | |
| Guardrails | 护栏 | |
| Human-in-the-loop | 人类在环 | |
| Code Review | 代码评审 | |
| Pull Request | 拉取请求（PR） | 首现双写 |
| Diff | 差异（diff） | 首现双写 |
| SAST | 静态应用安全测试（SAST） | 首现双写 |
| DAST | 动态应用安全测试（DAST） | 首现双写 |
| OWASP Top 10 | OWASP 十大安全风险 | |
| Supply Chain Attack | 供应链攻击 | |
| Vulnerability | 漏洞 | |
| Exploit | 漏洞利用 | |
| CI/CD | 持续集成/持续交付（CI/CD） | 首现双写 |
| Regression Test | 回归测试 | |
| Lint | 静态检查（lint） | 首现双写 |
| Refactor | 重构 | |
| Technical Debt | 技术债 | |
| SRE | 站点可靠性工程（SRE） | 首现双写 |
| Observability | 可观测性 | |
| Tracing | 链路追踪 | |
| Metrics | 指标 | |
| Logging | 日志 | |
| On-call | 值班 | |
| Runbook | 运行手册 | |
| Postmortem | 事故复盘 | |
| Incident | 事故 | |
| Kubernetes | Kubernetes | 不译（保留原名） |
| Pod | Pod | 不译 |
| Rollout | 发布推进（rollout） | 首现双写 |
| Latency | 时延 | |
| Throughput | 吞吐量 | |
| Multi-agent System | 多智能体系统 | |
| Orchestrator | 编排器 | |
| Sub-agent | 子智能体 | |
| RAG | 检索增强生成（RAG） | 首现双写 |
| Embedding | 嵌入向量 | |
| Vector Database | 向量数据库 | |
| Benchmark | 基准测试 | |
| Rubric | 评分标准（rubric） | 首现双写 |
| AAR | 事后复盘（AAR） | 首现双写 |
| KSTAR | KSTAR | 不译 |
| Second Brain | 第二大脑 | |
| Deployment | 部署 | |
| Documentation | 文档 | |
| Determinism | 确定性 | |
| Trade-off | 取舍 | |
| Spec | 规格说明（spec） | 首现双写 |
| PRD | 产品需求文档（PRD） | 首现双写 |
| Terminal | 终端 | |
| Autocomplete | 自动补全 | |
