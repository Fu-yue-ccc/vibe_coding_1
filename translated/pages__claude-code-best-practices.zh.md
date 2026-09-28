# Claude Code 概览

> 译自：pages__claude-code-best-practices.en.md ｜ 来源：本地材料

<!-- machine-translated: zh-CN | unit: pages__claude-code-best-practices -->

跳转到主要内容

Claude Code 文档首页

快速开始

使用 Claude Code 构建

部署

管理

配置

参考

资源

##### 快速开始

概览

快速上手

更新日志

##### 核心概念

Claude Code 如何工作

扩展 Claude Code

探索 .claude 目录

探索上下文窗口

##### 使用 Claude Code

存储指令与记忆

权限模式

常见工作流

最佳实践

##### 平台与集成

概览

远程控制

Chrome 扩展（beta）

计算机使用（预览）

Visual Studio Code

JetBrains IDE

Slack 中的 Claude Code

快速开始

你可以做什么

在各处使用 Claude Code

后续步骤

快速开始

# Claude Code 概览

Claude Code 是一款智能体化编程工具，可读取你的代码库、编辑文件、运行命令，并与你的开发工具集成。它可用于终端、IDE、桌面应用与浏览器。

Claude Code 是一款由 AI 驱动的编程助手，帮助你构建功能、修复缺陷并自动化开发任务。它能理解你的整个代码库，并可跨多个文件与工具协同完成工作。

​

## 快速开始

选择你的环境开始使用。多数入口需要 Claude 订阅或 Anthropic Console 账户。终端 CLI 与 VS Code 也支持第三方提供商。

终端

VS Code

桌面应用

Web

JetBrains

功能完整的 CLI，可让你直接在终端中使用 Claude Code。在命令行中编辑文件、运行命令并管理整个项目。要安装 Claude Code，请使用以下方式之一：

原生安装（推荐）

Homebrew

WinGet

macOS、Linux、WSL：

` curl -fsSL https://claude.ai/install.sh | bash `

Windows PowerShell：

` irm https: // claude.ai / install.ps1 | iex `

Windows CMD：

` curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd `

如果你看到 ` The token '&&' is not a valid statement separator `，说明你处在 PowerShell 而非 CMD 中，请改用上面的 PowerShell 命令。当你处在 PowerShell 时，提示符会显示 ` PS C:\ `。Windows 需要 Git for Windows，如果尚未安装请先安装。

原生安装会在后台自动更新，让你始终使用最新版本。

` brew install --cask claude-code `

Homebrew 安装不会自动更新。请定期运行 ` brew upgrade claude-code ` 以获取最新功能与安全修复。

` winget install Anthropic.ClaudeCode `

WinGet 安装不会自动更新。请定期运行 ` winget upgrade Anthropic.ClaudeCode ` 以获取最新功能与安全修复。

然后在任意项目中启动 Claude Code：

` cd your-project claude `

首次使用时会提示你登录。就这样！继续阅读快速上手 →

有关安装选项、手动更新或卸载说明，请参阅高级设置。如果遇到问题，请访问故障排查。

VS Code 扩展可在编辑器中直接提供行内差异（diff）、@ 提及、计划审查与会话历史。

为 VS Code 安装

为 Cursor 安装

或者在扩展视图中搜索 “Claude Code”（Mac 上为 ` Cmd+Shift+X `，Windows/Linux 上为 ` Ctrl+Shift+X `）。安装后，打开命令面板（ ` Cmd+Shift+P ` / ` Ctrl+Shift+P `），输入 “Claude Code”，然后选择 Open in New Tab。开始使用 VS Code →

一个独立应用，可在 IDE 或终端之外运行 Claude Code。以可视化方式审查差异、并排运行多个会话、安排周期性任务，并启动云端会话。下载并安装：

macOS（Intel 与 Apple Silicon）

Windows（x64）

Windows ARM64（仅远程会话）

