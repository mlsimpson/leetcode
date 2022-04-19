class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

		# higher O(mem), lower O(time):
		# return sorted(s) == sorted(t)

        count_s = {}
        count_t = {}

        for index in range(len(s)):
            count_s[s[index]] = 1 + count_s.get(s[index], 0)
            count_t[t[index]] = 1 + count_t.get(t[index], 0)

        # print(count_s, count_t)

        for char in count_s:
            if count_s[char] != count_t.get(char, 0):
                return False

        return True

