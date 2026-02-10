# 十九、底座平台API调用规范

## 8. 加密解密 API

## base.call.generalDecrypt

底座通用解密。

**函数签名**：
```typescript
declare function generalDecrypt(content?: string): string;
```

**参数说明**：
- `content`：需要解密的文本（可选）

**返回值**：
- 解密后的文本

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  const decryptedText = base.call.generalDecrypt('encrypted-content');
  console.log('解密后的文本:', decryptedText);
}
```

## base.call.generalEncrypt

底座通用加密。

**函数签名**：
```typescript
declare function generalEncrypt(content?: string): string;
```

**参数说明**：
- `content`：需要加密的文本（可选）

**返回值**：
- 加密后的文本

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  const encryptedText = base.call.generalEncrypt('plain-text');
  console.log('加密后的文本:', encryptedText);
}
```
