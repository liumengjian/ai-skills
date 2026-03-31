---
name: jjb-search-code-demo
description: 定义 JJB 项目搜索区代码演示示例。在实现 SearchForm 与 PageLayout 集成、formLine 或 onFinish 时参考。
---

# 搜索区规范（一级页面）

## 代码演示

```jsx
import { useState, useRef } from 'react';
import { Button, Form, Input } from 'antd';
import SearchForm from '@cqsjjb/jjb-react-admin-component/SearchForm';
import PageLayout from '@cqsjjb/jjb-react-admin-component/PageLayout';

function App() {
  const form = useRef();

  // 提交
  const onFinish = values => {

  }

  return (
    <PageLayout
      title="用户中心"
      formLine={(
        <SearchForm
          form={form}
          formLine={[
            <Form.Item
              noStyle
              name="keyword"
            >
              <Input
                allowClear
                placeholder="请输入关键字"
              />
            </Form.Item>
          ]}
          onReset={() => {
            form.current.submit();
          }}
          onFinish={onFinish}
        />
      )}
    >
      
    </PageLayout>
  )
}
```
