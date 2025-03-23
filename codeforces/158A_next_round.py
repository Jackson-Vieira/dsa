n, k = input().split(" ")
ps = input().split(" ")
print(len([i for i in ps if int(i) >= int(ps[int(k)-1]) and int(i) > 0]))