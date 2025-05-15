"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lcp = ""
        if (strs == None or len(strs) == 0):
            return lcp
        min_length = len(strs[0])
        for i in range (len(strs)):
            min_length = min(min_length, len(strs[i]))
        for i in range(0, min_length):
            current_char = strs[0][i]
            for j in range(0, len(strs)):
                if strs[j][i] != current_char:
                    return lcp
            lcp += current_char
        return lcp
