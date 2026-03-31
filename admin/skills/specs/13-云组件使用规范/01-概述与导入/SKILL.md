---
name: jjb-cloud-component-overview
description: 定义 JJB 云组件概述与导入规范。在需要使用 CloudComponent、ImportCloudComponent 或 @cqsjjb/jjb-cloud-component 时查阅。
---

# 云组件使用规范

## 概述与导入

## 概述

云组件支持动态加载远程 React 组件，实现组件的远程部署和动态更新。

- **组件库**：`@cqsjjb/jjb-cloud-component`
- **核心组件**：`CloudComponent` - 用于加载和渲染云组件
- **工具函数**：`ImportCloudComponent` - 手动导入云组件模块
- **样式管理**：`useUnMountCloudComponentStyle` - 卸载云组件样式
- **已发布的云组件检索表**：[https://cdn.cqjjb.cn/](https://cdn.cqjjb.cn/) - 查看所有已发布的云组件列表
- **可视化组件市场**：[https://jcloud.cqjjb.cn/container/home](https://jcloud.cqjjb.cn/container/home) - 可视化浏览和选择云组件

**📝 说明**：本文档仅介绍如何在项目中使用云组件。如何开发云组件、如何发布云组件不在本文档范围内。

**⚠️ 重要约束**：必须严格参考对应 MD 文档或 `.d.ts` 文件！不得猜测组件属性！

## 导入方式

```javascript
// 导入 CloudComponent 组件
import CloudComponent from '@cqsjjb/jjb-cloud-component/CloudComponent';

// 或从主入口导入
import { CloudComponent } from '@cqsjjb/jjb-cloud-component';

// 导入工具函数
import { ImportCloudComponent, useUnMountCloudComponentStyle } from '@cqsjjb/jjb-cloud-component';
```
