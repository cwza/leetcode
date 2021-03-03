from typing import List

# nums = [
#     12, 23, 34, 45, 56, 67, 78, 89,
#     123, 234, 345, 456, 567, 678, 789,
#     1234, 2345, 3456, 4567, 5678, 6789,
#     12345, 23456, 34567, 45678, 56789,
#     123456, 234567, 345678, 456789,
#     1234567, 2345678, 3456789,
#     12345678, 23456789,
#     123456789,
# ]

def generate_nums():
    "Using sliding window to generate all nums."
    digits = '123456789'
    nums = []
    for window_sz in range(2, 10):
        i, j = 0, window_sz
        while j <= len(digits):
            nums.append(int(digits[i:j]))
            i += 1
            j += 1
    return nums

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = generate_nums()
        return [num for num in nums if num>=low and num<=high]

low = 100
high = 300
result = Solution().sequentialDigits(low, high)
assert result == [123,234]

low = 1000
high = 13000
result = Solution().sequentialDigits(low, high)
assert result == [1234,2345,3456,4567,5678,6789,12345]