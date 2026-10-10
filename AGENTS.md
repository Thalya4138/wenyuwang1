# 工作区指令（AGENTS.md）

本仓库是个人 Python / CS 学习仓库：整合讲义（`cs_lecture/`）、知识点笔记（`note_maintained_by_myself/`）、课堂原件（`Resources from class/`）与练习（`Practice/`）。全貌见 [`README.md`](README.md)，资料源索引见 [`仓库索引.md`](仓库索引.md)。

---

## 一、笔记与讲义整理入口

涉及学习材料整理或系统答疑，先读正式源 [`笔记与讲义整理规范.md`](笔记与讲义整理规范.md)。
通用规则只在此修订，再同步到 `.dsh`；复述 Prompt 时完整返回其第 11 节。
课程底稿先保真；自主讲义自己写。标题同层同轴、先关系后概念、先具体过程后抽象规则。
来源身份和事实正确性分开，实测与历史记录分开，随笔不套正式章模板。

- Python 正式章节：[`执行手册`](note_maintained_by_myself/_AI维护须知.md) + [`写作验收`](note_maintained_by_myself/Python笔记本/_写作规范.md)。
- C++：[`专项入口`](note_maintained_by_myself/C++笔记本/AGENTS.md)，先核对运行状态与本轮任务。
- 共用历史：[`_HANDOFF.md`](note_maintained_by_myself/_HANDOFF.md)；旧记录需核对，不作为当前基线。
- 排版：[`语义颜色使用规范.md`](语义颜色使用规范.md)。

---

## 二、本仓库的既有约定

- 不提交教材原件、私人记忆、密钥令牌；`.gitignore` 已排除 `.venv/`、`.idea/`、`.ruff_cache/`、`git.worktrees/`、`2026fall-cs101yan/`。
- 验证环境：Windows 11，系统 `python` = 3.13.15，仓库 `.venv` = 3.14.7（`uv` 管理）。涉及版本差异的说法必须标明用的是哪一个。
- 代码风格用 `uv run ruff check .`；讲义正文以 Python 3.11+ 为基线。
- 改动笔记内容后，同步更新受影响的索引：根 [`README.md`](README.md)、[`仓库索引.md`](仓库索引.md)、以及笔记目录的 [`README.md`](note_maintained_by_myself/README.md) 与覆盖表。
- 文件路径含空格时（如 `Resources from class/`）在 Markdown 链接里写尖括号：`[标题](<Resources from class/>)`。

---

## 三、从 GitHub 更新资料前，先选择同步模式

每次用户要求从 GitHub 拉取、同步或更新仓库/资料时，先确认目标仓库、分支、更新源与本地改动，再让用户选择以下模式；本次请求已明确模式时无需重复询问。未选择前可以 fetch 和查看差异，但不改工作区文件。

1. **保留模式（推荐）**：接收上游新增和更新，保留本地修改与本地新增文件。工作区干净且可快进时用 `git merge --ff-only`；有本地改动时先做可恢复备份，再合并。双方修改重叠、上游删除本地修改过的文件或出现同名新增文件时，不静默覆盖本地内容；保留双方版本，说明冲突，必要时让用户决定。
2. **覆盖模式**：先备份本地提交、未提交修改与新增文件，再让本地已跟踪文件与选定上游版本一致；明确告知哪些本地修改会被替换。删除未跟踪/被忽略文件或清空目录需要另行明确授权，不能把选择覆盖模式视为允许删除整个目录。

完成后核对本地 HEAD、上游提交和工作区状态，报告新增/更新内容以及本地改动的保留或备份位置。拉取到本地与推送到个人 fork 是两件事，按用户请求的范围执行并分别汇报。

课程仓库 `2026fall-cs101yan/` 默认更新源为老师的 `upstream/main`（`GMyhf/2026fall-cs101`）；操作记录见 [`2026fall-cs101-使用说明.md`](2026fall-cs101-使用说明.md)。
