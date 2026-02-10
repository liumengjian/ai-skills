# 前端微应用开发规范 - 快速索引

> 本文档是前端开发规范的快速索引，用于帮助 Cursor 快速定位相关规范内容。  
> **完整规范已拆分为独立章节文件，位于 `chapters/` 目录下**

## 📋 快速查找表

### 🔴 AI执行约束（必须优先查阅）
- **规范强制性** → `chapters/22-AI执行约束/01-规范强制性.md`
- **禁止擅自补全** → `chapters/22-AI执行约束/02-禁止擅自补全.md`
- **依赖约束** → `chapters/22-AI执行约束/03-依赖约束.md`
- **实现一致性** → `chapters/22-AI执行约束/04-实现一致性.md`
- **交付标准** → `chapters/22-AI执行约束/05-交付标准.md`
- **代码注释规范** → `chapters/22-AI执行约束/06-代码注释规范.md`
- **自定义组件事件命名规范** → `chapters/22-AI执行约束/07-自定义组件事件命名规范.md`

### 🏗️ 项目结构与配置
- **项目目录结构** → `chapters/03-项目页面结构/01-项目目录结构示意图.md`
- **应用配置** → `chapters/02-应用配置与开发环境/`
- **路由配置** → `chapters/02-应用配置与开发环境/01-应用标识符与路由配置.md`
- **目录命名规范** → `chapters/03-项目页面结构/04-目录命名规范.md`
- **路由生成机制** → `chapters/03-项目页面结构/05-路由生成机制.md`
- **动态路由规范** → `chapters/03-项目页面结构/06-动态路由规范.md`
- **菜单注册规范** → `chapters/03-项目页面结构/11-菜单注册规范.md`

### 🎨 UI组件与交互规范
- **页面Layout** → `chapters/05-页面布局与通用UI规范/01-页面Layout.md`
- **搜索表单** → `chapters/06-搜索区规范/01-搜索表单组件.md`
- **表格规范** → `chapters/07-表格规范/`
- **表单规范** → `chapters/08-表单与交互规范/`
- **弹窗规范** → `chapters/09-弹窗规范/`
- **详情展示** → `chapters/12-详情展示规范/`

### 🔌 接口与数据层
- **接口定义规范** → `chapters/11-接口与数据层规范/02-接口定义规范.md`
- **命名空间与视图连接** → `chapters/11-接口与数据层规范/03-命名空间与视图连接.md`
- **字典数据获取** → `chapters/11-接口与数据层规范/05-字典数据获取规范.md`
- **禁止useEffect监听Action** → `chapters/11-接口与数据层规范/06-禁止useEffect监听接口action.md`
- **基座平台API** → `chapters/19-基座平台API调用规范/`

### 🧩 通用业务组件
- **富文本组件** → `chapters/10-通用业务组件使用规范/01-富文本组件.md`
- **图片上传** → `chapters/10-通用业务组件使用规范/02-图片上传组件.md`
- **文件上传** → `chapters/10-通用业务组件使用规范/04-文件上传组件.md`
- **地图组件** → `chapters/10-通用业务组件使用规范/07-地图组件.md`
- **云组件使用** → `chapters/13-云组件使用规范/`

### 🛠️ 工具与库
- **jjb-common-lib** → `chapters/21-jjb-common-lib/`
- **jjb-cmd** → `chapters/20-jjb-cmd/`

### 🔐 权限与环境
- **按钮权限控制** → `chapters/16-按钮权限控制规范/`
- **环境变量** → `chapters/14-环境变量与数据访问/`
- **接口动态文本配置** → `chapters/17-接口动态文本配置/`

### 🚀 构建与部署
- **构建部署** → `chapters/15-构建与部署/`
- **GitLab规范** → `chapters/18-GitLab规范/`

---

## 📚 完整章节列表

### 01-技术栈与基础
- `chapters/01-技术栈与基础/01-技术栈.md` - React 18、antd v5、less、dva运行时
- `chapters/01-技术栈与基础/02-基础组件库概述.md` - 基础组件库说明
- `chapters/01-技术栈与基础/03-全局运行时规范.md` - dva运行时规范
- `chapters/01-技术栈与基础/04-图片布局约束.md` - 图片布局规范
- `chapters/01-技术栈与基础/05-代码检查与调整规范.md` - 代码检查规范

