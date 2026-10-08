# C++ 入门讲义项目 · GitHub 资源调研报告

> 面向：北大工学院 2026 级本科生（力学强基），编程实现层面初学者、思维层面可讨论抽象概念；长期方向具身智能 / 机器人 / AI（软:硬 ≈ 7:3）。已有约 2.75 万行自维护中文 Python 笔记，现要建一份同规格、**完整可验证**的 C++17 基线讲义（核心语言逐条覆盖、标准库索引级完整、生态/进阶明确划界），环境为 Windows 11 + MSVC 14.51 + Windows SDK 10.0.26100，需要能用于判题机的写法。
>
> **本文所有 star 数、最后推送时间、许可证均通过 GitHub REST API 实时查询所得**（查询时间：检索会话当时），非记忆值。凡未能核实的项目一律标注「未核实」，不猜测。检索工具为 `web_search` / `web_fetch`，仅能访问 GitHub API 与公开网页，无法 `git clone` 或运行联网命令。

---

## 0. 先说结论：资源如何映射到讲义设计

这份讲义的目标不是「像某本书」，而是**结构闭合**。对应到资源，四层各有明确归属：

| 讲义层 | 需要的资源类型 | 本报告对应类别 |
|---|---|---|
| 核心语言逐条覆盖（100%） | 权威标准文本 + 语言特性清单 | 第 2 类（cppreference / 标准草案）+ 第 3 类（特性清单） |
| 标准库索引级完整 | 按头文件 / 按设施组织的参考 | 第 2 类（cppreference 索引） |
| 算法与判题机写法 | 可跑的模板库 + 题解库 | 第 4 类 + 第 5 类 |
| 结构参考（不逐字复制） | 中文社区笔记的**目录** | 第 6 类 |

**一句话原则**：第 2 类决定「完整性」，第 3、4 类决定「现代写法与判题可用性」，第 6 类只用于**对账**（核对知识点有没有漏），绝不进入正文。

---

## 1. C++ 入门 / 系统学习类

| 仓库 | 全名 | 用途一句话 | 适合度 | 许可 | 备注 |
|---|---|---|---|---|---|
| C++那些事 | `Light-City/CPlusPlusThings` | 中文 C++ 学习闭环：语言特性 + STL 实现剖析 + 并发，配套在线阅读站 | **高**：中文，章节粒度细，正好覆盖「语言→STL→并发」三段，结构可直接当参照系 | ⚠️ **API 返回无许可（license: null）** | 43,508 star / 8,795 fork；最后推送 **2026-05-16**（活跃）；43k 级中文 C++ 第一大仓。**无许可 = 未授权再分发**，只可作为「知识点有没有漏」的对照，绝不能搬正文 |
| Modern C++ Tutorial | `changkun/modern-cpp-tutorial` | 《现代 C++ 教程》：C++11 → C++26 特性逐个讲，中英双语、在线可读 | **高**：这是「C with Classes → 现代 C++」迁移的最佳单点资源，且逐版本组织，天然对应你「C++17 基线 / C++20-23 标进阶」的划分 | ✅ **MIT**（可放心引用代码片段，注意署名） | 25,874 star / 3,121 fork；最后推送 **2026-06-21**（活跃）；topics 明确含 `cpp20`、`modern-cpp` |
| C++ 新特性资料合集 | `0voice/cpp_new_features` | C++11/14/17/20/23 新特性 + 入门教程 + 书单 + 视频的**索引型**汇总 | 中：适合当「选读书目和外部链接的索引」，不是教程正文 | ⚠️ **无许可（license: null）** | 6,430 star / 1,256 fork；最后推送 **2025-06-18**（半活跃，2021 年建的合集，更新渐缓） |
| C++ 中文学习笔记 | `forhappy/CPlusPlus-Learnnote` | 中文 C++ 学习笔记 | 未核实 | 未核实 | ⚠️ **本次检索未通过 GitHub API 核实该仓库存在与元数据**（搜索中出现，但 `repo:` 精确查询未返回）。使用前请自行打开确认 |
| C/C++ 学习进阶指南 | `xiebaoma/xbm-CppGuide` | C/C++ 学习 + 后端开发进阶路线 | 未核实 | 未核实 | ⚠️ 同上，仅搜索结果中出现，未核实 star / 活跃度 / 许可 |
| 中文 C++ 学习资料 | `0voice/cpp_learning` | C++ 学习资料合集 | 未核实 | 未核实 | ⚠️ `repo:` 精确查询未返回（疑似已删除或改名），**不建议依赖** |

