"""
给你一个字符串 s，找到 s 中最长的回文子串。 



 示例 1： 

 
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
 

 示例 2： 

 
输入：s = "cbbd"
输出："bb"
 

 

 提示： 

 
 1 <= s.length <= 1000 
 s 仅由数字和英文字母组成 
 

 Related Topics 字符串 动态规划 👍 5492 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    @param s: 输入
    @return: 最长回文子串
    @时间复杂度：O(n^3)
    """

    def longestPalindrome(self, s: str):

        # 异常检测
        if s is None:
            return None

        # 最长回文子串，思路遍历字符串的长度
        for length in range(len(s), 0, -1):
            for i in range(len(s) - length + 1):

                left = i
                right = i + length - 1

                while left < right and s[left] == s[right]:
                    left = left + 1
                    right = right - 1

                if left >= right:
                    return s[i: i + length]

        return ""
# leetcode submit region end(Prohibit modification and deletion)


# leetcode submit region begin(Prohibit modification and deletion)
class Solution2:

    """
    @param s: 输入
    @return: 最长回文子串
    @方法：基于中心线的枚举法
    @时间复杂度：O(n^3)
    """

    def longestPalindrome(self, s: str):

        # 异常检测
        if not s:
            return s

        # 记录回文子串的起始点和长度
        answer = (0, 0)
        # 最长回文子串，遍历中心点
        for middle in range(len(s)):
            answer = max(answer, self.get_longest_palindrome_from(s, middle, middle))
            answer = max(answer, self.get_longest_palindrome_from(s, middle, middle + 1))

        return s[answer[1]:(answer[1] + answer[0])]

    def get_longest_palindrome_from(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1

        return right - left - 1, left + 1
# leetcode submit region end(Prohibit modification and deletion)


# leetcode submit region begin(Prohibit modification and deletion)
class Solution3:

    """
    @param s: 输入
    @return: 最长回文子串
    @方法：动态归划
    @时间复杂度：O(n^3)
    """

    def longestPalindrome(self, s: str):

        # 异常检测
        if not s:  # 相等于 s is None or s = ""
            return s

        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        for i in range(n):
            is_palindrome[i][i] = True
        for i in range(1, n):
            is_palindrome[i][i - 1] = True

        start, longest = 0, 1
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and s[i] == s[j]
                if is_palindrome[i][j] and length > longest:
                    longest = length
                    start = i

        return s[start:start + longest]

# leetcode submit region end(Prohibit modification and deletion)
