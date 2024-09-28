arr=[6,2,5,4,5,1,6]
ngr=[-1]*len(arr)

stack=[]
for i in range(len(arr)-1,-1,-1):

    while len(stack)>0 and stack[-1][0]>=arr[i]:
        stack.pop()
    if len(stack)==0:
        pass
    if len(stack)>0:
        if stack[-1][0]<arr[i]:
            ngr[i]=stack[-1][1]
        
    stack.append((arr[i],i))


ngl=[-1]*len(arr)

stack=[]
for i in range(len(arr)):
    while len(stack)>0 and stack[-1][0]>=arr[i]:
        stack.pop()
    if len(stack)==0:
        pass
    if len(stack)>0:
        if stack[-1][0]<arr[i]:
            ngl[i]=stack[-1][1]
        
    stack.append((arr[i],i))

print(ngl)
print(ngr)
finals=[]
for i in range(len(arr)):
    if ngr[i]==-1 or ngl[i]==-1:
        sums=1*arr[i]
        finals.append(sums)
    else:

        sums=ngr[i]-ngl[i]-1
        sums=sums*arr[i]
        finals.append(sums)

print(finals)
print(max(finals))