**给这个用户的具体建议**：这一类的价值是**目录对照**，不是内容。CPlusPlusThings 的目录（语言基础 / 类与对象 / STL 容器与算法 / 并发 / 实现剖析）可以作为「讲义第一部该有哪些章」的 check list；真正的语言权威解释请走第 2 类。

---

## 2. C++ 权威参考 / 标准相关

| 仓库 | 全名 | 用途一句话 | 适合度 | 许可 | 备注 |
|---|---|---|---|---|---|
| cppreference 离线版（英文） | `0mega3/cppreference-doc` | cppreference.com 的离线纯 HTML 归档 | 中高：**离线可检索**是这个用户真正需要的（Windows 本地、断网也能查标准库签名） | ✅ **CC-BY-SA-4.0**（与 cppreference 上游许可一致） | 仅 1 star，仓库很新（2026-04-25 创建）；但**价值不在 star 而在内容正确性**——它是上游内容的镜像。CC-BY-SA 是**传染性**许可：引用其文本必须同样以 CC-BY-SA 发布并署名，讲义若用 MIT 之类则**不可混用其文字** |
| cppreference 中文镜像 | `Jisu-Woniu/cppreference-zh-mirror` | 基于离线归档的 zh.cppreference.com 镜像，有 Cloudflare Workers 在线版 | 中：中文检索更方便；star 极少属正常（镜像类项目普遍如此） | ⚠️ **API 无许可字段（null）**，但镜像内容本身来自 cppreference（上游 CC-BY-SA-4.0） | 5 star；最后推送 **2026-07-26**（活跃）；56 MB 仓库，clone 后本地可查 |
| cppreference 中文镜像（个人自用） | `HengXin666/cppreference-zh-cn` | cppreference 20250404 中文镜像，附 GitHub Pages 在线版 | 中：多一个离线快照来源，可交叉验证快照时效 | 未核实（本次未取到 API 许可字段） | ⚠️ 仅在搜索结果中确认存在（含 Pages 站 `hengxin666.github.io/cppreference-zh-cn/`），**star / 推送时间未核实** |
| C++ 标准工作草案 | `cplusplus/draft` | ISO C++ 标准草案 LaTeX 源（当前主分支跟踪最新草案） | **高（定位特殊）**：这是**唯一**能回答「这条规则标准原文怎么写」的地方，做「逐条覆盖」时的最终仲裁者 | ⚠️ **API 返回无许可字段（null）**，标准草案的再分发条款需单独确认，**不可当作自由许可文本处理** | 229 star / 815 fork；最后推送 **2026-10-04**（非常活跃）；语言为 TeX；README 说明草案编号规则。**注意**：star 低不代表不重要——它的读者是标准委员会和编译器实现者 |
| C++ Core Guidelines | `isocpp/CppCoreGuidelines` | isocpp 官方的 C++ 核心准则（规则集 + 讨论 + 强制执行工具） | **高**：这是「现代 C++ 该怎么写」的工程共识来源，写讲义的「最佳实践 / 坑」章节时的权威依据 | ⚠️ **NOASSERTION**（API 返回 `Other`，未识别为标准 SPDX 许可）→ 需读仓库内 LICENSE 原文确认再使用 | 45,364 star / 5,556 fork；最后推送 **2026-10-01**（活跃）；246 open issues 说明在持续讨论 |

### 关于第 2 类的三个重要提醒

1. **cppreference 的许可**：本报告核实到的镜像仓库中，`0mega3/cppreference-doc` 明确声明 **CC-BY-SA-4.0**。cppreference 官方对内容的许可（历史上涉及 GFDL / CC-BY-SA 的组合）**本次未直接从上游确认**，标注为**未核实**；讲义若要引用其文字，请务必先到 cppreference 站点页脚核对当前许可。
2. **「可 clone」不等于「可复制」**：第 2 类里真正能当「标准化文本」用的是 `cplusplus/draft`（权威但不可自由再分发）和 `isocpp/CppCoreGuidelines`（许可为 NOASSERTION，需读原文）。**它们的正确用法是「核对与引用」，不是「搬运」。**
3. **离线检索的实际做法**：对这个用户，最实用的组合是「`0mega3/cppreference-doc`（或中文镜像）clone 到本地 + `cplusplus/draft` 作为仲裁」。前者解决「签名是什么」，后者解决「为什么是这样」。

