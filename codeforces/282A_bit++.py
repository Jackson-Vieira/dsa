v=0
for i in range(int(input())):
    s = input()  
    if s[1] == "+":
        v += 1
    else:
        v -= 1
print(v)