lists = list(map(int,input().split()))
lists.sort()
c= lists.pop()
a,b= lists.pop(),lists.pop()
if a+b==c:
    print("Yes")
else:
    print("No")