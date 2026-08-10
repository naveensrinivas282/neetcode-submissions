class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        dic={}
        longest=0
        for i in nums:
            length=1
            if i-1 not in nums:
                while i+1 in nums:
                    length+=1
                    i+=1
                if length>longest:
                    longest=length
        return longest