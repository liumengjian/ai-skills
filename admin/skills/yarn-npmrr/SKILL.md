---
name: yarn-npmrr
description: 使用yarn安装依赖包并设置npmrr源。Use when installing dependencies, adding packages, or managing project dependencies with yarn and npmrr registry.
---

# Yarn 与 npmrr 源配置

## 核心规范

在安装依赖包时，**必须使用 yarn**，并设置源为 npmrr。

### 命令格式

```bash
# 设置npmrr源
yarn config set registry https://registry.npmmirror.com

# 安装依赖（从npmrr源）
yarn install

# 添加依赖包
yarn add <package-name>

# 添加开发依赖
yarn add <package-name> -D

# 移除依赖
yarn remove <package-name>
```

### Windows PowerShell 注意事项

PowerShell 不支持 `&&` 作为语句分隔符，应使用分号 `;`：

```powershell
# 错误示例
yarn add react && yarn add react-dom

# 正确示例（单行）
yarn add react; yarn add react-dom

# 推荐方式（分步执行）
yarn add react
yarn add react-dom
```

## 使用场景

- 安装项目依赖：`yarn install`
- 添加新依赖：`yarn add <package>`
- 添加开发依赖：`yarn add <package> -D`
- 更新依赖：`yarn upgrade`
- 移除依赖：`yarn remove <package>`

## 关键词

- **yarn** / **npmrr** / **npmmirror**
- **安装依赖** / **添加依赖** / **依赖管理**
- **yarn add** / **yarn install** / **yarn remove**
