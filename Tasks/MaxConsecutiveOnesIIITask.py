def longestOnes(self, nums: list[int], k: int) -> int:

    l = 0
    r = 0
    zero_count = 0
    result = 0

    while r < len(nums):

        if nums[r] == 0:
            zero_count += 1

        while zero_count > k:

            if nums[l] == 0:
                zero_count -= 1

            l += 1


        result = max(result, r - l + 1)
        r += 1

    return result

#https://leetcode.com/problems/max-consecutive-ones-iii/description/