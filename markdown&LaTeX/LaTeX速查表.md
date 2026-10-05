# LaTeX 公式速查表（输入 → 效果）

> 用途：在 Markdown 笔记里打数学公式。
> 逻辑和《Markdown速查表》一样：**你打什么 → 变成什么**。
> 左边反引号里的是**你要打的原文**，中间是**渲染出来的样子**。中间那列要你的编辑器支持公式才会显示。

---

## 〇、先记这两条（其余都是查字典）

| 场景 | 打这个 | 说明 |
| --- | --- | --- |
| 公式混在句子里 | `` $x^2$ `` | 一个 `$` 包住，**紧贴文字不换行** |
| 公式单独占一行 | `$$x^2$$` | 两个 `$` 包住，**居中独占一行** |

写成这样：

```
质能方程是 $E = mc^2$，它很简洁。

$$
E = mc^2
$$
```

渲染出来是：

质能方程是 $E = mc^2$，它很简洁。

$$
E = mc^2
$$

> **两个坑**：① `$` 必须**成对**，少一个后面全乱；② `$` 和公式之间**不要加空格**。

---

## 一、最常用的 5 个

### 1. 上下标：`^` 和 `_`

| 打这个 | 显示 | 说明 |
| --- | --- | --- |
| `` $x^2$ `` | $x^2$ | 上标 |
| `` $x_i$ `` | $x_i$ | 下标 |
| `` $x^{2n}$ `` | $x^{2n}$ | 上标多于一个字符，要加 `{}` |
| `` $x_i^2$ `` | $x_i^2$ | 上下标可以同时来 |
| `` $a_{ij}$ `` | $a_{ij}$ | 双下标 |

> **规则**：`^` `_` 只管**后面一个字符**。要管一串，用 `{}` 括起来。

### 2. 分数：`\frac{分子}{分母}`

| 打这个 | 显示 |
| --- | --- |
| `` $\frac{a}{b}$ `` | $\frac{a}{b}$ |
| `` $\frac{x+1}{y-2}$ `` | $\frac{x+1}{y-2}$ |
| `` $\dfrac{a}{b}$ `` | $\dfrac{a}{b}$（行内也强制放大） |

> **反斜杠 `\` 是命令开头**，所有命令都是 `\命令名`。打错一个字母就报错，认准拼写。

### 3. 希腊字母：`\` + 英文名

| 打这个 | 显示 | 打这个 | 显示 |
| --- | --- | --- | --- |
| `\alpha` | $\alpha$ | `\beta` | $\beta$ |
| `\gamma` | $\gamma$ | `\delta` | $\delta$ |
| `\theta` | $\theta$ | `\lambda` | $\lambda$ |
| `\mu` | $\mu$ | `\pi` | $\pi$ |
| `\sigma` | $\sigma$ | `\omega` | $\omega$ |
| `\Delta` | $\Delta$ | `\Omega` | $\Omega$ |

> **首字母大写 = 大写希腊字母**（`\delta` → $\delta$，`\Delta` → $\Delta$）。

### 4. 求和 / 积分 / 极限：带上下限

| 打这个 | 显示 |
| --- | --- |
| `` $\sum_{i=1}^{n} a_i$ `` | $\sum_{i=1}^{n} a_i$ |
| `` $\int_{0}^{1} x\,dx$ `` | $\int_{0}^{1} x\,dx$ |
| `` $\lim_{x \to 0} \frac{\sin x}{x}$ `` | $\lim_{x \to 0} \frac{\sin x}{x}$ |
| `` $\prod_{i=1}^{n} i$ `` | $\prod_{i=1}^{n} i$ |

> 这里 `_` 是**下限**，`^` 是**上限**。`\to` 是右箭头 →，`\,` 是插入一点小空隙。

### 5. 根号 / 绝对值 / 自动伸缩的括号

| 打这个 | 显示 |
| --- | --- |
| `` $\sqrt{x}$ `` | $\sqrt{x}$ |
| `` $\sqrt[3]{x}$ `` | $\sqrt[3]{x}$ |
| `` $\lvert x \rvert$ `` | $\lvert x \rvert$ |
| `` $\left( \frac{a}{b} \right)$ `` | $\left( \frac{a}{b} \right)$ |
| `` $\left[ \frac{a}{b} \right]$ `` | $\left[ \frac{a}{b} \right]$ |

> 括号里有分数时，一定要用 `\left( ... \right)`，**普通括号不会自动变大**，会显得很丑。

---

## 二、需要时再查

### 6. 关系与运算符号

| 打这个 | 显示 | 意思 |
| --- | --- | --- |
| `\le` | $\le$ | 小于等于 ≤ |
| `\ge` | $\ge$ | 大于等于 ≥ |
| `\ne` | $\ne$ | 不等于 ≠ |
| `\approx` | $\approx$ | 约等于 ≈ |
| `\times` | $\times$ | 乘 × |
| `\cdot` | $\cdot$ | 点乘 · |
| `\pm` | $\pm$ | 正负 ± |
| `\infty` | $\infty$ | 无穷 ∞ |
| `\to` | $\to$ | 趋于 → |
| `\Rightarrow` | $\Rightarrow$ | 推出 ⇒ |
| `\in` | $\in$ | 属于 ∈ |
| `\subset` | $\subset$ | 包含于 ⊂ |
| `\cup` | $\cup$ | 并集 ∪ |
| `\cap` | $\cap$ | 交集 ∩ |
| `\forall` | $\forall$ | 任意 ∀ |
| `\exists` | $\exists$ | 存在 ∃ |
| `\nabla` | $\nabla$ | 梯度 ∇ |
| `\partial` | $\partial$ | 偏导 ∂ |

### 7. 多行公式对齐：`aligned`

用两个 `$` 包住，里面写成这样：

```
$$
\begin{aligned}
a &= b + c \\
  &= d + e
