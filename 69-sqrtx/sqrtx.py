class Solution:
    def mySqrt(self, x: int) -> int:
        x = x ** .5
        roundedDownNumber = math.floor(x)
        return roundedDownNumber
        