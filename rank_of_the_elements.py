from collections import Counter
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        lst=Counter(arr)
        d={}
        j=1
        for i in sorted(lst):
            d[i]=j
            j+=1
        
        lsts=[]
        for i in arr:
            lsts.append(d[i])
        return lsts
