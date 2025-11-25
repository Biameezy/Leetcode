class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n # we are looking for a number "diff" such that diff + n = target
            if diff in prevMap:
                 return [prevMap[diff], i]
            prevMap[n] = i     
        #complexity is O(n) - We iterate through the list exactly once.
