---
name: jjb-dva-runtime
description: 定义 JJB 后台应用必须使用的全局运行时规范。在搭建应用运行时、配置路由与 model 或进行状态管理时使用。基于 @cqsjjb/jjb-dva-runtime，实现自动化路由与 model 注册、接口 loading 与状态统一管理。
---

# 技术栈与基础

## 全局运行时规范

- 所有后台应用 **必须** 使用 `@cqsjjb/jjb-dva-runtime` 作为应用运行时

- 实现能力：

  - 自动化路由注册

  - 自动化 model 注册

  - 接口 loading / 状态统一管理
