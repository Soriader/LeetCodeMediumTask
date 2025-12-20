def maxVowels(self, s: str, k: int) -> int:

    vowels = "aeiou"
    left = 0
    right = 0
    actual_result = 0
    result = 0

    while right < len(s):

        if s[right] in vowels:
            actual_result += 1

        if actual_result > result:
            result = actual_result

        if right - left + 1 == k and s[left] in vowels:
            left += 1
            actual_result -= 1
        elif right - left + 1 == k:
            left += 1


        right += 1


    return result

#https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/