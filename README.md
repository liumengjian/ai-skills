# jjb-ai

**jjb-ai** 是 **JJB** 多端项目仓库：同时包含 **后台管理系统**、**小程序应用**，以及面向 Cursor 等编辑器的 **MCP、Rules、Skills、Agents** 等 AI 协作配置，便于业务研发与 AI 辅助规范一体维护。

## 项目组成

| 组成部分 | 说明 |
|---------|------|
| **后台管理系统** | 企业级后台（React、Ant Design、JJB 微应用与底座能力等），研发规范见 `admin/skills/` |
| **小程序应用** | 小程序端工程，代码位于 `applet/`（随业务迭代演进） |
| **MCP** | 禅道、MeterSphere、Chrome DevTools、Figma、Apifox 等外部能力接入，配置见 `admin/mcp.json` |
| **Rules** | 项目级协作与代码规则，见 `admin/rules/` |
| **Skills** | 分领域 SKILL 与 `specs/` 细粒度规范，见 `admin/skills/` |
| **Agents** | 预置 Agent 角色说明（如后台页面构建、接口与数据层对接），见 `admin/agents/` |

## 目录结构（摘要）

```
jjb-ai/
├── admin/
│   ├── rules/          # Cursor / 项目规则（如 PROJECT.md）
│   ├── skills/         # Skills 与 specs 规范全集（含 spec-index 总索引）
│   ├── agents/         # Agent 定义
│   └── mcp.json        # MCP 服务配置（勿提交真实密钥）
├── applet/             # 小程序端应用
└── README.md
```

各端 **依赖安装、本地启动、构建发布** 以对应子目录内工程为准（例如存在 `package.json` 时在其目录执行脚本）。

## 规范与 AI 协作入口

- **总索引**：`admin/skills/spec-index/SKILL.md`
- **完整关键词索引**：`admin/skills/spec-index/reference.md`
- **在 Cursor 中使用**：将 `rules`、`skills` 按团队约定映射到 `.cursor/rules/`、`.cursor/skills/` 等路径；参考 `admin/agents/` 配置 Agent；将 `admin/mcp.json` 合并进编辑器 MCP 配置并按需启用。

## MCP 与安全

`admin/mcp.json` 中的密钥类配置（如禅道 Cookie、平台 Token、Figma API Key 等）**不应提交到公共仓库**。请使用环境变量、私有配置或本地覆盖。各 MCP 的用法说明见 `admin/skills/` 下对应目录（如 `zentao-mcp-usage`、`meter-sphere-mcp-usage`、`apifox-mcp`、`figma-mcp`、`chrome-devtools`）。

## 技术栈（后台管理端规范摘要）

Skills 与 `specs/` 主要覆盖：React、Ant Design、`declareRequest` / `Connect`、底座平台 API、云组件、`jjb-cmd` 与 GitLab 部署等；小程序端技术栈以 `applet/` 内工程为准。

## 分支与协作

开发以仓库 Git 分支为准；修改 Rules / Skills / MCP 时建议评审，并与各端业务发布节奏对齐。
