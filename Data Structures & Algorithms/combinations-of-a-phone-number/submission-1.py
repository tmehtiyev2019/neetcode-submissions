class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        comb = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(start, char):

            if len(digits) == 0:
                return comb

            if start == len(digits):
                comb.append(char)
                return

            for i in digitToChar[digits[start]]:
                dfs(start+1, char + i)
        dfs(0,"")
        return comb


        