---

## 3. 现代 C++（C++11/14/17/20）最佳实践与迁移材料

| 仓库 | 全名 | 用途一句话 | 适合度 | 许可 | 备注 |
|---|---|---|---|---|---|
| modern-cpp-tutorial | `changkun/modern-cpp-tutorial` | 见第 1 类；同时是本类最强的**迁移材料**（按 C++11/14/17/20 逐版本铺开） | **高** | ✅ MIT | 25,874 star；最后推送 2026-06-21（活跃）。**是第 1 类与第 3 类的交集，挑 5 个时必留** |
| Modern C++ Features | `AnthonyCalandra/modern-cpp-features` | 现代 C++ 语言与库特性的**速查表**（每版本一节，代码示例极短） | **高**：做「逐条覆盖」时的**特性清单基线**——用它保证没有漏掉某个 C++17 特性，再逐条补讲 | ✅ **MIT** | 21,903 star / 2,263 fork；最后推送 **2026-06-09**（活跃）；topics 含 `cpp11`–`cpp23`；仓库仅 273 KB，**极适合作为覆盖率的对照清单** |
| C++ Best Practices | `cpp-best-practices/cppbestpractices` | Jason Turner 主持的协作式 C++ 最佳实践文集（外链 + 规则） | 中高：适合补讲义的「工程约定 / 工具链」章节，与本用户 MSVC 环境结合讲 clang-tidy 等 | ⚠️ **NOASSERTION**（`Other`），需读仓库内许可原文 | 8,839 star / 905 fork；⚠️ **最后推送 2024-08-06**（约两年未更新）→ **标注为「内容仍有价值但维护停滞」**，28 章左右的静态文档类项目，停滞影响相对小 |
| ModernCppStarter | `studentutu/ModernCppStarter`（为 `TheLartians/ModernCppStarter` 的已知分叉） | 现代 C++ 项目模板：CMake + CI + 代码覆盖 + clang-format + 依赖管理 | 中：讲义的「第一次把多个 .cpp 编成一个项目」章节可直接参照其目录结构 | 未核实（本次未取到该分叉的 API 元数据） | ⚠️ **本报告未能核实该分叉的 star / 推送 / 许可**；上游 `TheLartians/ModernCppStarter` 亦**未在本次 API 查询中核实**。请自行确认后使用 |
| C++17 完整指南（中译） | `MeouSker77/Cpp17` | 《C++17 The Complete Guide》个人中文翻译 | 中：C++17 细节深度足够，**但定位见第 6 类**（书稿类，只能结构参考） | ⚠️ **无许可（license: null）** | 1,752 star / 272 fork；最后推送 **2026-03-23**（活跃）；TeΧ 源，36 MB |

**迁移材料怎么用（回答「从 C with Classes 到现代 C++」这一问）**：
- **清单**：`AnthonyCalandra/modern-cpp-features` —— 回答「C++17 有哪些新东西，我讲全了吗」。
- **叙事**：`changkun/modern-cpp-tutorial` —— 回答「同一个需求，老写法和现代写法差在哪，为什么」。
- **判据**：`isocpp/CppCoreGuidelines` —— 回答「哪种写法是工程共识」。
- 三者是**清单 / 叙事 / 判据**三个不同层，不要混在一节里写。

---

## 4. 算法竞赛 / 判题机常用 C++ 模板与技巧仓库

