# 二、应用配置与开发环境

## 9. HTML 模板配置

- **配置来源**：HTML 模板配置来源于根目录 `jjb.config.js` 文件中的 `windowInject` 属性

- **配置结构**：

  ```javascript
  // jjb.config.js
  {
    windowInject: {
      // 应用标题
      title: '微应用',
      // 注入 CSS 链接集合
      links: ['https://test.test.com/index.js'],
      element: {
        root: {
          // 挂载 DOM 元素 ID
          id: 'root',
        },
      },
      // 注入 JS 链接集合
      scripts: ['https://test.test.com/index.js'],
    }
  }
  ```

- **配置说明**：

  - **title**：应用标题，会注入到 HTML 模板的 `<title>` 标签中

  - **links**：CSS 样式文件链接数组，用于在 HTML 头部注入外部样式表

  - **element.root.id**：React 应用挂载的 DOM 元素 ID，默认为 `'root'`

  - **scripts**：JavaScript 文件链接数组，用于在 HTML 中注入外部脚本文件

- **模板使用方式**：在 `index.html` 模板中通过 EJS 模板语法访问配置

  - **变量注入**：`windowInject` 配置会注入到 `htmlWebpackPlugin.options` 中，需要在模板中先解构获取变量

  - **模板示例**：

    ```html
    <!-- 解构配置变量 -->
    <% var { links, scripts, element, title } = htmlWebpackPlugin.options %>

    <!-- 注入 CSS 链接 -->
    <% for (const item of links) { %>
      <link type="text/css" rel="stylesheet" href="<%= item %>"></link>
    <% } %>

    <!-- 注入 JS 脚本 -->
    <% for (const item of scripts) { %>
      <script src="<%= item %>" type="text/javascript"></script>
    <% } %>

    <!-- 使用元素配置 -->
    <% const { root } = element; %>
    <div id="<%= root.id %>" style="width: 100%; height: 100%; position: relative"></div>
    ```

  - **变量说明**：

    - `links`：对应配置中的 `links` 数组，用于循环注入 CSS 链接

    - `scripts`：对应配置中的 `scripts` 数组，用于循环注入 JS 脚本

    - `element`：对应配置中的 `element` 对象，用于访问挂载元素配置

    - `title`：对应配置中的 `title` 字符串，可用于设置页面标题

- **使用场景**：适用于需要在 HTML 模板中动态注入外部资源（CSS、JS）或配置应用挂载点的场景
