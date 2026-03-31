---
name: jjb-button-permission-best-practices
description: 定义 JJB 按钮权限控制最佳实践。在使用 permission 方法、权限码命名、批量权限控制时查阅。
---

# 按钮权限控制规范

## 按钮权限控制最佳实践

- **按钮权限控制**：

  ```javascript
  // 使用 Permission + permission 方法
  {permission('add') && <Button>新增</Button>}
  ```

- **批量按钮权限控制**：

  ```javascript
  // 多个按钮权限中任意一个有按钮权限即显示
  {permission(['add', 'edit', 'delete']) && <Button>批量操作</Button>}
  ```

- **按钮权限码命名规范**：

  - 使用小驼峰命名，例如：`add`、`edit`、`delete`、`export`、`import`

  - 按钮权限码应与后端接口返回的按钮权限码保持一致

- **注意事项**：

  - 按钮权限加载期间会显示 Loading 状态，确保用户体验
