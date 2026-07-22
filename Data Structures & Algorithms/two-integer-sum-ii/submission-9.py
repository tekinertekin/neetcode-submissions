class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        middle_idx = -1
        for i in range(0,len(numbers)):
            if numbers[i] <= target // 2:
                middle_idx = i
            else:
                break
        last_point = middle_idx
        for i in range(middle_idx + 1, len(numbers)):
            j = last_point
            while True:
                print(numbers[i])
                print(numbers[j])
                print("end")
                if numbers[i] + numbers[j] == target:
                    return [j+1, i+1]
                elif numbers[i] + numbers[j] < target:
                    last_point = j + 1
                    break
                j -= 1



        