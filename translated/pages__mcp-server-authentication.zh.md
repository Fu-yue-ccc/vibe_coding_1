# 构建远程 MCP 服务器

> 译自：Build a Remote MCP server　｜　来源：https://developers.cloudflare.com/agents/guides/remote-mcp-server/

<!-- machine-translated: zh-CN | unit: pages__mcp-server-authentication -->

本指南将展示如何使用 Streamable HTTP 传输——当前 MCP 规格说明的标准——在 Cloudflare 上部署你自己的远程 MCP 服务器。你有两种选择：

不带认证 —— 任何人都可以连接并使用该服务器（无需登录）。

带认证与授权 —— 用户先登录才能访问工具，并且你可以根据用户的权限控制智能体可以调用哪些工具。

## 选择方案

Agents SDK 提供了多种创建 MCP 服务器的方式。请选择适合你的用例的方案：

| 方案 | 有状态？ | 是否需要 Durable Objects？ | 最适合 |
|---|---|---|---|
| `createMcpHandler()` | 否 | 否 | 无状态工具，最简单的搭建方式 |
| `McpAgent` | 是 | 是 | 有状态工具、按会话的状态、elicitation |
| 原生 `WebStandardStreamableHTTPServerTransport` | 否 | 否 | 完全控制，无 SDK 依赖 |

`createMcpHandler()` 是让无状态 MCP 服务器跑起来最快的方式。当你的工具不需要按会话维护状态时，就用它。

`McpAgent` 为每个会话提供一个 Durable Object，内置状态管理、elicitation 支持，并同时支持 SSE 与 Streamable HTTP 两种传输。

原生传输能给你完全的控制权——如果你想直接使用 `@modelcontextprotocol/sdk` 而不借助 Agents SDK 的辅助封装。

## 部署你的第一个 MCP 服务器

你可以先部署一个公开的 MCP 服务器——不带认证，之后再添加用户认证与有范围的授权。如果你已经知道自己的服务器需要认证，可以直接跳到下一节。

### 通过仪表板

下面的按钮会引导你完成把示例 MCP 服务器部署到你的 Cloudflare 账户所需的全部步骤：

部署完成后，该服务器将上线在你的 `workers.dev` 子域（例如 `remote-mcp-server-authless.your-account.workers.dev/mcp`）。你可以立即用 AI Playground（一个远程 MCP 客户端）、MCP inspector 或其他 MCP 客户端连接它。

系统会在你的 GitHub 或 GitLab 账户上为你的 MCP 服务器新建一个 git 仓库，并配置为：每当你向该仓库的 main 分支推送变更或合并拉取请求（PR）时自动部署到 Cloudflare。你可以克隆这个仓库、在本地开发，并开始用你自己的工具定制这个 MCP 服务器。

### 通过 CLI

你可以使用 Wrangler CLI 在本地机器上创建新的 MCP 服务器，并将其部署到 Cloudflare。

打开终端并运行以下命令：

```
npm create cloudflare@latest -- remote-mcp-server-authless --template=cloudflare/ai/demos/remote-mcp-authless
```

```
yarn create cloudflare remote-mcp-server-authless --template=cloudflare/ai/demos/remote-mcp-authless
```

```
pnpm create cloudflare@latest remote-mcp-server-authless --template=cloudflare/ai/demos/remote-mcp-authless
```

在安装过程中，请选择以下选项：- 对于「是否要添加 AGENTS.md 文件以帮助 AI 编程工具理解 Cloudflare API？」，选择 `No`。- 对于「是否要使用 git 进行版本控制？」，选择 `No`。- 对于「是否要部署你的应用？」，选择 `No`（我们会先测试服务器，再部署）。

现在，你已经搭好 MCP 服务器，依赖也已安装完毕。

进入项目文件夹：

终端窗口

```
cd remote-mcp-server-authless
```

在新项目所在的目录中，运行以下命令以启动开发服务器：

终端窗口

```
npm start
```

```
⏵ 正在启动本地服务器...
[wrangler:info] Ready on http://localhost:8788
```

查看命令输出中的本地端口。在本例中，MCP 服务器运行在端口 `8788` 上，MCP 端点 URL 为 `http://localhost:8788/mcp`。

要在本地测试该服务器：

在新的终端中运行 MCP inspector。MCP inspector 是一个交互式 MCP 客户端，让你可以从网页浏览器连接到你的 MCP 服务器并调用工具。

终端窗口

```
npx @modelcontextprotocol/inspector@latest
```

```
🚀 MCP Inspector is up and running at:
http://localhost:5173/?MCP_PROXY_AUTH_TOKEN=46ab..cd3
🌐 Opening browser...
```

MCP Inspector 会在你的网页浏览器中启动。你也可以手动启动它：打开浏览器并访问 `http://localhost:<PORT>`。请查看命令输出中 MCP Inspector 运行所用的本地端口。在本例中，MCP Inspector 服务于端口 `5173`。

在 MCP inspector 中，输入你的 MCP 服务器 URL（`http://localhost:8788/mcp`），然后选择 Connect。选择 List Tools 即可显示你的 MCP 服务器所暴露的工具。

