tx = 2
ty = 2
r = None
for i in range(5):
    mp = input().split(" ")
    if "1" in mp:
        for k in range(5):
            if mp[k] == "1":
               r = abs(i-2)+abs(k-2)

print(r)
