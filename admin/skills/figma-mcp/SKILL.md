---
name: figma-mcp
description: Fetches Figma design layout and styling data via get_figma_data for accurate UI implementation. Use when implementing designs from Figma, when user pastes a Figma file/frame/group link, or when converting Figma designs to code.
---

# Framelink Figma MCP 工具

通过 `figma-developer-mcp` 将 Figma 设计数据提供给 AI，用于按设计稿实现 UI。

## 数据源优先级（必读）

回答布局、样式、文案，或据此写代码时：

1. **先用本地快照**：根据 Figma 链接解析 **`fileKey`** 与 **`node-id`**（见下），算出目录名 **`<fileKey>-<node-id>`**，检查项目根目录 **`.design/<folder>/meta.json`** 与 **`figma-data.md`** 是否都存在。
2. **若两者皆存在**：**不得**仅为查阅设计数据而调用 Figma MCP（`get_figma_data` / `download_figma_images`）。使用 Read 读取 **`meta.json`**、**`figma-data.md`**，需要像素级对照时 Read **`preview.png`**（若存在）。
3. **仅在以下情况调用 MCP**：
   - 本地无对应目录，或缺少 **`meta.json` / `figma-data.md` 之一**；
   - 用户 **明确要求** 与 Figma **同步 / 刷新 / 更新 / 对齐最新设计稿**（或同义表述）；
   - 用户 **点名** 要从 Figma 源拉取（而非使用仓库内 `.design`）。
4. MCP 拉取或修正设计后：在 **`.design/<fileKey>-<node-id>/`** **新建或更新** `meta.json`、`figma-data.md`；按需更新 `preview.png`。**目录与命名规则**见项目根目录 `.design/README.md`。

### `<fileKey>-<node-id>` 命名（与 `.design/README.md` 一致）

- 从 URL 取 `fileKey`：`figma.com/design/<fileKey>/...`
- 从查询参数取 `node-id`（如 `3-2069`），**保持连字符**，勿改为冒号用于文件夹名
- 文件夹名：`<fileKey>-<node-id>`（例：`77QC1ADlbxF4sUnKCnfyRU-3-2069`）

调用 MCP 时，工具参数中的 `nodeId` 通常使用 **`3:2069`**（冒号）；本地目录名仍用 URL 的 **`3-2069`**。

## 触发场景

在以下场景下使用本技能（并遵守上文优先级）：

- 用户粘贴 Figma 链接（文件 / Frame / Group）
- 要求按 Figma 设计稿实现 UI
- 将设计稿转化为代码（React、Vue 等）

## 核心工具

| 工具 | 用途 |
|------|------|
| `get_figma_data` | 根据 Figma 链接获取布局、样式等设计数据 |
| `download_figma_images` | 按需导出 PNG/SVG 等（如 `preview.png`） |

## 使用流程

1. **解析链接**：从用户粘贴的 URL 得到 `fileKey`、`node-id`，映射到 `.design/<fileKey>-<node-id>/`。
2. **本地命中**：若该目录下 **已有** `meta.json` 与 `figma-data.md` → **只读本地**，继续实现或对照；不调用 MCP。
3. **本地未命中或用户要求同步**：调用 `get_figma_data`（及按需 `download_figma_images`）。
4. **落盘**：回写 `.design/.../meta.json`、`figma-data.md`，可选 `preview.png`（导出文件须落在**项目仓库**的 `.design` 下，若工具写入其它路径应复制进项目）。
5. **生成代码**：根据快照中的布局与样式信息生成实现。

## 最佳实践

- **分块实现**：一次聚焦一个 Frame 或 Group，避免一次处理整个复杂页面
- **提供上下文**：说明技术栈（React/Vue）、组件库、命名偏好等，便于生成更符合项目的代码
- **设计命名**：Figma 中给 Frame 有意义的命名，有利于生成更合理的 class 名
- **反复对照**：本地 `figma-data.md` + `preview.png` 与 `.api` 契约同理，便于多轮修改不再刷 MCP

## 返回数据说明

MCP 会对 Figma API 返回做简化（约压缩 90%），只保留与布局、样式相关的内容，减少无关信息对模型的影响。落盘时可将该返回全文写入 **`figma-data.md`**（可用 `yaml` 代码块包裹便于阅读）。

## 前置条件

- mcp.json 中已配置 `Framelink Figma MCP`，且 `FIGMA_API_KEY` 或 `--figma-api-key` 已正确设置
- Figma 个人访问令牌需具备 File content 和 Dev resources 的读取权限