现在你可以把 MCP 服务器部署到 Cloudflare 了。在项目目录中运行：

终端窗口

```
npx wrangler@latest deploy
```

如果你已经把某个 git 仓库连接到承载你的 MCP 服务器的 Worker，那么你可以通过推送变更、或向该仓库的 main 分支合并拉取请求来部署 MCP 服务器。

MCP 服务器将部署到你的 `*.workers.dev` 子域，地址为 `https://remote-mcp-server-authless.your-account.workers.dev/mcp`。

要测试远程 MCP 服务器，请取你已部署的 MCP 服务器的 URL（`https://remote-mcp-server-authless.your-account.workers.dev/mcp`），并填入运行在 `http://localhost:5173` 的 MCP inspector 中。

现在你已经有了一台 MCP 客户端可以连接的远程 MCP 服务器。

## 通过本地代理从 MCP 客户端连接

现在你的远程 MCP 服务器已经运行起来了，你可以使用 `mcp-remote` 本地代理，把 Claude Desktop 或其他 MCP 客户端连接到它——即使你的 MCP 客户端在客户端侧不支持远程传输或授权也可以。这样你就能用真实的 MCP 客户端测试与远程 MCP 服务器的交互会是怎样的。

例如，要从 Claude Desktop 连接：

更新你的 Claude Desktop 配置，使其指向你的 MCP 服务器 URL：

```
{
  "mcpServers": {
    "math": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://remote-mcp-server-authless.your-account.workers.dev/mcp"
      ]
    }
  }
}
```

重启 Claude Desktop 以加载该 MCP 服务器。完成之后，Claude 就能调用你的远程 MCP 服务器了。

要测试，请让 Claude 使用你的某个工具。例如：

```
Could you use the math tool to add 23 and 19?
```

Claude 应当调用该工具，并显示远程 MCP 服务器生成的结果。

要了解如何在其他 MCP 客户端中使用远程 MCP 服务器，请参阅 Test a Remote MCP Server。

## 添加认证

你先前部署的公开 MCP 服务器示例允许任何客户端在没有登录的情况下连接并调用工具。要为你的 MCP 服务器添加用户认证，你可以接入 Cloudflare Access 或第三方服务作为 OAuth 提供方。你的 MCP 服务器负责处理安全的登录流程，并签发访问 Token，供 MCP 客户端发起经过认证的工具调用。用户通过 OAuth 提供方登录，并以有范围的权限，授予其 AI 智能体与你的 MCP 服务器所暴露工具交互的许可。

### Cloudflare Access OAuth

你可以配置 MCP 服务器，要求通过 Cloudflare Access 进行用户认证。Cloudflare Access 充当身份聚合器，会验证用户邮箱、来自你现有身份提供方（如 GitHub 或 Google）的信号，以及 IP 地址或设备证书等其他属性。当用户连接到该 MCP 服务器时，系统会提示其登录到已配置的身份提供方，只有通过你的 Access 策略才会被授予访问权限。

分步部署指南请参阅 Secure MCP servers with Access for SaaS。

### 第三方 OAuth

你可以把 MCP 服务器连接到任何支持 OAuth 2.0 规格说明的 OAuth 提供方，包括 GitHub、Google、Slack、Stytch、Auth0、WorkOS 等。

下面的示例演示如何使用 GitHub 作为 OAuth 提供方。

#### 第 1 步 —— 创建一个新的 MCP 服务器

运行以下命令，创建一个使用 GitHub OAuth 的新 MCP 服务器：

```
npm create cloudflare@latest -- my-mcp-server-github-auth --template=cloudflare/ai/demos/remote-mcp-github-oauth
```

```
yarn create cloudflare my-mcp-server-github-auth --template=cloudflare/ai/demos/remote-mcp-github-oauth
```

```
pnpm create cloudflare@latest my-mcp-server-github-auth --template=cloudflare/ai/demos/remote-mcp-github-oauth
```

现在，你已经搭好 MCP 服务器，依赖也已安装完毕。进入该项目文件夹：

终端窗口

```
cd my-mcp-server-github-auth
```

你会注意到，在这个示例 MCP 服务器中，如果你打开 `src/index.ts`，最主要的差异在于 `defaultHandler` 被设置为 `GitHubHandler`：

TypeScript

```
import GitHubHandler from "./github-handler";

export default new OAuthProvider({
  apiRoute: "/mcp",
  apiHandler: MyMCP.serve("/mcp"),
  defaultHandler: GitHubHandler,
  authorizeEndpoint: "/authorize",
  tokenEndpoint: "/token",
  clientRegistrationEndpoint: "/register",
});
```

这确保你的用户会被重定向到 GitHub 进行认证。不过要让它真正跑起来，你还需要在后续步骤中创建 OAuth 客户端应用。

#### 第 2 步 —— 创建 OAuth 应用

你需要创建两个 GitHub OAuth 应用，才能把 GitHub 用作 MCP 服务器的认证提供方——一个用于本地开发，一个用于生产。

#### 第 2.1 步 —— 为本地开发创建新的 OAuth 应用

