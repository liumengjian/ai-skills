---
name: jjb-category-tree
description: 定义分类树组件规范。在使用左侧树形分类导航、分类搜索、右键菜单操作时使用。
---

# 页面布局与通用 UI 规范

## 分类树组件

分类树用于左侧导航区域，提供树形结构的浏览、搜索、右键菜单操作等功能。

### 布局与宽度

- 分类树作为左侧面板，**固定宽度**，通常为 **240px ~ 260px**，高度撑满父容器。
- 树内容区 `flex: 1; overflow: auto`，节点过多时可垂直滚动。
- 结构分区（自上而下）：
  1. **标题栏**：左侧显示标题文字（如"文件夹"），右侧放置新建图标按钮。
  2. **搜索栏**：输入框带搜索前缀图标，`size="small"`，支持 `allowClear`。
  3. **树主体**：`Spin` 包裹 `Tree` 组件，空数据时显示"暂无数据"占位提示。

```less
.category-tree {
  display: flex;
  flex-direction: column;
  height: 100%;

  .category-tree-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 12px 8px;
  }

  .category-tree-search {
    padding: 0 12px 8px;
  }

  .category-tree-body {
    flex: 1;
    overflow: auto;
    padding: 0 8px;
  }
}
```

### 树节点渲染

- 使用 `titleRender` 自定义节点内容，组合**高亮文本**与**悬停操作图标**。
- 使用 `fieldNames` 将后端字段映射为 Tree 所需格式（`title` → 显示名、`key` → 唯一标识、`children` → 子节点）。
- 设置 `blockNode` 使整行可点击，提升操作区域。
- 节点标题文本需设置溢出省略：

```less
.tree-node-title {
  flex: 1;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

```jsx
<Tree
  treeData={filteredTree}
  blockNode
  fieldNames={{ title: 'folderName', key: 'id', children: 'children' }}
  titleRender={(nodeData) => (
    <div className="tree-node">
      <span className="tree-node-title">{highlight(nodeData.folderName, searchValue)}</span>
      <Space className="tree-node-actions" size={4}>
        <FolderAddOutlined onClick={(e) => { e.stopPropagation(); handleCreate(nodeData.id); }} />
        <EditOutlined onClick={(e) => { e.stopPropagation(); handleRename(nodeData); }} />
        <DeleteOutlined onClick={(e) => { e.stopPropagation(); handleDelete(nodeData); }} style={{ color: '#ff4d4f' }} />
      </Space>
    </div>
  )}
/>
```

> **注意**：操作图标的 `onClick` 必须 `e.stopPropagation()` 阻止冒泡，避免触发树节点选中。

### 选中态与悬停交互

- 选中节点背景色使用浅蓝 `#e6f4ff`。
- 悬停时显示行内操作图标，默认隐藏，通过 CSS 控制：

```less
.tree-node-actions {
  display: none;
  flex-shrink: 0;
}

:global {
  .ant-tree-treenode:hover .tree-node-actions {
    display: inline-flex;
  }

  .ant-tree-treenode-selected .ant-tree-node-content-wrapper {
    background: #e6f4ff;
  }
}
```

- 节点内边距不宜过大，保持紧凑：`.ant-tree-node-content-wrapper { padding: 2px 4px; }`。

### 搜索匹配文字高亮

- 在搜索框中输入关键词后，树节点中**匹配的文字**需高亮显示。
- 高亮颜色使用主题蓝色 `#0064C8`。
- 实现方式：将节点标题文本按关键词拆分，匹配部分用 `<span style={{ color: '#0064C8' }}>` 包裹。
- 关键词中的正则特殊字符需转义处理。

```jsx
function highlight(text, keyword) {
  if (!keyword) return text;
  const escaped = keyword.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const regex = new RegExp(`(${escaped})`, 'gi');
  return text.split(regex).map((part, i) =>
    regex.test(part) ? <span key={i} style={{ color: '#0064C8' }}>{part}</span> : part
  );
}
```

- 搜索结果需 **过滤树**：保留标题匹配的节点，以及其子孙中有匹配的父节点（保持树结构）。
- 搜索有值时，应**自动展开所有匹配节点**，让用户直接看到结果。

### 右键菜单操作

- 使用 `Dropdown` + `menu` + `trigger={['contextMenu']}` 实现右键弹出菜单。
- `Dropdown` 包裹整个 `Tree` 组件，`onRightClick` 记录当前右键节点。
- 菜单项通常包括：**新建子文件夹**、**重命名**、**删除**（删除项标记 `danger: true`）。
- 删除操作需弹出二次确认弹窗（`Modal.confirm`），提示删除后不可恢复。

```jsx
const contextMenuItems = [
  { key: 'create', label: '新建子文件夹' },
  { key: 'rename', label: '重命名' },
  { key: 'delete', label: '删除', danger: true },
];

<Dropdown menu={{ items: contextMenuItems, onClick: handleContextMenuClick }} trigger={['contextMenu']}>
  <Tree
    treeData={filteredTree}
    onRightClick={({ node }) => setRightClickNode(node)}
    // ...
  />
</Dropdown>
```

- 右键新建子文件夹时，`parentId` 为右键节点的 id；标题栏新建按钮点击时，`parentId` 为当前选中节点 id（无选中则传 `null` 表示根级新建）。

### 新增/重命名弹窗

- 使用 `Modal` + `Input` 实现新增和重命名，两种操作复用同一弹窗，通过状态区分标题文案。
- 输入框绑定 `onPressEnter` 支持回车确认。
- 名称需 `trim()` 处理，空值不允许提交。
- Modal 的 `confirmLoading` 绑定提交 loading 状态，防止重复点击。

```jsx
<Modal
  title={modalType === 'create' ? (parentId != null ? '新建子文件夹' : '新建文件夹') : '重命名'}
  open={modalOpen}
  onOk={handleModalOk}
  onCancel={() => setModalOpen(false)}
  confirmLoading={submitLoading}
  destroyOnClose
>
  <Input
    placeholder="请输入文件夹名称"
    value={modalName}
    onChange={e => setModalName(e.target.value)}
    onPressEnter={handleModalOk}
  />
</Modal>
```

> `destroyOnClose` 确保每次打开弹窗时输入框状态被重置。

### Loading 状态

- 树数据加载时：使用 `Spin` 组件包裹树主体，绑定树数据的 loading 状态。
- 提交操作时：Modal 的 `confirmLoading` 绑定提交 loading，防止重复提交。
- 操作完成后需**重新请求树数据**刷新列表。

```jsx
<Spin spinning={treeLoading}>
  <div className="category-tree-body">
    {filteredTree.length > 0 ? <Tree ... /> : <div className="category-tree-empty">暂无文件夹</div>}
  </div>
</Spin>
```

### 空状态

- 树数据为空或搜索无结果时，显示居中占位文字"暂无文件夹"。
- 样式：`text-align: center; color: #999; padding: 24px 0; font-size: 13px;`。
