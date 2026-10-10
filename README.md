# wenyuwang1

个人 Python 学习仓库：整合讲义、OJ 练习与配套实验代码。

本仓库起步于一次 Git 练习（最初的 README 标题就是「Git Test Project」），当时只是验证本地目录如何初始化为仓库并推送到 GitHub。此后陆续装进了完整的计算机科学讲义、课堂原件和一批练习程序。

> 仓库地址：<https://github.com/Thalya4138/wenyuwang1>

## 内容结构

| 目录 | 内容 | 规模 |
|---|---|---|
| [`note_maintained_by_myself/`](note_maintained_by_myself/) | Python 知识点笔记（按覆盖表写、可验收） | 16 个文件 |
| [`Practice/`](Practice/) | Python / OJ 练习程序 | 21 个文件 |
| [`Resources from class/`](<Resources from class/>) | 课堂讲义原件（Jupyter notebook 与 `.py`），按课次加前缀 | 15 个文件 |

## `cs_lecture/` — 已移除

整合讲义（56 章 + 5 个配套实验）已于 2026-10-08 移除，见提交 `121cf58`「重构笔记目录，接入 C++ 笔记工程」。

内容仍在 git 历史里，可以取回：

```bash
git show 121cf58^:cs_lecture/CS_Lecture_Complete.md          # 合并版单文件
git checkout 121cf58^ -- cs_lecture/                          # 整个目录
```

## `note_maintained_by_myself/` — 我自己维护的知识点笔记

这个目录下是**两套独立、各自可验收**的笔记。入口见 [`note_maintained_by_myself/README.md`](note_maintained_by_myself/README.md)。

### Python 知识点笔记

一套**按覆盖表写、可验收**的 Python 知识点汇总，从环境配置讲到并发与网络，外加一份标准库索引。

- **覆盖表** — [`00_知识点总览.md`](note_maintained_by_myself/Python笔记本/00_知识点总览.md)：80 个条目，每条标注对应官方/runoob 章节、计划文件、展开程度与状态
- **三源交叉核对** — [`01a_三源交叉核对.md`](note_maintained_by_myself/Python笔记本/01a_三源交叉核对.md)：用官方 Tutorial / Language Reference / Module Index 三份目录逐条核对，列出仍缺的条目
- **正文 13 章** — [`Python笔记本/01_入门与环境.md`](note_maintained_by_myself/Python笔记本/01_入门与环境.md) ～ `12_并发与网络.md`，加 `99_标准库索引.md`
- **维护规矩** — [`_写作规范.md`](note_maintained_by_myself/Python笔记本/_写作规范.md)：每个代码块必须实跑并贴真实输出，章末必须有覆盖对账表与「诚实标注」
- **课堂主题随笔** — [`进制转换与信息编码、存储`](note_maintained_by_myself/随笔维护的笔记本/进制转换与信息编码、存储.md)：整合 Theory 2 的数制、位运算、数值与字符编码、声音／图像／视频数据量，附执行表、教学图与课件页码对照。

### C++ 入门讲义（进行中）

规格与上面那套对齐，但验证方式完全不同：**靠真正的编译器**（MSVC），不是解释器。基线 **C++17**。

- **覆盖表** — [`C++笔记本/00_知识点总览.md`](note_maintained_by_myself/C++笔记本/00_知识点总览.md)：14 章骨架，按「工具链→类型→表达式→控制流→函数→内存→类→错误→库→模板→资源→进阶」这条**认知依赖链**排章
- **三源交叉核对** — [`01a_三源交叉核对.md`](note_maintained_by_myself/C++笔记本/01a_三源交叉核对.md)：用 C++ 工作草案 / cppreference / Core Guidelines 核对，并**纠正了一处**把 C++11 基线误当 C++17 新特性的分类错误
- **正文** — 目前只有 [`01_从源代码到运行.md`](note_maintained_by_myself/C++笔记本/01_从源代码到运行.md)：从源文件到可执行文件的完整链条、编译开关、诊断怎么读、Windows 特有的坑
- **多 agent 协作规范** — [`_协作规范.md`](note_maintained_by_myself/C++笔记本/_协作规范.md)：Codex 在沙箱外写、本会话编译验收的文件交接协议
- **维护规矩** — [`_写作规范.md`](note_maintained_by_myself/C++笔记本/_写作规范.md) 与 [`_维护须知.md`](note_maintained_by_myself/C++笔记本/_维护须知.md)

> ⚠️ **两套笔记的执行手册不可互相套用**：C++ 侧要先跑 `vcvars64.bat`、
> 编译必须加 `/utf-8`（否则含中文的源文件直接编译失败），验证靠编译运行而非解释执行。

五份规范文件分工不同，别混着看：

