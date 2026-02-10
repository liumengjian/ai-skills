# 十六、按钮权限控制规范

## 2. Permission 使用方式

- **导入方式**：

  ```javascript
  import { Permission } from '@cqsjjb/jjb-common-decorator/permission';
  ```

- **使用方式**：使用装饰器语法包裹组件

  ```javascript
  import React from 'react';
  import { Permission } from '@cqsjjb/jjb-common-decorator/permission';

  function UserList(props) {
    const { permission } = props;
    
    return (
      <div>
        {permission('add') && <Button>新增</Button>}
        {permission('edit') && <Button>编辑</Button>}
        {permission(['add', 'edit']) && <Button>批量操作</Button>}
      </div>
    );
  }

  // 使用 Permission 装饰器
  export default Permission(UserList);
  ```

- **注入的 Props**：

  - `permission(code)`：按钮权限检查方法

    - 参数 `code`：按钮权限码（字符串）或按钮权限码数组

    - 返回值：`boolean`，表示是否有按钮权限

    - 数组参数：传入数组时，只要数组中任意一个按钮权限码存在即返回 `true`
