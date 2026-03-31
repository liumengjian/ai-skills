---
name: jjb-upload-speed-simple
description: 定义 JJB 单文件上传接口服务规范。在使用 FormData 上传、upload-speed-simple 或 FileUploader/ImageUploader 时使用。不能使用 declareRequest。
---

# 接口与数据层规范

## 单文件上传接口服务

> **⚠️ 重要说明**：本接口服务使用 FormData 格式上传文件，**不能使用 `declareRequest`**（`declareRequest` 仅支持 `application/json` 格式）。  
> 本接口为通用单文件上传服务，适用于需要直接调用上传接口的场景。

## 接口信息

- **接口地址**：`API_HOST + /attachment/files/upload-speed-simple`
- **请求方法**：`POST`
- **提交参数类型**：`FormData`
- **提交参数字段**：`file`
- **请求头**：`token: sessionStorage.token`

## 响应参数

接口成功响应后返回以下格式的数据：

```typescript
{
  "extValues": {},
  "skipUpload": boolean,
  "partNum": number,
  "fileId": string,
  "name": string,
  "fileUrl": string,           // 文件访问地址
  "previewUrl": string,         // 预览地址
  "downloadUrl": string,        // 下载地址
  "ext": string,                // 文件扩展名
  "timestamp": string,
  "needMerge": boolean,
  "size": string                // 文件大小（字节）
}
```

## 使用方式

### 方式一：使用 FileUploader 组件（推荐）

如果使用 `FileUploader` 组件，组件内部会自动调用此接口，无需手动调用：

```jsx
import FileUploader, { getValueProps, getValueFromEvent } from '@cqsjjb/jjb-react-admin-component/FileUploader';

<Form.Item
  label="上传附件"
  name="fileUrl"
  getValueProps={getValueProps}
  getValueFromEvent={getValueFromEvent}
>
  <FileUploader action={`${process.env.app.API_HOST}/attachment/files/upload-speed-simple`} />
</Form.Item>
```

### 方式二：手动调用接口

如果需要手动调用此接口（例如自定义上传逻辑），可以使用以下方式：

#### 使用 fetch API

```javascript
function uploadSingleFile(file) {
  const API_HOST = process.env.app.API_HOST;
  const token = sessionStorage.getItem('token');
  
  const formData = new FormData();
  formData.append('file', file);
  
  return fetch(`${API_HOST}/attachment/files/upload-speed-simple`, {
    method: 'POST',
    body: formData,
    headers: {
      'token': token,
      // 注意：使用 FormData 时不要手动设置 Content-Type，浏览器会自动设置
    },
  })
    .then(response => response.json())
    .then(data => {
      if (data && data.success !== false) {
        return data;
      } else {
        throw new Error(data?.errMessage || '上传失败');
      }
    });
}

// 使用示例
const fileInput = document.querySelector('input[type="file"]');
fileInput.addEventListener('change', async (e) => {
  const file = e.target.files[0];
  if (file) {
    try {
      const result = await uploadSingleFile(file);
      console.log('上传成功:', result.fileUrl);
    } catch (error) {
      console.error('上传失败:', error);
    }
  }
});
```

#### 使用 axios（如果项目中已引入）

```javascript
import axios from 'axios';

function uploadSingleFile(file) {
  const API_HOST = process.env.app.API_HOST;
  const token = sessionStorage.getItem('token');
  
  const formData = new FormData();
  formData.append('file', file);
  
  return axios({
    method: 'post',
    url: `${API_HOST}/attachment/files/upload-speed-simple`,
    data: formData,
    headers: {
      'token': token,
      'Content-Type': 'multipart/form-data',
    },
  })
    .then(response => {
      const data = response.data;
      if (data && data.success !== false) {
        return data;
      } else {
        throw new Error(data?.errMessage || '上传失败');
      }
    });
}
```

## 注意事项

1. **Token 获取**：Token 必须从 `sessionStorage.getItem('token')` 获取，确保用户已登录。

2. **API_HOST 配置**：接口地址通过 `process.env.app.API_HOST` 获取，确保已在 `jjb.config.js` 中正确配置。

3. **FormData 格式**：
   - 使用 FormData 时，浏览器会自动设置 `Content-Type` 为 `multipart/form-data`，**不要手动设置**（使用 fetch 时）。
   - 使用 axios 时，可以显式设置 `Content-Type: multipart/form-data`。

4. **文件字段名**：提交的 FormData 中文件字段名必须为 `file`。

5. **错误处理**：接口返回的 `success` 字段为 `false` 或存在 `errMessage` 时，表示上传失败。

6. **响应数据**：上传成功后，主要使用 `fileUrl`、`downloadUrl`、`previewUrl` 等字段。

## 相关章节

- **文件上传组件** → `../../10-通用业务组件使用规范/04-文件上传组件/SKILL.md`
- **图片上传组件** → `../../10-通用业务组件使用规范/02-图片上传组件/SKILL.md`
- **接口定义规范** → `../../11-接口与数据层规范/02-接口定义规范/SKILL.md`
- **接口服务配置** → `../../14-环境变量与数据访问/02-接口服务配置.md`
- **认证Token** → `../../14-环境变量与数据访问/04-认证Token.md`