| 仓库 | 全名 | 用途一句话 | 适合度 | 许可 | 备注 |
|---|---|---|---|---|---|
| KACTL | `kth-competitive-programming/kactl` | KTH 算法竞赛模板库：几何 / 图论 / 数据结构 / 数论，**带 CI 与单元测试**，可一键生成 LaTeX notebook | **高**：本类里**唯一「可信度最高」**的选择——有测试意味着代码被实际验证过，不是抄来的片段 | ✅ **CC0-1.0**（公共领域奉献，最宽松，可任意使用） | 3,556 star / 1,007 fork；最后推送 **2026-10-03**（非常活跃）；topics 含 `cc0`。**放进讲义示例最安全** |
| Code Library | `ShahjalalShohag/code-library` | 竞赛用模板、算法与数据结构合集（作者为知名竞赛选手） | 高：覆盖面广，适合当「选手实际在用的东西长什么样」的样本 | ✅ **MIT** | 3,725 star / 884 fork；最后推送 **2026-03-03**（活跃度中等偏上）；文档站含分类目录 |
| AtCoder Library | `atcoder/ac-library` | AtCoder 官方算法库（segtree / fenwick / modint / DSU / 字符串 / 数论），判题机原生支持 | **高（判题机关键）**：这是**平台官方**库，AtCoder 可直接 `#include <atcoder/all>`，是「判题机专用写法」的标准范例 | ✅ **CC0-1.0** | 2,369 star / 269 fork；最后推送 **2025-05-01**（约一年未更新，但官方库已稳定，属**功能完成型停滞**）；接口文档在 `atcoder.github.io/ac-library` |
| CP-Templates | `7oSkaaa/CP-Templates` | 竞赛模板集合（含文档站） | 中：模板组织方式可参考，深度不如 KACTL | ⚠️ **无许可（license: null）** | 167 star / 35 fork；最后推送 **2026-06-06**（活跃）；**量级小，属个人模板**，适合看「新手怎么起步搭自己的模板」 |
| OI Wiki | `OI-wiki/OI-wiki` | OI / ICPC 中文百科：算法 + 数据结构 + **语言基础与竞赛技巧** | **高**：中文、系统、活跃，且**是唯一同时覆盖「算法」和「竞赛里的 C++ 语言细节」的中文资源** | ⚠️ **无许可（license: null）**（页面内容另有 CC 声明，需另行确认） | 26,830 star / 4,696 fork；最后推送 **2026-10-07**（非常活跃）；26k star 量级；站点 `oi-wiki.org` |
| 算法竞赛模板库（Go，作对照） | `EndlessCheng/codeforces-go` | 灵茶山艾府的算法竞赛模板库 | 低（语言不符）：**本用户要 C++**，但可作为「模板库该怎么组织、怎么配题解」的中文范本 | ✅ MIT | 8,757 star / 826 fork；最后推送 **2026-10-08**（极活跃）。**明确列为对照，不作为 C++ 模板来源** |
| 算法模板（个人） | `lr580/algorithm_template` | ICPC/CCPC 适用的一些算法模板 | 未核实 | 未核实 | ⚠️ 搜索结果中出现，**star / 推送时间 / 许可均未核实** |
| C++17 竞赛笔记 | `qxf-72/Codeforces-Cpp` | 覆盖数据结构、图论、DP、数学、字符串的 C++17 竞赛笔记与可复用模板 | 未核实 | 未核实 | ⚠️ 搜索结果中出现，**元数据未核实**；定位与讲义契合（C++17 基线），值得后续确认 |
| 算法模板（个人） | `nehcoah/algorithm-template` | LeetCode / Codeforces / AtCoder 的模板与题解 | 未核实 | 未核实 | ⚠️ 元数据未核实 |

**判题机写法的三个硬约束（来自上面资源的共识，供讲义「判题机章节」使用）**：
1. **不要用平台不保证的扩展**：OI Wiki 与 ac-library 都能印证，判题机上 `bits/stdc++.h`、`__int128`、`pbds`（`ext/pb_ds`）属「主流平台可用但不标准」——讲义应把它们**单列一节讲清依赖边界**，而不是混在标准库章节里。
2. **复杂度与 I/O 是一等公民**：KACTL 与 OI Wiki 的组织方式都以「复杂度 + 适用条件」标注为先，讲义应照此在每个数据结构处标注。
3. **模板要能被验证**：KACTL 的价值核心是它的测试 CI，讲义里的每个模板代码块也应满足「实跑过、附真实输出」（与该用户 Python 笔记的既有规范一致）。

---

## 5. 练习题 / 项目驱动学习

