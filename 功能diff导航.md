# 功能 diff 导航

本文件只列功能简述；详细说明见 `.diff_docs/`（一功能一文件）。

| # | 功能简述 | 详细文档 |
|---|---|---|
| 1 | SEARCH/REPLACE 兼容中文全角/半角标点差异（仅 SEARCH 匹配；REPLACE 跟随 AI） | [.diff_docs/全角半角-SEARCH匹配兼容.md](.diff_docs/全角半角-SEARCH匹配兼容.md) |
| 2 | 废弃 `diff-fenced` / `patch`：独有 prompt 改为废弃提示（不改 `diff`） | [.diff_docs/废弃编辑格式-diff-fenced与patch.md](.diff_docs/废弃编辑格式-diff-fenced与patch.md) |
| 3 | `diff` prompt 追加 SEARCH 特别注意事项（全角/半角与空格须与原文一致） | [.diff_docs/diff-SEARCH特别注意事项prompt.md](.diff_docs/diff-SEARCH特别注意事项prompt.md) |
| 4 | `diff` 去掉 ONLY EVER 仅出块；要求块后中文回答与变更总结 | [.diff_docs/diff-回复须含中文总结.md](.diff_docs/diff-回复须含中文总结.md) |
| 5 | 固定显示版本为 `0.86.2`（不跟 setuptools_scm 的 `.dev` 浮动） | [.diff_docs/固定版本号0.86.2.md](.diff_docs/固定版本号0.86.2.md) |
| 6 | `detect-files`：提到文件加入对话改为路径点名 + 邻域 basename；开关不影响新建/未入对话编辑确认 | [.diff_docs/detect-files邻域匹配.md](.diff_docs/detect-files邻域匹配.md) |
