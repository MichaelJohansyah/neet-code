'''
    intinya : 
    Langsung sorting list dulu, terus bandingkan nilai dari elemen di
    index i dengan index di sebelahnya, bisa sebelah kiri (i - 1), atau 
    sebelah kanan (i + 1). Kalau nilainya sama, berarti ada nilai duplikat.
'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False