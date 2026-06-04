---
name: jjb-detail-presentation
description: 定义 JJB 详情展示数据呈现规范。在使用 antd/Descriptions、结构化展示或纯文本数据时使用。
---

# 详情展示规范

本规范旨在统一系统内所有详情类场景（Modal、Drawer、独立页面）的交互体验与视觉呈现。

## 数据呈现规范 (Data Presentation)

- **结构化展示**：详情页中的**纯文本数据展示**，**必须** 使用 `antd/Descriptions` 组件进行结构化排版。

- **适用范围**：上述 `Descriptions` 约定对 **独立详情页、Modal 内详情、Drawer 内详情** 均适用，无例外。

- **禁止行为**：

  - 禁止使用原生的 `div`、`p` 标签进行简单的文本堆砌。

  - 禁止使用 `Row` / `Col` 手动模拟表单布局，除非 `Descriptions` 无法满足极特殊的排版需求。

  - **禁止**为 `Descriptions` 设置 **`bordered`** 属性（含 `bordered={true}`）。不要因「表格感」或习惯用法而添加；视觉规范以无表线样式为准。

- **视觉一致性**：应根据数据量的大小，合理配置 `Descriptions` 的 `column` 属性（通常建议为 2 或 3；极窄区域如侧拉抽屉可用 `column={1}`，需与可读性权衡）。

- **实现自检**：编写或 Code Review 详情区时，显式确认未使用 `bordered`。
