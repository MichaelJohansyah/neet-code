class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}                                  # Membuat dictionary count untuk simpan banyak munculnya setiap angka
        freq = [[] for i in range(len(nums) + 1)]   # Menggunakan teknik list comprehension untuk membuat list bernama freq, dengan
                                                    # ukuran sepanjang len(nums) + 1, lalu di setiap elemen dalam list freq itu isinya
                                                    # list kosong []. Kode alternatif lain ada di bawah, tapi teknik ini lebih ringkas.

        for num in nums:                            
            count[num] = 1 + count.get(num, 0)      # Mulai hitung berapa kali setiap angka muncul dalam nums
        for num, cnt in count.items():              # Setelah dapat data banyak countnya, dimasukkanlah ke list freq.
            freq[cnt].append(num)                   # Misal kalau ada angka 3 muncul 2 kali, angka 3 itu masuk ke freq[2]
        
        res = []                                    # Membuat list res untuk menyimpan nilai angka berdasarkan jumlah muncul terbanyak
        for i in range(len(freq) - 1, 0, -1):       # Iterasi mundul dari indeks terbesar list freq (mulai dari len(freq) - 1, berhenti waktu sampai 0, index berkurang 1 setiap step) 
            for num in freq[i]:                     # Karena nilai di dalam freq[i] bisa lebih dari 1 angka, jadi dilakukan loop lagi dalam setiap freq[i]-nya.
                res.append(num)                     # Masing-masing angka dimasukkan ke list res, dari yang muncul terbanyak
                if len(res) == k:                   # Kalau len(res) == k berarti isi res sudah sebanyak k, jadi program selesai dan return nilai res.
                    return res
                
"""
Alternatif dari teknik list comprehension untuk buat list freq : 

freq = []
for i in range(len(nums) + 1):
    freq.append([])

"""