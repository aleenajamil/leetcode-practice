class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1= set(nums1) 
        s2=set(nums2)
        num1_distinct= list(s1-s2)
        num2_distinct= list(s2-s1)
        return [num1_distinct, num2_distinct]