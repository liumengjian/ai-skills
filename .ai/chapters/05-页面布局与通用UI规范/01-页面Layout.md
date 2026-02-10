# 五、页面布局与通用 UI 规范

## 1. 页面 Layout

- 除提示词明确不需要的情况下，所有页面 **必须** 使用：

  ```javascript
  import PageLayout from '@cqsjjb/jjb-react-admin-component/PageLayout'
  ```

  必须严格参考node_modules中对应依赖包的 MD 文档或 d.ts 文件！不得猜测组件属性！

- 禁止自定义页面根容器（除提示语明确要求的除外）

### 代码演示

```jsx
import { Button } from 'antd';
import PageLayout from '@cqsjjb/jjb-react-admin-component/PageLayout';

function App() {
  return (
    <PageLayout title="用户中心">
      
    </PageLayout>
  )
}
```

### API

| 属性              | 说明         |       类型        |   默认值 |
|-----------------|:-----------|:---------------:|------:|
| title           | 页面标题       |    `string`     |     - |
| extra           | 右上角扩展      |   `ReactNode`   |     - |
| header          | 自定义头部      |   `ReactNode`   |     - |
| footer          | 自定义底部      |   `ReactNode`   |     - |
| history         | 路由历史对象     |    `History`    |     - |
| noStyle         | 去除所有样式     |    `boolean`    | false |
| noBorder        | 取消边框       |    `boolean`    | false |
| formLine        | form 表单行   |  `ReactNode[]`  |     - |
| formLineStyle   | form 表单行样式 | `CSSProperties` |     - |
| previous        | 显示返回上一页    |    `boolean`    | false |
| transparent     | 背景透明       |    `boolean`    | false |
| contentStyle    | 内容区样式      | `CSSProperties` |     - |
| footerStyle     | 底部样式       | `CSSProperties` |     - |
| pageHeaderStyle | 头部样式       | `CSSProperties` |     - |
| style           | 容器样式       | `CSSProperties` |     - |
| onBack          | 自定义返回事件    |  `() => void`   |     - |

> **注意**：`previous` 为 `true` 时 `history` 必传，否则点击返回无效。
