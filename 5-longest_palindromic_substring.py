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

    def isPalindrome2(self, s: str) -> bool:

        if s == s[::-1]:
            print("True")
            return True

        print("False")
        return False

solution = Solution()
#print(solution.longestPalindrome("mystring"))
solution.isPalindrome2("abcba") # -> True
solution.isPalindrome("a") # -> True
solution.isPalindrome("ab") # -> False
solution.isPalindrome("abc") # -> False
solution.isPalindrome("abcdcba") # -> True