| 仓库 | 全名 | 用途一句话 | 适合度 | 许可 | 备注 |
|---|---|---|---|---|---|
| Hello 算法 | `krahets/hello-algo` | 《Hello 算法》：动画图解的数据结构与算法教程，**同一本书提供 Python / C++ / Java / Go 等 12 种语言实现** | **高（本类最佳）**：用户已有 Python 笔记 → 可**逐章对照 Python 与 C++ 实现**，这是「用已有知识锚定新语言」的最短路径；且方向含 AI 相关算法 | ⚠️ **NOASSERTION**（`Other`，需读仓库内许可原文） | 130,669 star / 15,501 fork（量级极高）；最后推送 **2026-08-17**（活跃）；站点 `hello-algo.com`。**是本清单 star 最高的仓库** |
| 代码随想录 | `youngyangyang04/leetcode-master` | 《代码随想录》LeetCode 刷题攻略：200 题顺序 + 图解 + 多语言（含 C++） | **高**：有**明确按主题排列的刷题顺序**，正好可以当作讲义的「每章课后练习索引」 | ⚠️ **无许可（license: null）** | 62,630 star / 12,292 fork；最后推送 **2026-08-03**（活跃）；262 open issues |
| TheAlgorithms / C++ | `TheAlgorithms/C-Plus-Plus` | 用 C++ 实现的教学向算法合集（数学 / 机器学习 / 计算机科学 / 物理） | 中高：**每个算法一个文件、可独立编译**，适合做「读懂一个小程序」的练手材料；含教育用途明确标注 | ✅ **MIT** | 34,744 star / 7,876 fork；最后推送 **2026-10-03**（非常活跃）；有 GitHub Pages 文档站 |
| 视觉 SLAM 十四讲（第 2 版） | `gaoxiang12/slambook2` | 《视觉 SLAM 十四讲》第 2 版配套代码：C++ + CMake + Eigen/OpenCV/Ceres/g2o | **中高（长期方向导向）**：这是**中文世界里把「C++ 用于机器人/具身智能」讲得最实**的项目书，配合作者的在线课程。对「软:硬 7:3、想做机器人」的用户，这是**从语言练习过渡到领域项目的桥梁** | ✅ **MIT** | 6,724 star / 2,193 fork；⚠️ **最后推送 2024-12-27**（约两年未更新）→ **明确标注「维护停滞但仍是该方向中文首选」**；208 open issues |
| Build Your Own X | `codecrafters-io/build-your-own-x` | 按技术主题（写数据库 / 编译器 / 操作系统…）组织的从零实现项目教程索引 | 中：用于挑「大作业」方向。**但仓库本身是链接集合**，不含教程正文 | ⚠️ **无许可（license: null）** | 552,138 star / 51,795 fork（全站量级最高之一）；最后推送 **2026-07-14**（活跃）；672 open issues |
| 项目驱动教程索引 | `practical-tutorials/project-based-learning` | 按语言分类的项目式教程索引（含 C++ 段） | 中：同上，找项目的入口，不是内容源 | ✅ **MIT** | 286,248 star / 36,565 fork；最后推送 **2026-10-05**（非常活跃） |
| C++ Projects | `CodesByMukul/Cpp-Projects` | 简单 C++ 项目集合 | 未核实 | 未核实 | ⚠️ 搜索结果中出现，**元数据未核实**；从命名看适合纯练手 |
| OOP C++ 项目 | `lewiii254/OOP-C-plus-plus` | 简单 C++ 项目集合 | 未核实 | 未核实 | ⚠️ 元数据未核实 |
| 解析几何图形练习 | `epcced/APT-CPP`（`epcced.github.io/APT-CPP`） | 入门级 C++ 习题（含 complex 等主题） | 未核实 | 未核实 | ⚠️ 来自搜索结果中的一份 PDF 习题说明，**仓库级元数据未核实** |

**练习题怎么接讲义**：建议「算法练习走 `hello-algo`（有 C++ 实现可对照）+ `leetcode-master`（有主题顺序）」，而「工程练习走 `slambook2`」——但 slambook2 依赖较重（Eigen/OpenCV/Ceres），**只适合作为第二学期的项目章**，不要在语言入门阶段引入。

---

## 6. 中文社区的 C++ 笔记仓库（结构参考，**不逐字复制**）

