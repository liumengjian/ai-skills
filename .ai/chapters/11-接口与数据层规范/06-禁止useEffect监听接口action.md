# 十一、接口与数据层规范

## 6. 禁止在 useEffect 依赖数组中监听接口 Action

> **⚠️ 重要约束**：**禁止在 `useEffect` 的依赖数组中监听接口 Action 函数本身。**

## 禁止行为

### ❌ 错误示例：在依赖数组中监听 Action 函数

```javascript
import React, { useEffect } from 'react';
import { Connect } from '@cqsjjb/jjb-dva-runtime';
import { NS_USER } from '~/enumerate/namespace';

function UserProfile({ user, fetchUserAction, dataListAction }) {
  // ❌ 错误：在依赖数组中监听 Action 函数
  useEffect(() => {
    fetchUserAction({ id: 1 });
  }, [fetchUserAction]); // ❌ 禁止监听 action 函数

  // ❌ 错误：在依赖数组中监听 Action 函数
  useEffect(() => {
    dataListAction({ page: 1 });
  }, [dataListAction]); // ❌ 禁止监听 action 函数

  return <div>{user.userInfo?.name}</div>;
}

export default Connect([NS_USER], true)(UserProfile);
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
      // 处理数据变化...
    }
  }, [user?.userInfo]); // ✅ 允许监听 state 数据

  // ✅ 正确：监听 loading 状态变化
  useEffect(() => {
    if (!user?.loading && user?.userInfo) {
      console.log('请求已完成');
      // 处理完成逻辑...
    }
  }, [user?.loading, user?.userInfo]); // ✅ 允许监听 state 数据

  return <div>{user.userInfo?.name}</div>;
}

export default Connect([NS_USER], true)(UserProfile);
```

### ✅ 方式三：监听多个 state 数据

```javascript
import React, { useEffect } from 'react';
import { Connect } from '@cqsjjb/jjb-dva-runtime';
import { NS_USER, NS_ORDER } from '~/enumerate/namespace';

function Dashboard({ user, order, fetchUserAction, fetchOrdersAction }) {
  useEffect(() => {
    fetchUserAction({ id: 1 });
    fetchOrdersAction();
  }, []); // ✅ 空依赖数组，仅调用一次

  // ✅ 正确：监听多个 state 数据变化
  useEffect(() => {
    if (user?.userInfo && order?.list) {
      console.log('用户和订单数据都已加载');
      // 处理数据...
    }
  }, [user?.userInfo, order?.list]); // ✅ 允许监听 state 数据

  return (
    <div>
      <div>{user.userInfo?.name}</div>
      <div>{order.list?.length} 个订单</div>
    </div>
  );
}

export default Connect([NS_USER, NS_ORDER], true)(Dashboard);
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

  // ✅ 正确：使用 useMemo 计算衍生数据，依赖 state 数据
  const displayName = useMemo(() => {
    return user?.userInfo?.name || '未加载';
  }, [user?.userInfo?.name]); // ✅ 允许监听 state 数据

  // ✅ 正确：监听 state 数据变化
  useEffect(() => {
    if (user?.userInfo) {
      // 处理数据变化...
    }
  }, [user?.userInfo]); // ✅ 允许监听 state 数据

  return <div>{displayName}</div>;
}

export default Connect([NS_USER], true)(UserProfile);
```

## 核心原则

1. **禁止监听 Action 函数**：不要在 `useEffect` 的依赖数组中监听 Action 函数本身（如 `fetchUserAction`、`dataListAction`）

2. **允许监听 state 数据**：可以在 `useEffect` 的依赖数组中监听 state 数据的变化（如 `user?.data`、`user?.userInfo`、`user?.loading`）

3. **空依赖数组**：如果只需要在组件挂载时调用一次 Action，使用空依赖数组 `[]`

4. **响应式更新**：React 会自动响应 state 变化并重新渲染，无需手动监听 Action 函数

## 为什么禁止监听 Action 函数？

### ⚠️ 核心原因：会造成监听死循环

**监听 Action 函数会导致死循环**，这是最严重的问题：

```javascript
// ❌ 错误示例：死循环
function UserProfile({ user, fetchUserAction }) {
  useEffect(() => {
    fetchUserAction({ id: 1 }); // 调用 action
  }, [fetchUserAction]); // 监听 action 函数

  // 死循环过程：
  // 1. useEffect 执行，调用 fetchUserAction
  // 2. fetchUserAction 执行，更新 state
  // 3. state 更新导致组件重新渲染
  // 4. 组件重新渲染时，fetchUserAction 可能创建新的函数引用
  // 5. fetchUserAction 引用变化，触发 useEffect 再次执行
  // 6. 回到步骤 1，形成死循环
}
```

**死循环的根本原因**：
- Action 函数在每次组件渲染时可能创建新的引用
- `useEffect` 检测到依赖项（Action 函数）变化，重新执行
- `useEffect` 执行时调用 Action，更新 state
- state 更新导致组件重新渲染
- 组件重新渲染时 Action 函数引用可能再次变化
- 循环往复，形成死循环

### 其他原因

1. **函数引用不稳定**：Action 函数可能在每次渲染时创建新的引用，导致 `useEffect` 频繁执行

2. **不必要的重新执行**：监听 Action 函数会导致 `useEffect` 在每次渲染时都可能重新执行，造成性能问题

3. **逻辑混乱**：监听 Action 函数而不是数据变化，会让数据流变得不清晰

4. **架构设计**：Connect 装饰器已经将 state 注入到组件中，应该监听 state 数据的变化，而不是 Action 函数

## 对比说明

| 依赖项类型 | 是否允许 | 说明 |
| :--------- | :------- | :--- |
| `fetchUserAction` | ❌ 禁止 | Action 函数本身 |
| `dataListAction` | ❌ 禁止 | Action 函数本身 |
| `user?.data` | ✅ 允许 | state 数据 |
| `user?.userInfo` | ✅ 允许 | state 数据 |
| `user?.loading` | ✅ 允许 | state 数据 |
| `order?.list` | ✅ 允许 | state 数据 |
| `[]` | ✅ 允许 | 空依赖数组，仅执行一次 |

## 总结

- ❌ **禁止**：`useEffect(() => {}, [dataListAction])` - 不能监听 Action 函数
- ✅ **允许**：`useEffect(() => {}, [user?.data])` - 可以监听 state 数据
- ✅ **允许**：`useEffect(() => {}, [])` - 空依赖数组，仅调用一次
- ✅ **推荐**：监听 state 数据变化，而不是 Action 函数引用
