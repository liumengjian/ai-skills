# 六、搜索区规范（一级页面）

## 4. API

| 属性            | 说明                        |                       类型                        |   默认值 |
|---------------|:--------------------------|:-----------------------------------------------:|------:|
| form          | form 实例                   |         `React.RefObject<FormInstance>`         |     - |
| style         | 样式                        |                 `CSSProperties`                 |     - |
| expand        | 是否展开，受控模式                 |                    `boolean`                    | false |
| defaultExpand | 内部默认展开状态，仅在 expand 未传入时生效 |                    `boolean`                    | false |
| colSize       | 列数                        |                    `number`                     |     3 |
| loading       | 查询 loading 状态             |                    `boolean`                    | false |
| formLine      | 表单行节点数组                   |                  `ReactNode[]`                  |     - |
| initialValues | 表单初始值                     |              `Record<string, any>`              |     - |
| onRef         | 获取 form 实例回调（已废弃）         | `(form: React.RefObject<FormInstance>) => void` |     - |
| onReset       | 重置回调                      |     `(values: Record<string, any>) => void`     |     - |
| onFinish      | 提交回调                      |     `(values: Record<string, any>) => void`     |     - |
| onExpand      | 展开/收起状态变化回调               |            `(open: boolean) => void`            |     - |
