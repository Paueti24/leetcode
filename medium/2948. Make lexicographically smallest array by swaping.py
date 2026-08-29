class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        k = limit
        array_tup = list(enumerate(nums))
        array_tup.sort(key=lambda item: item[1]) # sort nums in ascending order
        i = 0
        while i < n: # find groups [i,j) in O(n) and rearrange their elements in order
            j = i + 1
            while j < n and array_tup[j-1][1] + k >= array_tup[j][1]:
                j += 1
            
            idxs = [item[0] for item in array_tup[i:j]]
            idxs.sort()
            for idx, (_, val) in zip(idxs, array_tup[i:j]):
                nums[idx] = val
            i = j
        return nums
