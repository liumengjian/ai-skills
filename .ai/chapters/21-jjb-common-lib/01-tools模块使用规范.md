# 二十二、tools 模块使用规范

## 1. 概述

`tools` 模块是 `@cqsjjb/jjb-common-lib` 通用工具库中的核心模块，包含大量基础工具函数。开发时应优先使用工具库中的工具，避免重复造轮子。

### 1.1 使用建议

- **优先查找**：在实现功能前，应先查找 `tools` 模块中是否有对应的工具函数
- **避免重复**：不要重复实现工具库中已有的功能
- **参考文档**：使用前应参考 `reference/tools.md` 查看完整的 API 文档和使用示例

### 1.2 导入方式

```javascript
import { tools } from '@cqsjjb/jjb-common-lib';
```

## 2. 内置方法详解

### 2.1 JSON/数据解析与序列化

#### parseJSON(value)

解析 JSON 字符串。

**参数：**
- `value` (string): JSON 字符串

**返回值：**
- 如果不是 JSON 字符串，则返回传入的值；如果是 JSON 字符串，则返回解析后的对象/数组；如果解析失败返回传入的值

**示例：**
```javascript
tools.parseJSON('{"a":1}') // => { a: 1 }
```

#### parseObject(v)

序列化对象转真对象。

**参数：**
- `v` (string): JSON 字符串

**返回值：**
- 解析后的对象，如果解析失败返回 `{}`

**示例：**
```javascript
tools.parseObject('{"a":1}') // => { a: 1 }
```

#### parseArray(v)

序列化数组转真数组。

**参数：**
- `v` (string): JSON 字符串

**返回值：**
- 解析后的数组，如果解析失败返回 `[]`

**示例：**
```javascript
tools.parseArray('[1,2,3]') // => [1,2,3]
```

#### stringifyObject(v, replacer?, space?)

序列化对象为 JSON 字符串。

**参数：**
- `v` (any): 对象
- `replacer` (any, 可选): 替换函数
- `space` (number, 可选): 缩进，默认为 2

**返回值：**
- JSON 字符串，如果转换失败返回 `'{}'`

**示例：**
```javascript
tools.stringifyObject({a:1}) // => '{"a":1}'
```

#### stringifyArray(v, replacer?, space?)

序列化数组为 JSON 字符串。

**参数：**
- `v` (any[]): 数组
- `replacer` (any, 可选): 替换函数
- `space` (number, 可选): 缩进，默认为 2

**返回值：**
- JSON 字符串，如果转换失败返回 `'[]'`

**示例：**
```javascript
tools.stringifyArray([1,2]) // => '[1,2]'
```

### 2.2 数据清洗

#### cleanArray(v)

清洗数组，移除无效值。

**参数：**
- `v` (any[]): 数组

**返回值：**
- 清洗后的数组

**示例：**
```javascript
tools.cleanArray([1,2,null]) // => [1,2,null]
```

#### cleanObject(v)

清洗对象，移除 `undefined` 等无效属性。

**参数：**
- `v` (object): 对象

**返回值：**
- 清洗后的对象

**示例：**
```javascript
tools.cleanObject({a:1,b:undefined}) // => {a:1}
```

### 2.3 类型判断

#### isEmptyObject(v)

判断是否是空对象。

**参数：**
- `v` (any): 任意值

**返回值：**
- `boolean`: 是否是空对象

**示例：**
```javascript
tools.isEmptyObject({}) // => true
```

#### isEmptyStringObject(v)

判断是否是空字符串对象（字符串 `'{}'`）。

**参数：**
- `v` (any): 任意值

**返回值：**
- `boolean`: 是否是空字符串对象

**示例：**
```javascript
tools.isEmptyStringObject('{}') // => true
```

#### isEmptyStringArray(v)

判断是否是空字符串数组（字符串 `'[]'`）。

**参数：**
- `v` (any): 任意值

**返回值：**
- `boolean`: 是否是空字符串数组

**示例：**
```javascript
tools.isEmptyStringArray('[]') // => true
```

#### isNativeEvent(v)

判断是否是 Event 对象。

**参数：**
- `v` (any): 任意值

**返回值：**
- `boolean`: 是否是 Event 对象

**示例：**
```javascript
tools.isNativeEvent(new Event('click')) // => true
```

#### getPrimaryType(v)

获取基础类型字符串。

