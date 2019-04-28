N, L = map(int,input().split())
lists = []
for i in range(N):
    lists.append(input())

lists.sort()

s=""
for i in lists:
    s+=i
print(s)