class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        prev_value = 0
        
        for i in s:
            curr_value = roman[i]
        
            if curr_value > prev_value:
                result += curr_value - 2 * prev_value 
            else:
                result += curr_value
            prev_value = curr_value
            
        return result
    
first_solution = Solution()
print(first_solution.romanToInt("III"))
print(first_solution.romanToInt("LVIII"))
print(first_solution.romanToInt("MCMXCIV"))