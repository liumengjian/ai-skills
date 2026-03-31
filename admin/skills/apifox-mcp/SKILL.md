---
name: apifox-mcp
description: Reads OpenAPI Spec from Apifox project for API-driven code generation. Use when defining interfaces, implementing declareRequest, generating API client code, or when the user mentions Apifox, API documentation, or OpenAPI specs.
---

# Apifox MCP 工具

通过 `apifox-mcp-server` 将 Apifox 项目中的 OpenAPI Spec 提供给 AI，用于按接口文档生成代码、实现 `declareRequest`、定义请求模型等。

## 触发场景

在以下场景下优先调用 Apifox MCP：

- 按 Apifox 接口文档实现前端接口调用（declareRequest、http 调用）
- 生成与接口字段匹配的表格列、表单字段
- 需要接口路径、请求/响应结构、参数说明
- 用户提及 Apifox、API 文档、OpenAPI、接口定义

## 核心工具

调用前需查阅 `mcps/user-apifox/tools/*.json` 获取当前项目的工具名与参数 schema，工具名可能带项目后缀（如 `_qzukxd`）。

| 工具类型 | 用途 | 典型参数 |
|----------|------|----------|
| `read_project_oas_*` | 读取默认模块的 OpenAPI Spec 完整内容 | 无必需参数 |
| `read_project_oas_ref_resources_*` | 读取 Spec 内 `$ref` 引用的子文件内容 | `path`: 字符串数组，如 `["/paths/_get_pet.json"]` |
| `refresh_project_oas_*` | 从服务器重新下载最新 Spec（Apifox 有更新时） | 无必需参数 |

## 调用方式

使用 `call_mcp_tool` 调用，`server` 为 `user-apifox`：

```json
{
  "server": "user-apifox",
  "toolName": "read_project_oas_qzukxd",
  "arguments": {}
}
```

读取 `$ref` 引用文件示例：

```json
{
  "server": "user-apifox",
  "toolName": "read_project_oas_ref_resources_qzukxd",
  "arguments": {
    "path": ["/paths/_get_xxx.json", "/components/schemas/User.json"]
  }
}
```

## 典型流程

1. **获取 Spec**：调用 `read_project_oas_*` 获取完整 OpenAPI 文档
2. **解析接口**：从 `paths`、`components/schemas` 中提取接口路径、请求体、响应结构
3. **生成代码**：按项目规范（declareRequest、jjb-common-lib http）生成接口定义
4. **补充引用**：若 Spec 使用 `$ref`，用 `read_project_oas_ref_resources_*` 获取引用内容

## 最佳实践

- **先查 schema**：调用前阅读 `mcps/user-apifox/tools/` 下对应工具 descriptor，确认 `toolName` 与 `arguments` 结构
- **数据刷新**：若 Apifox 中接口有变更，先用 `refresh_project_oas_*` 拉取最新 Spec
- **结合规范**：生成接口代码时遵循项目 `api-data-layer`、`11-接口与数据层规范` 等技能

## 前置条件

- mcp.json 中已配置 `apifox`，且 `--site-id`（或 `--project-id`）指向正确项目
- 私有部署需配置 `APIFOX_ACCESS_TOKEN` 或对应环境变量
- Spec 数据本地缓存，Apifox 更新后需手动 `refresh`
