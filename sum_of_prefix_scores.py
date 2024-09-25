class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        d={}
        lst=[]
        for i in words:
            prefix=""
            x=0
            y=len(i)
            while x<y:
                prefix+=i[x]
                if prefix not in d.keys():
                    d[prefix]=1
                    x+=1
                else:
                    d[prefix]+=1
                    x+=1
        for i in words:
            prefix=""
            x=0
            y=len(i)
            nums=0
            while x<y:
                prefix+=i[x]
                if prefix in d.keys():
                    x+=1
                    nums+=d[prefix]
            lst.append(nums)

        return lst

                
        

        
        