### 02-应用配置与开发环境
- `chapters/02-应用配置与开发环境/01-应用标识符与路由配置.md` - 应用标识符、路由配置
- `chapters/02-应用配置与开发环境/02-路径别名与资源管理.md` - 路径别名配置
- `chapters/02-应用配置与开发环境/03-样式配置.md` - Less样式配置
- `chapters/02-应用配置与开发环境/04-Babel与TypeScript配置.md` - Babel/TS配置
- `chapters/02-应用配置与开发环境/05-代码优化工具.md` - 代码优化配置
- `chapters/02-应用配置与开发环境/06-开发服务配置.md` - 开发服务器配置
- `chapters/02-应用配置与开发环境/07-静态资源服务器配置.md` - 静态资源配置
- `chapters/02-应用配置与开发环境/08-应用启动与编译.md` - 启动与编译
- `chapters/02-应用配置与开发环境/09-HTML模板配置.md` - HTML模板
- `chapters/02-应用配置与开发环境/10-HTTP拦截器配置.md` - HTTP拦截器
- `chapters/02-应用配置与开发环境/11-构建工具与Webpack配置.md` - Webpack配置

### 03-项目页面结构
- `chapters/03-项目页面结构/01-项目目录结构示意图.md` - 标准目录结构
- `chapters/03-项目页面结构/02-InjectContext使用规范.md` - InjectContext上下文
- `chapters/03-项目页面结构/03-页面目录规则.md` - 页面目录规则
- `chapters/03-项目页面结构/04-目录命名规范.md` - 目录命名规范
- `chapters/03-项目页面结构/05-路由生成机制.md` - 路由自动生成
- `chapters/03-项目页面结构/06-动态路由规范.md` - 动态路由规则
- `chapters/03-项目页面结构/07-应用首页.md` - 应用首页配置
- `chapters/03-项目页面结构/08-其他文件夹定义.md` - 其他目录说明
- `chapters/03-项目页面结构/09-枚举值使用规范.md` - 枚举值规范
- `chapters/03-项目页面结构/10-组件开发规范.md` - 组件开发规范
- `chapters/03-项目页面结构/11-菜单注册规范.md` - 菜单注册规范

### 04-路由与导航
- `chapters/04-路由与导航/01-路由跳转方法.md` - 路由跳转API
- `chapters/04-路由与导航/02-获取查询参数.md` - 查询参数获取
- `chapters/04-路由与导航/03-获取路径参数.md` - 路径参数获取

### 05-页面布局与通用UI规范
- `chapters/05-页面布局与通用UI规范/01-页面Layout.md` - 页面布局组件
- `chapters/05-页面布局与通用UI规范/02-页面右上角操作区.md` - 右上角操作区

### 06-搜索区规范
- `chapters/06-搜索区规范/01-搜索表单组件.md` - 搜索表单使用
- `chapters/06-搜索区规范/02-搜索状态持久化.md` - 搜索状态持久化
- `chapters/06-搜索区规范/03-代码演示.md` - 代码示例
- `chapters/06-搜索区规范/04-API.md` - API文档

### 07-表格规范
- `chapters/07-表格规范/01-表格基础.md` - 表格基础用法
- `chapters/07-表格规范/02-表格操作栏.md` - 操作栏配置
- `chapters/07-表格规范/03-表格选择列.md` - 选择列功能
- `chapters/07-表格规范/04-批量操作.md` - 批量操作
- `chapters/07-表格规范/05-空数据状态.md` - 空数据展示
- `chapters/07-表格规范/06-删除确认.md` - 删除确认

### 08-表单与交互规范
- `chapters/08-表单与交互规范/01-表单组件基础规范.md` - 表单基础
- `chapters/08-表单与交互规范/02-下拉选择搜索功能.md` - 下拉搜索
- `chapters/08-表单与交互规范/03-表单布局规则.md` - 表单布局
- `chapters/08-表单与交互规范/04-表单字段占位规则.md` - 占位符规则
- `chapters/08-表单与交互规范/05-数据回填策略.md` - 数据回填
- `chapters/08-表单与交互规范/06-表单提交规范.md` - 表单提交
- `chapters/08-表单与交互规范/07-编辑新建模式.md` - 编辑/新建模式

