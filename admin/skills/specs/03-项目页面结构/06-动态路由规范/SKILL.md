---
name: jjb-dynamic-route
description: 定义 JJB 项目动态路由规范。在创建详情页、编辑页或使用 _id 后缀、获取 props.match.params、嵌套路由父级 index 与 props.children 出口时使用。
---

# 项目页面结构

## 动态路由规范

- **ID 动态路由**：当页面需要支持动态路由参数（如详情页、编辑页）时，文件夹命名使用 `_id` 后缀

  - 示例：`_id`、`_type`

  - 说明：系统会自动将 `_id` 识别为动态路由参数，并在路由中注入对应的 `id` 值

- **目录结构示例**：

  ```
  List/
  ├── index.js          # 列表页（或见下文「嵌套路由父级」纯出口）
  └── _id/
      └── index.js      # 动态路由详情页
  ```

## 嵌套路由父级 `index.js`（必须）

`@cqsjjb/jjb-dva-runtime` 自动化路由会把**子路由**渲染成父级组件的 **`props.children`**。因此：

- 只要某目录下存在**子路由目录**（如 `_id`、`_type` 或其它页面子文件夹），**该父级目录必须提供 `index.js`**。
- **禁止**仅保留 `Parent/_id/index.js` 而省略 `Parent/index.js`，否则路由树中间节点无法正确挂载，子页面可能白屏或命中 404。

### 父级仅有子路由、无独立页面 UI

典型场景：业务上只有「带子路径的详情/子页」（例如仅有 `InspectionRecordHazardList/_id` 对应 `/inspectionRecordHazardList/:id`），父级不参与具体布局。

父级 `Parent/index.js` **只做出口**，原样渲染子路由：

```javascript
import React from 'react';

export default function ParentRouteOutlet(props) {
  return props.children;
}
```

### 父级带 `_id` 时：与 `jjb-dva-runtime` 嵌套路由一致

自动化路由将子路由树作为父组件的 **`props.children`** 挂载（见 `@cqsjjb/jjb-dva-runtime/automatic/router.js` 内层 `Switch`）。**父级 `index.js` 必须渲染 `props.children`**，否则子页无法挂载。

- **禁止在父级用「无子路由时渲染列表」兜底**：在同一路由父级里写 `props.children ? children : <列表 />` 会与嵌套 `Switch` 的命中逻辑冲突，易出现 **「抱歉，您访问的应用页面不存在」** 等 404，或路径被错误截断。**列表页应放在同级独立目录**，与「仅带子路由的父级」拆成两个路由。

  **推荐目录示例**（列表 + 同前缀下钻）：

  ```
  InspectionRecordList/
  └── index.js              # /inspectionRecordList 检查记录列表
  InspectionRecord/
  ├── index.js              # 仅 return props.children
  └── _id/
      └── index.js          # /inspectionRecord/:id 下钻页
  ```

  菜单入口指向 **`/inspectionRecordList`**；列表内跳转使用 **`history.push(\`/inspectionRecord/${id}\`)`**（路径首段与目录 PascalCase 对应，运行时首字母小写）。

- **同屏「主从」布局**（列表与详情同页、需长期并排展示 `children`）：在**单页组件**内用局部 `children` 槽位即可，但不要与「文件树父子路由」混用兜底；若实现成本过高，优先采用上文「列表独立路由」方案。

- **代码示例**：

  **父级出口**（`InspectionRecord/index.js`）：

  ```javascript
  import React from 'react';

  export default function InspectionRecord(props) {
    return props.children;
  }
  ```

  **动态路由子页**（`InspectionRecord/_id/index.js`）：

  ```javascript
  import React from 'react';

  const Page = props => {
    const { id } = props.match.params;
    return <div>{id}</div>;
  };

  export default Page;
  ```

  **说明**：`props.match.params` 中的 `id` 对应 `_id` 目录。

## 自检清单

- [ ] 已存在 `.../某父级/_id/`（或其它子页面目录）时，是否已添加 **`某父级/index.js`**？
- [ ] 父级 `index.js` 是否在最终 JSX 中渲染了 **`props.children`**（纯出口或布局内嵌套均可）？
