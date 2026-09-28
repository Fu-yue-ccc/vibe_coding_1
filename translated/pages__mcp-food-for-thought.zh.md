# API 并不适合直接做成 MCP 工具

> 译自：APIs don't make good MCP tools　｜　来源：https://www.reillywood.com/blog/apis-dont-make-good-mcp-tools/

<!-- machine-translated: zh-CN | unit: pages__mcp-food-for-thought -->

Reilly Wood · 2025 年 8 月 5 日 · 4 分钟阅读

如今，模型上下文协议（Model Context Protocol，MCP）已经相当重要。它已成为让 LLM（大语言模型）访问他人所写工具的事实标准，而这自然会把它们变成智能体。但为一个新的 MCP 服务器编写工具并不容易，因此人们常常提出把现有 API 自动转换成（auto-converting）MCP 工具；通常借助 OpenAPI 元数据来实现（1、2）。

以我的经验，这种做法可行，但效果并不好。原因有以下几条：

## 智能体不擅长处理大量工具

众所周知，VS Code 对工具数量有 128 个的硬性上限——但许多模型在远未达到这个数量之前，就已经难以准确完成工具调用了。此外，每个工具及其描述都会占用宝贵的上下文窗口空间。

大多数 Web API 在设计时并没有考虑这些约束！当 API 由代码调用时，为同一个产品领域提供大量 API 没什么问题；但如果把每个 API 都映射成一个 MCP 工具，结果可能就不太好了。

从零开始专门设计的 MCP 工具，通常比单个 Web API 灵活得多：一个工具就能完成好几个单个 API 的工作。

## API 会迅速耗尽上下文窗口

设想一个每次返回 100 条记录的 API，而每条记录都很“宽”（比如 50 个字段）。把这些结果原样发给智能体，将消耗大量 Token；即使某个查询只需少数几个字段就能满足，所有字段最终还是会进入上下文窗口。

API 的分页通常按记录条数划分，但记录大小可能相差悬殊。一条记录可能包含一个大文本字段，占用 100,000 个 Token，而另一条可能只占 10 个。把这些 API 结果直接放进智能体的上下文窗口是场赌博：有时能成，有时会炸掉。

数据的格式也可能是问题。如今大多数 Web API 返回 JSON，但 JSON 是一种非常浪费 Token 的格式。看看这个：

`[{"firstName": "Alice", "lastName": "Johnson", "age": 28}, {"firstName": "Bob", "lastName": "Smith", "age": 35}]`

对比一下同样数据用 CSV 格式表示：

`firstName,lastName,age Alice,Johnson,28 Bob,Smith,35`

CSV 数据简洁得多——每条记录消耗的 Token 只有前者的一半。一般来说，CSV、TSV 或 YAML（用于嵌套数据）都比 JSON 更合适。

这些问题都不是无法克服的。你可以设想自动添加工具参数、让智能体只投影所需字段，自动截断或摘要化过大的结果，以及自动把 JSON 结果转换为 CSV（嵌套数据则转为 YAML）。但我见过的大多数服务器这几件事一件都没做。

## API 没有充分利用智能体的独特能力

API 返回供程序消费的结构化数据。这往往正是智能体希望从工具调用中得到的东西……但智能体也能处理其他更自由的指令形式。

例如，一个 `ask_question` 工具可以对某些文档执行一次检索增强生成（RAG）查询，然后以纯文本返回信息，用于指导下一次工具调用——完全跳过结构化数据。

或者，调用 `search_cities` 工具可以返回一个结构化的城市列表，并附带下一步该调用什么的建议：

`city_name,population,country,region Tokyo,37194000,Japan,Asia Delhi,32941000,India,Asia Shanghai,28517000,China,Asia Suggestion: To get more specific information (weather, attractions, demographics), try calling get_city_details with the city_name parameter.`

这种分层与工具串联（tool chaining）在 MCP 服务器中可能非常有效，而如果你只是把 API 自动转成工具，就会完全错过它。

## 如果智能体需要调用 API，它直接调用就好

像 Claude Code 这样的智能体现在非常擅长编写并执行代码，包括调用 Web API 的脚本。有些人甚至据此认为根本不需要 MCP！

我不同意这个结论，但我确实认为我们应该滑向冰球将要去的地方（skate to where the puck is going）。智能体的沙箱能力正在快速提升，如果智能体直接调用 API 既简单又安全，那我们不妨就这么做，省掉中间环节。

## 结论

智能体与 API 的典型消费者有本质区别。从现有 API 自动创建 MCP 工具是可行的，但这样做很可能效果不佳。当智能体拿到的工具是围绕其独特能力与局限设计的时候，它的表现最好。

土地价值与可负担性

工具调用既昂贵又有限

## 城市与代码

### 近期文章

### 💻 2025 回顾

2025 年 12 月 28 日

### 💻 MCP 到底有什么用？

2025 年 12 月 26 日

### 💻 工具调用既昂贵又有限

2025 年 9 月 18 日

### 💻 API 并不适合直接做成 MCP 工具

2025 年 8 月 5 日

### 🏗️ 土地价值与可负担性

2025 年 6 月 26 日

### 📝 我遭遇恶意 SEO 的经历

2025 年 6 月 16 日

查看更多文章

### 热门分类

软件 42

城市规划 11

最近 10

Rust 9

Web 9

数据库 8

LLM 8

Nushell 7

查看全部分类

#### 首页

#### 关于

#### 项目

### 近期文章

### 2025 回顾

2025 年 12 月 28 日

### MCP 到底有什么用？

2025 年 12 月 26 日

### 工具调用既昂贵又有限

2025 年 9 月 18 日

### API 并不适合直接做成 MCP 工具

2025 年 8 月 5 日

### 土地价值与可负担性

2025 年 6 月 26 日

### 我遭遇恶意 SEO 的经历

2025 年 6 月 16 日　查看更多文章
