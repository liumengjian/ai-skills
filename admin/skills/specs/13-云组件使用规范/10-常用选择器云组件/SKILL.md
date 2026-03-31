---
name: jjb-cloud-component-selectors
description: 定义 JJB 常用选择器云组件使用规范。在使用人员选择器等选择器云组件时查阅。
---

# 云组件使用规范

## 常用选择器云组件

## 人员选择器云组件

人员选择器云组件用于选择人员信息，支持多选功能。

### 组件地址

```
https://cdn.cqjjb.cn/jcloud/use/plugin/8affaf90794911eebf4ca14dc4217ddd/latest
```

### 组件属性

| 属性 | 类型 | 必需 | 默认值 | 描述 |
|------|------|------|--------|------|
| `value` | `Array<{ id: string, name: string }>` | ❌ | `[]` | 已选中的数据 |
| `onOk` | `(data: Array<{ id: string, name: string }>) => void` | ❌ | - | 确认回调，返回选中的数据 |
| `onCancel` | `() => void` | ❌ | - | 取消回调 |

### 类型定义

```typescript
// 人员数据类型
interface Person {
  id: string;
  name: string;
}

// 组件属性类型
interface PersonSelectorProps {
  value?: Person[];
  onOk?: (data: Person[]) => void;
  onCancel?: () => void;
}
```

### 基础用法

```javascript
import React, { useState } from 'react';
import CloudComponent from '@cqsjjb/jjb-cloud-component/CloudComponent';

function MyPage() {
  const [selectedPersons, setSelectedPersons] = useState([
    { id: '1', name: '张三' },
    { id: '2', name: '李四' }
  ]);

  const handleOk = (data) => {
    setSelectedPersons(data);
    console.log('已选择人员:', data);
  };

  const handleCancel = () => {
    console.log('取消选择');
  };

  return (
    <CloudComponent
      from="https://cdn.cqjjb.cn/jcloud/use/plugin/8affaf90794911eebf4ca14dc4217ddd/latest"
      componentKey="person-selector"
      componentProps={{
        value: selectedPersons,
        onOk: handleOk,
        onCancel: handleCancel
      }}
    />
  );
}

export default MyPage;
```

### 完整示例

```javascript
import React, { useState } from 'react';
import { Button, message } from 'antd';
import CloudComponent from '@cqsjjb/jjb-cloud-component/CloudComponent';

function PersonSelectorExample() {
  const [selectedPersons, setSelectedPersons] = useState([]);
  const [visible, setVisible] = useState(false);

  const handleOk = (data) => {
    setSelectedPersons(data);
    setVisible(false);
    message.success(`已选择 ${data.length} 个人员`);
    console.log('已选择人员:', data);
  };

  const handleCancel = () => {
    setVisible(false);
    message.info('已取消选择');
  };

  return (
    <div>
      <div style={{ marginBottom: 16 }}>
        <Button type="primary" onClick={() => setVisible(true)}>
          选择人员
        </Button>
        {selectedPersons.length > 0 && (
          <div style={{ marginTop: 16 }}>
            <p>已选择人员：</p>
            <ul>
              {selectedPersons.map((person) => (
                <li key={person.id}>
                  {person.name} (ID: {person.id})
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>

      {visible && (
        <CloudComponent
          from="https://cdn.cqjjb.cn/jcloud/use/plugin/8affaf90794911eebf4ca14dc4217ddd/latest"
          componentKey="person-selector"
          componentProps={{
            value: selectedPersons,
            onOk: handleOk,
            onCancel: handleCancel
          }}
        />
      )}
    </div>
  );
}

export default PersonSelectorExample;
```
