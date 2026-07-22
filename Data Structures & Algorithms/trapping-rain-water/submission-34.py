class Solution:
    def _helper(self, height: List[int]) -> int:
        if not height:
            return 0
        global_max = height[0]
        global_max_idx = 0
        area = 0
        local_max = 0
        local_max_idx = 0
        minus_area = 0
        for i in range(0,len(height)):
            print(i, local_max_idx, local_max, minus_area, height[i])
            if height[i] >= local_max:
                if local_max:
                    area += ((i-local_max_idx) * local_max) - minus_area
                local_max = height[i]
                minus_area = 0
                local_max_idx = i
            minus_area += height[i]
        return area


    def trap(self, height: List[int]) -> int:
        global_max = 0
        global_max_idx = 0
        area = 0
        for i in range(0, len(height)):
            if height[i] >= global_max:
                global_max = height[i]
                global_max_idx = i
        area += self._helper(height[0:global_max_idx + 1])
        print("data", height[0:global_max_idx + 1])
        print("area", area)
        area += self._helper(height[global_max_idx:len(height)][::-1])
        print("data", height[global_max_idx:len(height)][::-1])
        print("area", area)
        return area

        