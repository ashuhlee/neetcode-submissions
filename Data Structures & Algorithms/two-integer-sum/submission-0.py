class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            compl = target - num

            if compl in seen:
                return [seen[compl], idx]
            seen[num] = idx