### 09-弹窗规范
- `chapters/09-弹窗规范/01-弹窗使用规范.md` - 弹窗基础
- `chapters/09-弹窗规范/02-静态方法使用规范.md` - 静态方法
- `chapters/09-弹窗规范/03-最大高度限制.md` - 高度限制
- `chapters/09-弹窗规范/04-使用示例.md` - 使用示例

### 10-通用业务组件使用规范
- `chapters/10-通用业务组件使用规范/01-富文本组件.md` - 富文本编辑器
- `chapters/10-通用业务组件使用规范/02-图片上传组件.md` - 单图上传
- `chapters/10-通用业务组件使用规范/03-多图上传.md` - 多图上传
- `chapters/10-通用业务组件使用规范/04-文件上传组件.md` - 文件上传
- `chapters/10-通用业务组件使用规范/05-多附件上传.md` - 多附件上传
- `chapters/10-通用业务组件使用规范/06-图片裁剪组件.md` - 图片裁剪
- `chapters/10-通用业务组件使用规范/07-地图组件.md` - 地图组件

### 11-接口与数据层规范
- `chapters/11-接口与数据层规范/01-概述与核心架构.md` - 三层架构说明
- `chapters/11-接口与数据层规范/02-接口定义规范.md` - declareRequest使用
- `chapters/11-接口与数据层规范/03-命名空间与视图连接.md` - Connect装饰器
- `chapters/11-接口与数据层规范/04-目录命名规范.md` - API目录命名
- `chapters/11-接口与数据层规范/05-字典数据获取规范.md` - 字典数据Hooks
- `chapters/11-接口与数据层规范/06-禁止useEffect监听接口action.md` - 禁止监听Action函数

### 12-详情展示规范
- `chapters/12-详情展示规范/01-加载态管理.md` - 加载状态
- `chapters/12-详情展示规范/02-数据呈现规范.md` - 数据展示
- `chapters/12-详情展示规范/03-数据溯源逻辑.md` - 数据溯源

### 13-云组件使用规范
- `chapters/13-云组件使用规范/01-概述与导入.md` - 云组件概述
- `chapters/13-云组件使用规范/02-基础用法.md` - 基础用法
- `chapters/13-云组件使用规范/03-组件属性说明.md` - 属性说明
- `chapters/13-云组件使用规范/04-依赖管理.md` - 依赖管理
- `chapters/13-云组件使用规范/05-生命周期钩子.md` - 生命周期
- `chapters/13-云组件使用规范/06-高级用法.md` - 高级用法
- `chapters/13-云组件使用规范/07-手动导入与样式管理.md` - 手动导入
- `chapters/13-云组件使用规范/08-注意事项与最佳实践.md` - 最佳实践
- `chapters/13-云组件使用规范/09-完整示例.md` - 完整示例

### 14-环境变量与数据访问
- `chapters/14-环境变量与数据访问/01-主题色变量.md` - 主题色配置
- `chapters/14-环境变量与数据访问/02-接口服务配置.md` - 接口服务
- `chapters/14-环境变量与数据访问/03-全局环境变量注入.md` - 环境变量
- `chapters/14-环境变量与数据访问/04-认证Token.md` - Token认证

### 15-构建与部署
- `chapters/15-构建与部署/01-应用推送命令.md` - 推送命令
- `chapters/15-构建与部署/02-后端仓库配置.md` - 仓库配置
- `chapters/15-构建与部署/03-环境与分支映射.md` - 环境映射
- `chapters/15-构建与部署/04-应用推送机制.md` - 推送机制
- `chapters/15-构建与部署/05-使用说明.md` - 使用说明

### 16-按钮权限控制规范
- `chapters/16-按钮权限控制规范/01-重要提示.md` - 按钮权限说明
- `chapters/16-按钮权限控制规范/02-权限控制方式.md` - 按钮权限控制方式
- `chapters/16-按钮权限控制规范/03-Permission使用方式.md` - Permission组件
- `chapters/16-按钮权限控制规范/04-权限获取机制.md` - 按钮权限获取
- `chapters/16-按钮权限控制规范/05-权限控制最佳实践.md` - 按钮权限控制最佳实践

