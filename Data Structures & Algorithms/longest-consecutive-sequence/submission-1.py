class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tmp = set(nums)
        res = 0

        for num in tmp:
            if num - 1 not in tmp:
                streak, curr = 0, num
                while curr in tmp:
                    streak += 1
                    curr += 1
                res = max(res, streak)
        return res
