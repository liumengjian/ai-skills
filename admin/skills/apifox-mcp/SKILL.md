---
name: apifox-mcp
description: Reads OpenAPI Spec from Apifox project for API-driven code generation. Use when defining interfaces, implementing declareRequest, generating API client code, or when the user mentions Apifox, API documentation, or OpenAPI specs.
---

# Apifox MCP 工具

通过 `apifox-mcp-server` 将 Apifox 项目中的 OpenAPI Spec 提供给 AI，用于按接口文档生成代码、实现 `declareRequest`、定义请求模型等。

## 数据源优先级（必读）

回答某条接口的字段、类型、结构，或据此写代码时：

1. **先用本地契约**：根据 **`path` + HTTP 方法** 按下文规则算出 `<operation-folder>`，检查项目根目录是否存在 **`.api/<operation-folder>/spec.json` 与 `type.d.ts`**。
2. **若两者皆存在**：**不得**为此接口调用 Apifox MCP（`read_project_oas_*` / `read_project_oas_ref_resources_*` / `refresh_project_oas_*`）。直接用 Read 等工具读取上述文件，向用户说明内容或据此生成代码即可。
3. **仅在下述情况才调用 MCP**：
   - 本地 **无** 对应目录，或缺少 `spec.json` / `type.d.ts` 之一；
   - 用户 **明确要求** 与 Apifox **同步 / 刷新 / 更新 / 对齐最新文档**（或同义表述）；
   - 用户 **点名** 要从 Apifox / OpenAPI 源拉取（而非使用仓库内 `.api`）。
4. MCP 拉取或修正接口后：按「`.api` 本地契约目录」**回写或新建** `spec.json` 与 `type.d.ts`，供下次走规则 1–2。

## Apifox `int64` 与 Java `Long`（前端精度，必读）

Java **Snowflake / 分布式 Long 主键** 常超出 `Number.MAX_SAFE_INTEGER`（2^53−1）。Apifox 从后端导入时往往把 `Long` 标成 OpenAPI 的 **`integer` + `format: int64`**，容易和「前端用 `number` / `Number(x)`」混在一起，导致 **ID 在 JS 里被静默改值**。

落盘 `.api` 与写业务代码时：

1. **不要用 `Number()`、`parseInt`** 清洗仅用于透传的 **主键、外键类 Long ID**，除非你已确认值必然在安全整数范围内且后端只接受数字 JSON。
2. **优先在 `spec.json` / `type.d.ts` 里把这类字段写成 `string`（或与后端约定的字符串形态）**，并在 `description` 里注明「后端 Long / Apifox 显示 int64；前端按字符串保证精度」。这样仓库内契约与实现一致，也不会误导后续只读 OpenAPI 的自动化生成。
3. 若 Apifox 源 Spec 仍为 `integer`/`int64`，以 **本仓库 `.api` 校正后的类型** 为协作准绳；需要与文档门户完全一致时，再在 Apifox 里改模型或注明字符串序列化策略。

## 触发场景

- **默认**：用户问某接口详情或要对接实现时，若 `.api` 已有契约 → **只读本地文件**，不触发 MCP。
- **需调用 MCP 时**：本地无契约、不完整，或用户要求 **同步 Apifox / 刷新 Spec**；或用户明确要对照线上 OpenAPI。
- 其余：实现 `declareRequest`、表格列、表单字段、路径与参数说明等，**在有本地契约时均以 `.api` 为准**。

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

1. **解析目标**：确定接口 `path`、HTTP 方法，算出 `<operation-folder>`（见下文章节）。
2. **本地命中**：若 `.api/<operation-folder>/` 下 **已有** `spec.json` 与 `type.d.ts` → **读这两个文件即完成**，不写 MCP；向用户输出协议内容或继续写 `src/api` 等业务代码。
3. **本地未命中或用户要求同步**：再调用 `read_project_oas_*`（及按需 `read_project_oas_ref_resources_*`）解析 `paths` / `components`；必要时先 `refresh_project_oas_*`。
4. **落盘**：新建或更新 `.api/<operation-folder>/spec.json` 与 `type.d.ts`。
5. **生成业务代码**：按项目规范（`declareRequest`、`jjb-common-lib` http 等）在 `src/api` 等目录实现；类型可从 `.api/.../type.d.ts` 引用（纯 JS 项目可用 `jsconfig.json` 的 `include`；TS 项目配置 `tsconfig.json` 的 `include` / `paths` 使 `.api` 可被解析）