### 17-接口动态文本配置
- `chapters/17-接口动态文本配置/01-功能说明.md` - 功能说明
- `chapters/17-接口动态文本配置/02-Interpolation使用方式.md` - Interpolation组件
- `chapters/17-接口动态文本配置/03-注入的Props.md` - Props说明
- `chapters/17-接口动态文本配置/04-字段配置获取机制.md` - 配置获取
- `chapters/17-接口动态文本配置/05-使用示例.md` - 使用示例
- `chapters/17-接口动态文本配置/06-使用规范.md` - 使用规范

### 18-GitLab规范
- `chapters/18-GitLab规范/01-GitLab地址.md` - GitLab地址
- `chapters/18-GitLab规范/02-分支命名规范.md` - 分支命名
- `chapters/18-GitLab规范/03-仓库命名规范.md` - 仓库命名
- `chapters/18-GitLab规范/04-应用仓库目录结构.md` - 目录结构
- `chapters/18-GitLab规范/05-仓库管理规范.md` - 仓库管理
- `chapters/18-GitLab规范/06-权限与访问.md` - 权限访问
- `chapters/18-GitLab规范/07-注意事项.md` - 注意事项

### 19-基座平台API调用规范
- `chapters/19-基座平台API调用规范/01-概述与环境判断.md` - 概述与环境判断
- `chapters/19-基座平台API调用规范/02-URL格式化.md` - URL格式化
- `chapters/19-基座平台API调用规范/03-信息获取API.md` - 信息获取
- `chapters/19-基座平台API调用规范/04-系统信息对象.md` - 系统信息
- `chapters/19-基座平台API调用规范/05-表单引擎.md` - 表单引擎
- `chapters/19-基座平台API调用规范/06-面板控制API.md` - 面板控制
- `chapters/19-基座平台API调用规范/07-弹窗功能API.md` - 弹窗API
- `chapters/19-基座平台API调用规范/08-加密解密API.md` - 加密解密
- `chapters/19-基座平台API调用规范/09-菜单操作API.md` - 菜单操作
- `chapters/19-基座平台API调用规范/10-系统操作API.md` - 系统操作
- `chapters/19-基座平台API调用规范/11-批量操作API.md` - 批量操作
- `chapters/19-基座平台API调用规范/12-文件中心API.md` - 文件中心
- `chapters/19-基座平台API调用规范/13-注意事项与最佳实践.md` - 最佳实践
- `chapters/19-基座平台API调用规范/14-完整示例.md` - 完整示例

### 20-jjb-cmd
- `chapters/20-jjb-cmd/01-全局安装.md` - 全局安装
- `chapters/20-jjb-cmd/02-命令列表.md` - 命令列表
- `chapters/20-jjb-cmd/03-登录授权.md` - 登录授权
- `chapters/20-jjb-cmd/04-推送微前端包.md` - 推送包
- `chapters/20-jjb-cmd/05-发布云组件.md` - 发布组件
- `chapters/20-jjb-cmd/06-拉取AI配置.md` - 拉取配置
- `chapters/20-jjb-cmd/07-云组件开发指南.md` - 组件开发
- `chapters/20-jjb-cmd/08-常见问题.md` - 常见问题
- `chapters/20-jjb-cmd/09-相关章节.md` - 相关章节

### 21-jjb-common-lib
- `chapters/21-jjb-common-lib/01-tools模块使用规范.md` - tools工具
- `chapters/21-jjb-common-lib/02-http模块使用规范.md` - http模块
- `chapters/21-jjb-common-lib/03-qs模块使用规范.md` - qs模块
- `chapters/21-jjb-common-lib/04-crypto模块使用规范.md` - crypto加密
- `chapters/21-jjb-common-lib/05-color模块使用规范.md` - color颜色

### 22-AI执行约束（关键）
- `chapters/22-AI执行约束/01-规范强制性.md` - 规范强制性要求
- `chapters/22-AI执行约束/02-禁止擅自补全.md` - 禁止擅自补全
- `chapters/22-AI执行约束/03-依赖约束.md` - 依赖约束
- `chapters/22-AI执行约束/04-实现一致性.md` - 实现一致性
- `chapters/22-AI执行约束/05-交付标准.md` - 交付标准
- `chapters/22-AI执行约束/06-代码注释规范.md` - 代码注释规范
- `chapters/22-AI执行约束/07-自定义组件事件命名规范.md` - 事件命名规范