安装后，启动 Claude、登录，然后点击 Code 标签页开始编码。需要付费订阅。进一步了解桌面应用 →

在浏览器中运行 Claude Code，无需本地安装。启动长时间运行的任务，稍后回来查看结果；处理本地没有的仓库；或并行运行多个任务。支持桌面浏览器与 Claude iOS 应用。前往 claude.ai/code 开始编码。在 Web 上开始使用 →

适用于 IntelliJ IDEA、PyCharm、WebStorm 及其他 JetBrains IDE 的插件，支持交互式差异查看与选中内容上下文共享。从 JetBrains Marketplace 安装 Claude Code 插件并重启 IDE。开始使用 JetBrains →

​

## 你可以做什么

以下是你使用 Claude Code 的一些方式：

自动化你一直拖延的工作

Claude Code 处理那些消耗你一天的琐碎任务：为未测试的代码编写测试、修复整个项目中的静态检查（lint）错误、解决合并冲突、更新依赖，以及撰写发布说明。

` claude "write tests for the auth module, run them, and fix any failures" `

构建功能并修复缺陷

用自然语言描述你的需求。Claude Code 会规划方案、跨多个文件编写代码，并验证其可用。对于缺陷，粘贴错误信息或描述现象即可。Claude Code 会在你的代码库中追踪问题、定位根本原因并实施修复。更多示例请参阅常见工作流。

创建提交与拉取请求

Claude Code 可直接与 git 协作。它会暂存变更、编写提交信息、创建分支并打开拉取请求。

` claude "commit my changes with a descriptive message" `

在 CI 中，你可以用 GitHub Actions 或 GitLab CI/CD 自动化代码评审与问题分诊。

用 MCP 连接你的工具

模型上下文协议（MCP）是一个开放标准，用于把 AI 工具连接到外部数据源。借助 MCP，Claude Code 可以读取你 Google Drive 中的设计文档、更新 Jira 中的工单、从 Slack 拉取数据，或使用你自己的自定义工具。

通过指令、技能与钩子进行定制

` CLAUDE.md ` 是一个你添加到项目根目录的 markdown 文件，Claude Code 会在每次会话开始时读取它。用它来设定编码规范、架构决策、偏好库与评审清单。Claude 还会在工作中构建自动记忆，跨会话保存诸如构建命令与调试洞见等经验，而你无需撰写任何内容。创建自定义命令，把团队可共享的可重复工作流打包起来，例如 ` /review-pr ` 或 ` /deploy-staging `。钩子（hooks）让你在 Claude Code 动作前后运行 shell 命令，例如每次文件编辑后自动格式化，或在提交前运行静态检查。

运行智能体团队并构建自定义智能体

启动多个 Claude Code 智能体，让它们同时处理任务的不同部分。一个主智能体负责协调工作、分配子任务并合并结果。对于完全自定义的工作流，Agent SDK 让你可以构建由 Claude Code 工具与能力驱动的自有智能体，并完全掌控编排、工具访问与权限。

用 CLI 进行管道、脚本与自动化

Claude Code 可组合，并遵循 Unix 哲学。把日志管道输入它、在 CI 中运行它，或把它与其他工具串联：

```bash
# Analyze recent log output
tail -200 app.log | claude -p "Slack me if you see any anomalies"

# Automate translations in CI
claude -p "translate new strings into French and raise a PR for review"

# Bulk operations across files
git diff main --name-only | claude -p "review these changed files for security issues"
```

参阅 CLI 参考以获取完整的命令与参数集合。

安排周期性任务

按计划运行 Claude，以自动化重复性工作：晨间 PR 评审、夜间 CI 失败分析、每周依赖审计，或在 PR 合并后同步文档。

云端定时任务运行在 Anthropic 托管的基础设施上，因此即使你的电脑关机它们也会继续运行。可从 Web、桌面应用创建，或在 CLI 中运行 ` /schedule ` 创建。

