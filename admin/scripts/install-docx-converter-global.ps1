# 将 docx_to_markdown_with_images.py 安装到 %USERPROFILE%\.claude\scripts\（全项目共用）
$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$src = Join-Path $here "docx_to_markdown_with_images.py"
if (-not (Test-Path -LiteralPath $src)) {
    Write-Error "找不到源文件: $src"
}
$destDir = Join-Path $env:USERPROFILE ".claude\scripts"
New-Item -ItemType Directory -Force -Path $destDir | Out-Null
$dest = Join-Path $destDir "docx_to_markdown_with_images.py"
Copy-Item -LiteralPath $src -Destination $dest -Force
Write-Host "已安装: $dest"
Write-Host "依赖: pip install mammoth"
