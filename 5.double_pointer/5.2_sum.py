# -*- coding: utf-8 -*-
# @Time    : 2023/2/6 17:42
# @Author  : lenny
# @desc    :

# 两数之和
class Solution:

    @staticmethod
    def two_sum(nums: list[int], target: int) -> list[int]:
        records = dict()

        for index, value in enumerate(nums):
            if target - value in records:  # 遍历当前元素，并在map中寻找是否有匹配的key
                return [records[target - value], index]
            records[value] = index  # 遍历当前元素，并在map中寻找是否有匹配的key
        return []


test_obj = Solution()
print(test_obj.two_sum([2, 7, 11, 15], 9))
