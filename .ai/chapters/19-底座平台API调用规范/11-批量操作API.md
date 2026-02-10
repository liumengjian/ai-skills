# 十九、底座平台API调用规范

## 11. 批量操作 API

## base.call.batchExport

打开批量导出面板。

**函数签名**：
```typescript
declare function batchExport(option: { code: string }): void;
```

**参数说明**：
- `option.code`：导出 code，请从后端获取

**返回值**：
- `void`

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  // 从后端获取导出 code
  const exportCode = 'export-code-from-backend';
  base.call.batchExport({ code: exportCode });
}
```

## base.call.batchImport

打开批量导入面板。

**函数签名**：
```typescript
declare function batchImport(option: { code: string }): void;
```

**参数说明**：
- `option.code`：导入 code，请从后端获取

**返回值**：
- `void`

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  // 从后端获取导入 code
  const importCode = 'import-code-from-backend';
  base.call.batchImport({ code: importCode });
}
```
