class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)
        pivot=-1
        for i in range(n-2,pivot,-1):
            if nums[i]<nums[i+1]:
                pivot=i
                break
        if pivot!=-1:
            for j in range (n-1,pivot,-1):

                if nums[j]>nums[pivot]:
                    nums[j],nums[pivot]=nums[pivot],nums[j]
                    break
        left=pivot+1
        right=n-1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1



        """
        Do not return anything, modify nums in-place instead.
        """
        