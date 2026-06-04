---
name: jjb-no-action-in-hook-deps
description: 禁止在 useEffect/useMemo/useCallback 依赖数组中监听接口 Action 或内置函数。在 useEffect、useMemo、useCallback、fetchUserAction 或 state 监听时使用。
---

# 接口与数据层规范

## 禁止在 Hook 依赖数组中监听接口 Action 或内置函数

> **📌 一句话**：`declareRequest` 生成的 Action 以及 Connect 注入的内置函数（`dispatch`、`resetModelState`、`dispatchModelAction`、`getModelState`）**不得**出现在 `useEffect`、`useMemo`、`useCallback` 的依赖数组中。去掉即可，只监听 state 数据。

> **⚠️ 重要约束**：
> - **禁止**在 `useEffect`、`useMemo`、`useCallback` 的依赖数组中监听接口 Action 函数
> - **禁止**在 `useEffect`、`useMemo`、`useCallback` 的依赖数组中监听 `props.dispatch`
> - **禁止**在 `useEffect`、`useMemo`、`useCallback` 的依赖数组中监听 `props.resetModelState`
> - **禁止**在 `useEffect`、`useMemo`、`useCallback` 的依赖数组中监听 `props.dispatchModelAction`
> - **禁止**在 `useEffect`、`useMemo`、`useCallback` 的依赖数组中监听 `props.getModelState`

## 适用范围

| Hook | 是否禁止监听 Action/内置函数 | 原因 |
| :--- | :--- | :--- |
| `useEffect` | ❌ 禁止 | 函数引用变化 → 重复执行 → state 更新 → 引用再变 → 死循环 |
| `useMemo` | ❌ 禁止 | 函数引用变化 → 重新计算 → 返回新值/函数 → 触发下游 Hook → 死循环 |
| `useCallback` | ❌ 禁止 | 函数引用变化 → 重新创建回调 → 回调引用变化 → 触发下游 useEffect → 死循环 |

**三者本质相同**：这些函数在每次渲染时可能产生新引用，一旦作为 Hook 依赖，就会形成"state 更新 → 重新渲染 → 新引用 → Hook 重新执行 → state 更新"的死循环。

## 禁止行为

### ❌ 错误示例：useEffect 依赖中监听 Action 或内置函数

```javascript
import React, { useEffect } from 'react';
import { Connect } from '@cqsjjb/jjb-dva-runtime';
import { NS_USER } from '~/enumerate/namespace';

function UserProfile({ user, fetchUserAction, dataListAction, resetModelState, dispatchModelAction, getModelState }) {
  // ❌ 错误：在依赖数组中监听 Action 函数
  useEffect(() => {
    fetchUserAction({ id: 1 });
  }, [fetchUserAction]); // ❌ 禁止！死循环

  // ❌ 错误：在依赖数组中监听 Action 函数
  useEffect(() => {
    dataListAction({ page: 1 });
  }, [dataListAction]); // ❌ 禁止！死循环

  // ❌ 错误：在依赖数组中监听 resetModelState
  useEffect(() => {
    resetModelState(NS_USER, { loading: false });
  }, [resetModelState]); // ❌ 禁止！死循环

  // ❌ 错误：在依赖数组中监听 dispatchModelAction
  useEffect(() => {
    dispatchModelAction(NS_USER, 'dataListAction', { page: 1 });
  }, [dispatchModelAction]); // ❌ 禁止！死循环

  // ❌ 错误：在依赖数组中监听 getModelState
  useEffect(() => {
    const dataSource = getModelState(NS_USER, 'dataSource');
  }, [getModelState]); // ❌ 禁止！死循环

  return <div>{user.userInfo?.name}</div>;
}

export default Connect([NS_USER], true)(UserProfile);
```

### ❌ 错误示例：useCallback 依赖中监听 Action（常见错误！）

```javascript
import React, { useEffect, useCallback } from 'react';
import { Connect } from '@cqsjjb/jjb-dva-runtime';
import { NS_RESOURCE } from '~/enumerate/namespace';

function ResourceList({ resource, getResourceListAction, deleteResourceAction }) {
  const [pageIndex, setPageIndex] = useState(1);
  const [searchParams, setSearchParams] = useState({});

  // ❌ 错误：useCallback 依赖了 Action 函数
  const fetchList = useCallback(() => {
    const params = { pageIndex, pageSize: 10 };
    if (searchParams.name) params.name = searchParams.name;
    getResourceListAction(params);
  }, [pageIndex, searchParams, getResourceListAction]); // ❌ 禁止！死循环

  // fetchList 引用因 getResourceListAction 变化而不稳定 → 触发 useEffect 反复执行
  useEffect(() => {
    fetchList();
  }, [fetchList]);

  // ... 渲染
}

export default Connect([NS_RESOURCE], true)(ResourceList);
```

### ❌ 错误示例：useMemo 依赖中监听 Action

