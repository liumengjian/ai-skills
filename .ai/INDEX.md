# 前端微应用开发规范 - 快速索引

> 本文档是前端开发规范的快速索引，用于帮助 Cursor 快速定位相关规范内容。  
> **完整规范已拆分为独立章节文件，位于 `chapters/` 目录下**

---

## 📋 目录导航

### 基础配置
- **技术栈与组件库** → [`chapters/01-技术栈与基础.md`](./chapters/01-技术栈与基础.md)（React18、antd5、@cqsjjb/jjb-react-admin-component、@cqsjjb/jjb-common-lib、@cqsjjb/jjb-dva-runtime）
- **应用配置** → [`chapters/02-应用配置与开发环境.md`](./chapters/02-应用配置与开发环境.md)（jjb.config.js、appIdentifier、Babel、@cqsjjb/scripts、Webpack/Rspack 配置、资源导入）
- **项目结构** → [`chapters/03-项目页面结构.md`](./chapters/03-项目页面结构.md)（页面目录、命名规范、路由机制、枚举值使用、组件开发规范、InjectContext）
- **路由导航** → [`chapters/04-路由与导航.md`](./chapters/04-路由与导航.md)（history.push 使用、路由页面组件）

### UI 组件规范
- **页面布局** → [`chapters/05-页面布局与通用UI规范.md`](./chapters/05-页面布局与通用UI规范.md)（PageLayout、右上角操作区）
- **搜索区** → [`chapters/06-搜索区规范.md`](./chapters/06-搜索区规范.md)（SearchForm、状态持久化、router.query、formLine）
- **表格** → [`chapters/07-表格规范.md`](./chapters/07-表格规范.md)（Table、TableAction、批量操作、Empty、删除确认）
- **表单** → [`chapters/08-表单与交互规范.md`](./chapters/08-表单与交互规范.md)（Form、layout="vertical"、数据回填、提交规范、showSearch、allowClear、placeholder）
- **弹窗** → [`chapters/09-弹窗规范.md`](./chapters/09-弹窗规范.md)（Modal 使用、最大高度限制、context.modal）
- **业务组件** → [`chapters/10-通用业务组件使用规范.md`](./chapters/10-通用业务组件使用规范.md)（Editor、ImageUploader、FileUploader、ImageCropper、AMap、getValueProps）

### 数据层规范
- **接口定义** → [`chapters/11-接口与数据层规范.md`](./chapters/11-接口与数据层规范.md)（declareRequest、Connect、命名空间、字典数据、useDict）**⚠️ 注意：此章节仅适用于后端接口，不适用于基座平台API**
- **详情展示** → [`chapters/12-详情展示规范.md`](./chapters/12-详情展示规范.md)（Loading、Descriptions、数据溯源逻辑）

### 高级功能
- **云组件** → [`chapters/13-云组件使用规范.md`](./chapters/13-云组件使用规范.md)（CloudComponent、ImportCloudComponent、useUnMountCloudComponentStyle）
- **环境变量** → [`chapters/14-环境变量与数据访问.md`](./chapters/14-环境变量与数据访问.md)（主题色、API_HOST、Token、process.env.app）
- **构建部署** → [`chapters/15-构建与部署.md`](./chapters/15-构建与部署.md)（应用推送、jjb-cmd push java）
- **权限控制** → [`chapters/16-权限控制规范.md`](./chapters/16-权限控制规范.md)（Permission 装饰器）
- **动态文本** → [`chapters/17-接口动态文本配置.md`](./chapters/17-接口动态文本配置.md)（Interpolation、接口动态文本）
- **GitLab 规范** → [`chapters/18-GitLab规范.md`](./chapters/18-GitLab规范.md)（GitLab 地址、仓库管理、分支命名、代码提交）
- **基座平台API** → [`chapters/19-基座平台API调用规范.md`](./chapters/19-基座平台API调用规范.md)（baseAPI、父应用接口调用、window.__IN_BASE__、getClientInfo、getTenantInfo 等）**⚠️ 重要：调用基座平台API必须参考此章节，不要使用 declareRequest**

