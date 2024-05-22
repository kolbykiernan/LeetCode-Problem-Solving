class Solution:
    def mySqrt(self, x: int) -> int:
        x = math.sqrt(x)
        roundedDownNumber = math.floor(x)
        return roundedDownNumber
        