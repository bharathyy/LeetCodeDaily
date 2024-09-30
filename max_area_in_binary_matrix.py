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



def MAH(arr):
    