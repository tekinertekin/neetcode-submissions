class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res_l = [len(heights)] * len(heights)
        left_s_idx = []
        for i in range(0, len(heights)):
            while left_s_idx and heights[left_s_idx[-1]] > heights[i]:
                idx = left_s_idx.pop()
                res_l[idx] = i
            left_s_idx.append(i)
        res_r = [-1] * len(heights)
        right_s_idx = []
        for i in range(len(heights) - 1, -1, -1):
            while right_s_idx and heights[right_s_idx[-1]] > heights[i]:
                idx = right_s_idx.pop()
                res_r[idx] = i
            right_s_idx.append(i)
        mx = 0
        for i in range(0, len(heights)):
            area = heights[i] * ((res_l[i] - res_r[i]) - 1)
            if mx < area:
                mx=area
        return mx

        