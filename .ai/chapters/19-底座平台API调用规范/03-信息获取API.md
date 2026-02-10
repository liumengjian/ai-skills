# 十九、底座平台API调用规范

## 3. 信息获取 API

## base.getClientInfo

获取终端信息。

**函数签名**：
```typescript
declare function getClientInfo(option: {
  onFail?: (e: Error) => void,
  onSuccess?: (e: Record<string, any>) => void
}): void;
```

**参数说明**：
- `option.onFail`：失败回调函数（可选）
- `option.onSuccess`：成功回调函数（可选）

**返回值**：
- `void`

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  base.getClientInfo({
    onSuccess: (data) => {
      console.log('终端信息:', data);
      // 使用终端信息
    },
    onFail: (error) => {
      console.error('获取终端信息失败:', error);
    }
  });
}
```

## base.getTenantInfo

获取当前租户信息。

**函数签名**：
```typescript
declare function getTenantInfo(option: {
  onFail?: (e: Error) => void,
  onSuccess?: (e: Record<string, any>) => void
}): void;
```

**参数说明**：
- `option.onFail`：失败回调函数（可选）
- `option.onSuccess`：成功回调函数（可选）

**返回值**：
- `void`

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  base.getTenantInfo({
    onSuccess: (data) => {
      console.log('租户信息:', data);
    },
    onFail: (error) => {
      console.error('获取租户信息失败:', error);
    }
  });
}
```

## base.getUserInfo

获取当前登录用户信息。

**函数签名**：
```typescript
declare function getUserInfo(option: {
  onFail?: (e: Error) => void,
  onSuccess?: (e: Record<string, any>) => void
}): void;
```

**参数说明**：
- `option.onFail`：失败回调函数（可选）
- `option.onSuccess`：成功回调函数（可选）

**返回值**：
- `void`

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  base.getUserInfo({
    onSuccess: (data) => {
      console.log('用户信息:', data);
      // 使用用户信息
    },
    onFail: (error) => {
      console.error('获取用户信息失败:', error);
    }
  });
}
```
