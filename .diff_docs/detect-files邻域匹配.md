# detect-files：提到文件再加入对话

## 背景

官方 code 模式会扫描用户输入和模型回复里的文件名，弹 `Add file to the chat?`。候选集是全部 git tracked 文件，basename（如 `package.json`）只要全仓唯一就会触发。`map-tokens: 0` 只关掉仓库地图，不关掉这条扫描。

二开希望：只把高概率和当前代码有关的文件加入对话；并提供总开关。开关不得影响「新建文件」或「编辑尚未加入对话的文件」的确认。

## 改动位置

| 文件 | 作用 |
|---|---|
| `aider/args.py` | `--detect-files` / `--no-detect-files`，默认 True |
| `aider/main.py` | 把 `args.detect_files` 传给 Coder |
| `aider/coders/base_coder.py` | `check_for_file_mentions` 受开关控制；`related_only` 两层匹配与邻域 |
| `tests/basic/test_coder.py` | 邻域、tag 连接、开关不影响新建确认 |
| `tests/basic/test_main.py` | CLI 默认 / 开关 |
| `aider/website/docs/config/*`、`sample.aider.conf.yml` | 配置文档与样例 |

## 行为

`detect-files: false` / `--no-detect-files`：整段 mention 入对话扫描跳过。`Create new file?`、`Allow edits to file that has not been added to the chat?` 仍会问。

`detect-files: true`（默认）时，`check_for_file_mentions` 走 `get_file_mentions(..., related_only=True)`：

1. **高精度**：文本里出现带目录的完整相对路径（如 `src/foo/bar.ts`）→ 可加入。
2. **低精度**：只有 `package.json`、`utils.py` 这种 basename（含仓库根文件）→ 必须落在邻域：
   - 种子：已在 chat / read-only 的文件
   - 同目录，或一层父/子目录
   - 种子 tags 的 `ref`/`def` 能连上的文件（只解析种子和本次命中的少数文件，不扫全仓、不跑 PageRank）
3. chat 为空时，basename 不弹。

`get_file_mentions` 的默认调用（repo map 加权、context 模式 `ignore_current=True`）仍是官方的全仓 basename 匹配，不受邻域过滤。

## 配置

```yaml
# .aider.conf.yml
detect-files: true
```

`--no-detect-files` 或 `AIDER_DETECT_FILES=false` 可关。

## 注意

- 跨两层以上目录的真实需求，模型必须写出完整相对路径才会弹。
- 配置文件等抽不出 tree-sitter tag 的，只靠目录邻域。
- 关 `map-tokens` 不影响本功能；tags 在没有 RepoMap 时会懒创建只读 tags 缓存实例。
