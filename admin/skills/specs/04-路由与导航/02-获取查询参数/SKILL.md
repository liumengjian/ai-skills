---
name: jjb-route-query-params
description: 定义 JJB 项目获取路由查询参数规范。在使用 tools.router.query、获取 query 参数或搜索表单状态持久化时使用。禁止对路由参数进行类型转换。
---

# 路由与导航

## 获取路由参数

### 获取查询参数（Query 参数）

- **方法**：使用 `tools.router.query` 获取路由查询参数
- **适用范围**：适用于所有组件，不限于路由页面组件
- **返回格式**：返回一个 Proxy 对象，包含所有查询参数

  - 基本使用：

    ```javascript
    import { tools } from '@cqsjjb/jjb-common-lib';
    
    // 当前 URL: /user/list?page=1&size=10&status=active
    const queryParams = tools.router.query;
    // queryParams => { page: '1', size: '10', status: 'active' }
    ```

  - **禁止行为**：禁止对路由参数进行转换操作（如将 id 字段值转换为 number），这会导致 id 值失真。路由参数应保持原始字符串格式。

  - **详细 API 文档**：参考 [`21-jjb-common-lib/01-tools模块使用规范`](../../21-jjb-common-lib/01-tools模块使用规范.md)（查看"2.9 路由参数管理"章节）
  
  - **搜索表单场景**：在搜索表单中使用 `router.query` 进行状态持久化，参考 [`06-搜索区规范`](../../06-搜索区规范/02-搜索状态持久化/SKILL.md)
