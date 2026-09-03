class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, r = 0, -1
        longest = 0
        zero = False
        while r + 1 < len(nums):
            r += 1
            if nums[r] == 0:
                while zero:
                    if nums[l] == 0:
                        zero = False
                    l += 1
                zero = True
            
            # (r - l) => (r - l + 1) - 1 => length(window) - (deleted element)
            longest = max(longest, r - l) 
        return longest
