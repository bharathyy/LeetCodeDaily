arr=[9,2,1,4]
stack=[]
output=[0]*len(arr)
for i in range(len(arr)):
    while len(stack) > 0 and stack[-1][0] <= arr[i]:
        stack.pop()

    if len(stack) == 0:
        output[i] = i + 1
    else:
        output[i] = i - stack[-1][1]

    stack.append((arr[i], i))
print(output)