## `.api` 本地契约目录（项目根目录）

从 Apifox MCP 解析某条接口后，**必须在仓库根目录**维护并行结构，便于人机查阅、diff 与少刷 MCP。

### 目录结构

```text
.api/
  <operation-folder>/
    spec.json    # OpenAPI 3.x 自包含片段（paths + 本接口涉及的 components.schemas）
    type.d.ts    # 与 spec 对齐的 TypeScript 声明（仅类型，不参与 declareRequest 逻辑）
```

### `<operation-folder>` 命名规则

1. 取 OpenAPI **`path`**，去掉首字符 `/`，其余 `/` 改为 **`-`**（kebab-case 路径段串联）。
2. 末尾拼接 **HTTP 方法小写**：`-get`、`-post`、`-put`、`-delete`、`-patch` 等。

**示例**

| path | method | 目录名 |
|------|--------|--------|
| `/ai/conversation/message/page` | GET | `ai-conversation-message-page-get` |
| `/ai/conversation/message/{id}` | GET | `ai-conversation-message-id-get`（若 Spec 中为字面量 `{id}`，文件夹名用字面量 `id`，与团队约定一致即可） |

同一路径多方法时：**每个方法单独一层目录**（如 `...-get` 与 `...-delete`）。

### `spec.json` 要求

- 顶层为合法 OpenAPI 3.x 文档最小子集：`openapi`、`info`（可简要说明同步来源）、`paths`（**仅当前接口**）、`components.schemas`（仅当前接口响应/请求体引用的模型）。
- **禁止使用未解析的 `$ref` 指向仓库外文件**；从 MCP 取到的引用应 **内联展开** 或合并进本文件的 `components.schemas`。
- `info.version` 可用 `1.0.0`；若 Apifox 有变更，以 **更新 spec + type** 为准。

### `type.d.ts` 要求

- 导出 **Query / Path / Body**（按接口实际存在项）及 **响应体** 中与业务相关的类型；命名可与后端 CO/VO 一致，或与 `spec.json` 中 schema 标题一致。
- 字段可选性、枚举用注释标出合法取值，与 `spec.json` **保持一致**。
- **`integer` / `int64`（尤其对应 Java `Long` 的主键/外键）**：在 JS 侧若存在超大整数风险，**本地契约与类型应使用 `string`**，不得默认定为 `number`；见上文「Apifox int64 与 Java Long」。
- 文件顶部用简短注释标明 **METHOD + path**，并指向同目录 `spec.json`。

### 与 MCP 的配合

- **`spec.json` + `type.d.ts` 齐全时**：视为权威快照，**禁止**仅为「再看一眼字段」而调用 MCP；以 Read 工具输出的本地文件为准。
- **例外**：用户说 **同步/刷新/对齐 Apifox**，或本地缺一文件、或新接口尚未落盘 → 再调用 MCP，并 **回写** 两个文件。
- **新增接口**：从 MCP 拉全量或按需拉 `$ref` 后，**新建**对应 `<operation-folder>`，勿与既有目录合并混淆。

## 最佳实践

- **先 `.api` 后 MCP**：有齐套本地契约则不调用 MCP（见上文「数据源优先级」）。
- **调用 MCP 时先查 schema**：阅读 `mcps/user-apifox/tools/` 下对应工具 descriptor，确认 `toolName` 与 `arguments`。
- **同步意图**：仅当用户要求或本地缺失时 `refresh_project_oas_*` / 读 Spec；通过后 **必更新** `spec.json` 与 `type.d.ts`。
- **结合规范**：生成接口代码时遵循项目 `api-data-layer`、`11-接口与数据层规范` 等技能

## 前置条件

- mcp.json 中已配置 `apifox`，且 `--site-id`（或 `--project-id`）指向正确项目
- 私有部署需配置 `APIFOX_ACCESS_TOKEN` 或对应环境变量
- Spec 数据本地缓存，Apifox 更新后需手动 `refresh`
