---
name: jjb-form-required
description: 定义 JJB 项目表单必填标识规范。在使用 Form.Item required、rules 或禁止 label 自定义星号时使用。
---

# 表单与交互规范

## 表单组件

- **禁止在表单label属性中自定义必填星号效果**：

  - **强制要求**：禁止在表单 `label` 属性中手动添加星号（`*`）或其他自定义必填标识

  - **正确做法**：统一使用以下两种方式之一来标识必填字段：

    - **方式一**：使用 `required` 属性（推荐）
      ```javascript
      <Form.Item
        name="username"
        label="用户名"
        required
      >
        <Input placeholder="请输入用户名" />
      </Form.Item>
      ```

    - **方式二**：在 `rules` 中配置必填验证规则
      ```javascript
      <Form.Item
        name="username"
        label="用户名"
        rules={[{ required: true, message: '请输入用户名' }]}
      >
        <Input placeholder="请输入用户名" />
      </Form.Item>
      ```

  - **错误示例**（禁止）：
    ```javascript
    // ❌ 错误：在label中手动添加星号
    <Form.Item
      name="username"
      label="用户名 *"
    >
      <Input placeholder="请输入用户名" />
    </Form.Item>

    // ❌ 错误：在label中使用自定义必填标识
    <Form.Item
      name="username"
      label={<span>用户名 <span style={{ color: 'red' }}>*</span></span>}
    >
      <Input placeholder="请输入用户名" />
    </Form.Item>
    ```

  - **说明**：使用 `required` 属性或 `rules` 配置后，antd Form 组件会自动在 label 前添加红色星号，保持样式统一性和一致性