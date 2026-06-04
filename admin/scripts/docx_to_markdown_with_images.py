# -*- coding: utf-8 -*-
"""
将 DOCX 转为 Markdown，并把内嵌图片导出到同级 media 目录，Markdown 内使用相对路径引用。

说明：markitdown / MCP 用的默认 mammoth 路径在「表格+多图」等版式下经常出现图片被省略；
Office Viewer 是编辑器原生渲染 Word，与命令行转换不是同一套逻辑。
本脚本通过 mammoth 的 convert_image 将图片写入磁盘，便于 AI 与文档工具使用。

依赖：pip install mammoth

用法：
  python docx_to_markdown_with_images.py input.docx -o out.md
  python docx_to_markdown_with_images.py input.docx -o out.md --media-dir assets/req-images

全局安装（推荐，任意仓库可直接调用）：
  Windows: 复制本文件到 %USERPROFILE%\\.claude\\scripts\\
  或在 jjb-ai 仓库 .claude\\scripts 下执行: install-docx-converter-global.ps1
  然后: python "%USERPROFILE%\\.claude\\scripts\\docx_to_markdown_with_images.py" ...
"""

from __future__ import annotations

import argparse
import os
import sys


def main() -> int:
    try:
        import mammoth
    except ImportError:
        print("请先安装: pip install mammoth", file=sys.stderr)
        return 1

    parser = argparse.ArgumentParser(description="DOCX → Markdown，图片落盘")
    parser.add_argument("docx", help="输入 .docx 路径")
    parser.add_argument("-o", "--output", required=True, help="输出 .md 路径")
    parser.add_argument(
        "--media-dir",
        default="media",
        help="媒体目录（相对 output 所在目录），默认 media",
    )
    args = parser.parse_args()

    out_md = os.path.abspath(args.output)
    base_dir = os.path.dirname(out_md)
    media_rel = args.media_dir.strip("/\\").replace("\\", "/")
    media_abs = os.path.join(base_dir, media_rel.replace("/", os.sep))
    os.makedirs(media_abs, exist_ok=True)

    counter = {"n": 0}

    def save_image(image):
        content_type = image.content_type or "image/png"
        ext = content_type.split("/")[-1].lower()
        if ext in ("jpeg", "pjpeg"):
            ext = "jpg"
        counter["n"] += 1
        filename = f"image_{counter['n']:03d}.{ext}"
        path_abs = os.path.join(media_abs, filename)
        with image.open() as stream:
            data = stream.read()
        with open(path_abs, "wb") as f:
            f.write(data)
        rel_src = f"{media_rel}/{filename}".replace("\\", "/")
        return {"src": rel_src}

    docx_path = os.path.abspath(args.docx)
    if not os.path.isfile(docx_path):
        print(f"文件不存在: {docx_path}", file=sys.stderr)
        return 1

    with open(docx_path, "rb") as docx_file:
        result = mammoth.convert_to_markdown(
            docx_file,
            convert_image=mammoth.images.img_element(save_image),
        )

    for msg in result.messages:
        print(msg, file=sys.stderr)

    with open(out_md, "w", encoding="utf-8") as f:
        f.write(result.value)

    print(out_md, file=sys.stderr)
    print(f"images: {counter['n']}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
