# 三、项目页面结构

## 2. InjectContext 使用规范

- **强制约束**：禁止直接使用 `antd` 的静态方法（`Modal.confirm`、`message.success()`、`notification.info()` 等），必须通过 `InjectContext` 获取 `context.modal`、`context.message`、`context.notification` 使用
- **允许使用**：允许使用 `<Modal>` 组件标签形式（非静态方法）
- **使用方式**：在组件中使用 `useContext(InjectContext)` 获取上下文对象
- **使用示例**：
  ```javascript
  import React, { useContext } from 'react';
  import { Modal } from 'antd';
  import { InjectContext } from '~/enumerate/context';

  function MyComponent() {
    const context = useContext(InjectContext);
    const [modalOpen, setModalOpen] = useState(false);

    const handleSuccess = () => {
      // ✅ 正确：使用 context.message 替代 message.success() 静态方法
      context.message.success('操作成功！');
      // ❌ 错误：禁止使用 message.success() 静态方法
      // message.success('操作成功！');
    };

    const handleDelete = () => {
      // ✅ 正确：使用 context.modal.confirm 替代 Modal.confirm 静态方法
      context.modal.confirm({
        title: '确认删除',
        content: '确定要删除这条记录吗？',
        onOk: () => {
          // 删除逻辑
        },
      });
      // ❌ 错误：禁止使用 Modal.confirm 静态方法
      // Modal.confirm({ ... });
    };

    const handleNotify = () => {
      // ✅ 正确：使用 context.notification 替代 notification.info() 静态方法
      context.notification.info({
        message: '提示',
        description: '这是一条通知消息',
      });
      // ❌ 错误：禁止使用 notification.info() 静态方法
      // notification.info({ ... });
    };

    return (
      <div>
        <button onClick={handleSuccess}>成功提示</button>
        <button onClick={handleDelete}>删除确认</button>
        <button onClick={handleNotify}>通知</button>
        {/* ✅ 正确：允许使用 <Modal> 组件标签 */}
        <Modal
          open={modalOpen}
          onCancel={() => setModalOpen(false)}
          title="弹窗标题"
        >
          弹窗内容
        </Modal>
      </div>
    );
  }
  ```
