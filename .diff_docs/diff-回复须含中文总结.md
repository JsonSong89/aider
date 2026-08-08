# diff prompt：编辑块后须中文说明/总结

## 背景

原句 `ONLY EVER RETURN CODE IN A *SEARCH/REPLACE BLOCK*!` 语气过强，部分模型（如 GPT）会整段只输出 SEARCH/REPLACE，不再解释或总结。

## 改动

- `aider/coders/editblock_prompts.py`
  - 新增共享文案 `edit_reply_format`：可编辑源码必须在 SEARCH/REPLACE 内；块前可有短计划；**块后须中文回答（如有）+ 简要变更总结**
  - `main_system`：步骤改为含「块后中文总结」；去掉 ONLY EVER…
  - `system_reminder`：末尾改用 `edit_reply_format`
  - `example_messages`：两个示例在块后各加一句中文总结
- `aider/coders/editor_editblock_prompts.py`：`main_system` 同步使用 `edit_reply_format`

## 范围

- 影响 `diff` 与继承其 `system_reminder` 的 `editor-diff`
- 不改已废弃的 `diff-fenced` / `patch`
