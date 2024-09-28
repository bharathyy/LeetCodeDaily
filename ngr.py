arr=[6,2,5,4,5,1,6]
ngr=[-1]*len(arr)

stack=[]
for i in range(len(arr)-1,-1,-1):

    while len(stack)>0 and stack[-1]<=arr[i]:
        stack.pop()
    if len(stack)==0:
        pass
    if len(stack)>0:
        if stack[-1]>arr[i]:
            ngr[i]=stack[-1]
        
    

    stack.append(arr[i])
print(ngr)
