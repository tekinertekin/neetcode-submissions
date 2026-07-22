class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        kolon = [set() for _ in range(9)]
        satir = [set() for _ in range(9)]
        kutu = [set() for _ in range(9)]
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                nmb = board[i][j]
                if nmb != ".":
                    kutu_sayisi = int(j/3) + int(i/3)*3
                    if nmb in kolon[i] or nmb in satir[j] or nmb in kutu[kutu_sayisi]:
                        return False
                    kolon[i].add(nmb)
                    satir[j].add(nmb)
                    kutu[kutu_sayisi].add(nmb)
        return True
        