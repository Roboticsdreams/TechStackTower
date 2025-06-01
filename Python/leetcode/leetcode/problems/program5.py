class LongestPalindromic:
    """"
    Longest Palindromic Substring [Medium]

    Given a string s, return the longest palindromic substring in s.

    Example 1:
    Input: s = "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

    Example 2:
    Input: s = "cbbd"
    Output: "bb"

    Example 3:
    Input: s = "a"
    Output: "a"

    Example 4:
    Input: s = "ac"
    Output: "a"

    Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.
    """

    def longestPalindrome(self, s: str) -> str:
        self.maxlen = 0
        self.start = 0

        for i in range(len(s)):
            self.expandFromCenter(s, i, i)
            self.expandFromCenter(s, i, i + 1)
        return s[self.start:self.start + self.maxlen]

    def expandFromCenter(self, s, l, r):
        while l > -1 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        if self.maxlen < r - l - 1:
            self.maxlen = r - l - 1
            self.start = l + 1


def longestpalindrome_main():
    p5 = LongestPalindromic()
    return p5.longestPalindrome("babad")