m, n = map(int, input().split(" "))
a = m * n
print(a//2 if a%2 == 0 else ((a-1)//2))