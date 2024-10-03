class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum=sum(nums)
        remainder=total_sum%p
        if remainder==0:
            return 0
        
        prefix_sum=0
        mod={0:-1}
        min_length=len(nums)
        for i,num in enumerate(nums):
            prefix_sum+=num
            prefix_mod=prefix_sum%p
            target=(prefix_mod-remainder)%p
            if target in mod:
                min_length = min(min_length, i - mod[target])

            mod[prefix_mod]=i

        if min_length==len(nums):
            return -1
        return min_length

        