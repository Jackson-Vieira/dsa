n = int(input())

t = 0
for i in range(n):
    v = input()
    s = sum([int(k) for k in v.split(" ")])
    if s >= 2:
        t += 1
print(t)