---
name: jjb-table-scroll-height
description: 定义 JJB 项目表格滚动高度规范。在使用 AntdTableFuncControl、Connect 装饰器、scrollY 或表格滚动时使用。
---

# 表格（Table）规范

## 表格滚动高度

- 使用 `antd/Table` 的页面组件 **必须** 使用 `AntdTableFuncControl` 装饰器

- `AntdTableFuncControl` 用于为表格组件提供自动计算滚动高度的功能

- **导入方式**：

```javascript
import { AntdTableFuncControl } from '@cqsjjb/jjb-common-decorator/antd';
```

- **使用方式**：与 `Connect` 装饰器组合使用，`AntdTableFuncControl` 作为内层装饰器

```javascript
export default Connect([NS_BASIC], true)(AntdTableFuncControl(Field));
```

- **注入的 Props**：

  - `scrollY`：自动计算的表格滚动高度，可直接用于 Table 组件的 `scroll.y` 配置

### 代码演示

```jsx
import React, { useState, useEffect, useRef } from 'react';
import { Connect } from '@cqsjjb/jjb-dva-runtime';
import { AntdTableFuncControl } from '@cqsjjb/jjb-common-decorator/antd';
import { Table } from 'antd';
import { NS_BASIC } from '~/enumerate/namespace';

const Field = ({
  basicInfo: {
    fieldLoading,
    fieldList = [],
    fieldListTotal
  } = {},
  getFieldList,
  scrollY  // AntdTableFuncControl 注入的滚动高度
}) => {
  const [pageObj, setPageObj] = useState({
    pageIndex: 1,
    pageSize: 10
  });

  useEffect(() => {
    getFieldList({
      ...pageObj
    });
  }, [pageObj]);

  return (
    <Table
      rowKey="id"
      scroll={{
        y: scrollY - 16  // 使用注入的 scrollY，减去间距
      }}
      loading={fieldLoading}
      columns={[
        {
          title: '名称',
          dataIndex: 'name',
          key: 'name'
        },
        {
          title: '编码',
          dataIndex: 'code',
          key: 'code'
        }
      ]}
      pagination={{
        total: fieldListTotal,
        current: pageObj.pageIndex,
        pageSize: pageObj.pageSize,
        onChange: (pageIndex, pageSize) => {
          setPageObj({
            pageSize,
            pageIndex
          });
        }
      }}
      dataSource={fieldList}
    />
  );
};

// AntdTableFuncControl 作为内层装饰器，Connect 作为外层装饰器
export default Connect([NS_BASIC], true)(AntdTableFuncControl(Field));
```

### 使用要点

1. **装饰器顺序**：`AntdTableFuncControl` 必须作为内层装饰器，`Connect` 作为外层装饰器

2. **scrollY 使用**：`scrollY` 会自动根据页面布局计算，通常需要减去一定的间距（如 16px）以适应页面布局

3. **必须使用场景**：所有使用 `antd/Table` 的页面组件都必须使用此装饰器，以确保表格滚动高度正确计算

### 注意事项

- `scrollY` 的值会根据页面布局自动计算，无需手动设置

- 如果表格上方有其他元素（如搜索表单、标题等），`scrollY` 会自动考虑这些元素的高度

- 禁止在组件内部手动计算或设置表格滚动高度，必须使用 `AntdTableFuncControl` 提供的 `scrollY`
