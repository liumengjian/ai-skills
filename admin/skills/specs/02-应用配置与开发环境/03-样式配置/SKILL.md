---
name: jjb-style-config
description: 定义 JJB 项目样式配置规范。在导入 CSS/LESS、配置样式或选用样式格式时使用。微应用仅支持 .css 和 .less，禁止使用 scss、sass、stylus 等。覆盖 antd 时须注意 ant-prefix：勿使用默认 .ant-* 类名。
---

# 应用配置与开发环境

## 样式配置

- **CSS 样式导入**：使用 ESM 方式导入 CSS 样式文件

  ```javascript
  import './index.css';
  ```

- **LESS 样式导入**：使用 ESM 方式导入 LESS 样式文件

  ```javascript
  import './index.less';
  ```

- **支持的样式格式**：

  - **CSS**：支持 `.css` 格式的样式文件

  - **LESS**：支持 `.less` 格式的预处理样式文件

  - **格式限制**：**微应用仅支持 `.css` 和 `.less` 样式文件，其他格式（如 `.scss`、`.sass`、`.stylus` 等）不支持，禁止使用**

- **注意事项**：

  - 样式文件导入后会自动应用到当前组件或页面

  - LESS 文件支持嵌套、变量、混合等预处理特性

  - 样式文件路径可以使用相对路径或路径别名 `~`

  - 建议将样式文件与对应的组件文件放在同一目录下，便于管理

- **覆盖 antd 内部类名时的前缀约束**：

  - 项目通过 `jjb.config.js` 的 `framework.antd['ant-prefix']` 与 `Container` 中 `ConfigProvider` 的 `prefixCls` 修改了 antd 的类名前缀，**DOM 上不会出现文档中的默认 `ant-*` 类名**（详见 [`应用标识符与路由配置`](../01-应用标识符与路由配置/SKILL.md) 中「Ant Design 类名前缀」）。

  - 在 Less 中写 `.ant-form-item`、`.ant-tree-treenode` 等选择器**无效**；应改为与当前项目一致的 **`${ant-prefix}-*`**（从 `jjb.config.js` 读取实际值），或采用外层自有 `className` 包裹 + 有限子选择器，避免硬编码错误前缀。
