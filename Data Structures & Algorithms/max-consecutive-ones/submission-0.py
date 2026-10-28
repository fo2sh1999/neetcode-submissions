class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0 
        results =[]
        for num in nums:
            if num ==1:
                count +=1
            else:
                results.append(count)
                count = 0
        if nums and nums[-1]==1:
            results.append(count)
        return max(results)if results else 0