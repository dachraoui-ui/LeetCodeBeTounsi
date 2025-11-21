class Solution(object):
    def convertToTitle(self, col):
        res = ""
        while(col > 0) :
            col -= 1
            last_letter = col % 26
            letter = chr(last_letter + ord('A'))
            col = col // 26
            res = res + letter
        return res[::-1]

        