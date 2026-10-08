# RESULT-01 · 第 2 轮（对抗评审）

> 角色 B；2026-10-08。只修改指定 FIX 涉及的标记、注释与版本说明；新发现交给 A 复核。
> 标准核对锁定 **C++17 草案 N4659**，不以持续更新的 `eel.is/c++draft` 仲裁 C++17 规则。
> [N4659 官方原件](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2017/n4659.pdf)；下文条款链接是该草案的 HTML 转录。

本轮找到 A 验收单未发现的可证伪断言：第 9.2 节“`argc` 至少是 1、不是 0”与 `[basic.start.main]/2` 冲突；第 3.2 节“`#pragma` 非标准”与 `[cpp.pragma]` 冲突；第 4.3 节“调试信息 `/Zi` 时才有”被 `/Z7` 的文档及本机目标文件反证。第 9.2 节关于 `argv` 不可修改的断言也被独立实验反驳。不是“没有发现问题”。

## A. 对 A 实测结论的复核

### 命令环境与证据位置

从正文目录运行的实际入口：

```powershell
$env:PYTHONUTF8='1'
& C:\Users\Wang\anaconda3\python.exe -u tmp\ch01_round2_probe.py
```

这是 B 新写的采集器，未运行 A 的 `probe_ch01.py`。源文件、逐项 `.bat`、原始日志和 `results.json` 保留在 [`../tmp/ch01-round2/`](../tmp/ch01-round2/)。复现源码由 [`../tmp/ch01_round2_probe.py`](../tmp/ch01_round2_probe.py) 生成。临时目录在本轮可写工作区内，已经用 `git check-ignore` 确认忽略。

每个批处理先执行以下公共前缀，再执行表内命令；源码均为 UTF-8：

```bat
@echo off
call "C:\Program Files (x86)\Microsoft Visual Studio\18\BuildTools\VC\Auxiliary\Build\vcvars64.bat" >nul 2>&1
if errorlevel 1 exit /b 90
cd /d "%~dp0"
```

表内输出为真实日志的相关部分，不包含无关的 COFF 页表。完整输出在对应日志中。

| 复核对象 | 我的命令 | 我的输出 | 与 A 是否一致 | 结论 |
|---|---|---|---|---|
| `/FA`，明确禁用优化 | `cl /nologo /std:c++17 /EHsc /W4 /utf-8 /Od /FA /Faod.asm /c add.cpp /Fo:od.obj` | `/Odtp`；两条寄存器→栈的 `mov`，随后取回、`add`、`mov eax,ecx`、`ret 0`；退出 0 | 是，与 A 的指令序列一致 | 只验证本机 x64、该函数、这组开关下的样例 |
| 同一函数改为 `/O2` | `cl /nologo /std:c++17 /EHsc /W4 /utf-8 /O2 /FA /Fao2.asm /c add.cpp /Fo:o2.obj` | `/Ogtpy`；`lea eax, DWORD PTR [rcx+rdx]`；`ret 0`；退出 0 | 不同，是有意改变优化开关的对照 | A 原先猜的 `lea` 在这个配置下确实出现；不能把“本次没出现”泛化为“MSVC 不这样生成” |
| `/P`，与 A 同一源文件和开关 | `cl /nologo /std:c++17 /utf-8 /P expand.cpp`；采集器读文件长度与行数 | 源文件 **61 B**；`.i` **2 522 251 B / 85 972 行**；退出 0 | 是，三个数字全部一致 | 这是一次构建的统计值。正文已写“本机实测”，并未直接声称所有实现都一样 |
| `/P` 增加正文常用开关 | `cl /nologo /std:c++17 /EHsc /W4 /utf-8 /P expand.cpp` | `.i` **2 522 122 B**；退出 0 | 比 A 少 **129 B** | 仅改变开关组合就变了；本轮未进一步隔离是哪一个开关导致差异，不能猜归因 |
| `SQUARE(1 + 2)` 与 `SQUARE((1 + 2))` | `cl /nologo /std:c++17 /EHsc /W4 /utf-8 macro.cpp /Fe:macro.exe`；`macro.exe`；同开关加 `/P macro.cpp` | stdout 两行 **5 / 9**；运行退出 0；`.i` 有 `1 + 2 * 1 + 2` 和 `(1 + 2) * (1 + 2)` | 是 | 该合法宏调用按规定展开；它不能证明“宏从来不会有错误”这个无条件判断 |
| `main` 省略返回，观察终止清理 | `cl /nologo /std:c++17 /EHsc /W4 /utf-8 termination.cpp /Fe:termination.exe`；`termination.exe` | `main body` → `automatic destroyed` → `static destroyed`；运行退出 0 | A 的“等价于返回 0”成立，但解释不完整 | 局部自动对象先随离开 `main` 析构，随后正常终止处理静态对象。标准依据见下 |
| 编译器两套编号 | `cl /Bv /c add.cpp` | 工具路径含 `MSVC\14.51.36231`；`cl.exe` 版本 **19.51.36256.0**；退出 0 | 是 | 已补到正文第 6.3 节；不能把其中一个替换成另一个 |

`add.cpp` 的完整函数体与正文相同。`expand.cpp` 是第 3.1 节那个打印 `hi` 的完整程序，LF 文件长度为 61 B。宏实验重新写成两次输出，没有使用 A 的脚本。

优化对照的真实相关指令：

