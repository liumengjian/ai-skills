---
name: spec-index
description: 前端微应用开发规范总索引，快速定位领域 SKILL 与关键词对应的 specs。Use when searching for frontend specs, locating specs by keyword, or getting an overview of all specifications.
---

# 前端微应用开发规范 - 总索引

> 完整规范细则位于 `specs/` 目录下。根据任务类型优先查阅对应领域 SKILL。

## 关键 SKILL 入口

| 领域 | 路径 | 适用场景 |
|-----|------|---------|
| **布局与 UI** | `../layout-ui/SKILL.md` | 页面布局、搜索、表格、表单、弹窗、详情 |
| **项目结构与配置** | `../project-structure-config/SKILL.md` | 目录结构、路由、应用配置、技术栈 |
| **环境变量** | `../env-variables/SKILL.md` | 环境变量、主题色、Token、接口服务 |
| **接口与数据层** | `../api-data-layer/SKILL.md` | declareRequest、Connect、字典、Loading |
| **通用业务组件** | `../business-components/SKILL.md` | 富文本、上传、地图、云组件 |
| **权限与底座 API** | `../permission-base-api/SKILL.md` | 按钮权限、基座平台 API、Interpolation |
| **构建与部署** | `../build-deploy/SKILL.md` | jjb-cmd、jjb-common-lib、GitLab、推送部署 |
| **需求文档 → Markdown** | `../markdownify-mcp/SKILL.md`；`admin/scripts/docx_to_markdown_with_images.py` | Word/PDF 等转 `.md`（配图优先脚本）；转好后由 **`requirements-analysis`** 直接读该 `.md` |
| **Figma 设计快照** | `../figma-mcp/SKILL.md`；仓库根目录 `.design/` | 本地 `meta.json` + `figma-data.md` 与 `.api` 同期：优先读本地，避免重复 MCP |

## 快速查找（按类别）

**项目结构与配置** → `../specs/02-应用配置与开发环境/`、`../specs/03-项目页面结构/`  
**UI 组件** → `../specs/05-页面布局`、`../specs/06-搜索区`、`../specs/07-表格`、`../specs/08-表单`、`../specs/09-弹窗`、`../specs/12-详情`  
**接口与数据层** → `../specs/11-接口与数据层规范/`  
**业务组件** → `../specs/10-通用业务组件`、`../specs/13-云组件`  
**权限与环境** → `../specs/14-环境变量`、`../specs/16-按钮权限`、`../specs/17-接口动态文本`  
**底座 API** → `../specs/19-底座平台API调用规范/`  
**构建部署** → `../specs/15-构建与部署/`、`../specs/18-GitLab`、`../specs/20-jjb-cmd`、`../specs/21-jjb-common-lib`

## 关键词索引（常用）

| 关键词 | 路径 |
|-------|------|
| declareRequest / Connect / 命名空间 | `../specs/11-接口与数据层规范/02-接口定义规范/SKILL.md`、`03-命名空间与视图连接` |
| PageLayout / SearchForm / TableAction | `../specs/05-页面布局`、`../specs/06-搜索区`、`../specs/07-表格/02-表格操作栏` |
| ImageUploader / FileUploader / getValueProps / 数据脱敏 / 数据解密 | `../specs/10-通用业务组件使用规范/02-图片上传`、`04-文件上传`、`08-数据脱敏与解密` |
| Permission / Interpolation | `../specs/16-按钮权限控制规范`、`../specs/17-接口动态文本配置` |
| 环境变量 / process.env.app / Token | `../specs/14-环境变量与数据访问/` |
| CategoryTree / 分类树 / 树组件 | `../specs/05-页面布局与通用UI规范/03-分类树组件/SKILL.md` |
| 故障排查 / 接口返回HTML / 菜单加载失败 / 配置同步 / 本地联调 / Java集成 / 表单引擎调试 | `../specs/02-应用配置与开发环境/12-故障排查/SKILL.md` |
| ant-prefix / ConfigProvider prefixCls / 勿用 `.ant-*` 写样式 | `../specs/02-应用配置与开发环境/01-应用标识符与路由配置/SKILL.md`、`03-样式配置` |
| 路由跳转 / 查询参数 / 动态路由 | `../specs/04-路由与导航/`、`../specs/03-项目页面结构/05-路由生成` |
| 嵌套路由 / `_id` 父级 `index.js` / `props.children` | `../specs/03-项目页面结构/06-动态路由规范/SKILL.md`（「嵌套路由父级」） |
| InjectContext / 枚举值 | `../specs/03-项目页面结构/02-InjectContext`、`09-枚举值` |
| getClientInfo / __IN_BASE__ | `../specs/19-底座平台API调用规范/` |
| parseJSON / tools.router / dayjs | `../specs/21-jjb-common-lib/`、`../specs/01-技术栈/01-技术栈` |

## 使用建议

1. **按任务选 SKILL**：布局/表单/表格 → layout-ui；接口/数据 → api-data-layer
2. **关键词不明**：用本索引或直接查 `../specs/` 对应章节

## 完整索引

详细章节列表与完整关键词索引见 [reference.md](reference.md)
