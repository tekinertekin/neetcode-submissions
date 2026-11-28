class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for char in tasks:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
        l = [d[x] for x in d]
        mx = 0
        mx_num = 0
        for count in l:
            if count > mx:
                mx = count
                mx_num = 1
            elif count == mx:
                mx_num += 1
        area = (mx * (n+1)) - ((n+1)- mx_num)
        return max(len(tasks), area)
        