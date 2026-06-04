---
name: markdownify-mcp
description: >-
  使用 req-doc-markdownify（mcp-markdownify-server）将本地 PDF、DOCX 等转为 Markdown，供需求分析使用。
  在用户要解析需求文档、钉钉导出文件、PRD 转文本时使用。
---

# 需求文档 Markdownify MCP 使用指南

> **配图 PRD**：Word 含截图时 **优先** 使用 `admin/scripts/docx_to_markdown_with_images.py`（或复制到全局脚本目录），生成含 `![](…media/…)` 的 `.md`；纯文本、简单结构可用本 MCP `docx-to-markdown`。得到 `.md` 后，在业务仓库用 **`requirements-analysis`** 直接 **Read** 该文件做落点与清单，无需单独的「整理版」智能体。

## 何时使用

- 已把钉钉导出的 **PDF / Word（.docx）** 存到本机，需要转成 Markdown 再给 AI 做需求分析
- 用户提供「本地文件路径」，希望抽取正文与表格（效果受版式影响，需人工抽查）

## Cursor 中的服务名

配置键名：`req-doc-markdownify`（见 `admin/mcp.json`）。

首次用 `npx` 拉起时，包内 `preinstall` 会尝试执行 `python -m venv` 并安装 `markitdown`，**需本机已安装 Python 且可在终端执行 `python`**。若失败，请在终端手动执行一次 `npx -y mcp-markdownify-server` 查看报错。

**手动补环境（在 `mcp-markdownify-server` 包目录下，与 `package.json` 同级）**：

```powershell
python -m venv .venv
.\.venv\Scripts\pip.exe install "markitdown[docx]"
```

仅装 `markitdown` 不含 Word 依赖时，调用 `docx-to-markdown` 会报 `MissingDependencyException`；Word 须使用 **`markitdown[docx]`**（或 `markitdown[all]`）。PDF 可再按需安装 `markitdown[pdf]` 等，见 markitdown 文档。

## 常用工具

以下工具参数中的 **`filepath` 必须为绝对路径**（Windows 例如 `D:\\docs\\需求.docx`）。

| tool                 | 说明        | 必选参数   |
|----------------------|-------------|------------|
| `docx-to-markdown`   | Word 转 MD  | `filepath` |
| `pdf-to-markdown`    | PDF 转 MD   | `filepath` |
| `get-markdown-file`  | 读取已有 .md | `filepath` |

其他：`xlsx-to-markdown`、`pptx-to-markdown`、`image-to-markdown`、`webpage-to-markdown` 等见上游 README。

## 可选环境变量

- **`MD_SHARE_DIR`**：若设置，则 `get-markdown-file` 仅能读取该目录下的 Markdown，降低误读路径风险。

## 限制说明

- 上游 README 标注 **Windows 支持仍在完善**，复杂 PDF/扫描件可能需 OCR 或改导出 Word 再转。
- **钉钉链拉取** 不在本 MCP 内；流程为：钉钉下载 → 本地路径 → 调用 `docx-to-markdown` / `pdf-to-markdown`。

### Word 里的截图/图片为什么 MCP 里「没了」？

- **MCP / markitdown**：底层用 mammoth 等做结构转换，在 **表格嵌套、图文混排** 等版式下，经常出现 **整格图片被省略**，只保留右侧文字（与插件「看到的样子」不一致）。
- **Office Viewer（等插件）**：是编辑器 **按 Word 规则直接渲染**，不是把 docx 抽成纯 Markdown，所以版式与图片更完整。

**需要正文的图片一并给 AI 时**，优先用仓库脚本（导出 PNG + Markdown 相对路径）：

```powershell
pip install mammoth
python admin/scripts/docx_to_markdown_with_images.py ".temp\你的需求.docx" -o ".temp\你的需求.md" --media-dir "你的需求.media"
```

生成的 `.md` 中会包含 `![](你的需求.media/image_001.png)` 等引用，同目录旁会有图片文件夹。再让 AI `Read` 该 `.md` 即可。

- **选型**：纯文本、简单结构可用 MCP `docx-to-markdown`；**强依赖版面截图**时用本脚本或 **Pandoc**（`--extract-media`）做对照。

## 调用方式

使用 Cursor MCP 工具调用界面或 `call_mcp_tool`：`server` 为配置中的键名（如 `req-doc-markdownify`），`toolName` 为上表名称，`arguments` 传 JSON（如 `{ "filepath": "D:\\\\docs\\\\需求.docx" }`）。
