# 二十六、color 模块使用规范

## 1. 概述

`color` 模块是 `@cqsjjb/jjb-common-lib` 通用工具库中的颜色值模块，包含大量预定义的颜色值，提供统一的颜色管理，便于在项目中使用一致的颜色方案。

### 1.1 导入方式

```javascript
import { color } from '@cqsjjb/jjb-common-lib';
```

## 2. 颜色分类

### 2.1 基础颜色

提供常用的基础颜色值：

- `BLANK`: `#000` - 黑色
- `WHITE`: `#FFFFFF` - 白色
- `BLUE`: `#1890FF` - 蓝色
- `Blue_10`: `#199BFF` - 蓝色变体
- `GREEN`: `#52C41A` - 绿色
- `GREEN_10`: `#52C41A` - 绿色变体
- `GREEN_4B`: `#70BA4B` - 绿色变体
- `RED`: `#F5222D` - 红色
- `RED_10`: `#FF4D4F` - 红色变体
- `RED_5`: `#F16C69` - 红色变体
- `YELLOW`: `#fadb14` - 黄色
- `ORANGE`: `#FA8C16` - 橙色
- `PURPLE`: `#722ED1` - 紫色
- `PINK`: `#EB2F96` - 粉色
- `MAGENTA`: `#EB2F96` - 洋红色
- `CYAN`: `#13C2C2` - 青色
- `VOLCANO`: `#FA541C` - 火山红
- `GEEKBLUE`: `#2F54EB` - 极客蓝

### 2.2 灰色系

提供丰富的灰色值，用于文本、边框、背景等：

**深灰色（文本色）：**
- `GRAY`: `gray` - 灰色
- `GRAY_333`: `#333` - 深灰色
- `GRAY_444`: `#444` - 深灰色
- `GRAY_555`: `#555` - 深灰色
- `GRAY_666`: `#666` - 中灰色
- `GRAY_777`: `#777` - 中灰色
- `GRAY_888`: `#888` - 中灰色
- `GRAY_999`: `#595959` - 中灰色
- `GRAY_AAA`: `#AAA` - 浅灰色
- `GRAY_B8`: `#b8b8b8` - 浅灰色
- `GRAY_BBB`: `#BBB` - 浅灰色
- `GRAY_CCC`: `#888` - 浅灰色
- `GRAY_DDD`: `#DDD` - 浅灰色
- `GRAY_EEE`: `#EEE` - 浅灰色
- `GRAY_a2`: `#a2a2a2` - 浅灰色

**浅灰色系（背景色、边框色）：**
- `GRAY_F0`: `#F0F0F0` - 浅灰色背景
- `GRAY_F1`: `#F1F1F1` - 浅灰色背景
- `GRAY_F2`: `#F2F2F2` - 浅灰色背景
- `GRAY_F3`: `#F3F3F3` - 浅灰色背景
- `GRAY_F4`: `#F4F4F4` - 浅灰色背景
- `GRAY_F5`: `#F5F5F5` - 浅灰色背景
- `GRAY_F6`: `#F6F6F6` - 浅灰色背景
- `GRAY_F7`: `#F7F7F7` - 浅灰色背景
- `GRAY_F8`: `#F8F8F8` - 浅灰色背景
- `GRAY_F9`: `#F9F9F9` - 浅灰色背景
- `GRAY_F9FA`: `#F9FAFA` - 浅灰色背景
- `GRAY_FA`: `#FAFAFA` - 浅灰色背景
- `GRAY_FB`: `#FBFBFB` - 浅灰色背景
- `GRAY_FC`: `#FCFCFC` - 浅灰色背景
- `GRAY_FD`: `#FDFDFD` - 浅灰色背景
- `GRAY_FE`: `#FEFEFE` - 浅灰色背景
- `GRAY_f5fe`: `#edf5fe` - 浅蓝色灰色

**其他灰色：**
- `GREY_10`: `grey` - 灰色变体

### 2.3 特殊颜色

- `GRAYSKYBLUE`: `#F2F9FF` - 灰天蓝色

## 3. 使用示例

### 3.1 在 React 组件中使用

```javascript
import React from 'react';
import { color } from '@cqsjjb/jjb-common-lib';

function MyComponent() {
  return (
    <div style={{ 
      color: color.BLUE,
      backgroundColor: color.GRAY_F5,
      border: `1px solid ${color.GRAY_DDD}`
    }}>
      使用预定义颜色
    </div>
  );
}
```

### 3.2 在 CSS/Less 中使用

```less
// 在 Less 文件中
@import '~@cqsjjb/jjb-common-lib/dist/color.css';

.my-class {
  color: @color-blue;
  background-color: @color-gray-f5;
}
```

### 3.3 在样式对象中使用

