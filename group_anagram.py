'''
    Intinya dari isi strs, masing2 stringnya di sorting dulu biar sesuai urutan abjad
    contoh eat sama ate kalau di sorting hasilnya jadi aet
    setelah itu, aet itu dijadikan keynya supaya eat sama ate dimasukkan ke grup yg sama

    masih agak membingungkan, nanti coba dipelajari lagi
    materi inti : hashmap, dictionary, collection, value, key
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
        