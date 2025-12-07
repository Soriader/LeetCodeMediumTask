def lengthOfLongestSubstring(self, s) -> int:
    """
    :type s: str
    :rtype: int
    """

    if not s:
        return 0

    result = 0
    left = 0
    right = 0
    letters_in_window = set()

    while right != len(s):

        while s[right] in letters_in_window:
            letters_in_window.remove(s[left])
            left += 1

        letters_in_window.add(s[right])
        result = max(result, right - left + 1)
        right += 1

    return result

#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/