class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxor=0
        for i in range(len(nums)):
            maxor|=nums[i]
        count=[0]
        self.backtrack(nums,0,0,maxor,count)
        return count[0]
        

    def backtrack(self,nums,index,currentxor,maxor,count):
        if currentxor==maxor:
            count[0]+=1
        for i in range(index,len(nums)):
            self.backtrack(nums,i+1,currentxor|nums[i],maxor,count)
    
    
        