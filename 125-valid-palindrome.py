class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

# or

def isPalindrome(s):
    # filter non alphanumeric chars from string in place
    # s = ''.join(c for c in s if c.isalnum())
    s = ''.join(filter(str.isalnum, s))

    return (s == s[::-1])

