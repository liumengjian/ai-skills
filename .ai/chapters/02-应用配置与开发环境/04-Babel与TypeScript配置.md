# 二、应用配置与开发环境

## 4. Babel 与 TypeScript 配置

### 4.1. Babel 配置管理

- **配置文件**：应用的 Babel 配置统一在根目录 `jjb.babel.js` 文件中进行管理

  - 说明：所有 Babel 相关配置（如插件、预设等）应在此文件中统一维护，禁止在项目其他位置分散配置

### 4.2. TypeScript 开发配置

- **安装依赖**：

  ```bash
  yarn add ts-loader typescript -D
  ```

- **Webpack 配置**：在 `jjb.config.js` 文件的 `webpackConfig` 节点中添加 TypeScript 文件处理规则

  ```javascript
  // jjb.config.js
  {
    // ... 其他配置
    webpackConfig: {
      htmlWebpackPluginOption: {
        inject: true
      },
      module: {
        rules: [
          // 添加ts文件规则
          {
            test: /\.(ts|tsx)$/,
            loader: 'ts-loader'
          }
        ]
      }
    }
  }
  ```

- **TypeScript 配置文件**：在根目录新建 `tsconfig.json` 文件，配置内容如下：

  ```json
  {
    "compilerOptions": {
      "module": "commonjs",
      "target": "es5",
      "jsx": "react",
      "allowSyntheticDefaultImports": true,
      "experimentalDecorators": true,
      "baseUrl": "./",
      "paths": {
        "~/*": ["src/*"]
      }
    },
    "exclude": [
      "node_modules"
    ]
  }
  ```

- **配置说明**：

  - **module**：指定模块系统，使用 `"commonjs"` 兼容 Node.js 环境

  - **target**：编译目标 ES 版本，使用 `"es5"` 确保浏览器兼容性

  - **jsx**：指定 JSX 处理方式，使用 `"react"` 支持 React 组件

  - **allowSyntheticDefaultImports**：允许从没有默认导出的模块中默认导入

  - **experimentalDecorators**：启用装饰器支持，用于 `@Connect` 等装饰器语法

  - **baseUrl**：设置基础路径，用于解析非相对模块名

  - **paths**：路径映射配置，`"~/*"` 映射到 `"src/*"`，与项目路径别名保持一致

- **文件格式**：页面和组件文件格式改为 `.tsx` 即可使用 TypeScript 开发

- **注意事项**：

  - 安装依赖时需要使用 `-D` 参数，将 `ts-loader` 和 `typescript` 作为开发依赖安装

  - `tsconfig.json` 中的 `paths` 配置必须与项目的路径别名保持一致（`~` 指向 `src` 目录）

  - 配置变更后需要重启开发服务器才能生效
