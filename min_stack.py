

arr=[18,19,29,25,16]

stack1=[]
stack2=[]
def push(i):
    stack1.append(i)
        
    if len(stack2)==0 or stack2[-1]>i:
        stack2.append(i)


def int_get_min():
    if len(stack2)==0:
        return -1
    return stack2[-1]
def pop():
    if not stack1:
        return -1
    ans=stack1.pop()
    if ans==stack2[-1]:
        stack2.pop()
    return  ans


for i in arr:
    push(i)

print("Current minimum:", int_get_min())  

pop()
print("Current minimum after pop:", int_get_min())