| 仓库 | 全名 | 用途一句话 | 适合度 | 许可 | 备注 |
|---|---|---|---|---|---|
| C/C++ 面试知识总结 | `huihut/interview` | C/C++ 技术面试知识总结：语言、程序库、数据结构、算法、系统、网络、链接装载库 | **高（对账用）**：覆盖了「语言之外」的**链接 / 装载 / 内存 / 系统**这些讲义最容易漏的层，是查漏的好清单 | ⚠️ **NOASSERTION**（`Other`，需读仓库内许可原文） | 38,239 star / 8,060 fork；最后推送 **2026-09-17**（活跃）；有 Pages 站 `interview.huihut.com`。**注意定位**：面试向 ≠ 教学向，顺序和深度都要重排 |
| C++ 那些事 | `Light-City/CPlusPlusThings` | 见第 1 类 | 高 | ⚠️ 无许可 | 43,508 star；最后推送 2026-05-16 |
| C++ Core Guidelines 中译 | `rigtor/CN-CppCoreGuidelines` | CppCoreGuidelines 中文翻译 | 未核实 | 未核实 | ⚠️ `repo:` 精确查询返回 422/未命中，**仓库是否存在需自行确认**；另有搜索命中的 `rigtor/CppCoreGuidelines-zh-CN`（同样未核实） |
| C++17 完整指南（中译） | `MeouSker77/Cpp17` | 见第 3 类；**典型书稿类仓库** | 中（仅结构） | ⚠️ **无许可**，README 自述「仅供学习和交流使用，侵删」 | 1,752 star；最后推送 2026-03-23。**书稿类：不可再分发**，只能看目录与章节划分 |
| C++ Templates 第二版（中译） | `xiaoweiChen/Cpp-Templates-2nd` | 《C++ Templates: The Complete Guide, 2nd》非专业个人翻译 | 中（仅结构，且属进阶/模板专题） | 未核实（个人翻译，**书稿类，按不可再分发处理**） | ⚠️ star / 推送时间未核实 |
| C++ Templates 第二版（另一中译） | `shelsing/CPP-Templates-2nd--` | 同上，声称与原书排版一致，部分章节完成 | 中（仅结构） | 未核实（书稿类） | ⚠️ 未核实；README 自述部分章节仍在更新 |
| Professional C++ 第 6 版（中译） | `xiaoweiChen/Professional-cpp-6ed` | 《Professional C++ - 6th Edition》个人翻译 | 中（仅结构） | 未核实（书稿类） | ⚠️ 未核实 |
| Expert C++（中译） | `xiaoweiChen/Expert-Cpp` | 《Expert C++》个人翻译 | 低（进阶，非入门） | 未核实（书稿类） | ⚠️ 未核实 |
| 30 秒 C++ | `cjemerson/30-seconds-of-cpp` | 短小 C++ 代码片段合集（STL 用法速查） | 未核实 | 未核实 | ⚠️ `repo:` 精确查询未命中该 owner，**只从 raw.githubusercontent 链接确认过 README 存在** |
| C++ Core Guidelines（英文副本） | `daniel-j-h/CppCoreGuidelines` / `dnzbk/CppCoreGuidelines` / `TheSeanParker/Cpp-Core-Guidelines` | 上游 Core Guidelines 的第三方副本 / 成书代码 | 低：**一律优先用上游 `isocpp/CppCoreGuidelines`**，副本可能陈旧 | 未核实 | ⚠️ 均为搜索结果中出现，元数据未核实；**不建议使用副本** |

### 第 6 类的使用纪律（必须写进讲义的项目约定）

1. **只对账，不搬运。** 用法是「打开它的目录，逐条问自己：这个知识点我讲义里有没有？」而不是「照着它的段落改写」。
2. **书稿类仓库统一按「不可再分发」处理。** 本次核实到的典型是 `MeouSker77/Cpp17`（README 明写「仅供学习和交流使用，侵删」）。`xiaoweiChen/*`、`shelsing/CPP-Templates-2nd--` 系列同为个人翻译，未见明确开放许可，一并按此处理。
3. **无许可 ≠ 公共领域。** `Light-City/CPlusPlusThings`、`0voice/cpp_new_features`、`youngyangyang04/leetcode-master`、`OI-wiki/OI-wiki`、`cjemerson/30-seconds-of-cpp`(未核实) 在 API 中 `license: null`，**默认保留全部权利**。用于「核对知识点有无遗漏」属于合理参考，但**逐字复制、翻译改写、或整体搬目录结构进正文都有风险**。
4. **可安全引用的白名单**（本次已核实为宽松许可）：`changkun/modern-cpp-tutorial`(MIT)、`AnthonyCalandra/modern-cpp-features`(MIT)、`TheAlgorithms/C-Plus-Plus`(MIT)、`ShahjalalShohag/code-library`(MIT)、`gaoxiang12/slambook2`(MIT)、`practical-tutorials/project-based-learning`(MIT)、`kth-competitive-programming/kactl`(CC0)、`atcoder/ac-library`(CC0)、`0mega3/cppreference-doc`(CC-BY-SA-4.0，**传染，需同样以 CC-BY-SA 发布并署名**)。

---

## 7. 回答：哪些仓库适合「核对 C++ 知识点覆盖完整度」

