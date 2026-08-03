class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res_l = [len(heights) for i in heights]
        left_s = []
        left_s_idx = []
        for i in range(0, len(heights)):
            while left_s and left_s[-1] > heights[i]:
                left_s.pop()
                idx = left_s_idx.pop()
                res_l[idx] = i
            left_s.append(heights[i])
            left_s_idx.append(i)
        res_r = [-1 for i in heights]
        right_s = []
        right_s_idx = []
        for i in range(len(heights) - 1, -1, -1):
            print(i)
            while right_s and right_s[-1] > heights[i]:
                right_s.pop()
                idx = right_s_idx.pop()
                res_r[idx] = i
            right_s.append(heights[i])
            right_s_idx.append(i)
        print(res_l)
        print(res_r)
        mx = 0
        for i in range(0, len(heights)):
            area = heights[i] * ((res_l[i] - res_r[i]) - 1)
            if mx < area:
                mx=area
        return mx

        