请前往 github.com/settings/developers 创建一个新的 OAuth 应用，设置如下：

应用名称：`My MCP Server (local)`

主页 URL：`http://localhost:8788`

授权回调 URL：`http://localhost:8788/callback`

对于你刚创建的 OAuth 应用，把该应用的客户端 ID 添加为 `GITHUB_CLIENT_ID`，并生成一个客户端密钥，将其作为 `GITHUB_CLIENT_SECRET` 添加到项目根目录的 `.env` 文件中，这些将用于在本地开发中设置密钥。

终端窗口

```
touch .env
echo 'GITHUB_CLIENT_ID="your-client-id"' >> .env
echo 'GITHUB_CLIENT_SECRET="your-client-secret"' >> .env
cat .env
```

运行以下命令以启动开发服务器：

终端窗口

```
npm start
```

你的 MCP 服务器现在运行在 `http://localhost:8788/mcp`。

在新的终端中运行 MCP inspector。MCP inspector 是一个交互式 MCP 客户端，让你可以从网页浏览器连接到你的 MCP 服务器并调用工具。

终端窗口

```
npx @modelcontextprotocol/inspector@latest
```

在网页浏览器中打开 MCP inspector：

终端窗口

```
open http://localhost:5173
```

在 inspector 中，输入你的 MCP 服务器 URL：`http://localhost:8788/mcp`

在右侧的主面板中，点击 OAuth Settings 按钮，然后点击 Quick OAuth Flow。

你应当会被重定向到 GitHub 的登录或授权页面。在授权 MCP 客户端（即 inspector）访问你的 GitHub 账户后，你会被重定向回 inspector。

点击侧边栏中的 Connect，你应当会看到「List Tools」按钮，它会列出你的 MCP 服务器所暴露的工具。

#### 第 2.2 步 —— 为生产环境创建新的 OAuth 应用

你需要重复第 2.1 步，为生产环境创建一个新的 OAuth 应用。

前往 github.com/settings/developers 创建一个新的 OAuth 应用，设置如下：

应用名称：`My MCP Server (production)`

主页 URL：填入你已部署的 MCP 服务器的 workers.dev URL（例如 `worker-name.account-name.workers.dev`）

授权回调 URL：填入你已部署的 MCP 服务器的 workers.dev URL 的 `/callback` 路径（例如 `worker-name.account-name.workers.dev/callback`）

对于你刚创建的 OAuth 应用，使用 Wrangler CLI 添加客户端 ID 与客户端密钥：

终端窗口

```
npx wrangler secret put GITHUB_CLIENT_ID
```

终端窗口

```
npx wrangler secret put GITHUB_CLIENT_SECRET
```

```
npx wrangler secret put COOKIE_ENCRYPTION_KEY # add any random string here e.g. openssl rand -hex 32
```

设置一个 KV 命名空间

a. 创建该 KV 命名空间：

终端窗口

```
npx wrangler kv namespace create "OAUTH_KV"
```

b. 用生成的 KV ID 更新 `wrangler.jsonc` 文件：

```
{
  "kvNamespaces": [
    {
      "binding": "OAUTH_KV",
      "id": "<YOUR_KV_NAMESPACE_ID>"
    }
  ]
}
```

将 MCP 服务器部署到你的 Cloudflare `workers.dev` 域名：

终端窗口

```
npm run deploy
```

使用 AI Playground、MCP Inspector 或其他 MCP 客户端连接到运行在 `worker-name.account-name.workers.dev/mcp` 的服务器，并使用 GitHub 进行认证。

## 下一步

MCP Tools 为你的 MCP 服务器添加工具。

Authorization 自定义认证与授权。

## 要点回顾

- 远程 MCP 服务器有两种模式：不带认证（任何人可连接）与带认证和授权（用户登录后按权限访问工具）。
- 方案选择：`createMcpHandler()` 适合无状态工具且最易搭建；`McpAgent` 适合有状态工具与按会话状态；原生 `WebStandardStreamableHTTPServerTransport` 提供完全控制且无 SDK 依赖。
- 部署方式可以是仪表板引导，也可以用 Wrangler CLI 创建项目、本地 `npm start` 测试后再 `npx wrangler@latest deploy`。
- 本地测试使用 MCP inspector（`npx @modelcontextprotocol/inspector@latest`，默认 `http://localhost:5173`），连接 MCP 端点后可列出并调用工具。
- 客户端侧不支持远程传输或授权时，可用 `mcp-remote` 本地代理把 Claude Desktop 等 MCP 客户端接到远程服务器。
- 认证可选用 Cloudflare Access 作为身份聚合器，或接入支持 OAuth 2.0 的第三方提供方（GitHub、Google、Slack、Stytch、Auth0、WorkOS 等）。
- 以 GitHub 为例需创建两套 OAuth 应用（本地与生产），并通过 `wrangler secret` 设置 `GITHUB_CLIENT_ID`、`GITHUB_CLIENT_SECRET`、`COOKIE_ENCRYPTION_KEY`，再用 `OAUTH_KV` 命名空间支撑 OAuth 流程。