这是本调研最核心的一问。按**对账维度**分四层，每层只需要一个主源：

| 对账维度 | 主源 | 它能回答什么 | 许可与使用边界 |
|---|---|---|---|
| **标准库「索引级完整」** | `0mega3/cppreference-doc`（英文离线）或 `Jisu-Woniu/cppreference-zh-mirror`（中文离线） | 「这个头文件 / 这个重载 / 这个成员函数我讲了吗」——按头文件系统遍历，是唯一能做到「索引级」的源 | CC-BY-SA-4.0（传染）/ 镜像源许可未标；**只用于生成自己的覆盖清单，不复制其条目文字** |
| **核心语言「逐条覆盖」** | `AnthonyCalandra/modern-cpp-features` + `cplusplus/draft` | 前者给出「C++11/14/17/20/23 各自有哪些特性」的**可勾选清单**；后者在争议处给出**标准原文**（例如某特性是否属于 C++17、是否被弃用） | modern-cpp-features 为 MIT，可安全用作清单模板；draft 许可不明，**只引用不搬运** |
| **工程约定与「坑」** | `isocpp/CppCoreGuidelines` | 「这么写行不行 / 有什么隐患」——规则式条目天然可当 check list | NOASSERTION，需读仓库许可原文 |
| **算法与竞赛侧完整性** | `OI-wiki/OI-wiki` | 算法与数据结构在竞赛语境下的覆盖是否有缺口；**且它是中文、活跃、26k star 级**，是中文对账源里质量最稳的 | 无许可，只做知识核对 |

**具体对账流程（建议写进讲义项目的 `覆盖率设计` 文档）**：
1. 用 `modern-cpp-features` 生成**语言特性总表**（按 C++11/14/17/20 分组），每条标注「讲义章节号 / 深度（讲透 / 提及 / 划归进阶）」。
2. 用 cppreference 离线镜像**按头文件遍历标准库**，生成《标准库覆盖表》，标注「讲透 / 索引级（只给签名与用途）/ 划归进阶（如 `<regex>`、`<random>`、`<filesystem>`、并行算法）」。这一步直接落实「标准库做到索引级完整」。
3. 用 `OI-wiki` + `kactl` 对账**算法章节**是否存在缺口。
4. 用 `isocpp/CppCoreGuidelines` + `huihut/interview` 对账**工程与系统层**（链接、装载、内存模型、并发）是否漏讲。
5. 用 `CPlusPlusThings` 与 `huihut/interview` 的**目录**做最后一道「中文读者视角」查漏——只对比标题与顺序，**不读正文**。

---

## 8. 如果只挑 5 个

> 选择标准：① 覆盖「权威 / 现代写法 / 判题 / 练习 / 结构对账」五个不可替代的职能；② 许可允许实际使用；③ 2024 年后仍活跃。

| # | 仓库 | 职能（不可替代的理由） | 核实状态 |
|---|---|---|---|
| 1 | **`0mega3/cppreference-doc`**（备选：`Jisu-Woniu/cppreference-zh-mirror`） | **唯一能支撑「标准库索引级完整」的源**。断网可查、按头文件遍历，是这份讲义区别于普通教程的根基。许可 CC-BY-SA-4.0 明确可查。star 低完全不重要——内容来自 cppreference 上游 | ✅ 已核实（1 star / 2026-04-25 创建 / CC-BY-SA-4.0） |
| 2 | **`AnthonyCalandra/modern-cpp-features`** | **唯一「逐条可勾选」的现代特性清单**，直接把「核心语言 100% 逐条覆盖、C++20/23 标进阶」变成可操作的表。MIT 许可，可安全用作清单骨架。21.9k star、2026-06 仍在更新 | ✅ 已核实（21,903 star / 2026-06-09 / MIT） |
| 3 | **`changkun/modern-cpp-tutorial`** | **同时承担「入门系统学习」与「C with Classes → 现代 C++ 迁移」两职**，中英双语、按版本组织、MIT 许可。对本用户「已有 Python 基础、要建现代 C++ 讲义」的定位，这一个顶两个 | ✅ 已核实（25,874 star / 2026-06-21 / MIT） |
| 4 | **`kth-competitive-programming/kactl`** | **判题机模板的可信来源**：CC0 许可（最宽松）+ 带 CI 测试（代码被验证过）。满足用户「需要能用于判题机的写法」且「代码要实跑过」的双重要求。3.5k star、2026-10 活跃 | ✅ 已核实（3,556 star / 2026-10-03 / CC0-1.0） |
| 5 | **`krahets/hello-algo`** | **练习与「用 Python 知识锚定 C++」的最佳载体**：同一本书有 Python 与 C++ 双实现，130k star、2026-08 活跃。让用户能把已有的 2.75 万行 Python 笔记直接转成对照练习 | ✅ 已核实（130,669 star / 2026-08-17 / NOASSERTION→需读仓库许可原文） |

