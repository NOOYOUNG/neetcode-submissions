class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        for c in s :
            if(c.isalnum()) :
                filtered += c.lower()

        rs = filtered[::-1]

        return rs == filtered