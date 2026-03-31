---
name: jjb-loading-reset
description: 定义 JJB Loading 状态重置规范。在使用 resetModelState、弹窗/抽屉关闭或 confirmLoading 时使用。
---

# 接口与数据层规范

## Loading 状态重置规范

> **⚠️ 重要约束**：当 `declareRequest` 定义的接口 Action 的 loading 状态（如 `loading`、`confirmLoading`、`submitLoading` 等）在可关闭组件或页面中使用时，**必须在组件销毁或关闭时调用 `resetModelState` 重置对应的 loading 字段**。

## 问题说明

`declareRequest` 定义的接口 Action 会自动管理 loading 状态（如 `loading`、`confirmLoading`、`submitLoading` 等）。但在以下场景中，loading 状态可能无法自动重置：

- 接口请求异常中断
- 弹窗/抽屉在请求过程中被关闭
- 组件卸载时请求仍在进行
- 页面跳转时请求仍在进行

这会导致 loading 状态一直保持为 `true`，下次打开组件或进入页面时仍然显示加载状态，影响用户体验。

## 适用场景

以下场景需要特别注意重置 loading 状态：

1. **弹窗（Modal）**：弹窗关闭时
2. **抽屉（Drawer）**：抽屉关闭时
3. **页面组件**：页面卸载时
4. **条件渲染组件**：组件被条件隐藏时
5. **路由切换**：路由跳转时

## 解决方案

在组件销毁或关闭时，调用 `resetModelState` 重置对应的 loading 字段。

## 使用示例

### ✅ 场景一：弹窗中使用 confirmLoading

```javascript
import { useContext, useState, useEffect } from 'react';
import { Modal, Form, Input, Button } from 'antd';
import { Connect } from '@cqsjjb/jjb-dva-runtime';
import { InjectContext } from '~/enumerate/context';
import { NS_USER } from '~/enumerate/namespace';

function UserList({ createUserAction, resetModelState }) {
  const context = useContext(InjectContext);
  const [form] = Form.useForm();
  const [modalOpen, setModalOpen] = useState(false);

  // ✅ 推荐：使用 useEffect 监听弹窗状态，关闭时重置 loading
  useEffect(() => {
    if (!modalOpen) {
      resetModelState(NS_USER, { confirmLoading: false });
    }
  }, [modalOpen, resetModelState]);

  const handleSubmit = async (values) => {
    const res = await createUserAction(values);
    if (res.success) {
      context.message.success('创建成功！');
      setModalOpen(false);
    }
  };

  return (
    <>
      <button onClick={() => setModalOpen(true)}>新增用户</button>
      <Modal
        open={modalOpen}
        title="新增用户"
        onCancel={() => setModalOpen(false)}
        footer={[
          <Button key="cancel" onClick={() => setModalOpen(false)}>
            取消
          </Button>,
          <Button
            key="submit"
            type="primary"
            loading={createUserAction?.confirmLoading}
            onClick={() => form.submit()}
          >
            确定
          </Button>
        ]}
      >
        <Form form={form} layout="vertical" onFinish={handleSubmit}>
          <Form.Item name="name" label="用户名">
            <Input placeholder="请输入用户名" allowClear />
          </Form.Item>
        </Form>
      </Modal>
    </>
  );
}

export default Connect([NS_USER], true)(UserList);
```

### ✅ 场景二：抽屉中使用 submitLoading

```javascript
import { useState, useEffect } from 'react';
import { Drawer, Form, Button } from 'antd';
import { Connect } from '@cqsjjb/jjb-dva-runtime';
import { NS_ORDER } from '~/enumerate/namespace';

function OrderDrawer({ updateOrderAction, resetModelState, drawerOpen, onClose }) {
  const [form] = Form.useForm();

  // ✅ 抽屉关闭时重置 loading 状态
  useEffect(() => {
    if (!drawerOpen) {
      resetModelState(NS_ORDER, { submitLoading: false });
    }
  }, [drawerOpen, resetModelState]);

  const handleSubmit = async (values) => {
    const res = await updateOrderAction(values);
    if (res.success) {
      onClose();
    }
  };

  return (
    <Drawer
      open={drawerOpen}
      onClose={onClose}
      footer={
        <Button
          type="primary"
          loading={updateOrderAction?.submitLoading}
          onClick={() => form.submit()}
        >
          提交
        </Button>
      }
    >
      <Form form={form} onFinish={handleSubmit}>
        {/* 表单内容 */}
      </Form>
    </Drawer>
  );
}

export default Connect([NS_ORDER], true)(OrderDrawer);
```

