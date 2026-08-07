class TimeMap:
    d: dict

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [[value, timestamp]]
        else:
            self.d[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        l = 0
        r = len(self.d[key]) - 1
        while l <= r:
            mid = l + (r-l) // 2
            if self.d[key][mid][1] < timestamp:
                l = mid + 1
            elif self.d[key][mid][1] > timestamp:
                r = mid - 1
            else:
                return self.d[key][mid][0]
        return self.d[key][r][0] if r >= 0 else ""
        
