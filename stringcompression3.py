class Solution:
    def compressedString(self, word: str) -> str:
        i,n=0,len(word) 
        finals=""
        while i<n:
            current=word[i]
            number=1
            for j in range(i+1,i+9):
                if j<len(word):
                    if word[j]==current:
                        i+=1
                        number+=1
                    else:
                        break                    
                else:
                    break
            finals+=str(number)
            finals+=current
            i+=1
        return finals

            
            