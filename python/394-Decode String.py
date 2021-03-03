from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        "Recirsove, Time: O(n), Space: O(n) for recursive stack"
        n = len(s)
        def helper(start, end):
            "returns the decoded string of s[start, end)"
            result = ""
            times = 1
            i = start
            while i < end:
                # char, directly concat it to result
                if s[i].isalpha():
                    result += s[i]
                    i += 1
                # digit, combine all following digit to a decimal and store it in "times" variable
                elif s[i].isdigit():
                    for j in range(i+1, end):
                        if not s[j].isdigit():
                            times = int(s[i:j])
                            i = j
                            break
                # left bracket, find the corresbonding ] position and recursive call helper() on the string which between []
                # add it to the result
                elif s[i] == '[':
                    num_left = 1
                    for j in range(i+1, end):
                        if s[j] == '[':
                            num_left += 1
                        elif s[j] == ']':
                            num_left -= 1
                            if num_left == 0:
                                result += helper(i+1, j) * times
                                i = j + 1
                                break
            return result
        return helper(0, n)
    # def decodeString(self, s: str) -> str:
    #     "Stack, Time: O(n), Space: O(n)"
    #     "Tricky, Please see https://blog.csdn.net/fuxuemingzhu/article/details/79332894"
    #     cur_num = 0
    #     cur_str = ""
    #     num_stack = deque()
    #     str_stack = deque()
    #     for ch in s:
    #         if ch.isalpha():
    #             cur_str += ch
    #         elif ch.isdigit():
    #             cur_num = 10 * cur_num + int(ch)
    #         elif ch == '[':
    #             num_stack.append(cur_num)
    #             str_stack.append(cur_str)
    #             cur_num = 0
    #             cur_str = ""
    #         elif ch == ']':
    #             pre_num = num_stack.pop()
    #             pre_str = str_stack.pop()
    #             cur_str = pre_str + pre_num * cur_str
    #     return cur_str

s = "3[a]2[bc]"
result = Solution().decodeString(s)
assert result == "aaabcbc"

s = "3[a2[c]]"
result = Solution().decodeString(s)
assert result == "accaccacc"

s = "2[abc]3[cd]ef"
result = Solution().decodeString(s)
assert result == "abcabccdcdcdef"

s = "abc3[cd]xyz"
result = Solution().decodeString(s)
assert result == "abccdcdcdxyz"