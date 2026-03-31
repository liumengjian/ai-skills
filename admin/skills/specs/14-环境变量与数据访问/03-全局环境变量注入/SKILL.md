---
name: jjb-global-env-inject
description: 定义 JJB 全局环境变量注入规范。在使用 contextInject、process.env.app、window.process.env.app、iframe 或云组件访问变量时查阅。
---

# 环境变量与数据访问

## 全局环境变量注入

- **配置来源**：全局环境变量配置来源于根目录 `jjb.config.js` 文件中的 `contextInject` 属性

- **配置结构**：

  ```javascript
  // jjb.config.js
  {
    contextInject: {
      appName: '应用名称',
      version: '1.0.0',
      // 可注入任意自定义变量
    }
  }
  ```

- **注入机制**：`contextInject` 中配置的所有属性会自动注入到 `process.env.app` 对象中

- **访问方式**：在代码中通过 `process.env.app.变量名` 访问注入的全局变量

  - **示例**：

    ```javascript
    // 配置
    {
      contextInject: {
        appName: '应用名称'
      }
    }

    // 访问
    const appName = process.env.app.appName; // '应用名称'
    ```

- **双重访问方式**：除了通过 `process.env.app` 访问变量，还可以通过 `window.process.env.app` 访问变量，它们是等价的

  - **实现机制**：`window.process.env.app` 实际上是在 `index.html` 模板中手动绑定 `process.env.app` 的

  - **使用场景区别**：

    - **`process.env.app`**：只能在应用内使用，一旦脱离应用就无法访问

    - **`window.process.env.app`**：挂载到 `window` 对象上，可以在以下场景中访问：

      - **iframe 场景**：应用中使用 iframe 加载其他网页时，在 iframe 中无法访问 `process.env.app`，但可以通过 `window.process.env.app` 访问

      - **云组件场景**：在云组件中访问应用的变量时，可以通过 `window.process.env.app` 访问

  - **示例**：

    ```javascript
    // 应用内访问（两种方式等价）
    const apiHost1 = process.env.app.API_HOST;
    const apiHost2 = window.process.env.app.API_HOST;

    // iframe 或云组件中访问（只能使用 window 方式）
    const apiHost = window.process.env.app.API_HOST;
    ```

- **使用场景**：适用于需要在代码中全局访问的应用配置信息，如应用名称、版本号、业务标识等
