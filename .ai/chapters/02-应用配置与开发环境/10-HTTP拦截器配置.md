# 二、应用配置与开发环境

## 10. HTTP 拦截器配置

- **配置位置**：在 `public/index.html` 文件中配置 `window.jjbCommonGlobalConfig.httpInterceptor`

- **配置结构**：

  ```html
  <script>
    window.jjbCommonGlobalConfig = {
      // http拦截器
      httpInterceptor: {
        // 请求拦截
        request: (url, method, data, headers) => {
          // 处理你的请求拦截逻辑
          
          // 示例：给请求头添加一个租户ID
          if (!headers) {
            headers = {};
          }
          headers.tenantId = sessionStorage.getItem('tenantId');
          
          // 示例：修改请求URL
          // url = url.replace('/old-path', '/new-path');
          
          // 示例：修改请求数据
          // data = { ...data, timestamp: Date.now() };
          
          // 必须返回 Promise，resolve 值为数组 [url, method, data, headers]
          return Promise.resolve([
            url,
            method,
            data,
            headers
          ]);
        },
        // 响应拦截
        response: res => {
          // 处理你的响应拦截逻辑
          
          // 示例：统一处理响应数据
          // if (res.data && res.data.code === 200) {
          //   return Promise.resolve(res.data);
          // }
          
          // 示例：错误处理
          // if (res.response && res.response.status !== 200) {
          //   console.error('请求失败:', res.response.status);
          // }
          
          // 必须返回 Promise，resolve 值为处理后的响应对象
          return Promise.resolve(res);
        }
      }
    }
  </script>
  ```

- **请求拦截器说明**：

  - **函数签名**：`request(url: string, method: string, data?: object, headers?: object | false): Promise<[string, string, object, object | false]>`

  - **参数说明**：

    | 参数 | 类型 | 说明 |
    | :--- | :--- | :--- |
    | url | string | 请求URL地址 |
    | method | string | 请求方法（如 'get'、'post'、'put'、'delete'、'patch'） |
    | data | object | 请求数据（可选，默认为 `{}`） |
    | headers | object \| false | 请求头对象（可选，默认为 `false`，如果为 `false` 则使用默认请求头） |

  - **返回值**：**必须返回 Promise**，Promise resolve 的值必须为包含四个元素的数组：`[url, method, data, headers]`

    - 数组元素顺序固定：`[URL地址, 请求方法, 请求数据, 请求头]`
    - 返回的数组会作为参数传递给实际的请求函数执行

  - **执行时机**：在请求发送前执行，可以修改请求的 URL、方法、数据和请求头

  - **使用示例**：

    ```javascript
    request: (url, method, data, headers) => {
      // 确保 headers 是对象
      const reqHeaders = headers || {};
      
      // 添加 Token
      if (!reqHeaders.token && sessionStorage.getItem('token')) {
        reqHeaders.token = sessionStorage.getItem('token');
      }
      
      // 添加租户ID
      reqHeaders.tenantId = sessionStorage.getItem('tenantId');
      
      // 修改请求数据
      const reqData = {
        ...data,
        timestamp: Date.now()
      };
      
      return Promise.resolve([url, method, reqData, reqHeaders]);
    }
    ```

  - **使用场景**：适用于需要在请求发送前统一处理请求参数、添加请求头（如租户ID、Token等）、修改请求URL、添加时间戳等场景

- **响应拦截器说明**：

  - **函数签名**：`response(res: object): Promise<object>`

  - **参数说明**：

    | 参数 | 类型 | 说明 |
    | :--- | :--- | :--- |
    | res | object | 响应对象，包含完整的响应信息（成功时包含 `data`、`status` 等，失败时包含 `response`、`message` 等） |

  - **返回值**：**必须返回 Promise**，Promise resolve 的值为处理后的响应对象

  - **执行时机**：在响应返回后执行，**无论请求成功还是失败都会执行**

    - 成功时：响应对象包含 `data`、`status`、`headers` 等属性
    - 失败时：响应对象包含 `response`、`message`、`code` 等错误信息

  - **使用示例**：

    ```javascript
    response: res => {
      // 成功响应处理
      if (res.data && res.status === 200) {
        // 统一处理响应数据格式
        return Promise.resolve({
          ...res.data,
          success: res.data.success !== false
        });
      }
      
      // 错误响应处理
      if (res.response) {
        console.error('请求失败:', res.response.status, res.response.data);
      }
      
      return Promise.resolve(res);
    }
    ```

  - **使用场景**：适用于需要在响应返回后统一处理响应数据、错误处理、数据格式转换、统一错误提示等场景

- **注意事项**：

  - **配置时机**：HTTP 拦截器配置必须在应用启动前完成，建议放在 `public/index.html` 的 `<head>` 或 `<body>` 开始位置

  - **请求拦截器要求**：
    - 必须返回 Promise 对象
    - Promise resolve 的值必须为包含四个元素的数组：`[url, method, data, headers]`
    - 数组元素顺序固定，不能改变
    - 如果不需要修改某个参数，也需要原样返回

  - **响应拦截器要求**：
    - 必须返回 Promise 对象
    - Promise resolve 的值为处理后的响应对象
    - 响应拦截器会在请求成功和失败时都被调用，需要根据实际情况处理

  - **参数处理**：
    - 请求拦截器的 `headers` 参数可能为 `false`，使用时需要先判断或转换为对象
    - 请求拦截器的 `data` 参数默认为 `{}`，但可能为任意对象结构

  - **错误处理**：
    - 拦截器中的异步操作应使用 Promise 处理，确保拦截器链的正常执行
    - 如果拦截器抛出错误或返回的 Promise reject，可能导致请求失败
