s = input()
stack =[]

for i in s:
    if i == "B":
        if stack!=[]:stack.pop()
    else:
        stack.append(i)
result="".join(stack)
print(result)
