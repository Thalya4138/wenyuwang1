import math
while True:
    N = int(input())
    if N == 0:
        break
    ans = float("inf")
    for _ in range(N):
        V, T = map(int, input().split())
        if T >= 0:
            arrival = T + 4.5 / V * 3600
            ans = min(ans, arrival)
    print(math.ceil(ans))