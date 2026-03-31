---
name: zentao-mcp-usage
description: >-
  Guides use of the ZenTao MCP tool in Cursor to fetch and parse bug details from ZenTao.
  Use when the user mentions ZenTao bugs, wants to fix a bug, view bug details, or provides a ZenTao bug URL.
---

# 禅道 (ZenTao) MCP 工具使用指南

## 何时使用

在以下场景下应用本技能：

- 用户提供了禅道 Bug 的 URL
- 用户说要修复某个 Bug、查看 Bug 详情
- 用户提到禅道、zentao、Bug 单等关键词

## 可用工具

当前配置的禅道 MCP 服务器：`zentao-bug-fix`（对应 mcp.json 中的 key）

### fetch_zentao_bug

获取并解析禅道 Bug 详情。根据 Bug URL 解析标题、详情、步骤、结果、期望及基本信息，并返回相关图片。

**调用方式**：使用 `call_mcp_tool`，指定 `server` 和 `toolName`，传入 `arguments`。

**必选参数**：

| 参数     | 类型   | 说明                                      |
|----------|--------|-------------------------------------------|
| `bugUrl` | string | 禅道 Bug 页面的完整 URL                   |

**可选参数**：

| 参数     | 类型   | 默认值 | 说明                         |
|----------|--------|--------|------------------------------|
| `cookie` | string | -      | 用于身份验证的 Cookie 字符串 |
| `timeout`| number | 10000  | 请求超时时间（毫秒）         |

## 调用示例

### 基础用法（仅传 Bug URL）

```json
{
  "server": "zentao-bug-fix",
  "toolName": "fetch_zentao_bug",
  "arguments": {
    "bugUrl": "http://192.168.1.252/zentao/bug-view-33360.html"
  }
}
```

### 带 Cookie 和超时

需要登录态或目标站点有权限限制时，可传入 Cookie：

```json
{
  "server": "zentao-bug-fix",
  "toolName": "fetch_zentao_bug",
  "arguments": {
    "bugUrl": "http://192.168.1.252/zentao/bug-view-33360.html",
    "cookie": "your_session_cookie_here",
    "timeout": 15000
  }
}
```

## 使用流程

1. **先查工具 schema**：调用前查阅 MCP 工具 descriptor，确认 `zentao-bug-fix` 下 `fetch_zentao_bug` 的最新参数定义。
2. **调用工具**：使用 `call_mcp_tool` 传入正确的 `server`、`toolName` 和 `arguments`。
3. **处理结果**：解析返回的 Bug 标题、详情、步骤、结果、期望等信息，用于指导代码修改或问题分析。

## 典型工作流：修复禅道 Bug

1. 用户提供 Bug URL 或 Bug ID
2. 若只有 ID，组合为完整 URL，如：`{zentao_base}/bug-view-{id}.html`
3. 调用 `fetch_zentao_bug` 获取 Bug 详情
4. 根据「步骤」「期望」理解问题，定位相关代码
5. 编写或修改代码修复 Bug
6. 简要说明修复点与 Bug 的对应关系

## 注意事项

- `bugUrl` 需为可访问的完整 URL，包含协议和域名
- 如返回 401/403，通常需要补充有效的 `cookie`
- 若使用其他禅道 MCP 实现（如 ZenTaoMcp），工具名和参数可能不同，需对照其文档
