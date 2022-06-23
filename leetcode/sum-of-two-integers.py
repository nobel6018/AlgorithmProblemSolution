# https://leetcode.com/problems/sum-of-two-integers

# Given two integers a and b, return the sum of the two integers without using the operators + and -.

a = 1
b = 2

Q1 = a & b
Q3 = a ^ b
Q2 = Q3 & carry
carry = Q1 | Q2
sum = carry & Q3

MASK = 0xFFFFFFFF
a_bin = bin(a & MASK)[2:].zfill(32)

class Solution:
    def getSum(self, a: int, b: int) -> int:
