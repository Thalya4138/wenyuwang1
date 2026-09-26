# Python（通用编程语言）—算法—系统—人工智能：整合讲义

版本：2026-09-26 · 56 章 · 从第 0 章开始编号。

先建立能解释的程序，再理解算法、系统资源、学习与行动。英文术语在正文前十次出现附中文解释。配套代码、课程资源和资料处理边界随文提供。

可直接阅读 [合并版讲义](CS_Lecture_Complete.md)。解压后可按分卷阅读，并运行配套实验。

| 分卷 | 内容 |
|---|---|
| [基础与 Python](chapters/00_foundations.md) | 第 0—17 章：环境、语法、对象、可靠编程 |
| [算法与数据结构](chapters/01_algorithms.md) | 第 18—32 章：建模、证明、结构、搜索与优化 |
| [计算机系统](chapters/02_systems.md) | 第 33—38 章：表示、执行、内存、操作系统、网络、数据库与理论 |
| [数学与数值计算](chapters/03_mathematics.md) | 第 39—43 章：离散、线代、优化、概率与数组 |
| [机器学习与深度学习](chapters/04_learning.md) | 第 44—49 章：目标、评价、模型、梯度、视觉、序列与生成 |
| [语言、智能体与机器人](chapters/05_frontiers.md) | 第 50—55 章：大模型、工具、强化学习、世界模型与控制 |
| [练习与解释](06_exercises.md) | 16 道针对机制与反例的练习，以及实验入口 |
| [课程、论文和代码](07_resources.md) | 学习阶段、前置知识、获取途径与核验日期 |
| [资料映射与校正](08_source_map.md) | 原资料对应章节、版本区别、已校正问题与处理边界 |
| [英文术语速查](09_glossary.md) | 分卷跳读时补查 |
| [验证记录](10_validation.md) | 实际运行结果与未验证部分 |

## 配套实验

```bash
python labs/lab01_foundations.py
python labs/lab02_algorithms.py
python -m pip install numpy
python labs/lab03_learning.py
python labs/lab04_decision_control.py
python labs/lab05_retrieval_system.py
```

只有第三个实验需要 NumPy，其余只需 Python 标准库。正文以 Python 3.11 以上为基线，第三方库按自己的平台建立虚拟环境。全文讲义中的 PyTorch 示范未在本次环境实跑，已明确标注。

不需要按目录把所有内容预习完才开始动手。当前主线可以先读第 0—12 章，再做第一个小程序；算法随着课堂推进，数学与系统按需要并行。前沿章节可先抓问题，再沿前置知识回读。

此文件夹不包含原始教材、私人记忆或账户配置。之后可由你选择的工具将 Markdown 与实验代码推送到 GitHub。
