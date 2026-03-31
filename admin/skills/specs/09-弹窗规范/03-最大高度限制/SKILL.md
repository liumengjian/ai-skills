---
name: jjb-modal-max-height
description: 定义 JJB 项目 Modal 弹窗最大高度限制。在设置 styles.body、maxHeight 或 calc(100vh - 200px) 时使用。
---

# 弹窗（Modal）规范

- **最大高度限制**：**仅适用于 Modal 组件**。Modal 弹窗的最大高度不能超过窗口高度的 `100vh - 200px`，必须通过 `styles.body` 设置 `maxHeight: 'calc(100vh - 200px)'`。
- **不适用范围**：此规范不适用于 Drawer 组件或自定义弹窗组件。