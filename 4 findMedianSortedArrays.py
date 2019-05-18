#!/usr/bin/python3
# Author fengru
# -*- coding:utf-8 -*-
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        size = len(nums)

        if size % 2 == 1:
            return nums[size//2]

        if size % 2 == 0:
            return (nums[size//2] + nums[size//2 - 1])/2
if __name__ == '__main__':
    # nums1 = [1, 3]
    # nums2 = [2]

    nums1 = [1, 2]
    nums2 = [3, 4]
    s = Solution()
    median_num = s.findMedianSortedArrays(nums1, nums2)
    print(median_num)
