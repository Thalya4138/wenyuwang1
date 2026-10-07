
Python 自带的查询工具主要有 `help()`、`dir()`、`.__doc__`，再往后一点是 `inspect`。
## 1. `help()`
```
help(函数名)
```
比如：
```
help(print)
help(len)
help(str.split)
help(dict.get)
```
它会告诉你这个函数的参数、作用和说明。  
例如：
```
help(dict.get)
```
你会看到类似：
```
get(self, key, default=None, /)
```
意思就是：
```
字典.get(key, 默认值)
```
如果没有这个 key，就返回默认值，默认值没写时就是 `None`。
## 2. `dir()`
如果你想看一个对象“都有哪些方法”，用：
```
dir(对象)
```
比如：
```
dir(str)
```
会看到字符串能用的很多方法：
```
split
strip
replace
lower
upper
find
...
```
或者：
```
s = "hello"
dir(s)
```
也可以。
## 3. `.__doc__`
如果你已经知道函数名，只想快速看说明，可以：
```
print(str.split.__doc__)
```
比如：
```
print(dict.get.__doc__)
```
`.__doc__` 就是这个函数自带的 documentation string（文档字符串）。
## 4. `type()`
还有一个特别好用的：
```
type(x)
```
可以先看看一个东西到底是什么类型：
```
x = [1, 2, 3]
print(type(x))
# <class 'list'>
```
然后：
```
dir(list)
```
看 `list` 能干什么。
## 5. 查询思路
```
不知道它是什么
→ type(x)

知道类型，不知道有哪些方法
→ dir(x) 或 dir(type)

知道方法名，不知道怎么用
→ help(...)

只想快速看说明
→ .__doc__
```
比如你忘了 `split()`：
```
help(str.split)
```
忘了字典有什么：
```
dir(dict)
```
忘了 `get`：
```
help(dict.get)
```
## 6. `inspect.signature()`
如果以后开始看稍微复杂一点的库，还可以用：
```
import inspect
print(inspect.signature(print))
```
或者：
```
import inspect
print(inspect.signature(str.replace))
```
它主要用于看函数参数形式。
## 7. `help()` 的字符串查询
在 Python 交互环境里还可以：
```
help("str")
```
甚至：
```
help("dict.get")
```
也可以查。
## 核心记忆
```
type(x)       # 这是什么
dir(x)        # 它有什么
help(x)       # 它怎么用
```
这三个基本就是 Python 自带的“随身说明书”。