'''
    Inti : 
    s sama t disorting dulu, baru di bandingkan, kalau sama berarti return True,
    kalau tidak berarti return False.
    Supaya lebih efisien, kita bisa bandingkan dulu apakah s sama t punya banyak string yang sama.

    Perlu diingat : 
    Karena s sama t itu masih dalam bentuk string, kita tidak bisa langsung pakai fungsi .sort(),
    stringnya perlu di convert jadi list dulu.

    Jadi cara lainnya itu pake fungsi sorted(), karena mengabaikan variabelnya list atau string.

'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        if sorted(s) == sorted(t) : 
            return True
        else : 
            return False   