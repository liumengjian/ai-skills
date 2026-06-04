---
name: env-variables
description: 环境变量、主题色、接口服务配置、Token 认证。Use when configuring environment variables, API endpoints, or authentication.
---

# 环境变量与数据访问

## 配置项

| 规范 | 路径 |
|-----|------|
| 主题色变量 | `../specs/14-环境变量与数据访问/01-主题色变量/SKILL.md` |
| appIdentifier / ant-prefix（antd 类名非 `ant-*`） | `../specs/02-应用配置与开发环境/01-应用标识符与路由配置/SKILL.md` |
| 接口服务配置 | `../specs/14-环境变量与数据访问/02-接口服务配置/SKILL.md` |
| 全局环境变量注入 | `../specs/14-环境变量与数据访问/03-全局环境变量注入/SKILL.md` |
| 认证Token | `../specs/14-环境变量与数据访问/04-认证Token/SKILL.md` |

## 关键词

- **antd `ant-prefix`**：`framework.antd['ant-prefix']` → `process.env.app.antd['ant-prefix']`，样式勿用 `.ant-*`，见应用标识符规范
- **process.env.app** / **window.process.env.app**
- **iframe 环境变量** / **云组件环境变量**
- **API_HOST** / **production 环境配置**
