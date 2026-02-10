# 十九、底座平台API调用规范

## 10. 系统操作 API

## base.call.lockScreen

锁定底座屏幕，解锁需要输入登录密码。

**函数签名**：
```typescript
declare function lockScreen(): void;
```

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  base.call.lockScreen();
}
```

## base.call.loginOut

退出登录。

**函数签名**：
```typescript
declare function loginOut(force?: boolean): void;
```

**参数说明**：
- `force`：是否强制退出（可选）
  - 设置为 `true` 时不弹出询问确认弹窗，直接退出
  - 默认为 `false`，会弹出确认弹窗

**返回值**：
- `void`

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  // 普通退出（会弹出确认弹窗）
  base.call.loginOut();
  
  // 强制退出（不弹出确认弹窗）
  base.call.loginOut(true);
}
```
