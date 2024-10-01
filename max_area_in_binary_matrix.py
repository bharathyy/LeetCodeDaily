arr = [[1, 0, 1, 0], [1, 1, 1, 1]]  # Your matrix
hist = []
finals = []
col = len(arr[0])
row = len(arr)

for i in range(0, col):
    hist.append(arr[0][i])
finals.append(hist)

for i in range(1, row):
    hist = []
    for j in range(0, col):
        if arr[i][j] == 0:
            hist.append(0)
        else:
            hist.append(finals[i-1][j] + arr[i][j])
    finals.append(hist)

print("Histograms (Finals):")
for row in finals:
    print(row)

def MAH(arr):
    n = len(arr)
    nsl = [-1] * n  # Nearest Smaller to Left (store indices)
    nsr = [n] * n   # Nearest Smaller to Right (store indices)

    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            nsl[i] = stack[-1]
        stack.append(i)

    stack = []
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            nsr[i] = stack[-1]
        stack.append(i)

    max_area = 0
    for i in range(n):
        width = nsr[i] - nsl[i] - 1  # Width of the largest rectangle
        area = width * arr[i]        # Area of the rectangle
        max_area = max(max_area, area)

    return max_area

lst = []
for i in finals:
    lst.append(MAH(i))



print("Maximum Rectangle Area:", max(lst))
