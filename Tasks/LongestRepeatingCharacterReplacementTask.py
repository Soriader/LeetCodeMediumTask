def characterReplacement(self, s: str, k: int) -> int:

    left = 0
    right = 0
    max_freq = 0
    count_window = {}
    result = 0

    while right < len(s):

        if s[right] not in count_window:
            count_window[s[right]] = 1
        else:
            count_window[s[right]] += 1

        max_freq = max(max_freq, count_window[s[right]])

        while (right - left + 1) - max_freq > k:
            ch = s[left]
            count_window[ch] -= 1
            left += 1
            if count_window[ch] == 0:
                del count_window[ch]

        result = max(result, right - left + 1)

        right += 1

    return result

#https://leetcode.com/problems/longest-repeating-character-replacement/description/