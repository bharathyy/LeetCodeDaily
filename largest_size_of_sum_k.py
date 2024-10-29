arr = [4,1,5]
k=5
i,j=0,0
sum_=0
n=0
length = float('-inf')
while j<len(arr):
    sum_+=arr[j]
    n+=1
    if sum_ < k:
        j+=1
    elif sum_ == k:
        length = max(length , n)
        if n>1:
            n-=1
        sum_-= arr[i]
        j=i+2
        i=j
    else:
        sum_-= arr[i]
        j=i+2
        i=j
        

print(length)