桌面定时任务在你自己的机器上运行，可直接访问本地文件与工具

` /loop ` 在 CLI 会话中重复一条提示词，用于快速轮询

随处工作

会话不绑定于单一入口。随着情境变化，在环境之间移动工作：

离开工位后，用 Remote Control 从手机或任意浏览器继续工作

用 Message Dispatch 从手机派发任务，然后打开它创建的桌面会话

在 Web 或 iOS 应用上启动长时间运行的任务，然后用 ` claude --teleport ` 把它拉回终端

用 ` /desktop ` 把终端会话交接给桌面应用，以便进行可视化差异审查

从团队聊天中路由任务：在 Slack 中提及 ` @Claude ` 并附上缺陷报告，就能拿回一个拉取请求

​

## 在各处使用 Claude Code

每个入口都连接到同一个底层 Claude Code 引擎，因此你的 CLAUDE.md 文件、设置与 MCP 服务器在所有入口都能通用。除了上文的终端、VS Code、JetBrains、桌面与 Web 环境之外，Claude Code 还与 CI/CD、聊天与浏览器工作流集成：

我想……

最佳选择

从手机或其他设备继续本地会话

Remote Control

把来自 Telegram、Discord、iMessage 或我自己的 webhook 的事件推送到会话

Channels

在本地开始任务，在移动端继续

Web 或 Claude iOS 应用

按重复性计划运行 Claude

云端定时任务或桌面定时任务

自动化 PR 评审与问题分诊

GitHub Actions 或 GitLab CI/CD

为每个 PR 获得自动代码评审

GitHub Code Review

把来自 Slack 的缺陷报告路由为拉取请求

Slack

调试实时 Web 应用

Chrome

为自己的工作流构建自定义智能体

Agent SDK

​

## 后续步骤

安装好 Claude Code 之后，这些指南能帮助你更进一步。

快速上手：从探索代码库到提交修复，带你走完第一个真实任务

存储指令与记忆：用 CLAUDE.md 文件与自动记忆为 Claude 提供持久指令

常见工作流与最佳实践：充分利用 Claude Code 的模式

设置：为你的工作流定制 Claude Code

故障排查：常见问题的解决方案

code.claude.com：演示、定价与产品详情

这个页面对你有帮助吗？

快速上手

⌘ I

助手

回复由 AI 生成，可能包含错误。

## 要点回顾

- Claude Code 是一款智能体化编程工具（agentic coding tool），能读取整个代码库、编辑文件、运行命令，并可与终端、IDE、桌面应用与浏览器等多入口集成。
- 同一套底层引擎支撑所有入口，因此 CLAUDE.md、设置与 MCP 服务器在各入口之间通用，会话可以随情境在环境之间迁移（如 `/desktop`、`claude --teleport`、Remote Control）。
- 典型用途包括：自动化琐碎任务（补测试、修静态检查错误、解合并冲突、更新依赖、写发布说明）、用自然语言构建功能与修复缺陷、创建提交与拉取请求。
- 通过 `CLAUDE.md` 提供持久指令，通过自动记忆跨会话积累构建命令与调试洞见，通过自定义命令打包可共享工作流，通过钩子（hooks）在动作前后自动执行 shell 命令。
- 模型上下文协议（MCP）作为开放标准，把 Claude Code 连接到 Google Drive、Jira、Slack 等外部数据源与自有工具。
- 可启动多个智能体协同工作，由主智能体协调、分配子任务并合并结果；Agent SDK 支持在完全掌控编排、工具访问与权限的前提下构建自定义智能体。
- 遵循 Unix 哲学：可把日志管道输入、在 CI 中运行，或用 GitHub Actions / GitLab CI/CD 自动化代码评审与问题分诊；云端定时任务在托管基础设施上运行，关机也会继续执行。

> 回复由 AI 生成，可能包含错误。
