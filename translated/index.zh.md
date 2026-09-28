# CS146S：现代软件开发者（The Modern Software Developer）——离线镜像

斯坦福大学 · 2025 年秋季 · 讲师：Mihail Eric

离线镜像说明 —— 这是 themodernsoftware.dev 的本地保存版本，抓取于 2026 年 4 月 2 日。文章页面保存在 `pages/` 文件夹，PDF 文档保存在 `pdfs/` 文件夹。（YouTube）视频链接与 Google 幻灯片仍保留为外部链接。

## 课程简介

过去几年中，大语言模型为软件开发引入了革命性的新范式。传统的软件开发生命周期正被 AI 自动化在每个环节上重塑，这也引出一个问题：下一代软件工程师应当如何利用这些进步，把生产力提升 10 倍，并为自己的职业生涯做好准备？

本课程将说明：现代 AI 工具不仅能提升开发者生产力，还能让软件工程走向更广泛的人群。我们会展示软件开发如何从「0 到 1 的代码创作」演变为「规划 → 用 AI 生成 → 修改 → 重复」的迭代式工作流。学生将同时掌握传统软件工程难题背后的理论，以及当今解决这些难题的前沿 AI 工具。

通过动手工程任务，以及来自业界先驱（他们正在打造这些革命性工具）的分享，你将获得 AI 辅助开发、自动化测试、智能文档与安全漏洞检测方面的实践经验。到课程结束时，你将清晰地理解如何把最先进的 LLM 模型整合进复杂的开发工作流，并避开常见陷阱。

### 单元数

3 个单元

### 先修要求

具有相当于 CS111 的编程经验；建议修过 CS221/229。

### 形式

每周讲座、动手编码环节，以及来自业界的客座讲者。最终项目用于展示现代开发实践。

### 目标

掌握现代开发工具，理解 AI 辅助编码，学习自动化测试与部署，探索新兴软件趋势。

### 教室

420-041

### 答疑时间（Office Hours）

Mihail Eric：周五 12:00–12:30
Febie Lin：周三 9:00–11:00（Huang 地下一层）

### 作业截止时间

日历（Google 表格）

## 团队

- Mihail Eric —— 讲师
- Febie Lin —— 助教
- Brent Ju —— 助教

## 课程安排

### 第 1 周：编码 LLM 与 AI 开发导论

**主题**
- 课程事务说明
- LLM 到底是什么
- 如何有效地写提示词

**阅读**
- Deep Dive into LLMs（深入理解 LLM）
- Prompt Engineering Overview（提示工程概览）
- Prompt Engineering Guide（提示工程指南）
- AI Prompt Engineering: A Deep Dive（AI 提示工程深入探讨）
- How OpenAI Uses Codex（OpenAI 如何使用 Codex）

**作业**
- LLM Prompting Playground（LLM 提示词演练场）

**讲座**
- 周一 9/22：导论与 LLM 是如何制造的 —— 幻灯片
- 周五 9/26：面向 LLM 的强大提示技巧 —— 幻灯片

### 第 2 周：编码智能体的解剖结构

**主题**
- 工具使用与函数调用
- MCP（模型上下文协议）

**阅读**
- MCP Introduction（MCP 简介）
- Sample MCP Server Implementations（MCP 服务器实现示例）
- MCP Server Authentication（MCP 服务器认证）
- MCP Server SDK
- MCP Registry（MCP 注册表）
- MCP Food-for-Thought（关于 MCP 的思考）

**作业**
- AI IDE 中的第一步

**讲座**
- 周一 9/29：从零构建编码智能体 —— 幻灯片、已完成的练习
- 周五 10/3：构建自定义 MCP 服务器 —— 幻灯片、已完成的练习

### 第 3 周：AI IDE

**主题**
- 上下文管理与代码理解
- 面向智能体的 PRD（产品需求文档）
- IDE 集成与扩展

**阅读**
- Specs Are the New Source Code（规格说明就是新的源代码）
- How Long Contexts Fail（长上下文为何失效）
- Devin: Coding Agents 101（Devin：编码智能体入门）
- Getting AI to Work In Complex Codebases（让 AI 在复杂代码库中工作）
- How FAANG Vibe Codes（FAANG 如何做氛围编程）
- Writing Effective Tools for Agents（为智能体编写有效的工具）

**作业**
- 构建自定义 MCP 服务器

**讲座**
- 周一 10/6：AI IDE 深入解析 —— 幻灯片
- 周五 10/10：嘉宾：Silas Alberti（Cognition）—— 幻灯片
- 资源：设计文档模板

### 第 4 周：Claude Code 与智能体式编码

**主题**
- Claude Code 的架构与内部机理
- 智能体式编码工作流
- 面向智能体的上下文工程

**阅读**
- How Anthropic Uses Claude Code（Anthropic 如何使用 Claude Code）
- Claude Best Practices（Claude 最佳实践）
- Awesome Claude Agents
- Super Claude
- Good Context Good Code（好上下文，好代码）
- Peeking Under the Hood of Claude Code（一窥 Claude Code 内部）

**作业**
- 用 Claude Code 编码

**讲座**
- 周一 10/13：Claude Code 深入解析 —— 幻灯片
- 周五 10/17：嘉宾：Boris Cherney（Claude Code）—— 幻灯片

### 第 5 周：Warp 与 AI 终端

**主题**
- AI 原生终端开发
- 智能体式开发工作流

