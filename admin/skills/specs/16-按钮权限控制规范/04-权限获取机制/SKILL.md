---
name: jjb-button-permission-fetch
description: 定义 JJB 按钮权限获取机制。在了解 /system/operation/menus/list/current/buttons-perms 接口调用时查阅。
---

# 按钮权限控制规范

## Permission 使用方式

- **按钮权限获取机制**：

  - 组件挂载时自动调用 `/system/operation/menus/list/current/buttons-perms` 接口获取当前页面的按钮权限列表

  - 接口参数：`{ path: window.location.pathname }`
