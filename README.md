# wenyuwang1

个人 Python 学习仓库：整合讲义、OJ 练习与配套实验代码。

本仓库起步于一次 Git 练习（最初的 README 标题就是「Git Test Project」），当时只是验证本地目录如何初始化为仓库并推送到 GitHub。此后陆续装进了完整的计算机科学讲义、课堂原件和一批练习程序。

> 仓库地址：<https://github.com/Thalya4138/wenyuwang1>

## 内容结构

| 目录 | 内容 | 规模 |
|---|---|---|
| [`cs_lecture/`](cs_lecture/) | 整合讲义（56 章）+ 5 个配套实验 | 19 个文件 |
| [`note_maintained_by_myself/`](note_maintained_by_myself/) | Python 知识点笔记（按覆盖表写、可验收） | 16 个文件 |
| [`Practice/`](Practice/) | Python / OJ 练习程序 | 21 个文件 |
| [`Resources from class/`](<Resources from class/>) | 课堂讲义原件（Jupyter notebook 与 `.py`） | 12 个文件 |

## `cs_lecture/` — 整合讲义

版本 2026-09-26，从第 0 章编号至第 55 章，共 56 章。主线是「先建立能解释的程序，再理解算法、系统资源、学习与行动」。

- **[合并版单文件](cs_lecture/CS_Lecture_Complete.md)** — 适合通读或全文检索
- **分卷阅读** — 按主题拆分，见下表

| 分卷 | 章节 | 主题 |
|---|---|---|
| [基础与 Python](cs_lecture/chapters/00_foundations.md) | 0—17 | 环境、语法、对象、可靠编程 |
| [算法与数据结构](cs_lecture/chapters/01_algorithms.md) | 18—32 | 建模、证明、结构、搜索与优化 |
| [计算机系统](cs_lecture/chapters/02_systems.md) | 33—38 | 表示、执行、内存、操作系统、网络、数据库与理论 |
| [数学与数值计算](cs_lecture/chapters/03_mathematics.md) | 39—43 | 离散、线代、优化、概率与数组 |
| [机器学习与深度学习](cs_lecture/chapters/04_learning.md) | 44—49 | 目标、评价、模型、梯度、视觉、序列与生成 |
| [语言、智能体与机器人](cs_lecture/chapters/05_frontiers.md) | 50—55 | 大模型、工具、强化学习、世界模型与控制 |
| [练习与解释](cs_lecture/chapters/06_exercises.md) | — | 16 道针对机制与反例的练习，附实验入口 |
| [课程、论文和代码](cs_lecture/chapters/07_resources.md) | — | 学习阶段、前置知识与获取途径 |
| [资料映射与校正](cs_lecture/chapters/08_source_map.md) | — | 原资料对应章节、版本区别与处理边界 |
| [英文术语速查](cs_lecture/chapters/09_glossary.md) | — | 分卷跳读时补查 |
| [验证记录](cs_lecture/chapters/10_validation.md) | — | 实际运行结果与未验证部分 |

讲义自身的说明见 [`cs_lecture/README.md`](cs_lecture/README.md)。

### 配套实验

```bash
python cs_lecture/labs/lab01_foundations.py
python cs_lecture/labs/lab02_algorithms.py
python cs_lecture/labs/lab03_learning.py      # 唯一需要 NumPy
python cs_lecture/labs/lab04_decision_control.py
python cs_lecture/labs/lab05_retrieval_system.py
```

只依赖 Python 标准库（`lab03` 除外，需要 `numpy`，见 [`cs_lecture/requirements.txt`](cs_lecture/requirements.txt)）。讲义中的 PyTorch 示范未在本机实跑，原文已明确标注。

## `note_maintained_by_myself/` — Python 知识点笔记

一套**按覆盖表写、可验收**的 Python 知识点汇总，从环境配置讲到并发与网络，外加一份标准库索引。入口见 [`note_maintained_by_myself/README.md`](note_maintained_by_myself/README.md)。

- **覆盖表** — [`00_知识点总览.md`](note_maintained_by_myself/笔记本/00_知识点总览.md)：80 个条目，每条标注对应官方/runoob 章节、计划文件、展开程度与状态
- **三源交叉核对** — [`01a_三源交叉核对.md`](note_maintained_by_myself/笔记本/01a_三源交叉核对.md)：用官方 Tutorial / Language Reference / Module Index 三份目录逐条核对，列出仍缺的条目
- **正文 13 章** — `笔记本/01_入门与环境.md` ～ `12_并发与网络.md`，加 `99_标准库索引.md`
- **维护规矩** — [`_写作规范.md`](note_maintained_by_myself/笔记本/_写作规范.md)：每个代码块必须实跑并贴真实输出，章末必须有覆盖对账表与「诚实标注」
- **课堂主题随笔** — [`进制转换与信息编码、存储`](note_maintained_by_myself/随笔维护的笔记本/进制转换.md)：整合 Theory 2 的数制、位运算、数值与字符编码、声音／图像／视频数据量，附执行表、教学图与课件页码对照。

五份规范文件分工不同，别混着看：

| 规矩 | 管什么 | 位置 |
|---|---|---|
| 写作规范 | **这份笔记自己怎么验收**：自己话写、实跑、对账、诚实标注 | [`_写作规范.md`](note_maintained_by_myself/笔记本/_写作规范.md) |
| 整理规范 | **知识本身怎么分层组织**：同级标题同一分类轴、共性/差异/入口/机制分层、章末知识结构回收 | [`笔记与讲义整理规范.md`](笔记与讲义整理规范.md) |
| 颜色语义 | 行文中的颜色含义（黑=正文 / 红=坑 / 蓝=定义 / 绿=例子） | [`语义颜色使用规范.md`](语义颜色使用规范.md) |
| AI 维护须知 | **一个 agent 具体怎么干活**：红线、验证命令与真实基线、已知陷阱、汇报格式 | [`_AI维护须知.md`](note_maintained_by_myself/_AI维护须知.md) |
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

课堂分发的原始材料，保留原名与编号顺序，未做重写。

- **Jupyter notebook（6 个）** — 类型和算术表达式、内置函数和数学函数、关键字和变量的赋值、字符串、表（初步）、turtle star
- **Python 脚本（6 个）** — 逻辑判断和 if 语句、循环语句、自定义函数、其它机制、Python 入门实战程序、`6-input.py`

notebook 中保留了执行输出，便于对照课堂结果。

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

讲义正文以 Python 3.11 以上为基线；`cs_lecture/` 也可脱离 uv 单独运行，只需自备 `numpy`。

## 仓库约定

- 不包含教材原件、私人记忆或账户配置，也不提交任何密钥或令牌。
- 下列内容由 [`.gitignore`](.gitignore) 排除，不入库：`.venv/`、`.idea/`、`.ruff_cache/`、`__pycache__/`、`git.worktrees/`。
- `git.worktrees/` 是本地嵌套的 git worktree 目录。它曾被误记为 gitlink（无 `.gitmodules` 的「幽灵子模块」，在 GitHub 上渲染为死链），现已从索引移除并加入忽略规则。
