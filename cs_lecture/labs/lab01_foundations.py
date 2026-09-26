"""第 1—17 章：先预测输出，再运行。仅使用标准库。"""
from collections import Counter
from pathlib import Path
from tempfile import TemporaryDirectory
import re


def word_counts(text):
    """本实验只统计简单英文词；不是通用自然语言分词器。"""
    words = re.findall(r"[a-z]+", text.lower())
    return sorted(Counter(words).items(), key=lambda pair: (-pair[1], pair[0]))


def main():
    original = [[1], [2]]
    shallow = original.copy()
    shallow[0].append(9)
    print('共享内层对象：', original)
    independent = [row.copy() for row in original]
    independent[0].append(8)
    assert original == [[1, 9], [2]]
    print('逐行复制之后：', original, independent)
    assert word_counts('Tree graph TREE!') == [('tree', 2), ('graph', 1)]
    assert word_counts('') == []
    with TemporaryDirectory() as folder:
        path = Path(folder) / 'sample.txt'
        path.write_text('Graph tree graph.\nTREE algorithm.', encoding='utf-8')
        print('词频：', word_counts(path.read_text(encoding='utf-8')))
    print('实验通过。扩展：让输入文件路径由命令行指定。')


if __name__ == '__main__':
    main()
