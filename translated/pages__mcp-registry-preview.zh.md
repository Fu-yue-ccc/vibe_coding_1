# 推出 MCP 注册表

> 译自：Introducing the MCP Registry　｜　来源：https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/

<!-- machine-translated: zh-CN | unit: pages__mcp-registry-preview -->

跳转到内容

首页 » 文章

# 推出 MCP 注册表

预览版上线：一个用于发现公开可用 MCP 服务器的开放目录与 API。

2025 年 9 月 8 日 · 4 分钟阅读 · David Soria Parra（首席维护者）、Adam Jones（注册表维护者）、Tadas Antanavicius（注册表维护者）、Toby Padilla（注册表维护者）、Theodora Chu（Anthropic 的 MCP 产品经理）

今天，我们正式推出模型上下文协议（Model Context Protocol，MCP）注册表（MCP Registry）——一个面向公开可用 MCP 服务器的开放目录与 API，用于改善其可发现性与落地实现。通过统一服务器的分发与发现方式，我们既扩大了它们的触达范围，也让客户端更容易完成连接。

MCP 注册表现已开放预览。开始使用：

- 按照《向 MCP 注册表添加服务器》指南添加你的服务器（面向服务器维护者）
- 按照《访问 MCP 注册表数据》指南获取服务器数据（面向客户端维护者）

# MCP 服务器的单一权威数据源

2025 年 3 月，我们曾提到希望为 MCP 生态构建一个中心化注册表。今天我们宣布，官方 MCP 注册表已在 https://registry.modelcontextprotocol.io 上线。作为 MCP 项目的一部分，MCP 注册表以及其上游的 OpenAPI 规格说明均为开源——任何人都可以据此构建兼容的子注册表。

我们的目标是统一服务器的分发与发现方式，提供一个可供子注册表在其之上构建的主权威数据源。这反过来会扩大服务器的触达范围，帮助客户端更容易地在整个 MCP 生态中找到服务器。

## 公开子注册表与私有子注册表

在构建中心化注册表的过程中，我们很重视不去取代社区与企业已经建成的既有注册表。MCP 注册表作为公开可用 MCP 服务器的主权威数据源，各组织可以按自己的自定义标准创建子注册表。例如：

公开子注册表——例如与各个 MCP 客户端绑定的、带有明确取舍立场的“MCP 应用市场”——可以自由地增补和增强其从上游 MCP 注册表获取的数据。每一类 MCP 终端用户画像的需求都不同，如何以带立场的方式恰当地服务自己的终端用户，由各 MCP 客户端应用市场自行决定。

对于有严格隐私与安全要求的企业，私有子注册表将会存在；而 MCP 注册表为这些企业提供了一个可供构建的单一上游数据源。我们至少希望与这些私有实现共享 API schema，以便相关 SDK 与工具链能够在整个生态中共享。

无论哪种情况，MCP 注册表都是起点——它是 MCP 服务器维护者发布并维护其自报信息的集中位置，供下游消费方加工后再交付给各自的终端用户。

## 社区驱动的审核机制

MCP 注册表是 MCP 官方项目，由注册表工作组维护，并采用宽松许可。社区成员可以提交 issue，标记违反 MCP 审核准则的服务器——例如包含垃圾信息、恶意代码，或冒充合法服务的服务器。注册表维护者随后可以把这些条目加入拒绝名单（denylist），并追溯性地将其从公开访问中移除。

# 快速开始

开始使用：

- 按照《向 MCP 注册表添加服务器》指南添加你的服务器（面向服务器维护者）
- 按照《访问 MCP 注册表数据》指南获取服务器数据（面向客户端维护者）

MCP 注册表的这一预览版是为了在正式发布（general availability）之前帮助我们改进用户体验，不提供数据持久性保证或其他担保。我们建议采用 MCP 的各方密切关注其开发进展，因为在注册表正式发布之前可能会发生破坏性变更。

在持续开发注册表的过程中，我们欢迎大家在 modelcontextprotocol/registry GitHub 仓库上反馈与贡献：Discussion、Issues 与拉取请求（PR）都欢迎。

# 感谢 MCP 社区

MCP 注册表从一开始就是一项协作成果，我们无比感激广大开发者社区的热情与支持。

2025 年 2 月，它作为一个草根项目起步：MCP 的创造者 David Soria Parra 与 Justin Spahr-Summers 邀请 PulseMCP 和 Goose 团队协助构建一个中心化的社区注册表。来自 PulseMCP 的注册表维护者 Tadas Antanavicius 与来自 Block 的 Alex Hancock 合作，带头推进了最初的工作。很快，GitHub 的 MCP 负责人、注册表维护者 Toby Padilla 也加入进来；再后来，来自 Anthropic 的 Adam Jones 以注册表维护者身份加入，推动项目走到今天的发布。MCP 注册表开发工作的首次公告列出了来自至少 9 家公司的 16 位贡献者。

还有许多人做出了关键贡献，让这个项目得以成真：来自 Stacklok 的 Radoslav Dimitrov、来自 GitHub 的 Avinash Sridhar、来自 VS Code 的 Connor Peet、来自 NuGet 的 Joel Verhagen、来自 Last9 的 Preeti Dewani、来自 Microsoft 的 Avish Porwal、Jonathan Hefner，以及许多提供代码评审与开发支持的 Anthropic 和 GitHub 员工。我们同样感谢注册表贡献者名单上的每一位，以及参与讨论和 issue 的各位。

我们深切感谢每一位为这项基础性开源基础设施投入的人。我们在一起帮助全球的开发者与组织构建更可靠、具备上下文感知能力的 AI 应用。谨代表 MCP 社区，谢谢大家。
