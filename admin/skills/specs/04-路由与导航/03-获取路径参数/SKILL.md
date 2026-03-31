---
name: jjb-route-path-params
description: 定义 JJB 项目获取路由路径参数规范。在使用 props.match.params、获取动态路由 id 或路径参数时使用。禁止对路由参数进行类型转换。
---

# 路由与导航

## 获取路由参数

### 获取路径参数（Params 参数）

- **方法**：使用 `props.match.params` 获取路由路径参数
- **适用范围**：仅限路由页面组件（`src/pages/` 目录下的页面组件）
- **重要约束**：`match.params` 仅在路由页面组件中自动注入到 `props`

  - 使用示例：

    ```javascript
    // 路由配置: /user/detail/:id
    // 当前 URL: /user/detail/123
    function UserDetail(props) {
      const { id } = props.match.params;
      // id => '123'
      
      // 使用 id 进行数据请求等操作
      // ...
    }
    ```

- **禁止行为**：
  - 禁止在非路由页面组件中直接使用 `props.match.params`，应通过 `props` 传递参数
  - 禁止对路由参数进行转换操作（如将 id 字段值转换为 number），这会导致 id 值失真。路由参数应保持原始字符串格式
