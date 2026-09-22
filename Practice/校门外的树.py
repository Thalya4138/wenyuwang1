L, M = map(int, input().split())
S=set()
areas = []
for _ in range(M):
    a, b = map(int, input().split())
    sets=set(range(a,b+1))
    areas.append(sets)
for i in range(M):
    S |= areas[i]
print(L+1-len(S))

#集合的运算
#A & B    # 交集：两个集合共有的元素
#A | B    # 并集：两个集合所有元素，重复只算一次
#A - B    # 差集：A里有、B里没有
#A ^ B    # 对称差：只在其中一个集合里的元素
#set(range(start, end + 1))