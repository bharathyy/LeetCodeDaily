class Solution:
    def makeFancyString(self, s: str) -> str:
        
        n = len(s)
        i = 0
        ss = ""
        cur = ""
        k = 0

        while i < n:
            # If the current character matches the previous one
            if cur == s[i]:
                if k < 2:  # Only add if we have fewer than two consecutive characters
                    ss += s[i]
                    k += 1
            else:
                # Reset for a new character sequence
                cur = s[i]
                ss += s[i]
                k = 1  # Start counting new sequence

            i += 1  # Move to the next character

        return ss