### ✅ 场景三：页面组件中使用 loading

```javascript
import { useEffect } from 'react';
import { Connect } from '@cqsjjb/jjb-dva-runtime';
import { NS_PRODUCT } from '~/enumerate/namespace';

function ProductDetail({ product, fetchProductAction, resetModelState, productId }) {
  useEffect(() => {
    if (productId) {
      fetchProductAction({ id: productId });
    }

    // ✅ 组件卸载时重置 loading 状态
    return () => {
      resetModelState(NS_PRODUCT, { loading: false });
    };
  }, [productId, fetchProductAction, resetModelState]);

  if (product?.loading) {
    return <div>加载中...</div>;
  }

  return <div>{product?.data?.name}</div>;
}

export default Connect([NS_PRODUCT], true)(ProductDetail);
```

### ✅ 场景四：条件渲染组件中使用 loading

```javascript
import { useState, useEffect } from 'react';
import { Connect } from '@cqsjjb/jjb-dva-runtime';
import { NS_USER } from '~/enumerate/namespace';

function UserForm({ createUserAction, resetModelState, visible }) {
  const [form] = Form.useForm();

  // ✅ 组件隐藏时重置 loading 状态
  useEffect(() => {
    if (!visible) {
      resetModelState(NS_USER, { confirmLoading: false });
    }
  }, [visible, resetModelState]);

  if (!visible) {
    return null;
  }

  return (
    <Form form={form} onFinish={(values) => createUserAction(values)}>
      {/* 表单内容 */}
      <Button
        type="primary"
        htmlType="submit"
        loading={createUserAction?.confirmLoading}
      >
        提交
      </Button>
    </Form>
  );
}

export default Connect([NS_USER], true)(UserForm);
```

### ✅ 场景五：路由跳转时重置 loading

```javascript
import { useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import { Connect } from '@cqsjjb/jjb-dva-runtime';
import { NS_ORDER } from '~/enumerate/namespace';

function OrderList({ orderList, fetchOrderListAction, resetModelState }) {
  const location = useLocation();

  useEffect(() => {
    fetchOrderListAction();
  }, []);

  // ✅ 路由切换时重置 loading 状态
  useEffect(() => {
    return () => {
      resetModelState(NS_ORDER, { loading: false, confirmLoading: false });
    };
  }, [location.pathname, resetModelState]);

  return (
    <div>
      {/* 列表内容 */}
    </div>
  );
}

export default Connect([NS_ORDER], true)(OrderList);
```

## 核心原则

1. **必须重置**：当 loading 状态来源于 `declareRequest` 时，组件销毁或关闭时必须重置
2. **重置时机**：
   - 弹窗/抽屉：在 `onCancel`、`afterClose` 或 `useEffect` 中监听关闭状态
   - 页面组件：在 `useEffect` 清理函数中重置
   - 条件渲染：在 `useEffect` 中监听显示状态
   - 路由切换：在 `useEffect` 清理函数中重置
3. **重置字段**：根据 `declareRequest` 中定义的 loading 字段名进行重置（如 `loading`、`confirmLoading`、`submitLoading` 等）
4. **命名空间**：使用正确的命名空间常量（如 `NS_USER`）调用 `resetModelState`
5. **批量重置**：可以一次性重置多个 loading 字段

## 批量重置示例

```javascript
// ✅ 一次性重置多个 loading 字段
useEffect(() => {
  if (!modalOpen) {
    resetModelState(NS_USER, {
      loading: false,
      confirmLoading: false,
      submitLoading: false
    });
  }
}, [modalOpen, resetModelState]);
```

## 相关规范

- 关于 `resetModelState` 的详细用法，请参考 [`命名空间与视图连接`](../03-命名空间与视图连接/SKILL.md)
- 关于 `declareRequest` 的 loading 状态定义，请参考 [`接口定义规范`](../02-接口定义规范/SKILL.md)