### 核心约束
- **AI 执行约束** → [`chapters/20-AI执行约束.md`](./chapters/20-AI执行约束.md)（必须遵守）

---

## 🚀 常用规范速查

### 页面开发必读
| 场景 | 章节位置 | 关键点 |
|------|---------|--------|
| **创建新页面** | [`chapters/03-项目页面结构.md`](./chapters/03-项目页面结构.md) | 目录：`src/pages/Container/`，命名：大驼峰 |
| **页面布局** | [`chapters/05-页面布局与通用UI规范.md`](./chapters/05-页面布局与通用UI规范.md) | 必须使用 `PageLayout`，右上角操作区 |
| **搜索表单** | [`chapters/06-搜索区规范.md`](./chapters/06-搜索区规范.md) | 必须使用 `SearchForm`，状态用 `router.query`，formLine 布局 |
| **数据表格** | [`chapters/07-表格规范.md`](./chapters/07-表格规范.md) | 使用 `TableAction`，必须有 loading，空数据用 Empty |
| **表单提交** | [`chapters/08-表单与交互规范.md`](./chapters/08-表单与交互规范.md) | layout="vertical"，必须有 loading 防重提交，showSearch |
| **接口定义** | [`chapters/11-接口与数据层规范.md`](./chapters/11-接口与数据层规范.md) | 使用 `declareRequest`，Connect 连接，命名空间（**仅适用于后端接口**） |
| **基座平台API** | [`chapters/19-基座平台API调用规范.md`](./chapters/19-基座平台API调用规范.md) | 使用 `baseAPI`，必须先判断 `window.__IN_BASE__`（**不适用 declareRequest**） |
| **详情展示** | [`chapters/12-详情展示规范.md`](./chapters/12-详情展示规范.md) | 必须使用 Descriptions，Loading 状态，数据溯源逻辑 |

### 组件使用速查
| 组件 | 章节位置 | 导入路径 |
|------|---------|---------|
| **PageLayout** | [`chapters/05-页面布局与通用UI规范.md`](./chapters/05-页面布局与通用UI规范.md) | `@cqsjjb/jjb-react-admin-component/PageLayout` |
| **SearchForm** | [`chapters/06-搜索区规范.md`](./chapters/06-搜索区规范.md) | `@cqsjjb/jjb-react-admin-component/SearchForm` |
| **TableAction** | [`chapters/07-表格规范.md`](./chapters/07-表格规范.md) | `@cqsjjb/jjb-react-admin-component/TableAction` |
| **ImageUploader** | [`chapters/10-通用业务组件使用规范.md`](./chapters/10-通用业务组件使用规范.md) | `@cqsjjb/jjb-react-admin-component/ImageUploader` |
| **FileUploader** | [`chapters/10-通用业务组件使用规范.md`](./chapters/10-通用业务组件使用规范.md) | `@cqsjjb/jjb-react-admin-component/FileUploader` |
| **Editor** | [`chapters/10-通用业务组件使用规范.md`](./chapters/10-通用业务组件使用规范.md) | `@cqsjjb/jjb-react-admin-component/Editor` |
| **ImageCropper** | [`chapters/10-通用业务组件使用规范.md`](./chapters/10-通用业务组件使用规范.md) | `@cqsjjb/jjb-react-admin-component/ImageCropper` |
| **AMap** | [`chapters/10-通用业务组件使用规范.md`](./chapters/10-通用业务组件使用规范.md) | `@cqsjjb/jjb-react-admin-component/AMap` |

