def maxSumDivThree(self, nums) -> int:
    total = sum(nums)

    if total % 3 == 0:
        return total

    rem1 = sorted([x for x in nums if x % 3 == 1])
    rem2 = sorted([x for x in nums if x % 3 == 2])

    result = 0

    if total % 3 == 1:
        if rem1:
            result = max(result, total - rem1[0])
        if len(rem2) >= 2:
            result = max(result, total - rem2[0] - rem2[1])

    elif total % 3 == 2:
        if rem2:
            result = max(result, total - rem2[0])
        if len(rem1) >= 2:
            result = max(result, total - rem1[0] - rem1[1])

    return result

#https://leetcode.com/problems/greatest-sum-divisible-by-three/?envType=daily-question&envId=2025-11-23