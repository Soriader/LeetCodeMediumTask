def lengthOfLongestSubstring(s) -> int:
    """
    :type s: str
    :rtype: int
    """

    if not s:
        return 0

    iterator = 0
    result = 0

    while iterator < len(s):

        box_for_letters = ""

        for letter in s[iterator:]:

            if letter in box_for_letters:
                break
            else:
                box_for_letters += letter

        result = max(result, len(box_for_letters))
        iterator += 1

    return result

#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/