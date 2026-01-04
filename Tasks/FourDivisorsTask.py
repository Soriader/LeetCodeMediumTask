from math import isqrt

def sumFourDivisors(self, nums: list[int]) -> int:
    total = 0

    for num in nums:
        divisors = []
        for i in range(1, isqrt(num) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != num // i:
                    divisors.append(num // i)
                if len(divisors) > 4:
                    break
        if len(divisors) == 4:
            total += sum(divisors)

    return total

#https://leetcode.com/problems/four-divisors/description/?envType=daily-question&envId=2026-01-04