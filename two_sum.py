'''
    Intinya :
    Jumlahkan angka didalam list satu sama lain, tapi tidak boleh angka yang sama.
    Bikin nested loops, i sama j supaya tidak ada penjumlahan ganda.
    i dimulai dari 0 sampe akhir list, j dimulai dari setelah i (i + 1).
    
    Kalau ketemu nilai di index i sama j ketika dijumlahkan sama dengan target,
    langsung return i sama j-nya.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]