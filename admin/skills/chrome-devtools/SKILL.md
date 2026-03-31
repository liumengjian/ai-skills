---
name: chrome-devtools
description: Use Chrome DevTools MCP tools for browser automation, debugging, performance analysis, and web inspection. Use when automating browser actions, testing web pages, taking screenshots, analyzing network requests, running Lighthouse audits, or debugging frontend issues.
---

# Chrome DevTools MCP 工具

通过 `chrome-devtools-mcp` MCP 服务控制并检测 Chrome 浏览器，用于自动化、调试和性能分析。

## 触发场景

在以下场景下优先调用 Chrome DevTools MCP 工具：

- 浏览器自动化：点击、填写表单、导航、截图
- 前端调试：查看 Console 消息、网络请求、DOM 快照
- 性能分析：录制 Trace、Lighthouse 审计、内存快照
- 页面测试：模拟交互、验证页面行为

## 工具分类

### 输入自动化

| 工具 | 用途 |
|------|------|
| `click` | 点击元素 |
| `fill` / `fill_form` | 填写单个输入或完整表单 |
| `type_text` | 模拟键入文本 |
| `hover` | 悬停元素 |
| `press_key` | 按下键盘按键 |
| `drag` | 拖拽操作 |
| `handle_dialog` | 处理弹窗（alert/confirm） |
| `upload_file` | 上传文件 |

### 导航与页面

| 工具 | 用途 |
|------|------|
| `navigate_page` | 打开 URL |
| `new_page` | 新建标签页 |
| `list_pages` | 列出所有页面 |
| `select_page` | 切换当前页面 |
| `close_page` | 关闭页面 |
| `wait_for` | 等待元素或条件 |

### 调试与检查

| 工具 | 用途 |
|------|------|
| `take_screenshot` | 截取页面截图 |
| `take_snapshot` | 获取 DOM 快照 |
| `list_console_messages` | 列出 Console 消息 |
| `list_network_requests` | 列出网络请求 |
| `evaluate_script` | 在页面中执行 JS |
| `lighthouse_audit` | 运行 Lighthouse 审计 |

### 性能分析

| 工具 | 用途 |
|------|------|
| `performance_start_trace` | 开始性能录制 |
| `performance_stop_trace` | 停止并保存 Trace |
| `performance_analyze_insight` | 分析性能洞察 |
| `take_memory_snapshot` | 内存快照 |

## 使用须知

1. **前置条件**：确保 mcp.json 中 `chrome-devtools` 已配置，且 Chrome 可启动（本机使用 `--executablePath` 指定 Chrome 路径）。
2. **首次调用**：首次使用需要浏览器的工具时，MCP 会自动启动 Chrome。
3. **敏感信息**：工具会暴露浏览器内容和 DevTools 数据，避免在含敏感信息的页面使用。
4. **选择器**：`click`、`fill` 等常用 CSS 选择器；优先使用有含义的 `id`、`data-*` 或 `role` 属性。

## 典型流程

**表单自动化示例：**
1. `navigate_page` 打开目标 URL
2. `fill_form` 或 `fill` 填写表单
3. `click` 提交
4. `wait_for` 等待结果
5. `take_screenshot` 或 `take_snapshot` 验证

**性能分析示例：**
1. `navigate_page` 打开目标页面
2. `performance_start_trace` 开始录制
3. 执行需要的交互（如 `click`、`fill`）
4. `performance_stop_trace` 停止录制
5. `performance_analyze_insight` 查看分析结果
