def maxRotateFunction(self, nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0

    total_sum = sum(nums)

    f0 = 0
    for i in range(n):
        f0 += i * nums[i]

    result = f0
    current = f0

    for k in range(1, n):
        current = current + total_sum - n * nums[n - k]
        if current > result:
            result = current

    return result

#https://leetcode.com/problems/rotate-function/description/?envType=daily-question&envId=2026-05-01