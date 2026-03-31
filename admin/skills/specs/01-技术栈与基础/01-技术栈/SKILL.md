---
name: jjb-tech-stack
description: 定义 JJB 项目的标准技术栈。在构建 React 组件、配置项目依赖、选择库或遵循技术规范时使用。涵盖 React、antd、less、dva 运行时及日期处理。
---

# 技术栈与基础

## 技术栈

在项目开发中必须严格遵循以下技术栈选型：

- **React 18 + JSX**：核心 UI 框架

- **antd v5**：基础组件库

- **less**：样式预处理器

- **状态与运行时**：@cqsjjb/jjb-dva-runtime（基于 dvajs）

- **日期处理**：统一使用 dayjs 处理日期格式

## 使用说明

当编写代码或选择依赖时，应优先采用上述技术栈，不得引入与本规范冲突的替代方案（如 moment、其他 UI 库等）。
