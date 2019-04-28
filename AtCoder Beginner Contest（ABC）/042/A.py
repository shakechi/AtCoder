num = list(map(int,input().split()))

sums=0
for i in num:
    sums+=i

if sums ==17:
    print("YES")
else:
    print("NO")