**参数：**
- `v` (any): 任意值

**返回值：**
- `string`: 基础类型字符串（如 `'Number'`、`'String'` 等）

**示例：**
```javascript
tools.getPrimaryType(1) // => 'Number'
```

#### isTrueEnum(v)

判断是否等于 `'TRUE'`。

**参数：**
- `v` (any): 任意值

**返回值：**
- `boolean`: 是否等于 `TRUE_ENUM`（`'TRUE'`）

**示例：**
```javascript
tools.isTrueEnum('TRUE') // => true
```

#### isFalseEnum(v)

判断是否等于 `'FALSE'`。

**参数：**
- `v` (any): 任意值

**返回值：**
- `boolean`: 是否等于 `FALSE_ENUM`（`'FALSE'`）

**示例：**
```javascript
tools.isFalseEnum('FALSE') // => true
```

#### isBoolEnum(v)

判断是否是 `'TRUE'` 或 `'FALSE'`。

**参数：**
- `v` (any): 任意值

**返回值：**
- `boolean`: 是否是 `TRUE_ENUM` 或 `FALSE_ENUM`

**示例：**
```javascript
tools.isBoolEnum('TRUE') // => true
tools.isBoolEnum('FALSE') // => true
```

### 2.4 类型转换

#### toObject(v)

转换为对象。

**参数：**
- `v` (any): 任意值

**返回值：**
- 对象，如果为空对象则返回 `{}`

**示例：**
```javascript
tools.toObject(null) // => {}
```

#### toFunction(v)

转换为函数。

**参数：**
- `v` (any): 任意值

**返回值：**
- 函数，如果不是函数则返回 `noop`

**示例：**
```javascript
tools.toFunction(() => 1) // => () => 1
```

#### toArray(v)

转换为数组。

**参数：**
- `v` (any): 任意值

**返回值：**
- 数组，如果不是数组则返回 `[]`

**示例：**
```javascript
tools.toArray(1) // => []
```

#### toBoolEnum(v)

布尔值转字符串枚举。

**参数：**
- `v` (boolean): 布尔值

**返回值：**
- `'TRUE' | 'FALSE'`: 转换后的枚举字符串

**示例：**
```javascript
tools.toBoolEnum(true) // => 'TRUE'
tools.toBoolEnum(false) // => 'FALSE'
```

### 2.5 数组处理

#### uniqueArray(array)

字符串或数字数组去重复。

**参数：**
- `array` (T[], 可选): 数组，默认为 `[]`

**返回值：**
- 去重后的数组

**示例：**
```javascript
tools.uniqueArray([1,2,3,1]) // => [1,2,3]
```

### 2.6 字符串处理

#### classNames(...args)

绑定 className，支持字符串、数组等多种参数格式。

**参数：**
- `...args` (any[]): 类名参数，可以是字符串、数组等

**返回值：**
- `string`: 合并后的类名字符串

**示例：**
```javascript
tools.classNames('a', 'b', 'c') // => 'a b c'
tools.classNames('a', ['b', 'c']) // => 'a b c'
```

#### toCamelCase(str)

下划线转小驼峰。

**参数：**
- `str` (string): 下划线格式的字符串

**返回值：**
- `string`: 小驼峰格式的字符串，如果不是字符串则返回空字符串

**示例：**
```javascript
tools.toCamelCase('hello_world') // => 'helloWorld'
```

#### toPascalCase(str)

下划线转大驼峰。

**参数：**
- `str` (string): 下划线格式的字符串

**返回值：**
- `string`: 大驼峰格式的字符串，如果不是字符串则返回空字符串

**示例：**
```javascript
tools.toPascalCase('hello_world') // => 'HelloWorld'
```

### 2.7 环境检测

#### inIframe()

判断当前网页是否嵌入 iframe。

**返回值：**
- `boolean`: 是否在 iframe 中

**示例：**
```javascript
tools.inIframe() // => true/false
```

#### inWxBrowser()

判断当前网页是否在微信浏览器中。

**返回值：**
- `boolean`: 是否在微信小程序浏览器中

**示例：**
```javascript
tools.inWxBrowser() // => true/false
```

### 2.8 异步处理

#### asyncWait(fn, callback, maxCount?)

异步等待，通过检查函数 `fn` 返回真值时停止等待并执行回调。

