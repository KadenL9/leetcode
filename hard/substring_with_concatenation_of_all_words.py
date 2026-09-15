class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        indices = []
        words = sorted(words)
        wordlen = len(words[0])
        concatlen = len(words) * wordlen
        for x in range(len(s) - concatlen + 1):
            # determine if is a concatenation
            sample = s[x: x + concatlen]
            sample_words = [sample[i * wordlen: i * wordlen + wordlen] for i in range(len(words))]

            sample_words = sorted(sample_words)
        
            if words == sample_words:
                indices.append(x)
        
        return indices