def minSubArrayLen(self, target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """

    left = 0
    right = 0
    current_sum = 0
    result = float('inf')

    while right < len(nums):
        current_sum += nums[right]

        while current_sum >= target:
            result = min(result, right - left + 1)

            current_sum -= nums[left]
            left += 1

        right += 1

    return result if result != float('inf') else 0

#https://leetcode.com/problems/minimum-size-subarray-sum/description/