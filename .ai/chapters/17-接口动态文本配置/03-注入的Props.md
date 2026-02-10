# 十七、接口动态文本配置

## 3. 注入的 Props

- **interpolation**：字段配置对象

  - `interpolation.map`：字段码到字段对象的映射，键为 `fieldCode`，值为字段配置对象

  - `interpolation.list`：字段配置数组，包含所有字段配置信息

- **insert(fieldCode)**：获取字段重命名文本的方法

  - 参数 `fieldCode`：字段码（字符串）

  - 返回值：如果字段存在且可见（`visibleEnum` 为 false），返回 `fieldRename`（字段重命名文本），否则返回 `false`

  - 使用场景：用于获取单个字段的重命名文本，通常用于表单标签、页面文本等

  - **特殊字段 `DEFAULT_MENU`**：

    - 每个页面后端都会返回一个默认值 `DEFAULT_MENU`，表示页面的默认标题

    - 该值可以用于 `PageLayout` 组件的 `title` 属性，但**不是必须的**

    - 使用示例：`const pageTitle = insert('DEFAULT_MENU') || '默认标题';`

- **columns(columns)**：处理表格列配置的方法

  - 参数 `columns`：表格列配置数组

  - 返回值：处理后的表格列配置数组

  - 处理逻辑：

    - 遍历列配置数组

    - 如果列配置包含 `fieldCode`，则查找对应的字段配置

    - 如果字段存在且可见（`visibleEnum` 为 false），则用 `fieldRename` 替换 `title`

    - 如果字段不可见，则过滤掉该列（返回 `false`）

    - 如果列配置不包含 `fieldCode`，则保持原样
