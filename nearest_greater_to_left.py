arr=[2,8,6,4]
stack=[]
output=[-1]*len(arr)
n=1
for i in range(0,len(arr)):
    while len(stack)>0 and stack[-1]<arr[i]:
        stack.pop()

    if len(stack)>0: 
        output[i]=stack[-1]

    stack.append(arr[i])
    
print(output)
