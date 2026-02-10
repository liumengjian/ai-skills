# 二、应用配置与开发环境

## 11. 构建工具与 Webpack/Rspack 配置

### 1. 构建工具说明

- **构建工具**：`@cqsjjb/scripts` 是微应用开发和编译构建工具

  - **技术实现**：早期版本基于 Webpack 5 实现，最新版本基于 Rspack 实现

  - **配置扩展**：构建工具的扩展配置在 `jjb.config.js` 的 `webpackConfig` 属性中进行

  - **主要功能**：
    - 开发服务器启动与管理
    - 生产环境构建与打包
    - 根据 `appIdentifier` 生成构建产物目录结构

### 2. Webpack/Rspack 配置扩展

- **配置来源**：Rspack 配置扩展来源于根目录 `jjb.config.js` 文件中的 `webpackConfig` 属性

- **配置说明**：

  - **兼容性**：`webpackConfig` 兼容 Webpack 配置格式，支持自定义 Rspack 构建配置

  - **配置合并机制**：用户配置会与 `@cqsjjb/scripts` 默认配置进行合并，相同配置项会覆盖默认值

  - **默认配置**：`@cqsjjb/scripts` 已内置常用配置（如 CSS/LESS 处理、JS/TS 编译、图片/字体/媒体资源处理等），用户只需配置特殊需求

- **支持的配置项**：

  ```javascript
  // jjb.config.js
  {
    webpackConfig: {
      // 入口文件（可选，默认: 'src/main.js'）
      entry: 'src/main.js',
      
      // 输出配置（可选）
      output: {
        path: 'dist',
        publicPath: '/',
        filename: '[name].[hash].js'
      },
      
      // 模块解析配置（可选，会与默认配置合并）
      resolve: {
        alias: {
          '@': path.resolve(__dirname, 'src')
        }
      },
      
      // 模块规则配置（可选，会追加到默认规则后）
      module: {
        rules: [
          // 自定义 loader 规则
        ]
      },
      
      // 外部依赖配置（可选）
      externals: {
        'react': 'React',
        'react-dom': 'ReactDOM'
      },
      
      // 插件配置（可选）
      plugins: [
        // 自定义插件
      ],
      
      // 优化配置（可选）
      optimization: {
        minimize: true,
        splitChunks: {
          chunks: 'all'
        }
      },
      
      // HTML Webpack 插件配置（可选）
      htmlWebpackPluginOption: {
        inject: true
      },
      
      // 统计信息配置（可选）
      stats: {
        assets: true,
        chunks: false
      }
    }
  }
  ```

- **配置项说明**：

  | 配置项 | 类型 | 说明 | 默认值 |
  | :--- | :--- | :--- | :--- |
  | `entry` | string | 应用入口文件路径 | `'src/main.js'` |
  | `output` | object | 输出配置（path、publicPath、filename 等） | 根据 `appIdentifier` 自动生成 |
  | `resolve` | object | 模块解析配置（alias、extensions 等） | 默认包含 `~` 别名指向 `src` |
  | `module.rules` | array | 模块规则配置（loader 规则） | 默认包含 CSS/LESS、JS/TS、图片/字体/媒体处理规则 |
  | `externals` | object | 外部依赖配置 | `{}` |
  | `plugins` | array | 插件配置 | 默认包含 HTML 插件等 |
  | `optimization` | object | 优化配置（minimize、splitChunks 等） | 生产模式自动启用 |
  | `htmlWebpackPluginOption` | object | HTML Webpack 插件配置 | `{ inject: true }` |
  | `stats` | object | 构建统计信息配置 | 默认配置 |

- **配置示例**：

  - **示例1：自定义路径别名**

    ```javascript
    // jjb.config.js
    const path = require('path');

    module.exports = {
      // ...其他配置
      webpackConfig: {
        resolve: {
          alias: {
            '@': path.resolve(__dirname, 'src'),
            '@components': path.resolve(__dirname, 'src/components')
          }
        }
      }
    }
    ```

  - **示例2：自定义文件加载器（Loader）**

    ```javascript
    // jjb.config.js
    const appIdentifier = 'system';

    module.exports = {
      // ...其他配置
      webpackConfig: {
        module: {
          rules: [
            {
              // 加载MD文件
              test: /\.(md)$/,
              use: [
                {
                  loader: 'file-loader',
                  options: {
                    name: '[name].[hash].[ext]',
                    outputPath: appIdentifier + '/static/doc/'
                  }
                }
              ]
            }
          ]
        }
      }
    }
    ```

  - **示例3：配置外部依赖**

    ```javascript
    // jjb.config.js
    module.exports = {
      // ...其他配置
      webpackConfig: {
        externals: {
          'react': 'React',
          'react-dom': 'ReactDOM',
          'antd': 'antd'
        }
      }
    }
    ```

- **配置合并规则**：

  - **resolve**：用户配置会与默认配置合并，默认配置包含 `~` 别名指向 `src` 目录

  - **module.rules**：用户配置的规则会**追加**到默认规则后，不会覆盖默认规则

  - **其他配置项**：用户配置会覆盖默认配置

- **默认内置规则**：

  `@cqsjjb/scripts` 已内置以下处理规则，无需重复配置：

  - **CSS/LESS 文件**：自动处理 `.css` 和 `.less` 文件
  - **JS/TS 文件**：自动处理 `.js`、`.jsx`、`.ts`、`.tsx` 文件（使用 Babel）
  - **图片文件**：自动处理 `.png`、`.jpg`、`.jpeg`、`.gif`、`.ico`、`.bmp`、`.svg` 文件
  - **字体文件**：自动处理 `.eot`、`.woff`、`.ttf` 文件
  - **媒体文件**：自动处理 `.mp3`、`.mp4` 文件

- **配置参考**：所有配置项遵循 Webpack/Rspack 官方文档规范，具体配置选项请参考：

  - [Rspack 官方文档](https://rspack.dev/)
  - [Webpack 官方文档](https://webpack.js.org/configuration/)（Rspack 兼容 Webpack 配置格式）

- **使用场景**：适用于需要自定义构建行为、添加插件、配置别名、优化打包、处理特殊文件类型等高级构建需求

- **注意事项**：

  - **配置合并**：用户配置会与默认配置合并，`resolve` 和 `module.rules` 采用合并策略，其他配置项采用覆盖策略

  - **默认规则保留**：`module.rules` 中用户自定义的规则会追加到默认规则后，不会影响默认的 CSS/LESS、JS/TS、图片/字体/媒体处理规则

  - **谨慎配置**：建议仅在必要时进行扩展配置，避免过度自定义导致构建问题

  - **配置生效**：配置变更后需要重启开发服务器或重新构建才能生效

  - **路径别名**：默认已配置 `~` 别名指向 `src` 目录，用户可以通过 `resolve.alias` 添加其他别名，但建议保留 `~` 别名
