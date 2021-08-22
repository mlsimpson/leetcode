class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass

    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start <= end:
            if(s[start] == s[end]):
                start += 1
                end -= 1
            else:
                print("False")
                return False

        print("True")
        return True


solution = Solution()
#print(solution.longestPalindrome("mystring"))
solution.isPalindrome("abcba") # -> True
solution.isPalindrome("a") # -> True
solution.isPalindrome("ab") # -> False
solution.isPalindrome("abc") # -> False
solution.isPalindrome("abcdcba") # -> True