---

## 🔍 关键词索引

### 核心概念
- **declareRequest** → `chapters/11-接口与数据层规范/02-接口定义规范.md`
- **Connect装饰器** → `chapters/11-接口与数据层规范/03-命名空间与视图连接.md`
- **命名空间** → `chapters/11-接口与数据层规范/03-命名空间与视图连接.md`
- **InjectContext** → `chapters/03-项目页面结构/02-InjectContext使用规范.md`
- **base API** → `chapters/19-基座平台API调用规范/01-概述与环境判断.md`
- **云组件** → `chapters/13-云组件使用规范/01-概述与导入.md`
- **Loading状态** → `chapters/11-接口与数据层规范/02-接口定义规范.md`
- **三层架构** → `chapters/11-接口与数据层规范/01-概述与核心架构.md`
- **枚举值** → `chapters/03-项目页面结构/09-枚举值使用规范.md`
- **字典数据** → `chapters/11-接口与数据层规范/05-字典数据获取规范.md`
- **命名空间映射** → `chapters/11-接口与数据层规范/03-命名空间与视图连接.md`

### 技术栈
- **React** → `chapters/01-技术栈与基础/01-技术栈.md`
- **antd** → `chapters/01-技术栈与基础/01-技术栈.md`
- **dva** → `chapters/01-技术栈与基础/03-全局运行时规范.md`
- **less** → `chapters/01-技术栈与基础/01-技术栈.md`
- **@cqsjjb/jjb-react-admin-component** → `chapters/01-技术栈与基础/02-基础组件库概述.md`
- **@cqsjjb/jjb-common-lib** → `chapters/01-技术栈与基础/02-基础组件库概述.md`
- **@cqsjjb/jjb-dva-runtime** → `chapters/01-技术栈与基础/01-技术栈.md`
- **@cqsjjb/jjb-cloud-component** → `chapters/13-云组件使用规范/01-概述与导入.md`

### 业务组件
- **PageLayout** → `chapters/05-页面布局与通用UI规范/01-页面Layout.md`
- **SearchForm** → `chapters/06-搜索区规范/01-搜索表单组件.md`
- **TableAction** → `chapters/07-表格规范/02-表格操作栏.md`
- **Editor** → `chapters/10-通用业务组件使用规范/01-富文本组件.md`
- **ImageUploader** → `chapters/10-通用业务组件使用规范/02-图片上传组件.md`
- **FileUploader** → `chapters/10-通用业务组件使用规范/04-文件上传组件.md`
- **ImageCropper** → `chapters/10-通用业务组件使用规范/06-图片裁剪组件.md`
- **AMap** → `chapters/10-通用业务组件使用规范/07-地图组件.md`
- **CloudComponent** → `chapters/13-云组件使用规范/01-概述与导入.md`
- **Permission** → `chapters/16-按钮权限控制规范/03-Permission使用方式.md`
- **Interpolation** → `chapters/17-接口动态文本配置/02-Interpolation使用方式.md`

### UI组件与交互
- **搜索表单** → `chapters/06-搜索区规范/01-搜索表单组件.md`
- **搜索状态持久化** → `chapters/06-搜索区规范/02-搜索状态持久化.md`
- **表格** → `chapters/07-表格规范/01-表格基础.md`
- **表格操作栏** → `chapters/07-表格规范/02-表格操作栏.md`
- **表格选择列** → `chapters/07-表格规范/03-表格选择列.md`
- **批量操作** → `chapters/07-表格规范/04-批量操作.md`
- **空数据状态** → `chapters/07-表格规范/05-空数据状态.md`
- **删除确认** → `chapters/07-表格规范/06-删除确认.md`
- **表单** → `chapters/08-表单与交互规范/01-表单组件基础规范.md`
- **表单布局** → `chapters/08-表单与交互规范/03-表单布局规则.md`
- **表单提交** → `chapters/08-表单与交互规范/06-表单提交规范.md`
- **数据回填** → `chapters/08-表单与交互规范/05-数据回填策略.md`
- **弹窗** → `chapters/09-弹窗规范/01-弹窗使用规范.md`
- **弹窗静态方法** → `chapters/09-弹窗规范/02-静态方法使用规范.md`
- **详情展示** → `chapters/12-详情展示规范/02-数据呈现规范.md`
- **加载态** → `chapters/12-详情展示规范/01-加载态管理.md`

