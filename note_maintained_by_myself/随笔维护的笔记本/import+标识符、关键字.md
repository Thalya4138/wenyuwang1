##### import
◼ 使用import 语句导入模块：
	1. from math import *
		语义：导入 math 包的所有功能，并可直接可用
	2. import math
		语义：导入整个 math 包，以 math.sin, math.cos 形式使用
	3. from math import sin, cos, sqrt
		语义：导入 math 库函数 sin, cos 和 sqrt，并可直接可用
	❑ import math 后，执行 dir(math) 可列出 math 模块内容

##### 标识符、关键字
◼ 合法标识符 (identifier) 的语法要求
	 常用形式：字母开头的字母数字序列，下划线当作字母
	 区分大小写：OK, Ok, ok, oK 是不同的名字
	 允许用一般的 (非英文) unicode 字符序列，但并不建议
◼ 关键字 (keywords / reserved words)
	❑ Python 中一组特殊的名字，由语言规定
	❑ 每个关键字有其特殊意义，只能用在特定地方
	❑ 特别注意：关键字不能用作变量名
	❑ 类型名、函数名、程序包名等是普通标识符，不是关键字