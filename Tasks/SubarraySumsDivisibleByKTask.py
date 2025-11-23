def subarraysDivByK(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    remainder_count = {0: 1}
    current_sum = 0
    result = 0

    for num in nums:
        current_sum += num
        remainder = current_sum % k

        if remainder < 0:
            remainder += k

        if remainder in remainder_count:
            result += remainder_count[remainder]
            remainder_count[remainder] += 1
        else:
            remainder_count[remainder] = 1

    return result

#https://leetcode.com/problems/subarray-sums-divisible-by-k/description/