### 文件上传
- **图片上传** → `chapters/10-通用业务组件使用规范/02-图片上传组件.md`
- **多图上传** → `chapters/10-通用业务组件使用规范/03-多图上传.md`
- **文件上传** → `chapters/10-通用业务组件使用规范/04-文件上传组件.md`
- **多附件上传** → `chapters/10-通用业务组件使用规范/05-多附件上传.md`
- **图片裁剪** → `chapters/10-通用业务组件使用规范/06-图片裁剪组件.md`
- **getValueProps** → `chapters/10-通用业务组件使用规范/02-图片上传组件.md`
- **getValueFromEvent** → `chapters/10-通用业务组件使用规范/02-图片上传组件.md`

### 路由相关
- **路由跳转** → `chapters/04-路由与导航/01-路由跳转方法.md`
- **查询参数** → `chapters/04-路由与导航/02-获取查询参数.md`
- **路径参数** → `chapters/04-路由与导航/03-获取路径参数.md`
- **动态路由** → `chapters/03-项目页面结构/06-动态路由规范.md`
- **路由生成** → `chapters/03-项目页面结构/05-路由生成机制.md`
- **应用首页** → `chapters/03-项目页面结构/07-应用首页.md`
- **菜单注册** → `chapters/03-项目页面结构/11-菜单注册规范.md`
- **Container** → `chapters/03-项目页面结构/01-项目目录结构示意图.md`

### 接口与API
- **接口定义** → `chapters/11-接口与数据层规范/02-接口定义规范.md`
- **接口命名** → `chapters/11-接口与数据层规范/02-接口定义规范.md`
- **API目录命名** → `chapters/11-接口与数据层规范/04-目录命名规范.md`
- **getClientInfo** → `chapters/19-基座平台API调用规范/03-信息获取API.md`
- **getTenantInfo** → `chapters/19-基座平台API调用规范/03-信息获取API.md`
- **URL格式化** → `chapters/19-基座平台API调用规范/02-URL格式化.md`
- **表单引擎** → `chapters/19-基座平台API调用规范/05-表单引擎.md`
- **面板控制** → `chapters/19-基座平台API调用规范/06-面板控制API.md`
- **弹窗功能API** → `chapters/19-基座平台API调用规范/07-弹窗功能API.md`
- **加密解密API** → `chapters/19-基座平台API调用规范/08-加密解密API.md`
- **文件中心API** → `chapters/19-基座平台API调用规范/12-文件中心API.md`
- **__IN_BASE__** → `chapters/19-基座平台API调用规范/01-概述与环境判断.md`

### 工具库（jjb-common-lib）
- **tools** → `chapters/21-jjb-common-lib/01-tools模块使用规范.md`
- **parseJSON** → `chapters/21-jjb-common-lib/01-tools模块使用规范.md`
- **parseObject** → `chapters/21-jjb-common-lib/01-tools模块使用规范.md`
- **tools.router** → `chapters/21-jjb-common-lib/01-tools模块使用规范.md`
- **router.query** → `chapters/06-搜索区规范/02-搜索状态持久化.md`
- **http** → `chapters/21-jjb-common-lib/02-http模块使用规范.md`
- **qs** → `chapters/21-jjb-common-lib/03-qs模块使用规范.md`
- **crypto** → `chapters/21-jjb-common-lib/04-crypto模块使用规范.md`
- **AES加密** → `chapters/21-jjb-common-lib/04-crypto模块使用规范.md`
- **MD5** → `chapters/21-jjb-common-lib/04-crypto模块使用规范.md`
- **color** → `chapters/21-jjb-common-lib/05-color模块使用规范.md`

