class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in temperatures]
        s = []
        s_idx = []
        for i in range(0, len(temperatures)):
            print("a",s)
            while s and s[-1] < temperatures[i]:
                print(s)
                s.pop()
                idx = s_idx.pop()
                res[idx] = i - idx
            s.append(temperatures[i])
            s_idx.append(i)
        return res
        