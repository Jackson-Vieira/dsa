n = int(input())

for i in range(n):
    v = input()
    if len(v) > 10:
        print(v[0]+str(len(v)-2)+v[-1])
    else:
        print(v)