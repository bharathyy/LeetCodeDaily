arr=[1,2,2,3,1]
nsl=[-1]*len(arr)

stack=[]
for i in range(len(arr)):
    while len(stack)>0 and stack[-1]>=arr[i]:
        stack.pop()
    if len(stack)==0:
        pass
    if len(stack)>0:
        if stack[-1]<arr[i]:
            nsl[i]=stack[-1]

    stack.append(arr[i])
print(nsl)
