class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = []
        for i in range(0, len(position)):
            l.append([position[i], speed[i]])
        l.sort(key=lambda item: item[0])
        s = []
        for i in range(0, len(l)):
            arrive = (target - l[i][0]) / l[i][1]
            while s and s[-1] <= arrive:
                s.pop()
            s.append(arrive)
        return len(s)