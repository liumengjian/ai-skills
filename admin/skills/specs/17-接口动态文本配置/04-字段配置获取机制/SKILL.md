---
name: jjb-interpolation-field-config
description: 定义 JJB 字段配置获取机制。在了解 /system/operation/menus/menu-field/by-path 接口及返回数据结构时查阅。
---

# 接口动态文本配置

## 字段配置获取机制

- **接口调用**：组件挂载时自动调用 `/system/operation/menus/menu-field/by-path` 接口获取字段配置

- **接口参数**：`{ path: window.location.pathname }`

- **接口返回数据结构**：

  ```javascript
  {
    data: [
      {
        fieldCode: 'userName',      // 字段码
        fieldRename: '用户姓名',     // 字段重命名文本
        visibleEnum: false           // 是否可见（false 表示可见）
      },
      {
        fieldCode: 'email',
        fieldRename: '电子邮箱',
        visibleEnum: false
      }
    ]
  }
  ```
