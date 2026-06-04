---
name: jjb-theme-color-variables
description: 定义 JJB 主题色变量配置规范。在使用 @colorPrimary、process.env.app.antd、jjb.config.js framework 配置时查阅。
---

# 环境变量与数据访问

## 主题色变量

- **Less 文件**：使用 `@colorPrimary` 变量

- **JSX 内联样式**：使用 `process.env.app.antd['colorPrimary']` 变量

- **配置来源**：主题色配置来源于根目录 `jjb.config.js` 文件中的 `framework` 属性

- **`ant-prefix`（类名前缀）**：`framework.antd['ant-prefix']` 会注入为 `process.env.app.antd['ant-prefix']`，并在 `Container` 的 `ConfigProvider` 上作为 `prefixCls` 使用。antd 组件 DOM 类名为 **`${ant-prefix}-*`**，不是默认的 `ant-*`。**在 Less/CSS 中覆盖 antd 内部样式时不得使用 `.ant-` 选择器**，详见 [`应用标识符与路由配置`](../../02-应用配置与开发环境/01-应用标识符与路由配置/SKILL.md) 中「Ant Design 类名前缀」。

- **配置结构**：

  ```javascript
  // jjb.config.js
  {
    framework: {
      antd: {
        'ant-prefix': 'app-open-maic', // 示例：常与 appIdentifier 对应为 app-${appIdentifier}
        colorPrimary: '#1890ff'
      }
    }
  }
  ```

- **访问方式**：在 JSX 代码中通过 `process.env.app.antd['colorPrimary']` 即可访问配置的主题色值

- **扩展支持**：`framework.antd` 配置支持扩展其他 Less 变量，可在 `jjb.config.js` 中配置任意 antd 主题变量

  - **配置示例**：

    ```javascript
    // jjb.config.js
    {
      framework: {
        antd: {
          colorPrimary: '#1890ff',
          borderRadius: 6,
          colorSuccess: '#52c41a',
          // 可扩展其他 antd 主题变量
        }
      }
    }
    ```

  - **Less 文件使用**：配置的变量会自动注入为 Less 变量，在 `.less` 文件中可直接使用 `@colorPrimary`、`@borderRadius` 等变量

  - **JSX 内联样式使用**：通过 `process.env.app.antd['变量名']` 访问扩展的变量
