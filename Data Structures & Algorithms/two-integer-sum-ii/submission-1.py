class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i,n in enumerate(numbers):
            if target-n in seen:
                return [numbers.index(target-n)+1, i+1]
            seen[n]=0