---
name: jjb-search-persistence
description: 定义 JJB 项目搜索状态持久化规范。在使用 tools.router.query、router.query 管理搜索表单值或 URL 持久化时使用。
---

# 搜索区规范（一级页面）

## 搜索状态持久化

- **状态管理**：`SearchForm` 的表单值必须通过 `@cqsjjb/jjb-common-lib/tools` 中的 `router.query` 进行管理

  - **导入方式**：

    ```javascript
    import { tools } from '@cqsjjb/jjb-common-lib';
    const { router } = tools;
    ```

  - **访问查询参数**：

    ```javascript
    // router.query 返回 Proxy 对象
    const id = router.query.id; // string 类型
    ```

  - **设置查询参数**：

    ```javascript
    router.query = { id: '123' };
    router.query.id = '123';
    ```

  - **移除查询参数**：

    ```javascript
    router.query.id = undefined;
    router.query = { id: undefined };
    ```

  - **持久化机制**：

    - 查询参数自动写入地址栏 URL

    - 页面返回时自动从 `router.query` 读取并回填表单值