```javascript
import React, { useMemo } from 'react';
import { Connect } from '@cqsjjb/jjb-dva-runtime';
import { NS_RESOURCE } from '~/enumerate/namespace';

function ResourceList({ resource, getResourceListAction }) {
  const [pageIndex, setPageIndex] = useState(1);

  // ❌ 错误：useMemo 依赖了 Action 函数
  const queryConfig = useMemo(() => ({
    fetch: (params) => getResourceListAction(params),
    defaultPageSize: 10
  }), [getResourceListAction]); // ❌ 禁止！死循环

  // ... 渲染
}

export default Connect([NS_RESOURCE], true)(ResourceList);
```

## 正确做法

### ✅ 方式一：依赖数组为空（仅调用一次）

```javascript
import React, { useEffect } from 'react';
import { Connect } from '@cqsjjb/jjb-dva-runtime';
import { NS_USER } from '~/enumerate/namespace';

function UserProfile({ user, fetchUserAction }) {
  // ✅ 正确：依赖数组为空，仅在组件挂载时调用一次
  useEffect(() => {
    fetchUserAction({ id: 1 });
  }, []); // ✅ 空依赖数组

  return <div>{user.userInfo?.name}</div>;
}

export default Connect([NS_USER], true)(UserProfile);
```

### ✅ 方式二：监听 state 数据变化（推荐）

```javascript
import React, { useEffect } from 'react';
import { Connect } from '@cqsjjb/jjb-dva-runtime';
import { NS_USER } from '~/enumerate/namespace';

function UserProfile({ user, fetchUserAction }) {
  // ✅ 正确：组件挂载时调用 action
  useEffect(() => {
    fetchUserAction({ id: 1 });
  }, []);

  // ✅ 正确：监听 state 数据变化，而不是 action 函数
  useEffect(() => {
    if (user?.userInfo) {
      console.log('用户信息已加载:', user.userInfo);
    }
  }, [user?.userInfo]); // ✅ 允许监听 state 数据

  // ✅ 正确：监听 loading 状态变化
  useEffect(() => {
    if (!user?.loading && user?.userInfo) {
      console.log('请求已完成');
    }
  }, [user?.loading, user?.userInfo]); // ✅ 允许监听 state 数据

  return <div>{user.userInfo?.name}</div>;
}

export default Connect([NS_USER], true)(UserProfile);
```

### ✅ 方式三：useEffect 监听 state 组合变化（页面列表场景，推荐）

```javascript
import React, { useEffect, useState } from 'react';
import { Connect } from '@cqsjjb/jjb-dva-runtime';
import { NS_RESOURCE } from '~/enumerate/namespace';

function ResourceList({ resource, getResourceListAction, deleteResourceAction }) {
  const [pageIndex, setPageIndex] = useState(1);
  const [pageSize, setPageSize] = useState(10);
  const [searchParams, setSearchParams] = useState({});
  const [sortField, setSortField] = useState(null);
  const [sortOrder, setSortOrder] = useState(null);

  // ✅ 正确：依赖 state 数据，不依赖 action 函数
  useEffect(() => {
    const params = { pageIndex, pageSize };
    if (searchParams.name) params.name = searchParams.name;
    if (sortField) {
      params.orderBy = sortField;
      params.orderDirection = sortOrder === 'ascend' ? 'ASC' : 'DESC';
    }
    getResourceListAction(params);
    // ✅ 依赖列表只有 state 数据，没有 action 函数
  }, [pageIndex, pageSize, searchParams, sortField, sortOrder]);

  const handleDelete = async (record) => {
    const res = await deleteResourceAction({ ids: [record.id] });
    // 删除成功后，通过修改 state 触发 useEffect 刷新列表
    if (res.success) setPageIndex(1); // 重置到第一页，触发重新请求
  };

  // ... 渲染
}

export default Connect([NS_RESOURCE], true)(ResourceList);
```

### ✅ 方式四：使用 useMemo 计算衍生数据

```javascript
import React, { useEffect, useMemo } from 'react';
import { Connect } from '@cqsjjb/jjb-dva-runtime';
import { NS_USER } from '~/enumerate/namespace';

function UserProfile({ user, fetchUserAction }) {
  useEffect(() => {
    fetchUserAction({ id: 1 });
  }, []);

  // ✅ 正确：useMemo 依赖 state 数据
  const displayName = useMemo(() => {
    return user?.userInfo?.name || '未加载';
  }, [user?.userInfo?.name]); // ✅ 允许监听 state 数据

  return <div>{displayName}</div>;
}

export default Connect([NS_USER], true)(UserProfile);
```

### ✅ 方式五：页面列表 hooks 标准写法（useCallback 只依赖 state）

```javascript
import React, { useEffect, useState, useCallback } from 'react';
import { Connect } from '@cqsjjb/jjb-dva-runtime';
import { NS_RESOURCE } from '~/enumerate/namespace';

function ResourceList({ resource, getResourceListAction }) {
  const [pageIndex, setPageIndex] = useState(1);
  const [searchParams, setSearchParams] = useState({});

  // ✅ 正确：useCallback 只依赖 state 数据，不依赖 action
  const handleSearch = useCallback((values) => {
    setPageIndex(1);
    setSearchParams(values);
  }, []); // ✅ 空依赖或 state 数据

  // ✅ 正确：useEffect 只依赖 state 数据
  useEffect(() => {
    const params = { pageIndex, pageSize: 10, ...searchParams };
    getResourceListAction(params);
  }, [pageIndex, searchParams]); // ✅ 只有 state 数据

  // ... 渲染
}

export default Connect([NS_RESOURCE], true)(ResourceList);
```

