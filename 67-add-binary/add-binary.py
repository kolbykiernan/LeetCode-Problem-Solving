class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binary_a = int(a, 2)
        binary_b = int(b, 2)
        binary_sum = binary_a + binary_b
        return bin(binary_sum)[2:]

