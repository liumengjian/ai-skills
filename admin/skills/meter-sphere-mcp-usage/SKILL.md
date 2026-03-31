---
name: meter-sphere-mcp-usage
description: >-
  Guides use of the MeterSphere MCP tool in Cursor for automated smoke testing.
  Use when the user mentions MeterSphere, smoke testing, test cases, get test list, or run tests.
---

# MeterSphere MCP 工具使用指南

## 何时使用

在以下场景下应用本技能：

- 用户提到 MeterSphere、冒烟测试、测试用例
- 用户要求获取测试列表、查看测试详情、标记测试完成
- 用户需要配置或切换测试模块

## MCP 配置

配置位于 `~/.cursor/mcp.json`，meter-sphere 服务示例：

```json
{
  "meter-sphere": {
    "command": "npx",
    "args": ["-y", "@cqsjjb/meter-sphere-mcp-server"],
    "env": {
      "PLATFORM_PROJECT": "958396182437888",
      "PLATFORM_ORGANIZATION": "100001",
      "PLATFORM_MODULE_IDS": "[693465419956224]",
      "PLATFORM_X_AUTH_TOKEN": "82ad2192-5160-47c9-8047-61997acbc83f",
      "PLATFORM_CSRF_TOKEN": "JxSklAF+92FPavNzl6AoT/LSVCBwffCWIa+/1zrys/FFakvLflaSh56hPFGuRwlvKHOuGySLxAS6rBlPiIftqo6WtQ4RbPlokGOxzc5gSFo="
    },
    "description": "自动化冒烟测试平台 MCP 工具"
  }
}
```

### 配置说明（重要）

| 环境变量 | 是否可配置 | 说明 |
|----------|------------|------|
| PLATFORM_PROJECT | 固定 | 无需修改 |
| PLATFORM_ORGANIZATION | 固定 | 无需修改 |
| PLATFORM_X_AUTH_TOKEN | 固定 | 无需修改 |
| PLATFORM_CSRF_TOKEN | 固定 | 无需修改 |
| **PLATFORM_MODULE_IDS** | **需配置** | 默认模块 ID，多个用逗号分隔，JSON 数组字符串格式 |

### 配置 PLATFORM_MODULE_IDS

**单个模块**：`"[693465419956224]"`  
**多个模块**：`"[693465419956224, 693465419956225, 693465419956226]"`  
格式必须是 JSON 数组的字符串表示。

## 可用工具

MCP 服务器标识：`user-meter-sphere`（对应 mcp.json 中的 `meter-sphere`）

### get_test_list

获取测试用例列表，按优先级排序（P0 > P1 > P2 > P3），生成 TODO 清单。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| excludeCompleted | boolean | 否 | 是否排除已完成用例。用户要求「继续测试」「跳过已完成」时设为 true |
| moduleIds | string[] | 否 | 模块 ID 列表，按模块筛选。未传入时使用环境变量 PLATFORM_MODULE_IDS |

### get_test_detail

根据用例 ID 获取测试详情，包括测试步骤和 AI 测试提示语。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| testCaseId | string | 是 | 测试用例 ID |
| testPlanCollectionName | string | 是 | 测试点名称（从 get_test_list 返回） |

### get_test_progress

获取当前测试进度，包括已完成和未完成统计。无参数。

### mark_test_completed

标记指定用例为已完成。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| testCaseId | string | 是 | 测试用例 ID |
| priority | string | 是 | 优先级（P0/P1/P2/P3） |

### reset_test_progress

重置测试进度，清空所有已完成记录。无参数。

## 调用前必做

**先查阅工具 schema**：调用前到 `mcps/user-meter-sphere/tools/` 下读取对应 `*.json` descriptor，确认最新参数定义。

## 典型工作流

1. **获取待测列表**：`get_test_list`
   - 继续测试 / 跳过已完成：`excludeCompleted: true`
   - 指定模块：传入 `moduleIds: ["id1", "id2"]`，不传则用环境变量默认
2. **查看用例详情**：`get_test_detail`，需 `testCaseId`、`testPlanCollectionName`
3. **标记完成**：`mark_test_completed`，需 `testCaseId`、`priority`
4. **查看进度**：`get_test_progress`
5. **重置进度**：`reset_test_progress`

## 注意事项

- 工具仅用于静态代码分析验证，不涉及实际交互测试；涉及界面、用户操作的用例需提示用户手动验证
- `get_test_list` 的 `moduleIds` 可在调用时覆盖环境变量，无需修改 mcp.json 即可切换模块
- 修改环境变量 PLATFORM_MODULE_IDS 后需重启 Cursor 或重新加载 MCP 连接
- 多模块时逗号后需加空格以保证 JSON 格式正确
