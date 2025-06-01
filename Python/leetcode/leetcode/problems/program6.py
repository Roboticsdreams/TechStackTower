class ZigzagConversion:
    """"
    Zigzag Conversion [Medium]

    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"

    Write the code that will take a string and make this conversion given a number of rows:

    string convert(string s, int numRows);


    Example 1:
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"

    Example 2:
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I

    Example 3:
    Input: s = "A", numRows = 1
    Output: "A"

    Constraints:
    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000
    """

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        matrix = []
        for i in range(0, numRows):
            c = []
            for j in range(0, len(s)):
                c.append('-')
            matrix.append(c)

        rows = len(matrix)
        i = 0
        j = 0
        up = 0
        down = 1

        for cnt in range(len(s)):
            if down:
                if i <= rows - 1:
                    matrix[i][j] = s[cnt]
                    i = i + 1
                else:
                    down = 0
                    up = 1
                    i = i - 1
            if up:
                if i > 0:
                    i = i - 1
                    j = j + 1
                    matrix[i][j] = s[cnt]
                else:
                    up = 0
                    down = 1
                    i = i + 1
                    matrix[i][j] = s[cnt]
                    i = i + 1

        result = ""
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != '-':
                    result += matrix[i][j]

        return result

def zigzag_main():
    p6 = ZigzagConversion()
    return p6.convert("PAYPALISHIRING",3)