### 工具库速查
| 功能 | 章节位置 | 导入方式 |
|------|---------|---------|
| **路由查询参数** | [`chapters/06-搜索区规范.md`](./chapters/06-搜索区规范.md) | `import { tools } from '@cqsjjb/jjb-common-lib'; tools.router.query` |
| **HTTP 请求** | [`chapters/11-接口与数据层规范.md`](./chapters/11-接口与数据层规范.md) | `import { http } from '@cqsjjb/jjb-common-lib';`（**仅适用于后端接口**） |
| **基座平台API** | [`chapters/19-基座平台API调用规范.md`](./chapters/19-基座平台API调用规范.md) | 使用全局对象 `base`，如 `base.getClientInfo()`（**不适用 http 或 declareRequest**） |
| **加解密** | [`chapters/01-技术栈与基础.md`](./chapters/01-技术栈与基础.md) | `import { crypto } from '@cqsjjb/jjb-common-lib';` |
| **颜色值** | [`chapters/01-技术栈与基础.md`](./chapters/01-技术栈与基础.md) | `import { color } from '@cqsjjb/jjb-common-lib';` |
| **工具函数** | [`chapters/01-技术栈与基础.md`](./chapters/01-技术栈与基础.md) | `import { tools } from '@cqsjjb/jjb-common-lib';` |
| **QS 模块** | [`chapters/01-技术栈与基础.md`](./chapters/01-技术栈与基础.md) | `import { qs } from '@cqsjjb/jjb-common-lib';` |

### 构建工具速查
| 工具/配置 | 章节位置 | 说明 |
|---------|---------|------|
| **@cqsjjb/scripts** | [`chapters/02-应用配置与开发环境.md`](./chapters/02-应用配置与开发环境.md) | 微应用开发和编译构建工具（基于 Rspack） |
| **appIdentifier** | [`chapters/02-应用配置与开发环境.md`](./chapters/02-应用配置与开发环境.md) | 应用标识符，用于路由 basename 和构建产物命名 |
| **webpackConfig** | [`chapters/02-应用配置与开发环境.md`](./chapters/02-应用配置与开发环境.md) | Webpack/Rspack 配置扩展 |
| **GitLab 地址** | [`chapters/18-GitLab规范.md`](./chapters/18-GitLab规范.md) | 项目统一 GitLab 服务器地址和仓库管理规范 |

---

## ⚠️ 关键约束速查

### 必须遵守（违反会导致错误）
1. **组件属性**：禁止猜测组件属性，必须参考 MD 文档或 d.ts 文件
2. **接口数据**：禁止使用 `useState` 管理接口数据，必须使用 `declareRequest`
3. **页面布局**：必须使用 `PageLayout`（除非明确不需要）
4. **表单布局**：Form 的 `layout` 必须使用 `vertical`
5. **删除操作**：必须使用 `InjectContext` 中的 `context.modal.confirm` 二次确认
6. **Modal/Message/Notification 静态方法**：禁止直接使用 `antd` 的静态方法（`Modal.confirm`、`message.success()`、`notification.info()` 等），必须通过 `InjectContext` 获取使用；允许使用 `<Modal>` 组件标签形式
7. **空数据**：禁止留白，必须使用 `antd/Empty`
8. **输入控件**：必须包含 `allowClear` 和 `placeholder`
9. **下拉选择搜索**：除提示语明确要求不做搜索外，所有 `Select` 和 `Cascader` 必须支持搜索（添加 `showSearch`）
10. **构建工具**：使用 `@cqsjjb/scripts` 进行开发和构建，配置在 `jjb.config.js` 中
11. **InjectContext**：静态方法必须通过 `InjectContext` 使用 `context.modal`、`context.message`、`context.notification`
12. **代码注释**：函数、变量、常量、逻辑判断都必须加上详细注释
13. **事件命名**：自定义组件事件统一使用 `onXXX` 格式，命名要贴合实际功能
14. **组件开发**：新增组件推荐使用 Hooks 组件（函数式组件 + Hooks）
15. **字典数据**：统一使用 Hooks 方式获取，在 `api` 中定义接口（传统 http 方式），在 `hooks` 中创建 Hook
16. **枚举值使用**：后端返回的枚举值必须维护到 `~/enumerate/enum/index.js`，禁止硬编码判断
17. **接口数据格式**：创建新接口时必须询问用户接口返回的数据格式（JSON 示例），以便识别枚举值字段（例外：使用【gen-api-code】工具生成时无需询问）