```javascript
import { color } from '@cqsjjb/jjb-common-lib';

const styles = {
  header: {
    backgroundColor: color.WHITE,
    borderBottom: `1px solid ${color.GRAY_EEE}`,
    color: color.GRAY_333
  },
  button: {
    backgroundColor: color.BLUE,
    color: color.WHITE,
    border: `1px solid ${color.BLUE}`
  },
  error: {
    color: color.RED,
    backgroundColor: color.RED_10
  },
  success: {
    color: color.GREEN,
    backgroundColor: color.GREEN_10
  }
};
```

### 3.4 动态样式

```javascript
import { color } from '@cqsjjb/jjb-common-lib';

function getStatusColor(status) {
  switch (status) {
    case 'success':
      return color.GREEN;
    case 'error':
      return color.RED;
    case 'warning':
      return color.ORANGE;
    case 'info':
      return color.BLUE;
    default:
      return color.GRAY_666;
  }
}

function StatusBadge({ status }) {
  return (
    <span style={{ color: getStatusColor(status) }}>
      {status}
    </span>
  );
}
```

### 3.5 与 antd 组件结合

```javascript
import { Button } from 'antd';
import { color } from '@cqsjjb/jjb-common-lib';

function CustomButton() {
  return (
    <Button 
      style={{
        backgroundColor: color.BLUE,
        borderColor: color.BLUE,
        color: color.WHITE
      }}
    >
      自定义按钮
    </Button>
  );
}
```

## 4. 颜色使用建议

### 4.1 文本颜色

- **主要文本**：使用 `GRAY_333`、`GRAY_444`、`GRAY_555`
- **次要文本**：使用 `GRAY_666`、`GRAY_777`、`GRAY_888`
- **辅助文本**：使用 `GRAY_999`、`GRAY_AAA`、`GRAY_BBB`
- **禁用文本**：使用 `GRAY_CCC`、`GRAY_DDD`

### 4.2 背景颜色

- **页面背景**：使用 `GRAY_F5`、`GRAY_FA`、`WHITE`
- **卡片背景**：使用 `WHITE`、`GRAY_F9`
- **悬停背景**：使用 `GRAY_F0`、`GRAY_F1`
- **选中背景**：使用 `GRAYSKYBLUE`、`GRAY_f5fe`

### 4.3 边框颜色

- **主要边框**：使用 `GRAY_DDD`、`GRAY_EEE`
- **次要边框**：使用 `GRAY_F0`、`GRAY_F1`
- **强调边框**：使用 `BLUE`、`GREEN`、`RED` 等主题色

### 4.4 状态颜色

- **成功**：`GREEN`、`GREEN_10`
- **错误**：`RED`、`RED_10`、`RED_5`
- **警告**：`ORANGE`、`YELLOW`
- **信息**：`BLUE`、`Blue_10`、`CYAN`

## 5. 颜色命名规范

颜色命名遵循以下规范：

1. **基础颜色**：使用大写英文单词，如 `BLUE`、`RED`、`GREEN`
2. **灰色系**：使用 `GRAY_` 前缀 + 编号或十六进制值，如 `GRAY_333`、`GRAY_F5`
3. **颜色变体**：使用颜色名 + 下划线 + 编号，如 `RED_10`、`Blue_10`
4. **特殊颜色**：使用描述性名称，如 `GRAYSKYBLUE`、`GEEKBLUE`

## 6. 相关模块

- **详细文档**：参考 `reference/color.js` 查看完整的颜色值列表
- **antd 主题**：可与 antd 的主题配置结合使用

## 7. 注意事项

1. **颜色一致性**：建议在项目中统一使用 `color` 模块的颜色值，保持视觉一致性

2. **可访问性**：使用颜色时注意对比度，确保文本可读性

3. **主题适配**：如需支持深色模式，可能需要额外的颜色配置

4. **类型安全**：在 TypeScript 项目中，`color` 对象提供类型提示，便于使用

5. **性能**：颜色值是常量，不会影响性能，可以放心使用

## 8. 完整颜色列表

所有可用的颜色值：

```javascript
import { color } from '@cqsjjb/jjb-common-lib';

// 查看所有颜色
console.log(Object.keys(color));

// 获取特定颜色值
console.log(color.BLUE);      // #1890FF
console.log(color.GRAY_333);   // #333
console.log(color.GRAY_F5);    // #F5F5F5
```

## 9. 最佳实践

1. **统一管理**：使用 `color` 模块统一管理项目颜色，避免硬编码颜色值

2. **语义化使用**：根据颜色的语义使用，如成功用绿色，错误用红色

3. **层次分明**：使用不同深度的灰色创建视觉层次

4. **主题色**：选择一种或几种主题色（如蓝色）作为主要强调色

5. **文档记录**：在项目文档中记录颜色使用规范，便于团队协作