| 规矩 | 管什么 | 位置 |
|---|---|---|
| 整理规范 | **知识本身怎么分层组织**：同级标题同一分类轴、共性/差异/入口/机制分层、章末知识结构回收 | [`笔记与讲义整理规范.md`](笔记与讲义整理规范.md) |
| 写作规范（Python） | **Python 笔记自己怎么验收**：自己话写、实跑、对账、诚实标注 | [`Python笔记本/_写作规范.md`](note_maintained_by_myself/Python笔记本/_写作规范.md) |
| 写作规范（C++） | **C++ 讲义自己怎么验收**：代码块标记约定、锚点机检、`◐`/`☑` 口径 | [`C++笔记本/_写作规范.md`](note_maintained_by_myself/C++笔记本/_写作规范.md) |
| 颜色语义 | 行文中的颜色含义（黑=正文 / 红=坑 / 蓝=定义 / 绿=例子） | [`语义颜色使用规范.md`](语义颜色使用规范.md) |
| AI 维护须知 | **一个 agent 具体怎么干活**：红线、验证命令与真实基线、已知陷阱、汇报格式 | Python 侧 [`_AI维护须知.md`](note_maintained_by_myself/_AI维护须知.md)；C++ 侧 [`_维护须知.md`](note_maintained_by_myself/C++笔记本/_维护须知.md) |
| 工作区指令 | 给 AI 的入口：整理学习材料前先读第一、二份 | [`AGENTS.md`](AGENTS.md) |

三条边界写在这里，是为了不让人误以为它什么都包：

| 层 | 做法 |
|---|---|
| 核心语法 | 逐条展开 |
| 常用标准库 | **索引级完整**（全列出 + 一句话 + 官方链接），不展开教程 |
| 生态 / 进阶（框架、数据科学、爬虫、GUI、部署） | **明确不展开**，并写明原因 |

不逐字复制任何教程正文：知识点与结构可以照着讲，正文与示例都是自己写的。

## `Practice/` — 练习程序

单文件小程序的集合，多为 OJ 题解，覆盖输入输出、条件分支、循环、集合与位运算等基础训练。

- **题解类** — `Theatre Square.py`、`Beautiful Matrix.py`、`Petya and Strings.py`、`Police Recruits.py`、`Team.py`、`domino.py`、`校门外的树.py`、`高低位交换.py`、`特殊数之和.py`、`鸡兔同笼.py`、`整除问题.py`、`判断闰年.py`、`画矩形.py`、`阶乘求和.py`、`只出现一次的数字.py`、`Ride to school.py`
- **turtle 绘图** — `测试turtle.py`、`turtle警告.py`
- **入门讲解** — `一道题搞懂输入.py`、`一道题搞懂输出.py`
- **空壳入口** — `main.py`（`uv init` 生成，输出一行问候语）

## `Resources from class/` — 课堂原件

课堂分发的原始材料，内容未做重写。

文件名统一加 `第0N课-` 前缀，让排序按课次而不是按原编号走（原来第二周的 `1-` 与第三周的 `1-` 会混在一起）。
`第0N课` 对应课件里的「第 N 周」；课次**补零到两位**，这样 `第10课` 会排在 `第09课` 之后，而不是 `第02课` 之前。
课内序号（`-1-`、`-2-`）暂不补零——目前每课不超过 6 个文件；某课超过 9 个时再一起补。

**第02课**（Jupyter notebook 5 个 + 脚本 1 个）

- `第02课-1-类型和算术表达式.ipynb`
- `第02课-2-内置函数和数学函数.ipynb`
- `第02课-3-关键字和变量的赋值.ipynb`
- `第02课-4-字符串.ipynb`
- `第02课-5-表 (初步).ipynb`
- `第02课-6-input.py`

**第03课**

- `第03课-1-逻辑判断和 if 语句.py`
- `第03课-2-循环语句.py`
- `第03课-3-自定义函数.py`
- `第03课-4-其它机制.py`
- `第03课-5-turtle star.ipynb`

**第04课**（不在课件「本讲内容」清单里，按来源归在此）

- `第04课-1-coding-1.py`
- `第04课-2-coding-2.py`
- `第04课-2.3-Python入门实战程序.py`
- `第04课-3-cbrt.py`

notebook 中保留了执行输出，便于对照课堂结果。
第一周的课件是 PDF，不在本目录（仅在 WPS 云盘）。

## 环境与依赖

仓库用 [uv](https://docs.astral.sh/uv/) 管理环境，见 [`pyproject.toml`](pyproject.toml) 与 [`uv.lock`](uv.lock)。

```bash
uv sync                          # 按 uv.lock 建环境（Python 3.14）
uv run python Practice/main.py
uv run ruff check .              # 代码风格检查
```

| 项 | 值 |
|---|---|
| Python | 3.14（[`.python-version`](.python-version)） |
| 运行时依赖 | `ipykernel`、`numpy` |
| 开发依赖 | `ruff` |

讲义正文以 Python 3.11 以上为基线。

## 仓库约定

- 不包含教材原件、私人记忆或账户配置，也不提交任何密钥或令牌。
- 下列内容由 [`.gitignore`](.gitignore) 排除，不入库：`.venv/`、`.idea/`、`.ruff_cache/`、`__pycache__/`、`git.worktrees/`。
- `git.worktrees/` 是本地嵌套的 git worktree 目录。它曾被误记为 gitlink（无 `.gitmodules` 的「幽灵子模块」，在 GitHub 上渲染为死链），现已从索引移除并加入忽略规则。