**参数：**
- `fn` (() => any): 检查函数，返回真值时停止等待
- `callback` ((value: any) => void): 回调函数
- `maxCount` (number, 可选): 最大执行次数，默认为 0（无限制）

**返回值：**
- `void`

**示例：**
```javascript
tools.asyncWait(() => 1, (value) => console.log(value), 10)
```

### 2.9 路由参数管理

`router` 对象提供完整的路由参数管理能力，基于 `qs` 模块实现。

#### router.values()

获取路由参数值数组。

**返回值：**
- `string[]`: 路由参数值数组

**示例：**
```javascript
tools.router.values() // => ['1','2','3']
```

#### router.keys()

获取路由参数键数组。

**返回值：**
- `string[]`: 路由参数键数组

**示例：**
```javascript
tools.router.keys() // => ['a','b','c']
```

#### router.length

获取路由参数长度（只读）。

**返回值：**
- `number`: 路由参数长度

**示例：**
```javascript
tools.router.length // => 3
```

#### router.query

获取/设置路由参数对象。

**获取示例：**
```javascript
tools.router.query // => {a:1,b:2,c:3}
```

**设置示例：**
```javascript
tools.router.query = {a:1,b:2,c:3}
tools.router.query.a = 1
delete tools.router.query.a
```

#### router.has(name)

判断是否存在指定路由参数。

**参数：**
- `name` (string): 路由参数名

**返回值：**
- `boolean`: 是否存在该路由参数

**示例：**
```javascript
tools.router.has('a') // => true
```

#### router.add(name, value)

添加路由参数。

**参数：**
- `name` (string): 路由参数名
- `value` (any): 路由参数值

**返回值：**
- `void`

**示例：**
```javascript
tools.router.add('a', 1)
```

#### router.delete(name)

删除路由参数。

**参数：**
- `name` (string): 路由参数名

**返回值：**
- `void`

**示例：**
```javascript
tools.router.delete('a')
```

#### router.toString(prefix?)

转为字符串。

**参数：**
- `prefix` (boolean, 可选): 是否添加前缀 `?`，默认为 `false`

**返回值：**
- `string`: 路由参数字符串

**示例：**
```javascript
tools.router.toString(true) // => '?a=1&b=2&c=3'
```

### 2.10 文件处理

#### base64ToFile(base64, fileName)

base64 字符串转 File 对象。

**参数：**
- `base64` (string): base64 字符串
- `fileName` (string): 文件名

**返回值：**
- `File | undefined`: File 对象，转换失败返回 `undefined`

**示例：**
```javascript
tools.base64ToFile('data:image/png;base64,...', '123.png') // => File
```

#### fileToBase64(file)

File 对象转 base64 字符串。

**参数：**
- `file` (File): File 对象

**返回值：**
- `Promise<string | undefined>`: base64 字符串，转换失败返回 `undefined`

**示例：**
```javascript
tools.fileToBase64(new File([], '123.png')) // => Promise<'base64'>
```

### 2.11 枚举处理

#### getEnumLabel(data)

获取枚举标签。

**参数：**
- `data` (string | { label: string }): 枚举数据，可以是字符串或包含 `label` 属性的对象

**返回值：**
- `string | undefined`: 枚举标签

**示例：**
```javascript
tools.getEnumLabel({ label: '1' }) // => '1'
tools.getEnumLabel('label') // => 'label'
```

#### getEnumValue(data)

获取枚举值。

**参数：**
- `data` (string | { value: any }): 枚举数据，可以是字符串或包含 `value` 属性的对象

**返回值：**
- `any`: 枚举值

**示例：**
```javascript
tools.getEnumValue({ value: '1' }) // => '1'
tools.getEnumValue('value') // => 'value'
```

## 3. 使用注意事项

1. **错误处理**：大部分函数都有容错处理，解析失败或转换失败时会返回默认值（如 `{}`、`[]`、`undefined` 等），使用时应注意处理这些情况

2. **类型安全**：虽然工具函数提供了类型转换功能，但在 TypeScript 项目中仍应尽量保证类型安全

3. **性能考虑**：对于频繁调用的场景，应注意函数的性能表现

4. **参考文档**：详细的使用示例和 API 文档请参考 `reference/tools.md`

## 4. 相关模块

- **qs 模块**：`tools.router` 的核心技术基于 `qs` 模块实现
- **详细文档**：`reference/tools.md` 包含完整的 API 文档和使用示例
