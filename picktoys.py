s = "abaccab"
i, j = 0, 0
n = len(s)
max_length = 0
ss = {}

while j < n:
    # Add current character to the dictionary and increment count
    ss[s[j]] = ss.get(s[j], 0) + 1
    
    # Check if the substring has more than 2 distinct characters
    while len(ss) > 2:
        # Reduce count of the character at the start
        ss[s[i]] -= 1
        # Remove character from set if count becomes zero
        if ss[s[i]] == 0:
            del ss[s[i]]
        i += 1  # Slide the window from the left
    
    # Update max_length to the current length of the valid substring
    max_length = max(max_length, j - i + 1)
    j += 1

print(max_length)
