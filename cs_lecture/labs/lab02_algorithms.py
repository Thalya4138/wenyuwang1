"""第 18—32 章正文算法及小规模独立对照验证。仅标准库。"""


import sys

def solve(text):
    nums = list(map(int, text.split()))
    if not nums:
        return ''
    n = nums[0]
    if len(nums) != n + 1:
        raise ValueError('输入数量与 n 不一致')
    return str(sum(nums[1:]))

def rotate_clockwise(a):
    if not a:
        return []
    n, m = (len(a), len(a[0]))
    if any((len(row) != m for row in a)):
        raise ValueError('矩阵每行长度必须相同')
    out = [[0] * n for _ in range(m)]
    for r in range(n):
        for c in range(m):
            out[c][n - 1 - r] = a[r][c]
    return out

def brackets_ok(text):
    stack = []
    closing = {')': '(', ']': '[', '}': '{'}
    for ch in text:
        if ch in '([{':
            stack.append(ch)
        elif ch in closing:
            if not stack or stack.pop() != closing[ch]:
                return False
    return not stack

def lower_bound(a, target):
    lo, hi = (0, len(a))
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo

def next_greater(a):
    answer = [-1] * len(a)
    stack = []
    for i, x in enumerate(a):
        while stack and a[stack[-1]] < x:
            answer[stack.pop()] = i
        stack.append(i)
    return answer

def subsets(a):
    out, path = ([], [])

    def dfs(i):
        if i == len(a):
            out.append(path.copy())
            return
        dfs(i + 1)
        path.append(a[i])
        dfs(i + 1)
        path.pop()
    dfs(0)
    return out

import heapq

def largest_k(values, k):
    if k <= 0:
        return []
    heap = []
    for x in values:
        if len(heap) < k:
            heapq.heappush(heap, x)
        elif x > heap[0]:
            heapq.heapreplace(heap, x)
    return sorted(heap, reverse=True)

class DSU:

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a, b = (self.find(a), self.find(b))
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = (b, a)
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True

from collections import deque

def bfs_path(graph, start, goal):
    parent = {start: None}
    q = deque([start])
    while q:
        u = q.popleft()
        if u == goal:
            path = []
            while u is not None:
                path.append(u)
                u = parent[u]
            return path[::-1]
        for v in graph.get(u, []):
            if v not in parent:
                parent[v] = u
                q.append(v)
    return None

import heapq
from math import inf

def dijkstra(graph, source):
    dist = [inf] * len(graph)
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        du, u = heapq.heappop(heap)
        if du != dist[u]:
            continue
        for v, w in graph[u]:
            if w < 0:
                raise ValueError('Dijkstra 要求非负边权')
            nd = du + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist

def knapsack01(items, capacity):
    dp = [0] * (capacity + 1)
    for weight, value in items:
        if weight <= 0:
            raise ValueError('此实现要求正重量')
        for c in range(capacity, weight - 1, -1):
            dp[c] = max(dp[c], dp[c - weight] + value)
    return dp[capacity]

def kmp_positions(text, pattern):
    if not pattern:
        return list(range(len(text) + 1))
    pi = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    out, j = ([], 0)
    for i, ch in enumerate(text):
        while j and ch != pattern[j]:
            j = pi[j - 1]
        if ch == pattern[j]:
            j += 1
        if j == len(pattern):
            out.append(i - j + 1)
            j = pi[j - 1]
    return out

class Fenwick:

    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, i, delta):
        if not 1 <= i <= self.n:
            raise IndexError(i)
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def prefix(self, i):
        if not 0 <= i <= self.n:
            raise IndexError(i)
        total = 0
        while i:
            total += self.tree[i]
            i -= i & -i
        return total


def self_test():
    import random
    import bisect
    from itertools import combinations
    rng = random.Random(20)
    checks = 0
    for _ in range(200):
        n = rng.randrange(10)
        a = sorted(rng.randrange(-5, 6) for _ in range(n))
        target = rng.randrange(-6, 7)
        assert lower_bound(a, target) == bisect.bisect_left(a, target)
        checks += 1
        k = rng.randrange(0, 12)
        assert largest_k(a, k) == sorted(a, reverse=True)[:k]
        checks += 1
        shuffled = a.copy()
        rng.shuffle(shuffled)
        expected = [next((j for j in range(i+1,n) if shuffled[j]>shuffled[i]), -1)
                    for i in range(n)]
        assert next_greater(shuffled) == expected
        checks += 1
        text = ''.join(rng.choice('abc') for _ in range(n))
        pattern = ''.join(rng.choice('abc') for _ in range(rng.randrange(5)))
        expected = [i for i in range(len(text)+1) if text.startswith(pattern,i)]
        assert kmp_positions(text, pattern) == expected
        checks += 1
        items = [(rng.randrange(1,6),rng.randrange(0,12)) for _ in range(n)]
        capacity = rng.randrange(15)
        best = max((sum(items[i][1] for i in range(n) if mask>>i&1)
                    for mask in range(1<<n)
                    if sum(items[i][0] for i in range(n) if mask>>i&1)<=capacity),default=0)
        assert knapsack01(items, capacity) == best
        checks += 1
    for _ in range(40):
        n = rng.randrange(1,8)
        graph = [[] for _ in range(n)]
        ref = [[float('inf')]*n for _ in range(n)]
        for i in range(n):
            ref[i][i] = 0
            for j in range(n):
                if i != j and rng.random()<0.3:
                    weight = rng.randrange(0,10)
                    graph[i].append((j,weight))
                    ref[i][j] = weight
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    ref[i][j] = min(ref[i][j],ref[i][k]+ref[k][j])
        for source in range(n):
            assert dijkstra(graph,source) == ref[source]
            checks += 1
    f = Fenwick(20)
    data = [0]*20
    for _ in range(200):
        index,delta = rng.randrange(20),rng.randrange(-10,11)
        data[index] += delta
        f.add(index+1,delta)
        end = rng.randrange(21)
        assert f.prefix(end) == sum(data[:end])
        checks += 1
    assert brackets_ok('a{b[c](d)}')
    assert not brackets_ok('([)]')
    assert rotate_clockwise([[1,2,3],[4,5,6]]) == [[4,1],[5,2],[6,3]]
    assert bfs_path({0:[1],1:[2],2:[]},0,2) == [0,1,2]
    assert bfs_path({0:[]},0,1) is None
    assert {tuple(s) for s in subsets([1,2,3])} == {
        tuple(c) for k in range(4) for c in combinations([1,2,3],k)}
    dsu = DSU(4)
    assert dsu.union(0,1) and dsu.union(1,2)
    assert not dsu.union(0,2)
    assert dsu.find(0) == dsu.find(2) != dsu.find(3)
    print(f'通过 {checks} 个随机对照检查及 9 个确定性检查。')
    print('随机测试不是证明；正文给出各算法前提和不变量。')


if __name__ == '__main__':
    self_test()
