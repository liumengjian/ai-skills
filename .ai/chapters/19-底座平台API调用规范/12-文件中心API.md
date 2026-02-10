# 十九、底座平台API调用规范

## 12. 文件中心 API

## base.call.openFsPanel

打开文件中心面板。

**函数签名**：
```typescript
interface Option {
  fileType: 'ALL' | 'VIDEO' | 'PICTURE' | 'DOCUMENT';
  allowSwitch?: boolean;
  allowSelect?: boolean;
  filterParams?: {};
  selectedFileIds?: string[];
  selectedFileItems?: {}[];
  onOk?: () => string[];
  onSelect?: () => string[];
}

declare function openFsPanel(option: Option): void;
```

**参数说明**：
- `option.fileType`：文件类型
  - `'ALL'`：全部
  - `'VIDEO'`：视频
  - `'PICTURE'`：图片
  - `'DOCUMENT'`：文档
- `option.allowSwitch`：允许切换文件类型（可选）
- `option.allowSelect`：允许选择（可选）
- `option.filterParams`：过滤参数，请从后端获取（可选）
- `option.selectedFileIds`：已选文件ID集合（可选）
- `option.selectedFileItems`：已选文件对象集合（可选）
- `option.onOk`：确认回调（可选）
- `option.onSelect`：选择回调（可选）

**返回值**：
- `void`

**注意事项**：
- 调用 `openFsPanel` 时，在事件回调函数中必须阻止事件冒泡，否则出现异常情况，请使用 `e.stopPropagation()`

**使用示例**：
```javascript
// 在按钮点击事件中调用时，必须阻止事件冒泡
const handleOpenFileCenter = (e) => {
  e.stopPropagation(); // 必须阻止事件冒泡
  if (typeof window.__IN_BASE__ !== 'undefined') {
    base.call.openFsPanel({
      fileType: 'PICTURE',
      allowSwitch: true,
      allowSelect: true,
      selectedFileIds: ['file-id-1', 'file-id-2'],
      filterParams: {
        // 从后端获取的过滤参数
      },
      onOk: (selectedFileIds) => {
        console.log('确认选择的文件ID:', selectedFileIds);
        // 处理选择的文件
      },
      onSelect: (selectedFileIds) => {
        console.log('当前选择的文件ID:', selectedFileIds);
      }
    });
  }
};
```
