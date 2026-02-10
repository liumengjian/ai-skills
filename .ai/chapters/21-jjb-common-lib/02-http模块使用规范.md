# 二十三、http 模块使用规范

## 1. 概述

`http` 模块是 `@cqsjjb/jjb-common-lib` 通用工具库中的 HTTP 请求模块，基于 axios 高度封装，专为微应用场景设计。`declareRequest` 的接口请求就是基于此模块实现。

### 1.1 导入方式

```javascript
import { http } from '@cqsjjb/jjb-common-lib';
```

## 2. 内置方法详解

### 2.1 Get(api, data?, headers?)

GET 请求方法。

**参数：**
- `api` (string): 请求地址
- `data` (object, 可选): 提交数据，默认为 `{}`
- `headers` (object, 可选): 请求头，默认为 `{}`

**返回值：**
- `Promise<IResponse>`: 返回 Promise，解析为响应对象

**注意事项：**
- GET 请求不允许使用 `@` 操作符，如果使用会抛出错误

**示例：**
```javascript
http.Get(
  'http://xxx.xxx.com/api/...',
  { id: 1 },
  { token: 'xxx' }
).then(res => {
  console.log(res);
});
```

### 2.2 Post(api, data?, headers?)

POST 请求方法。

**参数：**
- `api` (string): 请求地址
- `data` (object, 可选): 提交数据，默认为 `{}`
- `headers` (object, 可选): 请求头，默认为 `{}`

**返回值：**
- `Promise<IResponse>`: 返回 Promise，解析为响应对象

**特殊说明：**
- 支持 `@` 操作符：如果 URL 中包含 `@`，数据不会包装在 `request` 字段中
- 不使用 `@` 操作符时，数据会自动包装在 `request` 字段中

**示例：**
```javascript
// 不使用 @ 操作符，数据会被包装在 request 字段中
http.Post('/api/user', { name: 'test' })
// 实际发送的数据: { request: { name: 'test' } }

// 使用 @ 操作符，数据直接发送
http.Post('@/api/user', { name: 'test' })
// 实际发送的数据: { name: 'test' }
```

### 2.3 Delete(api, data?, headers?)

DELETE 请求方法。

**参数：**
- `api` (string): 请求地址
- `data` (object, 可选): 提交数据，默认为 `{}`
- `headers` (object, 可选): 请求头，默认为 `{}`

**返回值：**
- `Promise<IResponse>`: 返回 Promise，解析为响应对象

**特殊说明：**
- 支持 `@` 操作符，行为与 Post 方法相同

**示例：**
```javascript
http.Delete('/api/user/1', {}, { token: 'xxx' })
  .then(res => console.log(res));
```

### 2.4 Put(api, data?, headers?, redirect?)

PUT 请求方法。

**参数：**
- `api` (string): 请求地址
- `data` (object, 可选): 提交数据，默认为 `{}`
- `headers` (object, 可选): 请求头，默认为 `{}`
- `redirect` (string, 可选): 重定向地址，默认为 `''`

**返回值：**
- `Promise<IResponse>`: 返回 Promise，解析为响应对象

**特殊说明：**
- 支持 `@` 操作符，行为与 Post 方法相同

**示例：**
```javascript
http.Put(
  '/api/user/1',
  { name: 'updated' },
  { token: 'xxx' },
  false
).then(res => console.log(res));
```

### 2.5 Patch(api, data?, headers?)

PATCH 请求方法。

**参数：**
- `api` (string): 请求地址
- `data` (object, 可选): 提交数据，默认为 `{}`
- `headers` (object, 可选): 请求头，默认为 `{}`

**返回值：**
- `Promise<IResponse>`: 返回 Promise，解析为响应对象

**特殊说明：**
- 支持 `@` 操作符，行为与 Post 方法相同

**示例：**
```javascript
http.Patch('/api/user/1', { name: 'patched' }, { token: 'xxx' })
  .then(res => console.log(res));
```

### 2.6 request(api, method, data?, headers?)

通用请求方法。

**参数：**
- `api` (string): 请求地址
- `method` (string): 请求方式（如 'get'、'post'、'put'、'delete'、'patch'）
- `data` (object, 可选): 提交数据，默认为 `{}`
- `headers` (object, 可选): 请求头，默认为 `false`

**返回值：**
- `Promise<IResponse>`: 返回 Promise，解析为响应对象

**说明：**
- 此方法支持请求拦截器，如果配置了请求拦截器，会先执行拦截器再发送请求

## 3. 响应数据格式 (IResponse)

所有请求方法返回的响应对象都遵循以下格式：