### 配置相关
- **应用标识符** → `chapters/02-应用配置与开发环境/01-应用标识符与路由配置.md`
- **路径别名** → `chapters/02-应用配置与开发环境/02-路径别名与资源管理.md`
- **环境变量** → `chapters/14-环境变量与数据访问/03-全局环境变量注入.md`
- **主题色变量** → `chapters/14-环境变量与数据访问/01-主题色变量.md`
- **Token认证** → `chapters/14-环境变量与数据访问/04-认证Token.md`
- **jjb.config.js** → `chapters/02-应用配置与开发环境/`
- **jjb.babel.js** → `chapters/02-应用配置与开发环境/04-Babel与TypeScript配置.md`
- **main.js** → `chapters/03-项目页面结构/01-项目目录结构示意图.md`
- **Babel配置** → `chapters/02-应用配置与开发环境/04-Babel与TypeScript配置.md`
- **Webpack配置** → `chapters/02-应用配置与开发环境/11-构建工具与Webpack配置.md`
- **HTTP拦截器** → `chapters/02-应用配置与开发环境/10-HTTP拦截器配置.md`
- **HTML模板** → `chapters/02-应用配置与开发环境/09-HTML模板配置.md`

### 目录结构
- **src/pages** → `chapters/03-项目页面结构/01-项目目录结构示意图.md`
- **src/api** → `chapters/03-项目页面结构/01-项目目录结构示意图.md`
- **src/components** → `chapters/03-项目页面结构/01-项目目录结构示意图.md`
- **src/enumerate** → `chapters/03-项目页面结构/01-项目目录结构示意图.md`
- **src/hooks** → `chapters/03-项目页面结构/01-项目目录结构示意图.md`
- **src/utils** → `chapters/03-项目页面结构/01-项目目录结构示意图.md`
- **目录命名规范** → `chapters/03-项目页面结构/04-目录命名规范.md`
- **页面目录规则** → `chapters/03-项目页面结构/03-页面目录规则.md`

### 按钮权限控制
- **按钮权限控制** → `chapters/16-按钮权限控制规范/02-权限控制方式.md`
- **按钮权限获取** → `chapters/16-按钮权限控制规范/04-权限获取机制.md`
- **按钮权限最佳实践** → `chapters/16-按钮权限控制规范/05-权限控制最佳实践.md`

### 构建与部署
- **jjb-cmd** → `chapters/20-jjb-cmd/02-命令列表.md`
- **推送应用** → `chapters/20-jjb-cmd/04-推送微前端包.md`
- **发布组件** → `chapters/20-jjb-cmd/05-发布云组件.md`
- **拉取AI配置** → `chapters/20-jjb-cmd/06-拉取AI配置.md`
- **应用推送机制** → `chapters/15-构建与部署/04-应用推送机制.md`
- **环境与分支映射** → `chapters/15-构建与部署/03-环境与分支映射.md`

### GitLab规范
- **GitLab地址** → `chapters/18-GitLab规范/01-GitLab地址.md`
- **分支命名** → `chapters/18-GitLab规范/02-分支命名规范.md`
- **仓库命名** → `chapters/18-GitLab规范/03-仓库命名规范.md`
- **仓库管理** → `chapters/18-GitLab规范/05-仓库管理规范.md`

### 云组件
- **ImportCloudComponent** → `chapters/13-云组件使用规范/07-手动导入与样式管理.md`
- **useUnMountCloudComponentStyle** → `chapters/13-云组件使用规范/07-手动导入与样式管理.md`
- **云组件生命周期** → `chapters/13-云组件使用规范/05-生命周期钩子.md`
- **云组件依赖管理** → `chapters/13-云组件使用规范/04-依赖管理.md`

### 其他重要概念
- **数据溯源** → `chapters/12-详情展示规范/03-数据溯源逻辑.md`
- **接口动态文本** → `chapters/17-接口动态文本配置/01-功能说明.md`
- **代码注释规范** → `chapters/22-AI执行约束/06-代码注释规范.md`
- **事件命名规范** → `chapters/22-AI执行约束/07-自定义组件事件命名规范.md`
- **交付标准** → `chapters/22-AI执行约束/05-交付标准.md`

---

## 💡 使用建议

1. **首次查阅**：优先查看 `22-AI执行约束` 章节，了解AI必须遵守的规范
2. **项目结构**：查看 `03-项目页面结构` 了解目录组织方式
3. **组件使用**：根据需要的组件类型，查找对应的章节（表格、表单、弹窗等）
4. **接口调用**：区分后端接口（`11-接口与数据层规范`）和基座API（`19-基座平台API调用规范`）
5. **关键词查找**：使用关键词索引快速定位相关规范

---

**最后更新**：索引文件会根据章节文件变化自动更新，确保索引准确性。