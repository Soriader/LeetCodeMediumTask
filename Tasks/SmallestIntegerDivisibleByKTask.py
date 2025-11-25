def smallestRepunitDivByK(self, k) -> int:
    """
    :type k: int
    :rtype: int
    """

    divisor = 0

    for number_length in range(1, k + 1):

        divisor = (divisor * 10 + 1) % k
        if divisor  == 0:
            return number_length

    return -1

#https://leetcode.com/problems/smallest-integer-divisible-by-k/description/?envType=daily-question&envId=2025-11-25