### 命名规范
- **页面/组件文件夹**：大驼峰（PascalCase），如 `UserList`
- **API 文件夹**：小驼峰（camelCase），如 `userList`
- **接口 Action**：小驼峰 + `Action` 后缀，如 `fetchUserAction`
- **路径别名**：统一使用 `~` 指向 `src` 目录

### 目录结构

> **说明**：以下为项目的**经典/标准目录结构示意图**，实际项目可能略有调整，但整体结构保持一致。

```
项目根目录/
├── public/
│   └── index.html              # 项目 HTML 模板
├── src/
│   ├── main.js                 # 应用入口文件
│   ├── pages/                  # 应用页面文件夹
│   │   └── Container/          # 应用页面入口容器（全局主题配置、InjectContext）
│   │       └── Entry/          # 默认入口页面
│   ├── components/              # 公共组件
│   ├── api/                    # 接口定义（小驼峰）
│   ├── enumerate/              # 枚举、常量、命名空间
│   │   ├── namespace/          # 命名空间定义
│   │   ├── enum/               # 枚举值
│   │   ├── constant/           # 常量
│   │   └── context/            # React Context（导出 InjectContext）
│   ├── hooks/                  # 自定义 Hooks 目录
│   └── utils/                  # 工具函数
├── jjb.config.js               # 应用配置文件
└── jjb.babel.js                # Babel 配置文件
```

**核心文件说明**：
- `src/main.js`：应用入口文件
- `src/pages/Container`：页面入口容器，负责全局主题配置和 `InjectContext` 注册（值为 `antd useApp()`）
- `src/enumerate/context`：导出 `InjectContext` 上下文（在 `Container` 中注册使用）
- `src/hooks/`：自定义 Hooks 目录（字典数据 Hook 等）
- `public/index.html`：项目 HTML 模板

---

## 🔍 按场景查找

### 场景：创建列表页
1. 创建页面目录 → [`chapters/03-项目页面结构.md`](./chapters/03-项目页面结构.md)
2. 使用 PageLayout → [`chapters/05-页面布局与通用UI规范.md`](./chapters/05-页面布局与通用UI规范.md)
3. 添加搜索表单 → [`chapters/06-搜索区规范.md`](./chapters/06-搜索区规范.md)
4. 定义接口 → [`chapters/11-接口与数据层规范.md`](./chapters/11-接口与数据层规范.md)（declareRequest）
5. 连接数据 → [`chapters/11-接口与数据层规范.md`](./chapters/11-接口与数据层规范.md)（Connect）
6. 渲染表格 → [`chapters/07-表格规范.md`](./chapters/07-表格规范.md)

### 场景：创建表单页
1. 创建页面目录 → [`chapters/03-项目页面结构.md`](./chapters/03-项目页面结构.md)
2. 使用 PageLayout → [`chapters/05-页面布局与通用UI规范.md`](./chapters/05-页面布局与通用UI规范.md)
3. 使用 Form（layout="vertical"）→ [`chapters/08-表单与交互规范.md`](./chapters/08-表单与交互规范.md)
4. 定义提交接口 → [`chapters/11-接口与数据层规范.md`](./chapters/11-接口与数据层规范.md)
5. 数据回填 → [`chapters/08-表单与交互规范.md`](./chapters/08-表单与交互规范.md)（数据回填策略）

### 场景：创建详情页
1. 创建页面目录 → [`chapters/03-项目页面结构.md`](./chapters/03-项目页面结构.md)（动态路由用 `_id` 后缀）
2. 使用 PageLayout → [`chapters/05-页面布局与通用UI规范.md`](./chapters/05-页面布局与通用UI规范.md)
3. 使用 Descriptions → [`chapters/12-详情展示规范.md`](./chapters/12-详情展示规范.md)（必须使用 Descriptions，禁止 div/p 标签）
4. 数据获取 → [`chapters/12-详情展示规范.md`](./chapters/12-详情展示规范.md)（数据溯源逻辑：使用行数据/通过接口获取/通过地址栏 ID）
5. Loading 状态 → [`chapters/12-详情展示规范.md`](./chapters/12-详情展示规范.md)（必须具备 Loading 状态）

