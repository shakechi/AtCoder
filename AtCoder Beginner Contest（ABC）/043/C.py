n = int(input())
lists = list(map(int,input().split()))
sums = sum(lists)
num = int(round(sums/n,0))
cost=0
for i in lists:
    cost+=pow(i-num,2)
print(cost)
