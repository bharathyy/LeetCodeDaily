arr=[[1,0,1,0],[1,1,1,1]]
hist=[]
finals=[]
col=len(arr[0])
row=len(arr)
for i in range(0,col):
    hist.append(arr[0][i])

finals.append(hist)

for i in range(1,row):
    hist=[]
    for j in range(0,col):
        if arr[i][j]==0:
            hist.append(0)
        else:
            hist.append(finals[i-1][j]+arr[i][j])

    finals.append(hist)
        
    
    print(finals)



def MAH(arr,lst):
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

    finals=[]
    for i in range(len(arr)):
        if ngr[i]==-1 or ngl[i]==-1:
            sums=1*arr[i]
            finals.append(sums)
        else:

            sums=ngr[i]-ngl[i]-1
            sums=sums*arr[i]
            finals.append(sums)

    lst.append(max(finals))



lst=[] 
for i in finals:
    MAH(i,lst)
print(lst)