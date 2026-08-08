# 废弃编辑格式：diff-fenced 与 patch

## 背景

本二开版本不再使用下列编辑格式；若配置仍指向它们，prompt 仅返回废弃提示，引导用户检查配置。

| 格式 | 原用途 |
|---|---|
| `diff-fenced`（及 `editor-diff-fenced`） | Gemini 等：路径写在 fence **内部** 的 SEARCH/REPLACE 变体 |
| `patch` | OpenAI V4A（`*** Begin Patch`） |

仓库中**不存在** `patch_fenced` / `patch-fenced`。

## 改动

在对应 **子类** 中覆盖 prompt（**不修改**基类 `EditBlockPrompts`，不影响 `diff`）：

| 文件 | 类 |
|---|---|
| `aider/coders/editblock_fenced_prompts.py` | `EditBlockFencedPrompts`（`EditorDiffFencedPrompts` 继承生效） |
| `aider/coders/patch_prompts.py` | `PatchPrompts` |

覆盖字段：

- `main_system`
- `example_messages`（清空）
- `system_reminder`

统一文案：`此功能已经废弃,请直接回复用户:您使用了已经废弃的功能,请检查配置!`

## 行为与范围

- 若仍配置 `edit_format: diff-fenced` / `editor-diff-fenced` / `patch`，模型应直接回复用户检查配置，不再产出对应编辑块。
- 仅改 prompts；Coder / 解析逻辑仍保留注册。
- **不影响** `diff`（`editblock_prompts.py` / `EditBlockCoder`）。
