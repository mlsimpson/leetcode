# constraints:
# longest substring w/out repeating chars
# needed: substring length, start indes, end index
# list of repeated character
# max length

class Solution:
    def lengthOfLongestSubstring(self, s: str):
        if len(s) == 0:
            return 0

        charlist = set()
        maxlen = 0

        # things to check:
        # - is a character repeated? if not, end the loop
        # - if not, add it to list of chars in string
        # - are we at EOL? if so, end the loop
        for start in range(len(s)):
            #charlist.add(s[start])
            end = start
            while end < len(s):
                #print("start: ", start, s[start], " end: ", end, s[end])
                if s[end] not in charlist:
                    charlist.add(s[end])
                    end += 1
                else:
                    break
                #print(charlist)
                maxlen = max(maxlen, (end - start))
                #print("maxlen: ", maxlen)
            charlist = set()

        print("maxlen: ", maxlen)
        return maxlen



solution = Solution()
#solution.lengthOfLongestSubstring("abcdde")
solution.lengthOfLongestSubstring("abcabcbb") # -> 3 "abc"
solution.lengthOfLongestSubstring("bbbbb") # -> 1 "b"
solution.lengthOfLongestSubstring("pwwkew") # -> 3 "wke"

