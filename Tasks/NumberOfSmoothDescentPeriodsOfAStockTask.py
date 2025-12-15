def getDescentPeriods(self, prices: list[int]) -> int:


    iterator = 1
    result = 0
    for i in range(len(prices) - 1):
        if prices[i] - 1 == prices[i + 1]:
            iterator += 1
        else:
            result += iterator * (iterator + 1) // 2
            iterator = 1
    result += iterator * (iterator + 1) // 2

    return result

#https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/description/?envType=daily-question&envId=2025-12-15