```typescript
interface IResponse<T = any> {
  // 数据总条数
  totalCount?: number;
  // 数据
  data?: T;
  // 是否成功
  success?: boolean;
  // 错误信息
  errMessage?: string;
}
```

## 4. 核心特性

### 4.1 自动 URL 处理

- 自动根据 `API_HOST` 配置添加请求前缀
- 支持通过 `getJJBCommonHttpConfig()` 配置 `API_HOST`
- 如果未配置 `API_HOST`，会从 `window.__JJB_ENVIRONMENT__.API_HOST` 读取
- 如果 URL 已经是完整的 HTTP/HTTPS 地址，则不会添加前缀

### 4.2 Token 自动注入

- 自动从 `window.sessionStorage.token` 读取 token
- 如果配置了 `getJJBCommonHttpConfig().header`，则使用配置的 header
- 否则自动将 token 添加到请求头的 `token` 字段

### 4.3 租户代码自动注入

- 自动从 `window.__JJB_ENVIRONMENT__.tenantCode` 读取租户代码
- 如果存在租户代码，会自动添加到请求头的 `tenantCode` 字段

### 4.4 请求/响应拦截器

- 支持通过全局配置设置请求拦截器：`getJJBCommonGlobalConfig().httpInterceptor.request`
- 支持通过全局配置设置响应拦截器：`getJJBCommonGlobalConfig().httpInterceptor.response`
- 拦截器可以是同步函数或返回 Promise 的异步函数

### 4.5 错误提示

- 接口返回错误时自动通过 `antd.message` 显示错误信息
- 错误信息来自响应数据的 `errMessage` 字段

### 4.6 超时配置

- 默认超时时间为 5 分钟（60000 * 5 毫秒）
- 可通过 `getJJBCommonGlobalConfig().httpTimeout` 配置超时时间

### 4.7 响应类型配置

- 默认响应类型为 `'json'`
- 可通过 `getJJBCommonGlobalConfig().httpResponseType` 配置响应类型

## 5. @ 操作符说明

`@` 操作符用于控制请求数据的包装方式：

- **不使用 `@` 操作符**：数据会被包装在 `request` 字段中
  ```javascript
  http.Post('/api/user', { name: 'test' })
  // 实际发送: { request: { name: 'test' } }
  ```

- **使用 `@` 操作符**：数据直接发送，不进行包装
  ```javascript
  http.Post('@/api/user', { name: 'test' })
  // 实际发送: { name: 'test' }
  ```

**注意事项：**
- GET 请求不允许使用 `@` 操作符
- POST、PUT、DELETE、PATCH 请求支持 `@` 操作符

## 6. 使用示例

### 6.1 基本 GET 请求

```javascript
import { http } from '@cqsjjb/jjb-common-lib';

http.Get('/api/users', { page: 1, pageSize: 10 })
  .then(res => {
    if (res.success) {
      console.log(res.dataSource);
    }
  })
  .catch(err => {
    console.error('请求失败', err);
  });
```

### 6.2 POST 请求（不使用 @ 操作符）

```javascript
http.Post('/api/user', {
  name: '张三',
  age: 25
}).then(res => {
  if (res.success) {
    console.log('创建成功');
  }
});
```

### 6.3 POST 请求（使用 @ 操作符）

```javascript
http.Post('@/api/user', {
  name: '张三',
  age: 25
}).then(res => {
  if (res.success) {
    console.log('创建成功');
  }
});
```

### 6.4 带自定义请求头的请求

```javascript
http.Post('/api/user', { name: 'test' }, {
  'Custom-Header': 'custom-value'
}).then(res => {
  console.log(res);
});
```

## 7. 环境要求

- 必须在 `window` 对象上定义 `__JJB_ENVIRONMENT__`，否则会输出错误日志
- 建议在应用启动时设置 `window.__JJB_ENVIRONMENT__`，包含以下字段：
  - `API_HOST`: API 基础地址
  - `tenantCode`: 租户代码（可选）

## 8. 相关模块

- **declareRequest**：接口请求声明基于此模块实现
- **详细文档**：参考 `reference/http.js` 查看完整的实现代码

## 9. 注意事项

1. **错误处理**：建议使用 `.catch()` 处理请求错误，虽然模块会自动处理部分错误，但网络错误等仍需要手动处理

2. **Token 管理**：Token 会自动从 `sessionStorage` 读取，确保在请求前已正确设置 token

3. **URL 配置**：确保正确配置 `API_HOST`，否则可能无法正确发送请求

4. **响应格式**：响应数据会被统一处理，建议使用 `success` 字段判断请求是否成功

5. **@ 操作符**：理解 `@` 操作符的作用，根据后端接口要求选择是否使用
