# 二十、GitLab 规范

## 1. GitLab 地址

- **项目统一 GitLab 地址**：`http://192.168.1.242:10985/`

## 2. 分支命名规范

- **分支命名格式**：`v_<Version>`
  - 示例：`v_1.0.0`、`v_2.1.3`
  - 版本号遵循语义化版本规范（主版本号.次版本号.修订号）

## 3. 仓库命名规范

### 3.1 微应用仓库命名

- **命名格式**：`front-jjb-<app-name>-app`
  - 示例：`front-jjb-general-login-h5-app`、`front-jjb-user-manage-app`
  - `<app-name>` 为应用名称，使用小写字母和连字符

### 3.2 云组件仓库命名

- **命名格式**：`jjb-web-saas-<app-name>-<component-name>`
  - 示例：`jjb-web-saas-pay-center-cashier`、`jjb-web-saas-auth-login`
  - `<app-name>` 为应用名称，`<component-name>` 为组件名称，使用小写字母和连字符

## 4. 应用仓库目录结构

### 4.1 系统应用

- **仓库目录**：`http://192.168.1.242:10985/jjb/dragon/v2/`
- **访问路径格式**：`http://192.168.1.242:10985/jjb/dragon/v2/<app>/frontend`
- **示例**：
  - 仓库地址：`http://192.168.1.242:10985/jjb/dragon/v2/jjb-saas-auth/frontend/front-jjb-general-login-h5`
  - 访问地址：`http://192.168.1.242:10985/jjb/dragon/v2/jjb-saas-auth/frontend/front-jjb-general-login-h5`

### 4.2 业务应用

- **仓库目录**：`http://192.168.1.242:10985/jjb/train/`
- **访问路径格式**：`http://192.168.1.242:10985/jjb/train/<app>/frontend`
- **示例**：
  - 仓库地址：`http://192.168.1.242:10985/jjb/train/cedu/frontend/jjb-cedu-manage-app`
  - 访问地址：`http://192.168.1.242:10985/jjb/train/cedu/frontend/jjb-cedu-manage-app`

### 4.3 云组件

- **仓库目录**：`http://192.168.1.242:10985/jjb/front-cloud-component`
- **访问路径格式**：`http://192.168.1.242:10985/jjb/front-cloud-component/<component-name>`
- **示例**：
  - 仓库地址：`http://192.168.1.242:10985/jjb/front-cloud-component/jjb-web-pay-center-cashier`
  - 访问地址：`http://192.168.1.242:10985/jjb/front-cloud-component/jjb-web-pay-center-cashier`

## 5. 仓库管理规范

### 5.1 仓库地址配置

- 所有项目仓库统一托管在项目 GitLab 服务器上
- 在 `jjb.config.js` 中配置后端 Git 地址时，应使用完整的 GitLab 仓库地址
- 根据应用类型选择对应的仓库目录结构

### 5.2 分支管理

- 遵循项目的分支管理策略
- 分支命名必须符合 `v_<Version>` 格式
- 不同环境对应不同的分支（参考 [`chapters/15-构建与部署.md`](./15-构建与部署.md)）
- 分支名称在 `jjb.config.js` 的 `environment` 配置中维护

### 5.3 代码提交规范

- 提交信息应清晰描述本次变更内容
- 遵循团队约定的提交信息格式
- 提交前确保代码通过构建和测试

## 6. 权限与访问

- 项目成员需具备相应的 GitLab 访问权限
- 权限管理由项目管理员统一配置
- 如需访问权限，请联系项目管理员

## 7. 注意事项

- 确保 GitLab 服务器地址可访问
- 创建新仓库时，必须遵循命名规范：
  - 微应用：`front-jjb-<app-name>-app`
  - 云组件：`jjb-web-saas-<app-name>-<component-name>`
- 分支命名必须遵循 `v_<Version>` 格式
- 推送代码前确认目标分支正确
- 遵循团队代码审查流程
- 重要变更需通过 Merge Request 进行代码审查
- 根据应用类型（系统应用/业务应用/云组件）选择正确的仓库目录结构