**为什么是这 5 个而不是「最火的 5 个」**：
- `Light-City/CPlusPlusThings`（43.5k star，中文第一）**没进前五**，理由是**无许可**且定位与第 3 项重叠——它更适合当**第 6 个对账源**，而不是正文依赖。
- `isocpp/CppCoreGuidelines`（45.4k star）**没进前五**，理由是它解决的是「怎么写更好」，而讲义当前阶段的第一优先级是「讲全了没有」；它应作为**第 6 个**加入工程实践章节。
- `cplusplus/draft` 是**仲裁者而非日常用源**，许可也不明，适合「有争议时查一次」，不适合列入常备 5 个。
- `atcoder/ac-library`（CC0、判题机官方库）与 kactl 职能重叠，作为**第 4 项的补充**而非替代：ac-library 适合讲「平台官方库长什么样」，kactl 适合讲「完整模板库怎么组织」。

**一个务实的补充建议**：若允许「第 6 个」，应选 `isocpp/CppCoreGuidelines`——因为它和已选的 5 个共同构成「**标准库 / 特性清单 / 语言叙事 / 判题 / 练习 / 工程约定**」六个正交职能，讲义的知识网络才算闭合。

---

## 9. 本报告的局限与未核实清单（诚实声明）

**核实方法**：全部元数据（star、fork、最后推送时间 `pushed_at`、SPDX 许可标识、`archived` 状态）通过 GitHub REST API（`api.github.com/repos/...` 与 `/search/repositories`）实时读取。本报告的 star 数是**查询当时的快照**，会随时间变化；「最后推送时间」判定活跃度的口径为「2024 年之后有推送 = 仍在维护」，与本报告使用者的要求一致。

**本次未能核实、因此不建议直接依赖的条目**（已在各表中标注 ⚠️ 未核实）：
`forhappy/CPlusPlus-Learnnote`、`xiebaoma/xbm-CppGuide`、`0voice/cpp_learning`、`HengXin666/cppreference-zh-cn`、`TheLartians/ModernCppStarter` 及其分叉 `studentutu/ModernCppStarter`、`lr580/algorithm_template`、`qxf-72/Codeforces-Cpp`、`nehcoah/algorithm-template`、`CodesByMukul/Cpp-Projects`、`lewiii254/OOP-C-plus-plus`、`epcced/APT-CPP`、`rigtor/CN-CppCoreGuidelines`、`xjf2001/Cpp-0-1-Resource`、`xiaoweiChen/*` 系列、`shelsing/CPP-Templates-2nd--`、`cjemerson/30-seconds-of-cpp`、`daniel-j-h|dnzbk|TheSeanParker` 的 Core Guidelines 副本。

**两项需要用户自行到上游确认的事实**：
1. **cppreference 站点当前的官方内容许可**（本报告只核实到镜像仓库 `0mega3/cppreference-doc` 声明 CC-BY-SA-4.0，未直接从 cppreference 官方页脚确认其 GFDL/CC-BY-SA 的具体组合）。
2. **`isocpp/CppCoreGuidelines` 与 `cpp-best-practices/cppbestpractices` 的 NOASSERTION 许可具体条款**（API 无法解析，需读仓库内 `LICENSE` 原文）。

**环境说明（未作为结论使用）**：用户给出的 MSVC 14.51 对应 Visual Studio 2026 / VS 2022 17.14 系列编译器的内部版本号（`_MSC_VER` 1941 一档），**本次调研未联网核实该版本号与 IDE 版本的对应关系**。讲义中凡涉及「编译器是否支持某特性」的表述，建议以 [cppreference 各设施页的「编译器支持」表](https://en.cppreference.com/w/cpp/compiler_support) 为准，而非依赖版本号推断。

---

*报告完成。所有带 ✅ 标记的条目均可直接点开 URL 复核；带 ⚠️ 未核实的条目请先自行确认再纳入讲义依赖。*
