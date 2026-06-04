---
name: read-remote-image-url
description: >-
  通过「URL 下载到工作区 + Read 工具」可靠读取远程截图/设计图（PNG、JPEG、GIF、WebP），用于需求对照、UI 还原与画面描述。
  在用户提供阿里文档/语雀/OSS 图片链接、或 URL 抓取工具对二进制图片失败时使用。
---

# 远程图片 URL 读取流程

## 何时使用

- 用户给出 **图片直链**（如 `*.png` / `*.jpg`），需要 **描述界面、对照 PRD、或和代码页对比**
- 对 URL 使用 **网页/文档抓取工具** 得到 **非 200、500 或无法解码**，但浏览器可打开
- 工作区内 **已有图片文件**：跳过下载，直接对路径执行 **Read**

## 不适用

- 需登录、防盗链、签名过期的一次性 URL：应用侧不可用时不要反复重试下载；请用户导出到本地再 `Read`
- 仅信任业务相关或用户明确提供的 URL；**勿**对未知链接做批量下载

## 推荐流程（顺序执行）

1. **（可选）** 对 URL 发起一次抓取/HEAD：若已能得到可用图片内容，可直接使用；**多数环境下对二进制图片会失败**，此时进入步骤 2。
2. **下载到工作区**（须为仓库内或可写路径，便于 Read）：
   - **Windows（PowerShell）**：`curl` 常指向 `Invoke-WebRequest`，须使用 **`curl.exe`**。
   - **链式命令（必读）**：Windows 自带的 **PowerShell 5.x** 不支持 `cd ... && curl.exe ...`（`&&` 会解析失败，导致 **curl 根本没执行**）。智能体应二选一：
     - **推荐**：在同一 shell 内先 `Set-Location "<工作区根目录>"`，再执行 `curl.exe ...`（两条命令或一行用 **`;`** 分隔：`Set-Location "..."; curl.exe ...`）。
     - 仅当明确在 **PowerShell 7+** 环境时，才可使用 `&&`。
   - `-o` 的相对路径相对于 **当前工作目录**，故必须先切到工作区再下载，或通过终端工具的 working directory 设为工作区后再只写 `curl.exe` 一行。
   - 示例（路径按实际工作区调整）：

```powershell
Set-Location "D:\workspace\your-repo"
curl.exe -sL -o ".temp/tmp-remote-image.png" "https://example.com/path/to/image.png"
```

   - **（可选）** 与下载是 **另一次请求**：`curl.exe -sI "<URL>"` 仅取响应头，用于确认 `HTTP/1.1 200`、`Content-Type: image/*`；不做预检时可省略，只执行上面带 `-o` 的一次下载即可。
3. **Read**：对保存后的 **绝对路径或相对工作区路径** 调用 Read（工具支持 **jpeg/png/gif/webp**），根据返回的图像理解结果回答用户。
4. **清理**：分析结束后 **删除** 临时文件，避免把无关二进制提交进 Git。

## 与本地文件的关系

- 用户已提供 **`D:\...\shot.png`** 或仓库内 `requirements/...png`：**直接 Read**，无需 `curl`。

## 自检

- [ ] 临时文件放在 `.temp/` 或明确临时目录，且已删除或已加入 `.gitignore`
- [ ] Windows 使用 `curl.exe`，避免 PowerShell 假 `curl` 报错
- [ ] Windows PowerShell 5.x 不用 `&&` 链式 `cd` 与 `curl`；用 `Set-Location` + `;` 或分两次执行，并确认 `curl` 退出码为 0、目标文件非空
- [ ] Read 失败时检查扩展名是否为支持格式，或文件是否实际为 HTML 错误页（可查看文件头或前几字节）