### 场景：文件上传
1. 单图上传 → [`chapters/10-通用业务组件使用规范.md`](./chapters/10-通用业务组件使用规范.md)（ImageUploader + getValueProps）
2. 多图上传 → [`chapters/10-通用业务组件使用规范.md`](./chapters/10-通用业务组件使用规范.md)（antd/Upload）
3. 单附件上传 → [`chapters/10-通用业务组件使用规范.md`](./chapters/10-通用业务组件使用规范.md)（FileUploader）
4. 多附件上传 → [`chapters/10-通用业务组件使用规范.md`](./chapters/10-通用业务组件使用规范.md)（antd/Upload）

### 场景：调用基座平台API
1. 判断是否在底座中 → [`chapters/19-基座平台API调用规范.md`](./chapters/19-基座平台API调用规范.md)（必须先判断 `window.__IN_BASE__`）
2. 调用baseAPI → [`chapters/19-基座平台API调用规范.md`](./chapters/19-基座平台API调用规范.md)（使用 `base.getClientInfo()`、`base.getTenantInfo()` 等）
3. **⚠️ 重要**：基座平台API**不使用** `declareRequest` 或 `http`，直接使用全局对象 `base`

### 场景：应用部署
1. 配置后端仓库 → [`chapters/18-GitLab规范.md`](./chapters/18-GitLab规范.md)（GitLab 地址、仓库命名、分支命名）
2. 配置 jjb.config.js → [`chapters/15-构建与部署.md`](./chapters/15-构建与部署.md)（javaGit、javaGitName、javaGitBranch）
3. 执行推送命令 → [`chapters/15-构建与部署.md`](./chapters/15-构建与部署.md)（`jjb-cmd push java <环境>`）
4. **⚠️ 重要**：确保已取得后端仓库 Git 权限，否则推送失败

---

## 📝 接口定义模板速查

> **⚠️ 重要区分**：
> - **后端接口**：使用 `declareRequest`（见下方模板）
> - **基座平台API**：使用全局对象 `base`，参考 [`chapters/19-基座平台API调用规范.md`](./chapters/19-基座平台API调用规范.md)

### 后端接口（使用 declareRequest）

#### GET 请求（列表）
```javascript
export const getListAction = declareRequest(
  'loading',
  'Get > /api/list',
  'list: [] | res.data || [] & total: 0 | res.totalCount || 0'
);
```

#### POST 请求（创建）
```javascript
export const createAction = declareRequest(
  'confirmLoading',
  'Post > @/api/create'
);
```

#### GET 请求（详情）
```javascript
export const getDetailAction = declareRequest(
  'loading',
  'Get > /api/detail/{id}',
  'detail: {} | res.data || {}'
);
```

#### Connect 使用（推荐方式）
```javascript
import { Connect } from '@cqsjjb/jjb-dva-runtime';
import { NS_USER } from '~/enumerate/namespace';

function Component({ user, fetchUserAction }) {
  useEffect(() => {
    fetchUserAction({ id: 1 });
  }, []);
  
  return <div>{user.userInfo?.name}</div>;
}

export default Connect([NS_USER], true)(Component);
```

### 基座平台API（使用 base 对象）

#### 获取终端信息示例
```javascript
// ⚠️ 重要：必须先判断是否在底座中
if (typeof window.__IN_BASE__ !== 'undefined') {
  // 使用 baseAPI 获取终端信息
  base.getClientInfo({
    onSuccess: (data) => {
      console.log('终端信息:', data);
    },
    onFail: (error) => {
      console.error('获取失败:', error);
    }
  });
}
```

**⚠️ 重要提示**：
- 基座平台API**不使用** `declareRequest`、`Connect` 或 `http`
- 必须使用全局对象 `base`，如 `base.getClientInfo()`、`base.getTenantInfo()` 等
- 调用前必须先判断 `window.__IN_BASE__` 是否存在
- 详细API列表和使用方法请参考 [`chapters/19-基座平台API调用规范.md`](./chapters/19-基座平台API调用规范.md)

