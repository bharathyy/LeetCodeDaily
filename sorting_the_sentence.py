class Solution:
    def sortSentence(self, s: str) -> str:
        lst=s.split(" ")
        d={}
        for i,j in enumerate(lst):
            curr=""
            curr_num=0
            for x in j:
                if x.isdigit():
                    curr_num=x
                else:
                    curr+=x
            d[curr_num]=curr

        ss=""
        for key in sorted(d):
            ss+=d[key]
            ss+=" "
        ss = ss.strip() 
        return ss