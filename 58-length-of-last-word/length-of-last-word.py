class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_text = s.split()
        if not split_text:
            return 0
        last_word = split_text[-1]
        return(len(last_word))