### InjectContext 使用模板
```javascript
import React, { useContext, useState } from 'react';
import { Modal } from 'antd';
import { InjectContext } from '~/enumerate/context';

function MyComponent() {
  const context = useContext(InjectContext);
  const [modalOpen, setModalOpen] = useState(false);

  // ✅ 正确：使用 context.message 替代 message.success() 静态方法
  context.message.success('操作成功！');
  context.message.error('操作失败！');
  // ❌ 错误：禁止使用 message.success() 静态方法

  // ✅ 正确：使用 context.modal.confirm 替代 Modal.confirm 静态方法
  context.modal.confirm({
    title: '确认删除',
    content: '确定要删除这条记录吗？',
    onOk: () => {
      // 删除逻辑
    },
  });
  // ❌ 错误：禁止使用 Modal.confirm 静态方法

  // ✅ 正确：使用 context.notification 替代 notification.info() 静态方法
  context.notification.info({
    message: '提示',
    description: '这是一条通知消息',
  });
  // ❌ 错误：禁止使用 notification.info() 静态方法

  // ✅ 正确：允许使用 <Modal> 组件标签
  return (
    <Modal open={modalOpen} onCancel={() => setModalOpen(false)}>
      弹窗内容
    </Modal>
  );
}
```

---

## 🎯 快速定位关键词

| 关键词 | 章节文件 |
|--------|---------|
| `declareRequest` | [`chapters/11-接口与数据层规范.md`](./chapters/11-接口与数据层规范.md) |
| `Connect` | [`chapters/11-接口与数据层规范.md`](./chapters/11-接口与数据层规范.md) |
| `PageLayout` | [`chapters/05-页面布局与通用UI规范.md`](./chapters/05-页面布局与通用UI规范.md) |
| `SearchForm` | [`chapters/06-搜索区规范.md`](./chapters/06-搜索区规范.md) |
| `TableAction` | [`chapters/07-表格规范.md`](./chapters/07-表格规范.md) |
| `router.query` | [`chapters/06-搜索区规范.md`](./chapters/06-搜索区规范.md) |
| `ImageUploader` | [`chapters/10-通用业务组件使用规范.md`](./chapters/10-通用业务组件使用规范.md) |
| `Form.Item` | [`chapters/08-表单与交互规范.md`](./chapters/08-表单与交互规范.md) |
| `Modal.confirm` | [`chapters/07-表格规范.md`](./chapters/07-表格规范.md)、[`chapters/09-弹窗规范.md`](./chapters/09-弹窗规范.md) |
| `InjectContext` | [`chapters/03-项目页面结构.md`](./chapters/03-项目页面结构.md) |
| `context.modal` | [`chapters/03-项目页面结构.md`](./chapters/03-项目页面结构.md)、[`chapters/09-弹窗规范.md`](./chapters/09-弹窗规范.md) |
| `context.message` | [`chapters/03-项目页面结构.md`](./chapters/03-项目页面结构.md) |
| `context.notification` | [`chapters/03-项目页面结构.md`](./chapters/03-项目页面结构.md) |
| `Descriptions` | [`chapters/12-详情展示规范.md`](./chapters/12-详情展示规范.md) |
| `Permission` | [`chapters/16-权限控制规范.md`](./chapters/16-权限控制规范.md) |
| `Interpolation` | [`chapters/17-接口动态文本配置.md`](./chapters/17-接口动态文本配置.md) |
| `appIdentifier` | [`chapters/02-应用配置与开发环境.md`](./chapters/02-应用配置与开发环境.md) |
| `@cqsjjb/scripts` | [`chapters/02-应用配置与开发环境.md`](./chapters/02-应用配置与开发环境.md) |
| `showSearch` | [`chapters/08-表单与交互规范.md`](./chapters/08-表单与交互规范.md) |
| `useDict` / 字典数据 | [`chapters/11-接口与数据层规范.md`](./chapters/11-接口与数据层规范.md) |
| `onXXX` 事件命名 | [`chapters/20-AI执行约束.md`](./chapters/20-AI执行约束.md) |
| Hooks 组件 | [`chapters/03-项目页面结构.md`](./chapters/03-项目页面结构.md) |
| 枚举值使用 | [`chapters/03-项目页面结构.md`](./chapters/03-项目页面结构.md) |
| 接口数据格式询问 | [`chapters/20-AI执行约束.md`](./chapters/20-AI执行约束.md) |
| GitLab / 仓库管理 | [`chapters/18-GitLab规范.md`](./chapters/18-GitLab规范.md) |
| `getValueProps` | [`chapters/10-通用业务组件使用规范.md`](./chapters/10-通用业务组件使用规范.md) |
| `router.query` | [`chapters/06-搜索区规范.md`](./chapters/06-搜索区规范.md) |
| `formLine` | [`chapters/06-搜索区规范.md`](./chapters/06-搜索区规范.md) |
| `baseAPI` / `base` | [`chapters/19-基座平台API调用规范.md`](./chapters/19-基座平台API调用规范.md) |
| `window.__IN_BASE__` | [`chapters/19-基座平台API调用规范.md`](./chapters/19-基座平台API调用规范.md) |
| `base.getClientInfo` / 获取终端信息 | [`chapters/19-基座平台API调用规范.md`](./chapters/19-基座平台API调用规范.md) |
| `base.getTenantInfo` / 获取租户信息 | [`chapters/19-基座平台API调用规范.md`](./chapters/19-基座平台API调用规范.md) |
| `base.formatURL` | [`chapters/19-基座平台API调用规范.md`](./chapters/19-基座平台API调用规范.md) |
| 基座平台API / 父应用接口 | [`chapters/19-基座平台API调用规范.md`](./chapters/19-基座平台API调用规范.md) |
| `CloudComponent` | [`chapters/13-云组件使用规范.md`](./chapters/13-云组件使用规范.md) |
| `process.env.app` | [`chapters/14-环境变量与数据访问.md`](./chapters/14-环境变量与数据访问.md) |
| `history.push` | [`chapters/04-路由与导航.md`](./chapters/04-路由与导航.md) |
| 数据溯源逻辑 | [`chapters/12-详情展示规范.md`](./chapters/12-详情展示规范.md) |
| `allowClear` / `placeholder` | [`chapters/08-表单与交互规范.md`](./chapters/08-表单与交互规范.md) |

