---
name: jjb-declare-request
description: 定义 JJB 接口定义规范。在使用 declareRequest、Action 命名、Loading 状态或 resetModelState 时使用。必须参考 MD/d.ts 文档。
---

# 接口与数据层规范

## 接口定义规范 (declareRequest)

所有接口必须通过 `@cqsjjb/jjb-dva-runtime/declareRequest` 进行声明。该方法通过字符串 DSL 实现请求配置与数据处理。

必须严格参考对应 MD 文档或 d.ts 文件！

## 基本语法

```javascript
declareRequest(
  a?: string,  // 参数1：Loading 状态标识（可选）
  b: string,    // 参数2：请求表达式（必填）
  c?: string   // 参数3：响应数据处理表达式（可选）
)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
| :--- | :--- | :--- | :--- |
| a | string | 否 | 请求时绑定的 Loading 状态标识，例如 `"loading"`、`"confirmLoading"` |
| b | string | 是 | 请求表达式，格式：`Method [> @] URL`，支持完整 http[s] 路径 |
| c | string | 否 | 响应数据处理表达式，用于从响应结果中取值并赋给目标字段 |

## 定义示例

```javascript
// 示例1：获取试卷列表（完整参数）
export const getExamResDataAction = declareRequest(
  'examResDataLoading', // 参数1：Loading 状态字段名
  'Get > /com-train/exams', // 参数2：请求方法 > 接口路径
  'examResData: [] | res.data || [] & examResDataTotal: 0 | res.totalCount || 0' // 参数3：数据映射与默认值
);

// 示例2：仅定义请求（省略参数1和参数3）
export const getUserInfoAction = declareRequest(
  'Get > /api/user/{id}' // 仅必填参数
);

// 示例3：POST 请求使用 @ 标记
export const createUserAction = declareRequest(
  'createUserLoading',
  'Post > @/api/user', // @ 标记忽略 request 包裹层
  'userId: "" | res.data.id || ""'
);
```

## 命名格式

`[name]Action` 统一使用 **小驼峰 (camelCase)** 命名

### ⚠️ 禁止使用的关键字

**禁止使用以下关键字作为 Action 名称**，这些是 `Connect` 装饰器注入的保留字段和方法，使用会导致冲突异常：

- `dispatch`：Dva dispatch 方法
- `resetModelState`：重置模型状态方法
- `dispatchModelAction`：手动调用 Action 方法
- `getModelState`：获取模型状态方法
- `props`：命名空间对应的 props 对象
- `models`：所有连接的模型对象
- `action`：通用 Action 标识（避免冲突）

### ❌ 错误示例

```javascript
// ❌ 错误：使用了保留关键字
export const dispatch = declareRequest('Get > /api/user');
export const resetModelState = declareRequest('Get > /api/user');
export const dispatchModelAction = declareRequest('Get > /api/user');
export const getModelState = declareRequest('Get > /api/user');
export const props = declareRequest('Get > /api/user');
export const models = declareRequest('Get > /api/user');
export const action = declareRequest('Get > /api/user');
```

### ✅ 正确示例

```javascript
// ✅ 正确：使用符合规范的命名
export const fetchUserAction = declareRequest('Get > /api/user');
export const getUserListAction = declareRequest('Get > /api/users');
export const createUserAction = declareRequest('Post > @/api/user');
export const updateUserAction = declareRequest('Put > @/api/user/{id}');
```

## 请求表达式规范

- **格式**：`Method [> @] URL`

- **支持的 HTTP 方法**：

  - `Get`：GET 请求
  - `Post`：POST 请求
  - `Put`：PUT 请求
  - `Delete`：DELETE 请求
  - `Patch`：PATCH 请求

- **@ 标记说明**：

  - **作用**：忽略请求体中 `request` 对象的包裹层，直接传递数据

  - **限制**：**Get 请求不能使用 @**，其他请求方法可选

  - **示例**：

    ```javascript
    // ✅ POST 请求使用 @，忽略 request 包裹
    'Post > @/api/user'

    // ❌ GET 请求禁止使用 @
    'Get > @/api/user/{id}'  // 错误写法
    ```

- **URL 路径规范**：

  - **普通路径**：例如 `/api/xxx/list`

  - **模板插值**：支持占位符 `{}`，调用时会替换为参数值

    ```javascript
    // 示例：URL 模板插值
    'Get > /api/user/{id}'  // 调用时 {id} 会被替换为实际参数值
    ```

  - **完整 HTTP 路径**：支持完整的 http[s] 路径

  - **请求格式限制**：**仅支持 `application/json` 格式**，其他格式不支持

## 响应表达式规范

- **格式**：`targetField: defaultValue | expression & ...`

- **组成部分**：

  - `targetField`：目标字段名称

  - `defaultValue`：当结果为空时的默认值

  - `expression`：从响应对象中获取数据的 JS 表达式

  - `&`：支持多个字段连接

  - `res`：固定上下文对象，表示响应结果

- **示例**：

  ```javascript
  // 示例：多字段映射
  'dataSource: [] | res.data || [] & total: 0 | res.total || 0'
  ```

  表示：

  - 将结果赋值给 `dataSource`，默认值为 `[]`，优先取 `res.data`，如果为空则取 `[]`

  - `&` 连接下一个字段

  - 将结果赋值给 `total`，默认值为 `0`，优先取 `res.total`，如果为空则取 `0`

- **AI 约束**：**必须根据后端返回结构精确配置此映射**

## 使用规则总结

1. **@ 标记限制**：Get 请求不能用 `@`，其他请求方法可选

2. **URL 模板插值**：支持路径模板插值 `{id}`，调用时自动替换

3. **参数可选性**：参数 a（Loading 状态）、c（响应处理）可选，不写也能正常工作

4. **请求格式**：仅支持 `application/json` 格式

## Loading 状态管理规范

> **⚠️ 重要约束**：当 `declareRequest` 定义的接口 Action 在弹窗、抽屉等可关闭组件中使用时，**必须在组件销毁时调用 `resetModelState` 重置对应的 loading 字段**。

### 问题说明

`declareRequest` 定义的接口 Action 会自动管理 loading 状态（如 `loading`、`confirmLoading`、`submitLoading` 等）。但在以下场景中，loading 状态可能无法自动重置：

- 接口请求异常中断
- 弹窗/抽屉在请求过程中被关闭
- 组件卸载时请求仍在进行

这会导致 loading 状态一直保持为 `true`，下次打开组件时仍然显示加载状态，影响用户体验。

### 解决方案

在组件销毁时（如弹窗的 `onCancel`、`afterClose` 或 `useEffect` 清理函数），调用 `resetModelState` 重置对应的 loading 字段。

### 示例

```javascript
import { useEffect } from 'react';
import { Connect } from '@cqsjjb/jjb-dva-runtime';
import { NS_USER } from '~/enumerate/namespace';

function UserModal({ createUserAction, resetModelState, modalOpen }) {
  useEffect(() => {
    if (!modalOpen) {
      // ✅ 弹窗关闭时重置 loading 状态
      resetModelState(NS_USER, { confirmLoading: false });
    }
  }, [modalOpen, resetModelState]);

  // ... 其他代码
}

export default Connect([NS_USER], true)(UserModal);
```

### 相关规范

- 关于 loading 状态重置的详细说明和多种场景示例，请参考 [`Loading状态重置规范`](../08-Loading状态重置规范/SKILL.md)
- 关于 `resetModelState` 的详细用法，请参考 [`命名空间与视图连接`](../03-命名空间与视图连接/SKILL.md)
