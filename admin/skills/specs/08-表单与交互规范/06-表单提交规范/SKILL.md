---
name: jjb-form-submit
description: 定义 JJB 项目表单提交规范。在配置提交按钮、loading 防重提交或 declareRequest 时使用。
---

# 表单与交互规范

## 表单提交

- 所有提交按钮：

  - 必须有 loading 防重提交，loading 字段来源 `declareRequest` 具体参考运行时 MD 文档