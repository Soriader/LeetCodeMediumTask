def findDifferentBinaryString(self, nums: list[str]) -> str:

    result = "0" * len(nums[0])
    iterator = 0
    len_of_nums = len(nums[0])
    is_in_nums = False

    while not is_in_nums:
        result = format(iterator, f'0{len_of_nums}b')

        if result not in nums:
            is_in_nums = True

        iterator += 1


    return result

#https://leetcode.com/problems/find-unique-binary-string/description/?envType=daily-question&envId=2026-03-08