**阅读**
- Warp vs Claude Code
- How Warp Uses Warp to Build Warp（Warp 如何用 Warp 构建 Warp）
- Warp University（Warp 大学）

**作业**
- 用 Warp 做智能体式开发

**讲座**
- 周一 10/20：Warp 与 AI 终端 —— 幻灯片
- 周五 10/24：嘉宾：Zach Lloyd（Warp）—— 幻灯片（Figma）

### 第 6 周：AI 安全与漏洞检测

**主题**
- 安全测试（SAST 与 DAST）
- 提示注入攻击
- AI 辅助漏洞检测
- OWASP Top 10

**阅读**
- SAST vs DAST
- Copilot Remote Code Execution via Prompt Injection（通过提示注入实现 Copilot 远程代码执行）
- Finding Vulnerabilities in Modern Web Apps Using Claude Code and OpenAI Codex（用 Claude Code 与 OpenAI Codex 发现现代 Web 应用的漏洞）
- Agentic AI Threats: Identity Spoofing and Impersonation Risks（智能体 AI 威胁：身份伪造与冒充风险）
- OWASP Top Ten: The Leading Web Application Security Risks（OWASP 十大：最主要的 Web 应用安全风险）
- Context Rot: Understanding Degradation in AI Context Windows（上下文腐化：理解 AI 上下文窗口中的退化）
- Vulnerability Prompt Analysis with O3（用 O3 做漏洞提示分析）

**作业**
- 编写安全的 AI 代码

**讲座**
- 周一 10/27：AI 安全深入解析 —— 幻灯片
- 周五 10/31：嘉宾：Isaac Evans（Semgrep）

### 第 7 周：AI 驱动的代码评审

**主题**
- 代码评审最佳实践
- AI 辅助代码评审
- 自动化评审工具

**阅读**
- Code Reviews: Just Do It（代码评审：去做就对了）
- How to Review Code Effectively（如何高效评审代码）
- AI-Assisted Assessment of Coding Practices in Modern Code Review（现代代码评审中编码实践的 AI 辅助评估）
- AI Code Review Implementation Best Practices（AI 代码评审落地最佳实践）
- Code Review Essentials for Software Teams（软件团队的代码评审要点）
- Lessons from Millions of AI Code Reviews（来自数百万次 AI 代码评审的经验）

**作业**
- 代码评审练习

**讲座**
- 周一 11/3：AI 代码评审深入解析 —— 幻灯片
- 周五 11/7：嘉宾：Tomas Reimers（Graphite）—— 幻灯片

### 第 8 周：全栈 AI 开发与部署

**主题**
- 多技术栈 Web 应用开发
- AI 辅助的部署流水线

**作业**
- 多技术栈 Web 应用构建

**讲座**
- 周一 11/10：全栈 AI 开发 —— 幻灯片
- 周五 11/14：嘉宾：Gaspar Garcia（Vercel）—— 幻灯片

### 第 9 周：SRE、可观测性与智能体值班

**主题**
- 站点可靠性工程（SRE）基础
- 可观测性与监控
- 值班工程中的 AI 智能体
- 多智能体系统

**阅读**
- Introduction to Site Reliability Engineering（站点可靠性工程导论）
- Observability Basics You Should Know（你应该了解的可观测性基础）
- Kubernetes Troubleshooting with AI（用 AI 排查 Kubernetes 问题）
- Your New Autonomous Teammate / Benefits of Agentic AI in On-call Engineering（你的新自主队友／智能体 AI 在值班工程中的价值）
- Role of Multi Agent Systems in Making Software Engineers AI-native（多智能体系统如何让软件工程师成为 AI 原生）

**讲座**
- 周一 11/17：SRE 与 AI 可观测性 —— 幻灯片
- 周五 11/21：嘉宾：Mayank Agarwal 与 Milind Ganjoo（Resolve）—— 幻灯片

### 第 10 周：AI 在软件工程中的未来

**主题**
- AI 辅助开发的未来趋势
- 行业视角与职业影响
- 最终项目展示

**讲座**
- 周一 12/1：嘉宾：Martin Casado（a16z）
- 周五 12/5：最终项目展示

## 常见问题（FAQ）

### 这门课适合谁？

本课程面向有编程经验（相当于 CS111）的学生，他们希望学习如何利用现代 AI 工具大幅提升软件开发生产力。建议（但非必须）修过 CS221/229。

### 在这门课里我会做出什么？

学生将完成每周的动手作业，涵盖 LLM 提示、MCP 服务器开发、AI IDE 使用、Claude Code 工作流、安全分析、代码评审自动化以及全栈 Web 应用。课程以最终项目收尾，用于展示现代开发实践。

### 我们会用到哪些工具？

课程涉及一系列 AI 开发工具，包括 Claude Code、Warp 终端、Cursor/Windsurf IDE、Semgrep、Graphite 与 Vercel。我们还会使用模型上下文协议（MCP）以及各类 LLM API。

### 成绩如何评定？

成绩依据每周作业、课堂讨论参与度以及最终项目。具体截止时间见作业日历。

### 讲座有录像吗？

请向课程团队确认录像是否提供。每次讲座的幻灯片已在上方教学大纲中给出链接。

### 如何联系教学团队？

- Mihail Eric：答疑时间 周五 12:00–12:30
- Febie Lin：答疑时间 周三 9:00–11:00（Huang 地下一层）
- Brent Ju：联系方式见课程 Slack/Ed。
