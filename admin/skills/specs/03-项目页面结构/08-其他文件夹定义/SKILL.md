---
name: jjb-other-folders
description: 定义 JJB 项目其他文件夹用途。在了解 utils、enumerate、constant、context、hooks 等目录定义时使用。
---

# 项目页面结构

## 其他文件夹定义

- 工具库：`src/utils/index.js`

- 枚举值：`src/enumerate/enum/index.js`
  - 用于维护后端返回数据中的枚举值
  - 详细使用规范请参考 [`09-枚举值使用规范`](../09-枚举值使用规范/SKILL.md)

- 常量：`src/enumerate/constant/index.js`

- React 全局 Context：`src/enumerate/context/index.js`

- Hooks 目录：`src/hooks/`（用于存放自定义 Hooks）
