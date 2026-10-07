ch = input()
def pyramid(ch):
    n = ord(ch)-ord("A")+1
    for i in range(1, n + 1):
        line = " " * (n - i)
        for j in range(1, i + 1):
            line += chr(ord('A') + j - 1)
        for j in range(i - 1, 0, -1):
            line += chr(ord('A') + j - 1)
        print(line)
pyramid(ch)