# 十九、底座平台API调用规范

## 7. 弹窗功能 API

## base.call.openPopupAbout

打开关于系统弹窗。

**函数签名**：
```typescript
declare function openPopupAbout(): void;
```

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  base.call.openPopupAbout();
}
```

## base.call.openPopupSearch

打开全局搜索弹窗。

**函数签名**：
```typescript
declare function openPopupSearch(): void;
```

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  base.call.openPopupSearch();
}
```

## base.call.openPopupGuide

打开新手引导弹窗。

**函数签名**：
```typescript
declare function openPopupGuide(): void;
```

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  base.call.openPopupGuide();
}
```
