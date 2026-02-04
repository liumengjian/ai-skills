# 十九、基座平台API调用规范

## 一、概述

当应用部署到基座平台（父应用）中时，子应用可以通过一套 **baseAPI** 访问基座平台提供的接口，实现子应用与父应用之间的通信和数据交互。

- **全局对象**：`base` - 提供应用与底座之间交互的 API
- **使用场景**：子应用需要获取基座平台提供的能力或数据时
- **调用方式**：通过 `base.xxx()` 的方式调用基座平台提供的接口

**⚠️ 重要约束**：所有 API 必须在应用处于底座中时才有效！调用前需要判断 `window.__IN_BASE__` 变量是否存在。

## 二、判断是否在底座中

在调用 baseAPI 之前，必须先判断当前应用是否运行在底座中：

```javascript
// 判断当前应用是否在底座中
const isInBase = typeof window.__IN_BASE__ !== 'undefined';

if (isInBase) {
  // 可以安全调用 baseAPI
  base.getClientInfo({
    onSuccess: (data) => {
      console.log('终端信息:', data);
    },
    onFail: (error) => {
      console.error('获取失败:', error);
    }
  });
} else {
  console.warn('当前应用不在底座中，无法调用 baseAPI');
}
```

## 三、URL 格式化

### 3.1 base.formatURL

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

## 四、信息获取 API

### 4.1 base.getClientInfo

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

### 4.2 base.getTenantInfo

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

### 4.3 base.getUserInfo

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

## 五、系统信息对象

### 5.1 base.systemInfo

获取系统信息对象（同步获取）。

**类型定义**：
```typescript
interface systemInfo {
  baseTenantId: string;  // 租户ID
  clientId: string;     // 终端ID
  orgId: string;        // 机构/组织ID
  redirect: string;     // 退出登录重定向地址
}
```

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  const systemInfo = base.systemInfo;
  console.log('租户ID:', systemInfo.baseTenantId);
  console.log('终端ID:', systemInfo.clientId);
  console.log('机构ID:', systemInfo.orgId);
  console.log('退出登录重定向地址:', systemInfo.redirect);
}
```

### 5.2 base.themeConfig

获取系统主题配置对象（同步获取）。

**类型定义**：
```typescript
interface themeConfig {
  algorithm: string;      // 主题算法，参考 https://ant-design.antgroup.com/docs/react/customize-theme-cn#基本算法algorithm
  borderRadius: string;  // 圆角
  colorPrimary: string;   // 品牌色
}
```

**使用示例**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  const themeConfig = base.themeConfig;
  console.log('主题算法:', themeConfig.algorithm);
  console.log('圆角:', themeConfig.borderRadius);
  console.log('品牌色:', themeConfig.colorPrimary);
  
  // 使用主题配置
  import { ConfigProvider } from 'antd';
  import { theme } from 'antd';
  
  const algorithm = themeConfig.algorithm === 'darkAlgorithm' 
    ? theme.darkAlgorithm 
    : theme.defaultAlgorithm;
  
  <ConfigProvider
    theme={{
      algorithm,
      token: {
        borderRadius: parseInt(themeConfig.borderRadius),
        colorPrimary: themeConfig.colorPrimary,
      },
    }}
  >
    {/* 应用内容 */}
  </ConfigProvider>
}
```

## 六、插件功能

### 6.1 base.plugin.openFormilyDesign

打开表单引擎（旧版）。

**函数签名**：
```typescript
declare function openFormilyDesign(designCode?: string): void;
```

**参数说明**：
- `designCode`：表单设计 Code（可选）
  - 如果为空，则认为是新增表单
  - 如果不为空，则认为是修改表单

**返回值**：
- `void`

