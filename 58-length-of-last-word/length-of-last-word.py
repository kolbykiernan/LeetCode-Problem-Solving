class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_text = s.split()
        last_word = split_text[-1]
        return(len(last_word))