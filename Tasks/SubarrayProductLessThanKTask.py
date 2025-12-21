def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:

    if k <= 1:
        return 0

    result = 0
    left = 0
    right = 0
    actual_result = 1

    while right < len(nums):

        actual_result *= nums[right]

        while actual_result >= k:
            actual_result /= nums[left]
            left += 1

        result += right - left + 1

        right += 1

    return result


#https://leetcode.com/problems/subarray-product-less-than-k/