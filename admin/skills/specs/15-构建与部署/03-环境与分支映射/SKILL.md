---
name: jjb-env-branch-mapping
description: 定义 JJB 环境与分支映射规范。在理解 jjb-cmd push 环境参数与 javaGitBranch 映射时查阅。
---

# 构建与部署

## 应用推送

- **环境与分支映射**：

  - 推送命令会根据指定的环境参数，自动从 `environment` 配置中获取对应的 `javaGitBranch` 分支名称

  - 例如：`jjb-cmd push java development` 会推送到 `development` 环境配置中指定的 `javaGitBranch` 分支
