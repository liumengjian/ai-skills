---
name: jjb-route-generation
description: 定义 JJB 项目路由自动生成机制。在理解路由来源、页面与路由映射或 jjb-dva-runtime 路由时使用。
---

# 项目页面结构

## 路由生成机制

- **自动化路由**：应用的自动化路由由 `@cqsjjb/jjb-dva-runtime` 根据 `src/pages/` 目录中的路由页面文件自动生成路由树

  - 说明：无需手动配置路由，系统会根据页面文件结构自动生成对应的路由映射
