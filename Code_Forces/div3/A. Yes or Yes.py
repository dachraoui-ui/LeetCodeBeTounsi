t = int(input())

while t > 0:
    t -= 1
    s = input().strip()
    
    if "YY" in s:
        print("NO")
    else:
        print("YES")