## 核心原则

1. **禁止在任何 Hook 依赖中监听 Action 或内置函数**：`useEffect`、`useMemo`、`useCallback` 的依赖数组都不得包含以下函数：
   - Action 函数（`fetchUserAction`、`dataListAction`、`getResourceListAction`、`deleteXxxAction` 等由 `declareRequest` 生成的）
   - 内置函数（`dispatch`、`resetModelState`、`dispatchModelAction`、`getModelState`）

2. **允许监听 state 数据**：可以在依赖数组中监听 state 数据的变化（如 `user?.data`、`user?.userInfo`、`user?.loading`）

3. **空依赖数组**：如果只需要在组件挂载时调用一次，使用空依赖数组 `[]`

4. **响应式更新**：React 会自动响应 state 变化并重新渲染，无需手动监听这些函数

## 为什么禁止监听这些函数？

### ⚠️ 核心原因：会造成 React 渲染死循环

**监听 Action 或内置函数会导致死循环**：

```javascript
// ❌ 错误示例：useEffect 死循环
function UserProfile({ user, fetchUserAction }) {
  useEffect(() => {
    fetchUserAction({ id: 1 }); // 调用 action
  }, [fetchUserAction]); // 监听 action 函数 → 死循环！
}

// ❌ 错误示例：useCallback 间接死循环（场景）
function ResourceList({ getResourceListAction }) {
  const [pageIndex] = useState(1);

  const fetch = useCallback(() => {
    getResourceListAction({ page: pageIndex });
  }, [pageIndex, getResourceListAction]); // ← action 在依赖中！

  useEffect(() => { fetch(); }, [fetch]); // fetch 频繁变化 → 死循环！
}
```

**死循环过程**：
1. Hook 执行，调用 Action → 更新 state
2. state 更新 → 组件重新渲染
3. 重新渲染时 Action/内置函数可能创建新引用
4. 新引用 → Hook 检测到依赖变化 → 重新执行
5. 回到步骤 1，无限循环

### 其他原因

1. **函数引用不稳定**：这些函数在每次渲染时可能创建新引用，导致 Hook 频繁执行
2. **不必要的重新执行**：造成性能问题
3. **逻辑混乱**：监听函数而不是数据变化，数据流不清晰
4. **架构设计**：Connect 已将 state 注入组件，应监听 state 数据而非函数

## 对比说明

| 依赖项类型 | useEffect | useMemo | useCallback | 说明 |
| :--------- | :--- | :--- | :--- | :--- |
| `fetchUserAction` | ❌ 禁止 | ❌ 禁止 | ❌ 禁止 | Action 函数 |
| `dataListAction` | ❌ 禁止 | ❌ 禁止 | ❌ 禁止 | Action 函数 |
| `getResourceListAction` | ❌ 禁止 | ❌ 禁止 | ❌ 禁止 | Action 函数 |
| `deleteXxxAction` | ❌ 禁止 | ❌ 禁止 | ❌ 禁止 | Action 函数 |
| `getModelState` | ❌ 禁止 | ❌ 禁止 | ❌ 禁止 | 内置函数 |
| `resetModelState` | ❌ 禁止 | ❌ 禁止 | ❌ 禁止 | 内置函数 |
| `dispatchModelAction` | ❌ 禁止 | ❌ 禁止 | ❌ 禁止 | 内置函数 |
| `dispatch` | ❌ 禁止 | ❌ 禁止 | ❌ 禁止 | 内置函数 |
| `user?.data` | ✅ 允许 | ✅ 允许 | ✅ 允许 | state 数据 |
| `user?.userInfo` | ✅ 允许 | ✅ 允许 | ✅ 允许 | state 数据 |
| `user?.loading` | ✅ 允许 | ✅ 允许 | ✅ 允许 | state 数据 |
| `order?.list` | ✅ 允许 | ✅ 允许 | ✅ 允许 | state 数据 |
| `[]` | ✅ 允许 | — | ✅ 允许 | 空依赖数组 |

## 总结

- ❌ **禁止**：`useEffect(() => {}, [dataListAction])` — 不能监听 Action 或内置函数
- ❌ **禁止**：`useCallback(() => {}, [getListAction])` — 不能监听 Action 或内置函数
- ❌ **禁止**：`useMemo(() => {}, [deleteAction])` — 不能监听 Action 或内置函数
- ✅ **允许**：`useEffect(() => {}, [user?.data])` — 可以监听 state 数据
- ✅ **允许**：`useEffect(() => {}, [])` — 空依赖数组，仅调用一次
- ✅ **推荐**：监听 state 数据变化，而不是 Action 或内置函数引用
