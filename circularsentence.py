class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        lst = sentence.split(" ")
        ss=[]
        for i in range(len(lst)):
            x=lst[i]
            ss.append(x[0])
            ss.append(x[-1])
        if ss[0]==ss[-1]:
            pass
        else:
            return False
        for i in range(1,len(ss)-2):
            if i%2!=0:
                if ss[i]==ss[i+1]:
                    pass
                else:
                    return False
        return True
        


             
        