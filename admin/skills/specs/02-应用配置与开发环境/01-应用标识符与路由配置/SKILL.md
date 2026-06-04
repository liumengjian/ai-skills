---
name: jjb-app-identifier-routing
description: 定义 JJB 应用标识符与路由配置规范。在配置 jjb.config.js、设置 appIdentifier 或了解构建产物命名规则时使用。基于 appIdentifier 实现路由 basename 与构建产物命名。含 framework.antd ant-prefix 与 ConfigProvider：antd DOM 类名为 ${ant-prefix}-*，勿用默认 ant-* 写样式。
---

# 应用配置与开发环境

## 应用标识符与路由配置

- **应用标识符 (appIdentifier)**：

  - 位置：根目录 `jjb.config.js` 文件中的 `appIdentifier` 属性

  - 作用：
    - 作为应用的唯一标识符，`@cqsjjb/jjb-dva-runtime` 基于此属性自动生成应用路由的 `basename`
    - `@cqsjjb/scripts` 基于此属性实现构建产物的命名

  - 构建产物命名规则：`@cqsjjb/scripts` 会根据 `appIdentifier` 的值生成对应的构建产物目录和文件
    - 示例：当 `appIdentifier = 'myApp'` 时，构建产物结构为：
      ```
      dist/
      ├── myApp/
      │   └── static/
      │       └── ...
      └── myApp.html
      ```

  - 修改方式：在根目录 `jjb.config.js` 文件的 `appIdentifier` 节点中进行配置

- **Ant Design 类名前缀（`ant-prefix`）与 `appIdentifier` 的约束**：

  - **配置位置**：根目录 `jjb.config.js` → `framework.antd['ant-prefix']`。微应用模板中通常与 `appIdentifier` 对应为 **`app-${appIdentifier}`**（示例：`appIdentifier: 'open-maic'` → `'ant-prefix': 'app-open-maic'`），**以项目实际配置为准**。

  - **运行时行为**：`src/pages/Container/index.js` 中 `ConfigProvider` 使用 `prefixCls={window.process.env.app.antd['ant-prefix']}`（与上述配置一致）。因此 antd 组件在 DOM 上的类名**不是**官方文档中的默认 `ant-*`，而是 **`${ant-prefix}-*`**（示例：`ant-btn` → `app-open-maic-btn`，`ant-tree-treenode` → `app-open-maic-tree-treenode`）。

  - **禁止假设 `ant-` 前缀**：编写 **Less/CSS 覆盖**、**E2E 选择器**、**从 antd 文档复制的样式片段** 时，不得写死 `.ant-btn`、`.ant-tree-*` 等默认类名，否则在本项目中**不会命中任何节点**。

  - **推荐做法**：
    - 优先给业务根节点设置自有 `className`（如 `className="xxx-page__tree"`），样式写在该类名下，仅必要时用**不依赖前缀**的选择方式（如 `[class*='-tree-treenode']` 等，需带注释并限定在外层容器内，避免误伤）；
    - 或在样式中显式使用当前项目的完整前缀（与 `jjb.config.js` 中 `ant-prefix` 保持一致，**模板/多应用时注意随项目变更**）。

  - **相关规范**：样式文件通用约定见 [`样式配置`](./../03-样式配置/SKILL.md)；主题与 `framework.antd` 见 [`主题色变量`](./../../14-环境变量与数据访问/01-主题色变量/SKILL.md)。
