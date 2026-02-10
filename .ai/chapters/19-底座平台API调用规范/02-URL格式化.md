# 十九、底座平台API调用规范

## 2. URL 格式化

## base.formatURL

格式化 URL，绑定底座的 Token 到 URL 上。

**函数签名**：
```typescript
declare function formatURL(url: string, query?: Record<string, any>): string;
```

**参数说明**：
- `url`：URL 地址
- `query`：额外的查询参数（可选）

**返回值**：
- 返回格式化后的 URL（已绑定 Token）

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  // 格式化 URL，自动绑定 Token
  const formattedUrl = base.formatURL('/api/user/list', { page: 1, size: 10 });
  console.log('格式化后的URL:', formattedUrl);
}
```