\end{aligned}
$$
```

渲染出来：

$$
\begin{aligned}
a &= b + c \\
  &= d + e
\end{aligned}
$$

> `&` 是**对齐点**（想让哪个符号竖直对齐，就在它前面放 `&`），`\\` 是**换行**。

### 8. 分段函数：`cases`

```
$$
f(x) =
\begin{cases}
x^2, & x > 0 \\
0,   & x \le 0
\end{cases}
$$
```

渲染出来：

$$
f(x) =
\begin{cases}
x^2, & x > 0 \\
0,   & x \le 0
\end{cases}
$$

### 9. 矩阵

| 打这个（外层包 `$...$`） | 显示 |
| --- | --- |
| `\begin{pmatrix} a & b \\ c & d \end{pmatrix}` | $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ |
| `\begin{bmatrix} a & b \\ c & d \end{bmatrix}` | $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$ |
| `\begin{vmatrix} a & b \\ c & d \end{vmatrix}` | $\begin{vmatrix} a & b \\ c & d \end{vmatrix}$ |

> `p` = 圆括号 (parenthesis)，`b` = 方括号 (bracket)，`v` = 竖线（行列式）。

### 10. 公式里插文字：`\text{}`

| 打这个 | 显示 |
| --- | --- |
| `` $v = \frac{s}{t}$ `` | $v = \frac{s}{t}$ |
| `` $v = \frac{s}{t} \quad (\text{匀速直线运动})$ `` | $v = \frac{s}{t} \quad (\text{匀速直线运动})$ |

> **公式里的中文和汉字必须放进 `\text{}`**，否则不显示或报错。

### 11. 控制空隙

| 打这个 | 效果 |
| --- | --- |
| `\,` | 很小的空隙 |
| `\ ` | 一个空格 |
| `\quad` | 一个汉字的空隙 |
| `\qquad` | 两个汉字的空隙 |
| `\\` | 公式内换行 |

---

## 三、怎么让你的笔记显示公式

写对了但显示成 `$x^2$` 一堆乱码，是**编辑器没开公式渲染**，不是写错：

| 编辑器 | 做法 |
| --- | --- |
| **VSCode** | 预览用 `Ctrl+Shift+V`；若不行，设置里搜 `markdown.math` 勾上 `Enabled`；装插件 `Markdown+Math` 也可 |
| **Typora** | 原生支持，什么都不用设，写完 `Ctrl+/` 切源码模式 |
| **Obsidian** | 原生支持，直接就能看 |
| **GitHub / 语雀** | 支持 `$...$`，直接写 |
| **记事本 / 微信** | **不支持**，只会看到原文 |

> 想快速单独试一条公式，用在线编辑器最快：搜「KaTeX 在线编辑器」或打开 [latex.codecogs.com](https://latex.codecogs.com/eqneditor/editor.php)，左边打、右边立刻出图。

---

## 四、如果要用 LaTeX 写整篇文档（.tex → PDF）

这种是**另一种东西**：不是往 `.md` 里插公式，而是整个文件都用 LaTeX 语法写，最后编译成排版精美的 PDF。

**你的电脑现在没装编译器**，两条路：

| 方案 | 说明 | 成本 |
| --- | --- | --- |
| **Overleaf（推荐先试）** | 网页版，注册即用，零安装。上传 `LaTeX笔记模板.tex`，编译器选 **XeLaTeX**，点 Recompile 出 PDF | 免费，5 分钟上手 |
| **本地装** | 装 MiKTeX 或 TeX Live（1～4 GB），之后用 `xelatex 文件名.tex` 编译 | 一次装好，长期离线可用 |

**文档骨架长这样**（结构对应你熟悉的那套）：

| 你想要的 | LaTeX 写法 |
| --- | --- |
| 一级标题 | `\section{标题}` |
| 二级标题 | `\subsection{标题}` |
| 加粗 | `\textbf{加粗}` |
| 斜体 | `\textit{斜体}` |
| 无序列表 | `\begin{itemize} \item 内容 \end{itemize}` |
| 有序列表 | `\begin{enumerate} \item 内容 \end{enumerate}` |
| 表格 | `\begin{tabular}{ll} ... \end{tabular}` |
| 引用块 | `\begin{quote} 内容 \end{quote}` |
| 插入图片 | `\includegraphics[width=0.8\textwidth]{图.png}` |
| 居中 | `\begin{center} 内容 \end{center}` |
| 换行 | `\\` |
| 注释 | `% 这一行不显示` |

> 完整可用的笔记模板见同目录的 **`LaTeX笔记模板.tex`**，六个问题式章节和 `总结模板.md` 一模一样。

---

## 五、练习题

1. 打出：$\frac{1}{2}$
2. 打出：$x_1^2 + x_2^2$
3. 打出：$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$
4. 打出分段函数：$f(x)=\begin{cases} 1, & x>0 \\ -1, & x<0 \end{cases}$

答案：

```
1. $\frac{1}{2}$
2. $x_1^2 + x_2^2$
3. $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$
4. $f(x)=\begin{cases} 1, & x>0 \\ -1, & x<0 \end{cases}$
```
