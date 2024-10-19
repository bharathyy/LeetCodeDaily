s = "forfo"
a = "for"

ss = set(a)
print(ss)

lst = set()
n = 0
for i in range(len(s)):
    lst.add(s[i])
    
    if i >= len(a) - 1:  
        if lst == ss:
            n += 1
        
        lst.remove(s[i - (len(a) - 1)])

print(n)
