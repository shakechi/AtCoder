s = input()
target = set(s)
flg=True

for i in target:
    if s.count(i) % 2 != 0:
        print("No")
        flg=False
        break
if flg:
    print("Yes")