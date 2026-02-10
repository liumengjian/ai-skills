# 十九、底座平台API调用规范

## 6. 面板控制 API

## base.call.closeAllPanel

关闭底座所有操作面板。

**函数签名**：
```typescript
declare function closeAllPanel(): void;
```

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  base.call.closeAllPanel();
}
```

## base.call.openServiceMenuPanel

打开全部服务菜单。

**函数签名**：
```typescript
declare function openServiceMenuPanel(): void;
```

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  base.call.openServiceMenuPanel();
}
```

## base.call.openOrganizePanel

打开组织单位选择面板。

**函数签名**：
```typescript
declare function openOrganizePanel(): void;
```

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  base.call.openOrganizePanel();
}
```

## base.call.openActiveSystem

激活系统。

**函数签名**：
```typescript
declare function openActiveSystem(): void;
```

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  base.call.openActiveSystem();
}
```

## base.call.openCachePanel

打开数据缓存面板。

**函数签名**：
```typescript
declare function openCachePanel(): void;
```

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  base.call.openCachePanel();
}
```

## base.call.openMsgPanel

打开消息面板。

**函数签名**：
```typescript
declare function openMsgPanel(): void;
```

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  base.call.openMsgPanel();
}
```

## base.call.openWorkOrderPanel

打开系统工单面板。

**函数签名**：
```typescript
declare function openWorkOrderPanel(): void;
```

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  base.call.openWorkOrderPanel();
}
```

## base.call.openSystemPanel

打开系统设置面板。

**函数签名**：
```typescript
declare function openSystemPanel(): void;
```

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  base.call.openSystemPanel();
}
```

## base.call.openTransferPanel

打开导入导出记录面板。

**函数签名**：
```typescript
declare function openTransferPanel(): void;
```

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  base.call.openTransferPanel();
}
```
