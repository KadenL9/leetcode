class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minimum = min([len(s) for s in strs])
        for x in range(minimum):
            common = strs[0][x]
            for s in strs:
                if s[x] != common:
                    return strs[0][:x]

        return strs[0][:minimum]