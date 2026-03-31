---
name: jjb-auth-token
description: 定义 JJB 认证 Token 获取规范。在需要获取认证令牌、sessionStorage token 时查阅。
---

# 环境变量与数据访问

## 认证 Token

- **Token 获取**：通过 `sessionStorage.getItem('token')` 获取认证令牌
