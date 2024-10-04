class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)==2:
            return skill[0]*skill[1]
        
        skill.sort()
        i=0
        j=len(skill)-1
        sums=skill[i]+skill[j]
        total=0
        while i<j:
            if (skill[i]+skill[j])==sums:
                total+=(skill[i]*skill[j])
                i+=1
                j-=1
            else:
                return -1
        return total