```asm
; /Od 的 od.asm
; Function compile flags: /Odtp
mov DWORD PTR [rsp+16], edx
mov DWORD PTR [rsp+8], ecx
mov eax, DWORD PTR b$[rsp]
mov ecx, DWORD PTR a$[rsp]
add ecx, eax
mov eax, ecx
ret 0

; /O2 的 o2.asm
; Function compile flags: /Ogtpy
lea eax, DWORD PTR [rcx+rdx]
ret 0
```

`/Od` 确实禁用优化；但“未优化”“生成调试信息”“链接调试版 CRT”是不同选择。这里没有 `/Zi`、`/Z7` 或 `/MDd`、`/MTd`，不能据此说是完整的“调试模式”。`.asm` 中的 `; Line 2` 是文本清单注释，不是调试器读取的行号表。参见 [MSVC `/Od`](https://learn.microsoft.com/en-us/cpp/build/reference/od-disable-debug?view=msvc-170)、[清单开关](https://learn.microsoft.com/en-us/cpp/build/reference/fa-fa-listing-file?view=msvc-170) 与 [调试信息格式](https://learn.microsoft.com/en-us/cpp/build/reference/z7-zi-zi-debug-information-format?view=msvc-170)。没有猜解 `/Odtp` 中未单独核实的字母含义。

`main` 的准确规则是：控制流到达其末尾具有返回 0 的效果；从 `main` 返回先离开函数并销毁相应自动对象，再以返回值执行 `std::exit` 的终止语义，后者包含静态对象析构等清理。**直接调用 `std::exit` 不替代离开当前函数时的自动对象析构。** 非 `main` 的普通非 `void` 函数是“控制流到达末尾”才有 UB，不能把“源码没有 `return`”本身判成 UB。[`[basic.start.main]/4–5`](https://timsong-cpp.github.io/cppwp/n4659/basic.start.main)、[`[basic.start.term]/1`](https://timsong-cpp.github.io/cppwp/n4659/basic.start.term)、[`[support.start.term]/9`](https://timsong-cpp.github.io/cppwp/n4659/support.start.term)、[`[stmt.return]/2`](https://timsong-cpp.github.io/cppwp/n4659/stmt.return)。

### 新攻击的编译证据

**参数字符串实验**（`argv.cpp`；直接在已有字符范围内改写，没有扩容）：

```cpp
#include <cstdio>
int main(int argc, char** argv) {
    if (argc > 1 && argv[1][0]) {
        argv[1][0] = 'X';
        std::puts(argv[1]);
    }
    std::printf("sentinel_null=%d\n", argv[argc] == nullptr);
}
```

命令 `cl /nologo /std:c++17 /EHsc /W4 /utf-8 argv.cpp /Fe:argv.exe`，接着 `argv.exe abc`；真实 stdout：

```text
Xbc
sentinel_null=1
```

运行退出 **0**，编译警告 **0**。这至少直接反驳“本机参数字符串不能改”的教学结论；也没有找到 A 声称的 C++17 标准禁止条款。不要把改写已有字符，混同为可以向后越界增加字符。

**原始字符串边界实验**：`raw_bad.cpp` 把内容中的 `)"` 当作普通字符，源行是 `int main() { const char* p = R"(left )" right)"; (void)p; }`。

命令 `cl /nologo /std:c++17 /EHsc /W4 /utf-8 raw_bad.cpp /Fe:raw_bad.exe`，真实退出 **2**，诊断：

```text
raw_bad.cpp(1): error C2146: 语法错误: 缺少“;”(在标识符“right”的前面)
raw_bad.cpp(1): error C2059: 语法错误:“)”
raw_bad.cpp(1): error C2001: 字符串字面量中的换行符
raw_bad.cpp(1): error C2065: “right”: 未声明的标识符
raw_bad.cpp(1): error C2143: 语法错误: 缺少“;”(在“字符串”的前面)
raw_bad.cpp(1): fatal error C1075: “{”: 未找到匹配令牌
```

改用自定义分隔符的独立程序 `std::puts(R"tag(left )" right)tag");`，同一编译开关，运行真实输出 `left )" right`，退出 **0**、警告 **0**。本实验只说明该错误余串被本机拒绝，不把所有畸形字符串统一归为运行时 UB。

**目标文件格式实验**：`dumpbin /nologo /headers od.obj` 输出 `File Type: COFF OBJECT`，即使没开调试信息开关也存在 `.debug$S`（大小 `A8`）；不能仅凭节名推断存在完整源码调试信息。加 `/Z7` 编译为 `z7.obj` 后，头部输出 `.debug$S` 大小 `248`、`.debug$T` 大小 `47C`；它们是十六进制值。`/Z7` 命令没有 `/Zi`。[MSVC 文档](https://learn.microsoft.com/en-us/cpp/build/reference/z7-zi-zi-debug-information-format?view=msvc-170)明确区分对象内调试信息与单独 PDB，故正文“`/Zi` 时才有”不成立。

**Shell 对照**：在实验目录执行 `argv.exe abc`，PowerShell 报 `CommandNotFoundException`；`& .\argv.exe abc` 正常输出上述两行；`cmd.exe /d /c 'argv.exe abc'` 也正常输出上述两行。记录见 [`../tmp/ch01_shell_probe.txt`](../tmp/ch01_shell_probe.txt)。这是两种 shell 的查找规则差异，不是 C++ 语言规则，也不是 PowerShell 的脚本执行策略开关。[PowerShell 官方说明](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_command_precedence?view=powershell-7.5)。

## B. 依赖实现 / 未指定 / UB 的说法（A 未标的）

分类不能硬塞成三桶：**工具实现细节**不是天然属于标准术语“实现定义”；**程序不良构成（ill-formed）**也不应自动当作运行时 UB。下表分清标准规则、标准允许的差异、工具约定和错误断言。重复出现的同一断言合并列出。

| 位置 | A 的说法 | 准确归类 | 依据（标准条款或实测） | 建议改法 |
|---|---|---|---|---|
| 0、1、2 节工具链图 | `.cpp` 必须逐步生成 `.asm`、`.obj`、`.exe` | 工具链教学模型，不是标准规定的磁盘文件流水线 | [`[lex.phases]/1.7 及脚注`](https://timsong-cpp.github.io/cppwp/n4659/lex.phases)允许阶段合并，没有外部文件一一对应要求 | 保留图，标明“本机传统工具链的概念简图”，不说所有 C++ 实现必生成 `.asm` |
| 第 1 节 ④→⑤、第 6.2 节 `main` 行 | 操作系统装载后“从 `main` 开始执行” | 错误的实现机制表述 | MSVC 默认入口是 CRT 启动函数，随后调用 `main`；[MSVC `/ENTRY`](https://learn.microsoft.com/en-us/cpp/build/reference/entry-entry-point-symbol?view=msvc-170)；标准另有静态对象初始化及正常终止语义 | 图中增加“加载器与运行时启动→调用 main”；区分 OS 入口与用户程序入口。链接成功也不保证加载、运行及输出一定成功 |
| 第 0、3.1 节及自测 2 | `#include` 把所有文本“原样复制” | 合法包含有标准规则，但“原样”过度简化 | [`[cpp.include]/2–4`](https://timsong-cpp.github.io/cppwp/n4659/cpp.include)、`[lex.phases]/1.3–4`：被包含内容仍须分词、去注释、条件选择及宏展开 | 改为“包含内容参与当前翻译单元的预处理”；不是最终展开结果保留头文件的原始字节 |
| 第 2 节预处理器“只认 #” | 只认指令，不处理普通代码 | 错误 | 第 3.2 节自己的宏调用就出现在普通表达式里；[`[cpp.replace]`](https://timsong-cpp.github.io/cppwp/n4659/cpp.replace)、[`[cpp.rescan]`](https://timsong-cpp.github.io/cppwp/n4659/cpp.rescan)规定记号替换与重扫描 | 它不做完整 C++ 类型检查，但会分解、处理普通文本中的预处理记号；不等于简单字符串查找替换 |
| 第 3.1、15 节 `.i` 大小 | 61 B→2 522 251 B | 本机观察值，已有限定；不是新发现的错误 | A 同开关完全复现；加 `/EHsc /W4` 后少 129 B | 补“依赖源码字节、头实现版本、开关及清单格式”；不要把两次同环境一致当标准量级 |
| 第 3.2 节 `SQUARE` | 该宏输出 5、9 | 标准规则下有确定结果，本机复现 | 记号展开与乘法优先级；本轮 `macro.log` | 这条保留，不因措辞争议作废真实输出 |
| 第 3.2 节“宏从来没错” | 宏永远正确 | 无依据的无条件判断 | [`[cpp.replace]/2`](https://timsong-cpp.github.io/cppwp/n4659/cpp.replace)：不合要求的重定义可使程序 ill-formed；拼接也有合法性限制 | 限定为“这个合法调用按定义展开，但定义不满足想求平方的意图”；宏定义也可以错误 |
| 第 3.2 节 `#pragma` 行 | `#pragma` 非标准 | **被标准直接证伪** | [`[cpp.pragma]/1`](https://timsong-cpp.github.io/cppwp/n4659/cpp.pragma)有标准语法，具体效果实现定义，不认识的 pragma 被忽略 | `#pragma` 是标准指令；`once` 是具体实现提供的扩展语义 |
| 第 3.2 节宏只能在诊断中看到展开体 | 错误信息里“只看得到展开后的样子” | 工具诊断能力的断言，无本轮证据 | 不能从 `/P` 的文本输出推导调试器及全部诊断的能力 | 去掉“只”；单独说明宏替换不等于函数调用。本轮未测宏溯源诊断 |
| 第 4.1 节名字修饰、寄存器和栈 | 修饰串与寄存器搬运是 C++ 必然形式 | 本机 ABI / 开关结果，非标准编码保证 | `od.asm` 与 `o2.asm` | 明说 MSVC x64 样例；“参数不是传进函数”改成“该样例的传参和访问被实现为这些指令” |
| 第 4.1 节 `/Odtp` 与行号 | 默认就是调试模式；汇编注释是调试器的依据 | 不成立的推论 | A 节开关对照、`/Od`、`/FA`、`/Z7`、`/Zi` 官方说明 | 分开优化、清单、调试信息及 CRT 选择，不把未优化直接叫调试构建 |
| 第 4.2 节“永远看不到别的 .cpp” | 编译器绝不能跨 TU 分析 | 普通分别编译的教学假设，不能无条件泛化 | [MSVC `/GL`](https://learn.microsoft.com/en-us/cpp/build/reference/gl-whole-program-optimization?view=msvc-170)支持整个程序优化 | “普通分别编译时，不靠另一 TU 的源码完成当前 TU 名字查找”；优化不替代声明规则 |
| 第 4.3 节四项表 | 目标文件必有机器码、符号表、重定位、调试信息 | 全部是目标格式/工具构建层描述，不是四项标准保证 | `dumpbin` 确认本机 COFF；`[lex.phases]/1.7`不规定该文件布局 | 表头限定“本机常见 COFF 目标文件”；按实际所需可为空；不据此要求所有实现的文件一样 |
| 第 4.3 节 `/Zi` 时才有 | 调试信息唯一入口是 `/Zi`，都在 obj 里 | **本机及官方文档反证** | `/Z7` 实验与[三种格式说明](https://learn.microsoft.com/en-us/cpp/build/reference/z7-zi-zi-debug-information-format?view=msvc-170) | `/Z7` 对象内，`/Zi` 主要在 PDB 并由对象关联；汇编注释另算 |
| 第 5、10 节重复定义 | 重复非 inline 定义一定以指定链接码报错 | 示例在本机成立；跨 TU 的标准违规不保证诊断形式 | [`[basic.def.odr]/4、6`](https://timsong-cpp.github.io/cppwp/n4659/basic.def.odr)；A 原始日志 | 写“本例 MSVC 报 LNK2005”；多 TU `inline` 定义也有一致性要求，不是任意不同函数体都可放行 |
| 第 6.2 节 `std` 行 | 标准库“所有东西”都在 std | 过度概括 | [`[headers]/4–5`](https://timsong-cpp.github.io/cppwp/n4659/headers)：C 库兼容名字有规则，宏不受命名空间限定，是否先在全局声明部分名字是未指定 | 限定“本例 cout 在 std”；宏与 C 兼容头规则留给相应章节 |
| 第 6.4 节注释 | 两种注释、块注释不能嵌套 | 标准保证；FIX 已由 A 在工作期间补入 | [`[lex.comment]`](https://timsong-cpp.github.io/cppwp/n4659/lex.comment)、`[lex.phases]/1.3`；新例子基线输出 1、2 | 保留；解释阶段 2 续行先于注释处理，“// 到行末”指逻辑行末 |
| 第 6.5、15 节不写 return | 任何非 main 的 int 函数不写 return 就 UB | 触发条件表述过宽 | [`[stmt.return]/2`](https://timsong-cpp.github.io/cppwp/n4659/stmt.return) | 必须实际到达末尾；始终抛出异常等情况不因没有 return 自动 UB。main 的隐式 0 特例保留 |
| 第 7 节 GCC/Clang 对照及默认标准 | 开关及默认版本 | 已标未本机实测；是工具版本事实 | 本轮未安装、未运行这些工具 | 不取消已有未实测标签，不拿 MSVC 结果证明 GCC/Clang |
| 第 8.2 节 error/warning | warning 表示标准合法行为，error 表示语言非法 | 不能作为标准合法性的判据 | [`[intro.compliance]/1–2、8`](https://timsong-cpp.github.io/cppwp/n4659/intro.compliance)：需诊断不等于必须拒绝；UB 可没有诊断，扩展可诊断后接受；`/WX`也改变退出策略 | 先讲本工具如何继续/停止，再讲“成功编译≠合法且安全”；不能称读取未初始化 int 是标准合法行为 |
| 第 8.2 节 `/WX` 证据 | `.exe` 不存在就证实 `.obj` 不生成 | 证据对象混淆，不能这样推出 | A 日志实际只核对 `uninit_wx.exe` 是否存在 | 若要说 obj 未生成，单独检查新目录中的 obj；本轮未重复原八项实验 |
| 第 9.1 节所有非零都失败 | 程序退出值的含义 | 0/EXIT_SUCCESS 表成功有标准规则，其它值的具体返回状态依实现；“非零都失败”也是 shell/工具约定 | [`[support.start.term]/9.3`](https://timsong-cpp.github.io/cppwp/n4659/support.start.term) | 区分语言终止语义、主机映射和脚本约定；不要保证所有平台原样保留任意 int |
| 第 9.2 节“至少 1，不是 0” | argc 标准下限为 1 | **错误；标准保证的是非负** | [`[basic.start.main]/2`](https://timsong-cpp.github.io/cppwp/n4659/basic.start.main) | 本机普通启动通常为 1；标准允许 0。argc==0 时 argv[0]==argv[argc] 为 null；argc>0 时 argv[0] 为有效终止字符串，可为空串，不能是 null |
| 第 9.2 节“字符串不能修改（标准如此）” | char* 内容法定只读 | 错误的禁令；本机实测可改写 | A 节 `argv.exe abc` 输出 Xbc；N4659 的 `[basic.start.main]` 未给出这个禁令 | 参数字符串可就地改写已有字符，别越界；“业务代码通常只读”只能是使用建议。**不把 C 标准关于 main 的条文冒充 C++17 原文** |
| 第 10 节头文件与翻译单元 | header 必定是磁盘上的 .h/.hpp | 常见实现，不是完整标准概念 | [`[headers]`脚注 168](https://timsong-cpp.github.io/cppwp/n4659/headers)指出 header 不必是源文件；[`[lex.separate]/1`](https://timsong-cpp.github.io/cppwp/n4659/lex.separate)给 TU 组成 | 本机用户头文件通常如此；TU 还须扣除条件编译跳过的部分 |
| 第 10.1 节匹配提示 | “经常把人带偏”，只是长得像 | 频率与心理效果没有证据；示例里的签名确实不同 | A 日志中全局 add(int,int) 与库内部命名空间中的 add(big_integer&,unsigned) 不同；[LNK2019](https://learn.microsoft.com/en-us/cpp/error-messages/tool-errors/linker-tools-error-lnk2019?view=msvc-170)、[修饰名说明](https://learn.microsoft.com/en-us/cpp/build/reference/decorated-names?view=msvc-170) | 保留诊断，写“检查命名空间、参数、调用约定与完整修饰名；提示不是已满足所需符号”。未测链接器候选排序算法，不能断言其仅按外观筛选 |
| 第 11.1 节 argv[0] 完整路径 | “这次实测证实它是完整路径”被用于一般说明 | 本次观察不能推出所有启动方式 | [Microsoft main 文档](https://learn.microsoft.com/en-us/cpp/cpp/main-function-command-line-args?view=msvc-170)指出 CreateProcess 启动时 argv[0] 可不是可执行名 | “本次启动得到完整路径”；不要把路径当标准值；反例条件见第 9.2 节 |
| 第 11.1 节空指针、第 13 节未初始化 int | 示例本身有 UB；具体崩溃值来自本机 | UB；原 UB 标签基本正确，但“Linux 同样错误就是 SIGSEGV”太绝对 | N4659 `[dcl.init]` 的不确定值规则；原文已标空指针 UB，未重新执行 UB 程序 | 保留不进确定输出基线；不同系统也不保证每次必崩溃，更不保证具体码 |
| 第 12.1 节中文不加 utf-8 必报错 | 任意中文源都必报四个诊断 | 本机某份字节序列的现象，不是普遍规则 | [MSVC `/utf-8` 文档](https://learn.microsoft.com/en-us/cpp/build/reference/utf-8-set-source-and-executable-character-sets-to-utf-8?view=msvc-170)还说明 BOM 检测等默认行为 | 保留该文件真实诊断，补“无 BOM 的 UTF-8 文件被错误解码”的条件；控制台页与源解码选择也不要混同 |
| 第 12.2 节代码页 936 仍显示正常 | 输出正常被当作终端链已经通 | 只证实采集端解码正常，不能自动证实交互控制台渲染 | A 程序由采集器取 stdout；本轮也用 UTF-8 解码输出管道，未肉眼验交互终端 | 区分 stdout 字节、采集器解码、终端显示；除非另有截图或交互证据，不写成所有 936 控制台都正常 |
| 第 12.3 节原始字符串 | 反斜杠不转义 | 标准保证，但缺终止边界，不是原句本身错误 | [`[lex.string]`语法与 /2](https://timsong-cpp.github.io/cppwp/n4659/lex.string)及 raw_bad/raw_good 实测 | 空分隔符遇到 `)"` 就结束；可换不冲突的分隔符，最多 16 字符；分隔符禁止空格、圆括号、反斜杠及规定的控制空白。不是内容中单独的 `)` 或 `"` 都禁用 |
| 第 12.4 节 PowerShell 必须 .\\ | 永远不能裸名运行当前文件 | 默认命令查找规则，有安全动机；不是 C++ 或脚本执行策略事实 | A 节 PS/cmd 对照、PowerShell 官方文档 | 默认写 .\\；完整路径也可；若目标目录明确加入 PATH，裸名可被找到。cmd.exe 在本次默认环境可以找当前目录 |

`第 12.4 节“Windows 下可执行文件必须有 .exe”`也不应当作 C++ 规则，但本轮没有独立验证改扩展名后的加载行为，**不把这一项计入已证伪清单**。

## C. 混层（≥2 处）

### 明确需要重组的地方

| 位置 | 混了哪两根轴 | 重组方案 |
|---|---|---|
| 第 3 节 3.1“用 /P 看展开”、3.2“指令清单”；3.2 内又跳到宏坑、constexpr 替代 | 工具观察入口 / 指令种类；内部又混宏机制、反例、替代建议 | 选“预处理行为种类”为功能轴：包含 / 宏替换 / 条件选择 / 诊断与控制。`/P` 放在前置观察例；宏反例及 constexpr 比较挂在“宏替换”的更低一级。宏括号坑不是标准规则的特例，而是一般展开规则的后果 |
| 第 4 节 4.1“看汇编”、4.2“翻译单元边界”、4.3“目标文件里有什么” | 工具观察入口 / 编译作用范围规则 / 产物结构机制 | 选“编译的契约”为主轴：输入边界 / 语义与生成处理 / 输出及其用途；把 `/FA` 作为输出观察例，ABI 与优化作为该例的边界 |
| 第 11 节前三项调试手段与 11.4 安装调试器入口 | 定位手段 / 工具获取；而且 warning 在编译期，前两项在运行后或运行中 | 选“故障定位所处阶段”：构建前后的警告检查 / 运行结束的退出状态 / 运行过程的观测；每类下面再放工具手段。安装入口放附带的环境准备说明，不与定位手段并列 |
| 整章第 1–12 节 | 流程阶段（3–5）/ 操作步骤（6）/ 配置入口（7）/ 排错方法（8、11）/ 平台特例（12） | A 下一轮可考虑“流程地图→构建与启动→失败的定位”三个上位部分；不是本轮直接改节号。否则第 2 节把五阶段称主线，却不能解释后半章的同级目录 |

### 对第 1–12 节逐节判定

| 节 | 判定 | 理由或局部处理 |
|---|---|---|
| 1 | 全景例基本成立；主线宣言与后续同级标题不一致 | 先保留例与流程图，澄清“工具链简图”，上位结构问题见上表 |
| 2 | 五环按流程位置分类，表内一致 | “声明/定义”的解释宜作为编译与链接之间的规则说明；不需要因它是机制解释就另开同级章 |
| 3 | 有混层 | 见上表；宏坑不应被误归成规则的特殊例外 |
| 4 | 有混层 | 见上表 |
| 5 | 只一个 5.1 子标题，不存在同级子标题冲突 | 错误形态可按链接失败原因分类；需补 inline 的规则条件，属于事实边界 |
| 6 | 6.1–6.3 按动手步骤，6.4 注释、6.5 特例观察、6.6 警告输出已换轴 | 注释属于“解释程序”的下层，警告观察属于“编译”的下层；这是后续结构建议，本轮不搬段落 |
| 7 | 表按配置目的组织可以成立；子标题又转为“标准选择/异常模型/脚本复用” | 前两者是配置能力，脚本是配置固化的工具方式，应另挂到操作入口之下 |
| 8 | 8.1 格式入口、8.2 类别规则、8.3 排错过程是混层 | 改成“诊断提供的信息→工具继续或拒绝的策略→依据诊断定位”的层次；也可把三者降为一段解读流程的步骤 |
| 9 | 可成立 | “程序与启动环境交换的信息”轴下，退出状态与输入参数并列；规则各自在子节内讲 |
| 10 | 主表主动比较概念与关系，基本成立 | 10.1 是说明这些关系的复现实验；没有多个不同轴的同级子标题，不能机械报混层 |
| 11 | 有混层 | 见上表；前三项若定义为“定位手段”可并列，问题主要在工具安装入口及未区分阶段 |
| 12 | **不采纳“编码/路径/运行方式必然混层”的指控** | 按“平台故障种类”是同一轴；12.1/12.2 应共挂编码，再比较源解码与输出解码。12.3 字符串转义本身是跨平台语言规则，应明确“Windows 路径使这个通用问题常见”，不能说它只在 Windows 有 |

## D. 覆盖缺口（对照 [lex] / [cpp]）

“覆盖条目 0.1–0.9”不等于“完整展开 `[lex]` 和 `[cpp]` 的每一条”。本章需要承担的是工具链必需的语义与边界；数字字面量、全部关键字等可在后续语言章展开，但应有准确分配，不能把五步流程图当作标准两章的完整覆盖。

| 缺口 | 标准依据 | 该放哪一节 |
|---|---|---|
| **九阶段与五步工具链图的关系** | [`[lex.phases]/1.1–9`](https://timsong-cpp.github.io/cppwp/n4659/lex.phases) | 第 2 节补简短对照：标准是翻译语义顺序，图是工具操作；运行不在九阶段之内 |
| 源字符映射→反斜杠续行→分词/注释→预处理的先后 | `[lex.phases]/1.1–4`；[`[lex.pptoken]`](https://timsong-cpp.github.io/cppwp/n4659/lex.pptoken) | 第 2–3 节；连接编码、注释逻辑行、宏不是任意字符替换。注释已补，但先后关系仍缺 |
| 执行字符集转换与相邻字符串连接 | `[lex.phases]/1.5–6`、[`[lex.string]/13`](https://timsong-cpp.github.io/cppwp/n4659/lex.string) | 第 2 节点出位置，字符串章展开。需说明不是运行时拼接、也不是 #define 的拼接运算 |
| 模板实例化的独立概念阶段 | `[lex.phases]/1.8` | 第 2 节标“当前认识、模板章展开”；不要用汇编阶段替代它 |
| 条件编译的完整基本入口：`#if`/`#elif`/`#else`、`defined` | [`[cpp.cond]`](https://timsong-cpp.github.io/cppwp/n4659/cpp.cond) | 第 3.2 节补最低限度的选择流程；当前只列 ifdef/ifndef/endif，后来提 #if 0，却未解释分支选择 |
| C++17 的头存在性检查 `__has_include` | `[cpp.cond]/1–5` | 第 3 节“认识即可”；不要将 C++20 的模块等混入 |
| 宏的对象形式/函数形式、参数替换、重扫描与作用范围 | [`[cpp.replace]`](https://timsong-cpp.github.io/cppwp/n4659/cpp.replace)、[`[cpp.rescan]`](https://timsong-cpp.github.io/cppwp/n4659/cpp.rescan) | 第 3 节分层：先说记号与展开规则，再演示 SQUARE。全文的单个反例不等于覆盖机制 |
| 字符串化 `#`、记号拼接 `##`、可变参数宏及 `__VA_ARGS__` | [`[cpp.stringize]`](https://timsong-cpp.github.io/cppwp/n4659/cpp.stringize)、[`[cpp.concat]`](https://timsong-cpp.github.io/cppwp/n4659/cpp.concat)、`[cpp.replace]` | 第 3 节进阶索引，明确暂不展开；不要称预处理只有表内那几项 |
| `#undef`/`#error`/`#line` 只有名字没有用途 | [`[cpp.replace]`](https://timsong-cpp.github.io/cppwp/n4659/cpp.replace)、[`[cpp.error]`](https://timsong-cpp.github.io/cppwp/n4659/cpp.error)、[`[cpp.line]`](https://timsong-cpp.github.io/cppwp/n4659/cpp.line) | 第 3 节各给一句作用：撤销宏、发诊断并使程序不良构成、改变推定文件/行号。它们**不是完全没提**，只是没讲 |
| `_Pragma` 运算、空指令 `#`、预定义宏 | [`[cpp.pragma.op]`](https://timsong-cpp.github.io/cppwp/n4659/cpp.pragma.op)、[`[cpp]`语法](https://timsong-cpp.github.io/cppwp/n4659/cpp)、[`[cpp.predefined]`](https://timsong-cpp.github.io/cppwp/n4659/cpp.predefined) | 第 3 节可认识或进阶；`__FILE__`/`__LINE__` 可连接诊断，`__cplusplus` 连接标准模式但 MSVC 还要查工具开关行为 |
| **include guard 与 pragma once 未比较** | `[cpp.cond]` + `[cpp.replace]`；[`[cpp.pragma]`](https://timsong-cpp.github.io/cppwp/n4659/cpp.pragma)；[MSVC once](https://learn.microsoft.com/en-us/cpp/preprocessor/once?view=msvc-170) | 第 10 节头文件组织：保护宏使用标准指令；once 的效果是扩展。两者按 TU 防重复包含，不能修复多个 TU 各自定义同一个非 inline 函数的问题 |
| `<...>`/`"..."` 的搜索边界、header 与物理文件不等价 | [`[cpp.include]/2–4`](https://timsong-cpp.github.io/cppwp/n4659/cpp.include)、[`[headers]`脚注 168](https://timsong-cpp.github.io/cppwp/n4659/headers) | 第 3 节讲包含，第 10 节回收；具体搜索顺序依实现，不编造 GCC/Clang 本机结果 |
| 原始字符串结束模式与分隔符 | `[lex.string]`语法、/2；本轮两种 raw 实测 | 第 12.3 节补边界，详细字面量规则交给字符串章 |
| 0.1“选择与安装”仍没有安装步骤或可比较的选择说明 | 这是覆盖表项目目标，不是 `[lex]` 的规范要求 | 第 6 节当前只是使用“已安装”的工具集，第 7 节只对照开关；需承认“安装流程未展开”，或另补经过验证的安装指导 |
| 0.4 条目含优化，正文“必认四开关”表没给优化入口 | 同属覆盖表目标；`/Od`、`/O2` 为 MSVC 工具配置 | 第 7 节补优化配置及与调试信息的区别；本轮已得到可用对照证据，当前仅在第 4 节含糊提“开优化” |
| 0.6 有形参说明，但缺“传入两个实际参数→遍历对应字符串”的可用例 | `[basic.start.main]/2` 规定数据结构，教学“概念+最小例子”是覆盖表要求 | 第 9.2 节。当前空函数和第 11 节默认启动的 argc=1 不能代替实际参数解析；本轮 argv 实验可作为修订素材 |
| 0.8 的断点/单步/变量观察缺最小概念模型 | 覆盖表目标；不是标准条款要求 | 第 11 节。已坦诚没调试器，不能因此声称字面能力已经覆盖；可先给“暂停→一步→读状态”的概念，再明确实操延期 |

九阶段的简要语义顺序：字符映射 → 续行 → 预处理记号与注释 → 指令/宏 → 字面量执行字符集 → 相邻字符串连接 → 语法语义翻译 → 所需模板实例化 → 外部引用解析与链接。它是 **as-if 顺序**，不是要求工具实际启动九个进程或生成九个文件。[`[lex.phases]`](https://timsong-cpp.github.io/cppwp/n4659/lex.phases)。

对 `01a_三源交叉核对.md` 第七节的复核：**“移动语义、RAII 等主题不是整体在 C++17 才出现”这条纠正成立，不应翻回原来的错误标签。** 但“主题属于语义模型”与“某项规则在 C++17 改变”不是互斥分类；例如值类别/复制省略模型在 C++17 有规则变化。应采用“主题归属 + 具体规则版本”两条注记，避免误读成这些主题在 C++17 全部没有变化。[WG21 P0135R1](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2016/p0135r1.html)。另外，01a 使用的现代草案章号与 C++17 N4659 不同：后者 `[expr]` 是第 8 章、`[cpp]` 是第 19 章；仲裁本章时使用条款标签及版本，不能套用现代章号。

## E. 我改了哪些地方（文件 + 节号 + 一句话）

| 文件 / 位置 | 本轮处理 | FIX |
|---|---|---|
| `01_从源代码到运行.md` 第 9.2 节 | 给能独立运行、确定为空 stdout 的 main 形参示例加 `example/result` 标记；本机编译成功、退出 0，2 条未用参数警告 | FIX-01-1 |
| 同文件第 11.1 节 | 去掉输出随启动路径变化的 `argv` 示例的自动标记和前缀匹配说明；保留原代码、A 的真实运行样例以及手动验证说明 | FIX-01-1：服从本轮“完整输出确定”的判据 |
| 同文件第 6.4 节 | A 在本轮读取期间已补入两种注释与不嵌套规则及可运行例，本轮验其输出 1、2；B 只把错误的“下一节 /P”定位修成实际第 3.1 节 | FIX-01-2；不把 A 已写的内容冒称 B 新写 |
| 同文件第 6.3 节 | 明确工具集目录版本 14.51.36231 与编译器内部版本 19.51.36256.0 | FIX-01-3 |
| `_handoff/RESULT-01.md` | 新建本轮 A–G 对抗评审、复现依据与范围说明；开始时此文件不存在 | 交付物 1 |
| `_handoff/ATTACK-01-REPLY.md` | 新建一段最危险心智模型的答复 | 交付物 3 |

**实时状态差异**：REVIEW 记录的“0 块”是旧状态。B 首次读取正文时已经有 7 个标记；后续再次读取时 A 已补注释及警告例，变成 **8 个标记**（其中一个前缀匹配），覆盖表也在工作期间更新。因此没有回退 A 的这些修改。B 最终是 **8 个 exact 标记**，不是把“0→8”全部算作自己的写作量。

**本轮确定输出基线**（实际命令）：

```powershell
$env:PYTHONUTF8='1'
& C:\Users\Wang\anaconda3\python.exe ..\..\tmp\verify_cpp.py 01_从源代码到运行.md --keep -v
```

真实汇总：

```text
=== 01_从源代码到运行.md : 8 块 ===
合计 8 块 ｜ 输出一致 8 ｜ 预期编译失败 0 ｜ 无预期输出 0 ｜ 不符合预期 0
```

8 块均编译成功并输出一致；**3 条警告**：`ch01_unused_warn` 的 `C4189` 1 条，`ch01_main_args_shape` 的 `C4100` 2 条。保留的编译日志在 `../tmp/cppverify-work/`，验证汇总在 [`../tmp/ch01_verify_round2.txt`](../tmp/ch01_verify_round2.txt)。没有给 UB、多文件、函数片段或路径输出块伪造确定结果。

结构命令 `& C:\Users\Wang\anaconda3\python.exe tmp\ch01_audit.py`：**16 个二级标题、16 条目录标签与还原锚点全部逐字匹配**。REVIEW 的“15 条（0–15）”计数有误：从 0 到 15 是 16 项。正文共 **26 个 cpp 围栏块**，其中 8 个是本轮可独立运行且确定输出的标记块；其余不纳入这一基线。

独立采集的最终成功一轮共 **13 次 cl 调用，12 次退出 0、1 次按设计退出 2**（raw_bad），不是把故意失败报成成功；编译源码共 8 份，其中 7 份的对应构建成功、1 份预期拒绝。这不是重跑原任务全部八项：只复核 `/FA`、`/P`、宏，并增加终止、参数、字符串及格式边界实验。

## F. 我确信有问题但没改的（留给 A 判断，说明为什么没改）

1. 第 9.2 节 argc 下限与 argv 禁令、第 3.2 节 pragma 的标准性、第 4.1/4.3 节调试模型，依据已经在 A/B 节；请优先出 FIX-01b。它们不在当前三项 FIX 的指定正文修改位置内，故未扩张修复范围。
2. 第 0/2/3 节纯文本与“只认 #”模型、第 1/6 节 OS 入口、第 4.2 节“永远”、第 8.2 节警告等于合法行为、第 12 节条件过宽，按 B 表逐项核对后改；不能靠一条总括“说明文字已全面准确”核销。
3. include guard、条件选择入口与九阶段关系需要补知识层次，不宜本轮顺手重排整章。C 节给了可以落地的轴，D 节区分必须补与可以明确延期的部分。
4. 全局覆盖表由 A 负责，本轮没有修改；0.1/0.4/0.6/0.8 的深度缺口不应当用“表里有落点”覆盖过去。0.8 现有边界说明已经诚实，不把它污名化为偷偷遗漏，但它仍不是断点/单步教学。
5. 第 13 节自测 7 的题干写 `.\main.exe` 报错，答案却解释裸名 `main.exe` 为什么报错，前提不一致；可直接对照题干与答案复核。没有擅自改题。
6. 根索引、父目录 `_HANDOFF.md` 在本轮可写根之外；没有修改它们。目录节号和覆盖编号未因 B 改动改变，新环境事实与基线已写在本交接单，可由 A 合并进父交接文件。

## G. 诚实的空白（哪些我没验、为什么）

- 没有实测 argc==0 的本机启动方式，且不能从 Windows 常规 argc==1 推断标准下限；这项用 N4659 文本证伪。没有将构造一个普通函数调用冒充“操作系统调用 main”的实验。
- C++17 `[basic.start.main]` 未逐字写出 C 标准那段关于字符串可修改的完整措辞；因此报告不用 C 条文充当 C++ 原文。保留本机写入实验、C++ 参数类型和无禁止条款的核对结果，A 若要逐条引用可修改性的独立规范文字，仍需明确其来源。
- 未重跑链接错误、未初始化变量、编码诊断、`/WX`、调试器安装检查等原轮完整实验；这些项引用 A 原始日志时明确只是证据审查。没有声称本轮再次验证其具体诊断文字。
- 未使用调试器逐步运行，未验证全部宏诊断溯源能力、LNK 候选匹配算法、所有 shell 的 PATH/PATHEXT 特殊配置、所有非法原始字符串或不同 ABI。
- 未运行 GCC/Clang，也没有声称工具对照表已在本机验证；没有把 C++20/23 特性写进正文主干。
- 没有证明 UTF-8 管道输出等同于活动代码页 936 下的交互终端视觉显示；保留这一证据差别。
- 没有验证 `/P` 两组开关相差 129 B 的单一因果来源；报告仅陈述观测。
- 当前 `python` 命令不可用；`py -3.13` 找不到运行时；仓库 `.venv` 的基础解释器路径失效。实用替代是 **Anaconda Python 3.13.9**，C++ 仍是指定的 MSVC。未修复用户 Python 环境。
- 自写采集器最初的 `/Fa:od.asm` 与汇编解码选择曾导致产物读取失败；改为 `/Faod.asm`，编译器诊断按 UTF-8、汇编清单按 cp936 解码后**重新完整采集**，最终 `results.json` 属于成功完成的那轮，不拿前两轮的脚本退出当验证成功。原始字节另存 `.bin`。
- 保存为 `.ps1` 的 shell 复现脚本在本会话被 `AuthorizationManager` 拒绝执行；没有修改执行策略。上文 shell 输出来自同一组命令的直接执行，记录在 `ch01_shell_probe.txt`，不声称脚本文件整体通过。
- 没有提交、推送、改覆盖表状态或声称整章全部断言已通过。下一步由 A 根据本报告逐条复核并产生 REVIEW-01b / FIX-01b。
