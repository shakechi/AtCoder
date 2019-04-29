N,_ = map(int,input().split())
lists=list(map(str,input().split()))

for i in range(N,100000):
    flg=True
    for j in str(i):
        if j in lists:
            flg = False
            break
    if flg:
        print(i)
        break