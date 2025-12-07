def totalFruit(self, fruits: list[int]) -> int:
    count = {}
    left = 0
    right = 0
    result = 0

    while right < len(fruits):

        while fruits[right] not in count and len(count) == 2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1

        if fruits[right] in count:
            count[fruits[right]] += 1
        elif fruits[right] not in count and len(count) != 2:
            count[fruits[right]] = count.get(fruits[right], 0) + 1

        result = max(result, right - left + 1)
        right += 1

    return result

#https://leetcode.com/problems/fruit-into-baskets/description/