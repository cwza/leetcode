
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1, version2 = version1.split('.'), version2.split('.')
        sz1, sz2 = len(version1), len(version2)
        for i in range(max(sz1, sz2)):
            if i >= sz1: version1.append('0')
            if i >= sz2: version2.append('0') 
            num1, num2 = int(version1[i]), int(version2[i])
            if num1 > num2: return 1
            if num2 > num1: return -1
        return 0

version1 = "0.1"
version2 = "1.1"
result = Solution().compareVersion(version1, version2)
assert result == -1

version1 = "1.0.1"
version2 = "1"
result = Solution().compareVersion(version1, version2)
assert result == 1

version1 = "7.5.2.4"
version2 = "7.5.3"
result = Solution().compareVersion(version1, version2)
assert result == -1

version1 = "1.01"
version2 = "1.001"
result = Solution().compareVersion(version1, version2)
assert result == 0

version1 = "1.0"
version2 = "1.0.0"
result = Solution().compareVersion(version1, version2)
assert result == 0