**监听表单引擎关闭**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  // 打开表单引擎
  base.plugin.openFormilyDesign('design-code-123');
  
  // 监听表单引擎关闭事件
  window.addEventListener('message', (e) => {
    const { data, type } = e.data;
    if (type === 'EVENT_FORMILY_DESIGN_EXIT') {
      // 表单引擎返回数据
      console.log('表单设计数据:', data);
      // 处理表单设计数据
    }
  });
}
```

### 6.2 base.plugin.openFormilyDesignNew

打开新版表单引擎。

**函数签名**：
```typescript
declare function openFormilyDesignNew(designCode?: string): void;
```

**参数说明**：
- `designCode`：表单设计 Code（可选）
  - 如果为空，则认为是新增表单
  - 如果不为空，则认为是修改表单

**返回值**：
- `void`

**监听表单引擎关闭**：
```javascript
if (typeof window.__IN_BASE__ !== 'undefined') {
  // 打开新版表单引擎
  base.plugin.openFormilyDesignNew('design-code-123');
  
  // 监听表单引擎关闭事件
  window.addEventListener('message', (e) => {
    const { data, type } = e.data;
    if (type === 'EVENT_FORMILY_DESIGN_EXIT_NEW') {
      // 表单引擎返回数据
      console.log('表单设计数据:', data);
      // 处理表单设计数据
    }
  });
}
```

## 七、调用功能 API（base.call.*）

### 7.1 面板控制

#### base.call.closeAllPanel

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

#### base.call.openServiceMenuPanel

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

#### base.call.openOrganizePanel

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

#### base.call.openActiveSystem

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

#### base.call.openCachePanel

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

#### base.call.openMsgPanel

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

#### base.call.openWorkOrderPanel

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

#### base.call.openSystemPanel

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

#### base.call.openTransferPanel

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

### 7.2 弹窗功能

#### base.call.openPopupAbout

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

#### base.call.openPopupSearch

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

#### base.call.openPopupGuide

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

### 7.3 加密解密

#### base.call.generalDecrypt

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

#### base.call.generalEncrypt

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

### 7.4 菜单操作

#### base.call.getMenuInfoByPath

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

#### base.call.openMenu

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

### 7.5 系统操作

#### base.call.lockScreen

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

#### base.call.loginOut

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

### 7.6 批量操作

#### base.call.batchExport

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

#### base.call.batchImport

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

### 7.7 文件中心

#### base.call.openFsPanel

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

## 八、注意事项和最佳实践

### 8.1 必须遵守

1. **环境判断**：所有 baseAPI 调用前必须判断 `typeof window.__IN_BASE__ !== 'undefined'`，确保应用运行在底座中
2. **错误处理**：对于异步 API（如 `getClientInfo`、`getTenantInfo`、`getUserInfo`），必须提供 `onFail` 回调处理错误情况
3. **参数验证**：调用 API 前验证必要参数是否存在，避免运行时错误

### 8.2 最佳实践

1. **封装工具函数**：将 baseAPI 调用封装成工具函数，统一处理环境判断和错误处理
2. **类型定义**：为 baseAPI 的返回数据定义 TypeScript 类型，提升代码可维护性
3. **异步处理**：对于返回 Promise 的 API（如 `getMenuInfoByPath`），使用 `async/await` 或 `.then().catch()` 处理异步逻辑
4. **事件监听**：对于需要监听事件的 API（如表单引擎），在组件挂载时添加监听，在组件卸载时移除监听

### 8.3 常见错误

1. **未判断环境**：直接调用 baseAPI 而不判断是否在底座中，导致运行时错误
2. **缺少错误处理**：调用异步 API 时未提供 `onFail` 回调，导致错误无法捕获
3. **参数错误**：传递错误的参数类型或格式，导致 API 调用失败
4. **事件监听泄漏**：添加了事件监听但未在组件卸载时移除，导致内存泄漏

## 九、完整示例

```javascript
import React, { useEffect, useState } from 'react';

function MyPage() {
  const [userInfo, setUserInfo] = useState(null);
  const [systemInfo, setSystemInfo] = useState(null);

  useEffect(() => {
    // 判断是否在底座中
    if (typeof window.__IN_BASE__ !== 'undefined') {
      // 获取用户信息
      base.getUserInfo({
        onSuccess: (data) => {
          setUserInfo(data);
          console.log('用户信息:', data);
        },
        onFail: (error) => {
          console.error('获取用户信息失败:', error);
        }
      });

      // 获取系统信息（同步）
      const sysInfo = base.systemInfo;
      setSystemInfo(sysInfo);
      console.log('系统信息:', sysInfo);

      // 监听表单引擎关闭事件
      const handleFormilyDesignExit = (e) => {
        const { data, type } = e.data;
        if (type === 'EVENT_FORMILY_DESIGN_EXIT') {
          console.log('表单设计数据:', data);
          // 处理表单设计数据
        }
      };

      window.addEventListener('message', handleFormilyDesignExit);

      // 清理函数
      return () => {
        window.removeEventListener('message', handleFormilyDesignExit);
      };
    } else {
      console.warn('当前应用不在底座中，无法使用 baseAPI');
    }
  }, []);

  const handleOpenMenu = async () => {
    if (typeof window.__IN_BASE__ !== 'undefined') {
      try {
        // 获取菜单信息
        const menuInfo = await base.call.getMenuInfoByPath({ path: '/user/list' });
        // 打开菜单
        base.call.openMenu(menuInfo, { id: 123 });
      } catch (error) {
        console.error('打开菜单失败:', error);
      }
    }
  };

  const handleOpenFileCenter = (e) => {
    e.stopPropagation(); // 必须阻止事件冒泡
    if (typeof window.__IN_BASE__ !== 'undefined') {
      base.call.openFsPanel({
        fileType: 'PICTURE',
        allowSelect: true,
        onOk: (selectedFileIds) => {
          console.log('选择的文件ID:', selectedFileIds);
        }
      });
    }
  };

  return (
    <div>
      {systemInfo && (
        <div>
          <p>租户ID: {systemInfo.baseTenantId}</p>
          <p>终端ID: {systemInfo.clientId}</p>
        </div>
      )}
      
      {userInfo && (
        <div>
          <p>用户信息已加载</p>
        </div>
      )}

      <button onClick={handleOpenMenu}>打开菜单</button>
      <button onClick={handleOpenFileCenter}>打开文件中心</button>
    </div>
  );
}

export default MyPage;
```