---

## 💡 使用建议

1. **首次开发**：按顺序阅读 [`chapters/01-技术栈与基础.md`](./chapters/01-技术栈与基础.md) → [`chapters/11-接口与数据层规范.md`](./chapters/11-接口与数据层规范.md)，了解整体架构
2. **日常开发**：使用本索引快速定位相关章节文件
3. **遇到问题**：使用关键词搜索，定位到具体章节文件
4. **组件使用**：先查索引找到组件章节文件，再查看完整规范

---

**文件结构说明**：
- 完整规范已拆分为 20 个独立章节文件，位于 `chapters/` 目录下
- 每个章节文件对应一个主题，便于快速定位和查阅
- 索引文件中的链接指向对应的章节文件

**重要提示**：
- 所有组件使用前必须严格参考对应 MD 文档或 `.d.ts` 文件，禁止猜测组件属性
- **接口调用区分**：
  - **后端接口**：必须使用 `declareRequest` + `Connect` 方式管理，禁止使用 `useState` 管理接口数据
  - **基座平台API**：必须使用全局对象 `base`（如 `base.getClientInfo()`），**不使用** `declareRequest`、`Connect` 或 `http`，调用前必须先判断 `window.__IN_BASE__`
- 所有静态方法（`Modal.confirm`、`message.success()` 等）必须通过 `InjectContext` 使用
- 所有表单必须使用 `layout="vertical"`，所有输入控件必须包含 `allowClear` 和 `placeholder`
- 所有 `Select` 和 `Cascader` 必须支持搜索（添加 `showSearch`），除非明确要求不做搜索
