# 十七、接口动态文本配置

## 2. Interpolation 使用方式

- **导入方式**：

  ```javascript
  import { Interpolation } from '@cqsjjb/jjb-common-decorator/namespace';
  ```

- **使用方式**：使用高阶组件（HOC）包裹页面组件

  ```javascript
  import React from 'react';
  import { Interpolation } from '@cqsjjb/jjb-common-decorator/namespace';

  function UserList(props) {
    const { interpolation, insert, columns } = props;
    
    // 使用 insert 方法获取字段重命名文本
    const userNameLabel = insert('userName') || '用户名';
    
    // 使用 columns 方法处理表格列配置
    const tableColumns = columns([
      { fieldCode: 'userName', dataIndex: 'name', width: 200 },
      { fieldCode: 'email', dataIndex: 'email', width: 200 },
      { dataIndex: 'phone', title: '手机号', width: 150 } // 没有 fieldCode 的列不受影响
    ]);
    
    return (
      <div>
        <div>{userNameLabel}: 张三</div>
        <Table columns={tableColumns} dataSource={data} />
      </div>
    );
  }

  // 使用 Interpolation 包裹组件
  export default Interpolation(UserList);
  ```
