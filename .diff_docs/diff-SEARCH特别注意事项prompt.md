# diff prompt：SEARCH 特别注意事项

## 背景

中文等非 ASCII 场景下，模型常把 SEARCH 中的全角标点改成半角、或改动空格数量，导致精确匹配失败。除匹配侧兼容外，在 prompt 侧加强提醒。

## 改动

- 文件：`aider/coders/editblock_prompts.py`（`diff` / `EditBlockPrompts.system_reminder`）
- 在「新建文件：`REPLACE` section」说明之后、`{rename_with_shell}` 之前，追加中文优先的 `# 特别注意事项` 段落，强调：
  - 禁止对 SEARCH「自动纠正」原文
  - 全角/半角标点、空格数量与种类（含 Tab）须与原文一致
  - 附简短中文示例；不与上文 EXACTLY MATCH 总则长篇重复

## 范围

- 仅 `diff` 的 `system_reminder`；`editor-diff` 继承同一 `system_reminder`，一并生效。
- 未改已废弃的 `diff-fenced` / `patch` prompts。
