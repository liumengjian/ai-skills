---
name: figma-mcp
description: Fetches Figma design layout and styling data via get_figma_data for accurate UI implementation. Use when implementing designs from Figma, when user pastes a Figma file/frame/group link, or when converting Figma designs to code.
---

# Framelink Figma MCP 工具

通过 `figma-developer-mcp` 将 Figma 设计数据提供给 AI，用于按设计稿实现 UI。

## 触发场景

在以下场景下优先调用 Figma MCP：

- 用户粘贴 Figma 链接（文件 / Frame / Group）
- 要求按 Figma 设计稿实现 UI
- 将设计稿转化为代码（React、Vue 等）

## 核心工具

| 工具 | 用途 |
|------|------|
| `get_figma_data` | 根据 Figma 链接获取布局、样式等设计数据 |

## 使用流程

1. **获取链接**：在 Figma 中右击 Frame 或 Group → `Copy/Paste as` → `Copy link to selection`
2. **发起请求**：在对话中粘贴链接，并说明需求（如「按这个设计实现组件」）
3. **调用工具**：Agent 使用 `get_figma_data` 拉取设计数据
4. **生成代码**：根据返回的布局和样式信息生成对应实现代码

## 最佳实践

- **分块实现**：一次聚焦一个 Frame 或 Group，避免一次处理整个复杂页面
- **提供上下文**：说明技术栈（React/Vue）、组件库、命名偏好等，便于生成更符合项目的代码
- **设计命名**：Figma 中给 Frame 有意义的命名，有利于生成更合理的 class 名

## 返回数据说明

MCP 会对 Figma API 返回做简化（约压缩 90%），只保留与布局、样式相关的内容，减少无关信息对模型的影响。

## 前置条件

- mcp.json 中已配置 `Framelink Figma MCP`，且 `FIGMA_API_KEY` 或 `--figma-api-key` 已正确设置
- Figma 个人访问令牌需具备 File content 和 Dev resources 的读取权限
