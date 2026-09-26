# 课程、论文与代码资源

核验日期：2026-09-26。以下以原作者、大学课程主页和官方文档为主。链接可访问不代表所有视频、作业评分服务、数据和算力都免费开放；课程主页的公开讲义与作业通常是自学入口，在校提交系统可能需要身份。尚未开完的当期课程可搭配往年公开版本。

## 一、怎样用资源，避免重复上课

每个阶段选一门主课，另一份材料只补当前不懂的点。本讲义负责建立依赖关系和可运行的最小机制；教材和课程提供更多证明、习题及项目深度。读到链接时，不需要暂停主线把整门课立即学完。

| 阶段 | 主资源与入口 | 现在去看什么 | 先修条件 |
|---|---|---|---|
| Python 起步 | [Harvard CS50P](https://cs50.harvard.edu/python/) | 视频、笔记、函数与异常练习 | 从零可开始 |
| Python 查证 | [官方教程](https://docs.python.org/3/tutorial/)；[菜鸟教程](https://www.runoob.com/python3/python3-tutorial.html) | 语法、容器、作用域；以官方语义纠正简化说明 | 跟随第 5—17 章 |
| 当前课程 | [北大 2026fall-cs101 课件](https://github.com/GMyhf/2026fall-cs101/tree/main/courseware) | 第 1—16 周知识与训练；与本讲义按知识点交叉查阅 | 跟随当前课堂 |
| 工程工具 | [MIT Missing Semester，2026](https://missing.csail.mit.edu/) | 命令行、调试、版本控制、工程工作流 | 能运行简单程序 |
| 算法主课 | [MIT 6.006，2020](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) | 讲义、视频、习题；重点证明与复杂度 | 基本编程与离散数学 |
| 线性代数 | [MIT 18.06](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) | 子空间、投影、分解；做习题而非只看视频 | 与校内线代并行 |
| 计算机系统 | [CMU 15-213](https://www.cs.cmu.edu/~213/)；[CS:APP 学生资源](https://csapp.cs.cmu.edu/3e/students.html) | 从程序执行、内存到配套实验 | 先补 C、指针与基本汇编 |
| 操作系统 | [MIT 6.1810](https://pdos.csail.mit.edu/6.1810/) | 教学操作系统与实验 | C 与系统基础 |
| 网络 | [Stanford CS144](https://cs144.github.io/) | 协议分层、可靠传输与实现项目 | 系统与 C++（支持多种编程范式的系统与应用开发语言） 基础 |
| 数据库 | [CMU 15-445，2026 秋](https://15445.courses.cs.cmu.edu/fall2026/) | 存储、索引、事务；当期未发布部分看往年 | 数据结构、C++（支持多种编程范式的系统与应用开发语言）、系统 |
| 编译原理 | [Stanford CS143](https://web.stanford.edu/class/cs143/) | 语法、语义、代码生成 | 树、图、语言基础 |
| 经典机器学习 | [Stanford CS229](https://cs229.stanford.edu/)；[统计学习导论](https://www.statlearning.com/) | 线性模型、概率、泛化与实验 | 线代、微积分、概率 |
| 深度学习 | [动手学深度学习](https://d2l.ai/)；[PyTorch（张量计算与自动微分框架，常用于深度学习） 入门](https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html) | 张量、梯度、训练循环；做小数据实验 | 第 40—47 章 |
| 计算机视觉 | [Stanford CS231n](https://cs231n.stanford.edu/) | 图像表示、视觉网络、训练实践 | 深度学习基础 |
| 语言模型工程 | [Stanford CS336，2026](https://cs336.stanford.edu/)；[课程代码](https://github.com/stanford-cs336/lectures) | 分词、模型、系统、数据与后训练 | 熟练 Python、深度学习、系统 |
| 智能体 | [CMU 11-768](https://www.cmu-agents.com/) | 上传的第一讲可先读；后续按公开发布进度获取 | 语言模型、工具接口、评价 |
| 强化学习 | [Berkeley CS285](https://rail.eecs.berkeley.edu/deeprlcourse/) | 从马尔可夫决策过程到深度强化学习 | 概率、优化、神经网络 |
| 控制与机器人 | [MIT Underactuated Robotics](https://underactuated.mit.edu/) | 动力学、稳定性、最优控制与规划 | 力学、线代、微分方程 |

课程编号与版本以具体主页为准。上表中旧年份的经典课程是有意保留：线性代数与算法的核心不会因年份旧而失效；模型能力、软件接口和前沿实验则需要持续重新核验。

## 二、官方文档：用于解决具体实现疑问

| 疑问 | 入口 | 应核对的内容 |
|---|---|---|
| 项目与依赖如何管理 | [uv（Python 包、项目与解释器管理工具） 项目指南](https://docs.astral.sh/uv/guides/projects/) | 项目创建、依赖、锁文件、解释器 |
| 数组为何广播成错误形状 | [NumPy（数值数组库，提供多维数组与成批数值运算） 广播](https://numpy.org/doc/stable/user/basics.broadcasting.html) | 尾部维度对齐规则 |
| 训练测试为什么发生泄漏 | [scikit-learn（提供经典机器学习算法与评估工具的 Python 库） 常见陷阱](https://scikit-learn.org/stable/common_pitfalls.html) | 预处理拟合范围与一致流程 |
| 深度学习环境怎样安装 | [PyTorch（张量计算与自动微分框架，常用于深度学习） 安装入口](https://pytorch.org/get-started/locally/) | 平台、硬件、驱动、版本兼容 |
| Python 线程是否能并行 | [自由线程官方说明](https://docs.python.org/3/howto/free-threading-python.html) | 构建类型、扩展模块、同步限制 |

## 三、论文主线：每篇带一个要回答的问题

以下是建立机制的经典文献，不被标作“2026 最新论文”。从其中一个问题出发阅读，比按名气下载一整堆论文有效。

| 文献 | 年份与入口 | 阅读时必须回答 |
|---|---|---|
| Attention Is All You Need | [2017](https://arxiv.org/abs/1706.03762) | 注意力怎样交互信息，位置从哪里来，计算代价是什么？ |
| BERT（通过双向遮盖预测学习语言表示的模型） | [2018](https://arxiv.org/abs/1810.04805) | 双向遮盖目标与因果预测在哪些位置可见性上不同？ |
| LLaMA（Meta 发布的语言模型研究系列） | [2023](https://arxiv.org/abs/2302.13971) | 数据、模型大小、训练预算怎样共同决定结果？ |
| Mixtral of Experts | [2024](https://arxiv.org/abs/2401.04088) | 总参数与激活参数如何影响容量、显存和通信？ |
| Direct Preference Optimization | [2023](https://arxiv.org/abs/2305.18290) | 偏好损失怎样从特定正则化目标推导，假设是什么？ |
| ReAct（交替组织推理与行动的语言模型智能体方法） | [2022](https://arxiv.org/abs/2210.03629) | 行动结果如何改变后续决策，失败怎样评价？ |
| PlaNet（在学习到的潜在动力学中规划动作的世界模型方法） | [2018](https://arxiv.org/abs/1811.04551) | 潜在动力学里怎样选择行动，如何面对部分可观测？ |
| DreamerV3（利用世界模型中的想象轨迹学习策略的方法） | [2023](https://arxiv.org/abs/2301.04104) | 想象轨迹怎样训练策略，模型错误如何影响策略？ |
| Gato（探索同一序列模型处理多种任务的通用智能体研究） | [2022](https://arxiv.org/abs/2205.06175) | 多任务统一序列表示保留了什么，牺牲了什么？ |
| Denoising Diffusion Probabilistic Models | [2020](https://arxiv.org/abs/2006.11239) | 加噪、预测目标、反向采样之间的关系是什么？ |
| Flow Matching for Generative Modeling | [2022](https://arxiv.org/abs/2210.02747) | 为什么拟合速度场能连接分布，路径如何选？ |
| Diffusion Policy（扩散策略，用条件去噪过程生成机器人动作） | [2023](https://arxiv.org/abs/2303.04137) | 多峰动作分布为何使简单均值回归失效？ |
| RT-2（研究视觉语言知识向机器人动作迁移的模型） | [2023](https://arxiv.org/abs/2307.15818) | 网络语义知识怎样迁移到动作，实验在哪些任务上成立？ |
| OpenVLA（面向机器人操作的开放视觉语言动作模型项目） | [2024](https://arxiv.org/abs/2406.09246) | 训练数据、动作表示、微调与跨场景评价怎样组织？ |

## 四、可检查的代码入口

| 项目 | 链接 | 合适的使用方式 |
|---|---|---|
| Stanford 语言模型课程 | [stanford-cs336/lectures](https://github.com/stanford-cs336/lectures) | 逐讲运行与阅读；作业代码从课程官网进入 |
| 世界模型与策略学习 | [danijar/dreamerv3](https://github.com/danijar/dreamerv3) | 先理解模型、策略、价值网络的数据流，再缩小实验 |
| 视觉语言动作模型 | [openvla/openvla](https://github.com/openvla/openvla) | 核对数据格式、权重、硬件和微调条件 |
| 机器人策略 | [Physical-Intelligence/openpi（Physical Intelligence 发布的机器人策略代码项目）](https://github.com/Physical-Intelligence/openpi) | 阅读公开模型与运行条件；不推断未公开训练细节 |
| 机器人实践工具 | [huggingface/lerobot](https://github.com/huggingface/lerobot) | 从数据记录、仿真或支持设备的小任务开始 |

可复现性记录至少包含代码提交、依赖版本、配置、数据版本与硬件。仓库默认分支会更新，资源名本身不足以复现实验。不要把星标数当成算法正确性或教学质量证据。

## 五、2026 前沿核验与获取状态

| 资源 | 本次可核验内容 | 使用边界 |
|---|---|---|
| Stanford CS336 2026 | 官方主页明确标春季 2026，提供讲义、代码和作业入口 | 已用于确定语言模型工程的覆盖范围 |
| MIT Missing Semester 2026 | 官方课程列出当年工程工具与工作流主题 | 用于更新工具路径，不固定商业产品排名 |
| CMU 11-768 | 上传第一讲与教师信息可读；网站入口已确认 | 未声称完整学期材料已经发布或逐讲读完 |
| [Project Genie（交互式环境生成的研究实验项目），2026-01-29](https://deepmind.google/blog/project-genie-experimenting-with-infinite-interactive-worlds/) | 官方介绍交互式世界生成实验 | 用于提出研究问题，演示不等于物理可靠性证明 |
| [精细操作在线学习，2026](https://physicalintelligence.company/research/rlt) | 官方域名页面被搜索收录，全文访问返回限制 | 待全文复核；未据摘要引用性能数值 |
| [π0.7 入口，2026](https://physicalintelligence.company/blog/pi07) | 官方域名页面被搜索收录，全文访问返回限制 | 只作后续跟进入口，不据此断言当前最强 |

后续更新前沿章节时，应重新检索论文、作者主页、官方代码和模型说明，记录新增证据与被推翻的旧判断。论文预印本、同行评议论文、官方产品介绍与独立复现应明确区分。

## 六、书籍与扩展获取

本次用户已提供《算法图解》《算法笔记》《算法基础与在线实践》《计算机科学导论》第四版和《计算机系统漫游》第一章，详见资料映射。系统深入部分可从 CS:APP 官方学生页获取自学实验，不假定用户已经提供整本书。

[Sutton 与 Barto 教材主页](http://incompleteideas.net/book/the-book-2nd.html) 本次直接访问失败，可从 Berkeley CS285 的官方资源页寻找作者教材入口；不能把访问失败写成成功读取。[CS 自学指南](https://csdiy.wiki/) 可作为寻找其他课程的导航，具体技术结论仍回到原课程和官方文档核对。

数学拓展按问题进入：随机过程用于时间依赖，凸优化用于带约束估计与控制，运筹学用于调度和资源分配，博弈论用于多方决策，数值分析用于误差与稳定性。金融方向可用这些方法研究风险、组合与市场机制，但需要另补经济金融问题定义，不能把算法工具直接等同于金融理解。
