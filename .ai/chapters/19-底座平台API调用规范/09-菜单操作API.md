# 十九、底座平台API调用规范

## 9. 菜单操作 API

## base.call.getMenuInfoByPath

根据菜单地址获取菜单信息。

**函数签名**：
```typescript
declare function getMenuInfoByPath(option: { path: string }): Promise<Record<string, any>>;
```

**参数说明**：
- `option.path`：菜单地址

**返回值**：
- `Promise<Record<string, any>>`：菜单对象集合

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  base.call.getMenuInfoByPath({ path: '/user/list' })
    .then((menuInfo) => {
      console.log('菜单信息:', menuInfo);
      // 使用菜单信息打开菜单
      base.call.openMenu(menuInfo, { id: 123 });
    })
    .catch((error) => {
      console.error('获取菜单信息失败:', error);
    });
}
```

## base.call.openMenu

打开菜单，在 Tag 栏加上菜单标签。

**函数签名**：
```typescript
declare function openMenu(data: Record<string, any>, query?: Record<string, any>): void;
```

**参数说明**：
- `data`：菜单数据，请通过 `base.call.getMenuInfoByPath` 获取
- `query`：需要携带的额外参数（可选）

**返回值**：
- `void`

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  // 先获取菜单信息
  base.call.getMenuInfoByPath({ path: '/user/list' })
    .then((menuInfo) => {
      // 打开菜单并携带参数
      base.call.openMenu(menuInfo, { id: 123, type: 'detail' });
    });
}
```
