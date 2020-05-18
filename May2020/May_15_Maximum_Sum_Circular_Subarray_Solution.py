"""
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.
(Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once. 
(Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j
with k1 % A.length = k2 % A.length.)

"""

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        k = self.Kadane(A)
        
        CS = 0
        for i in range(len(A)):
            CS += A[i]
            A[i] = -A[i]
        CS = CS+ self.Kadane(A)
        
        if CS > k and CS != 0:
            return CS
        else:
            return k
        
    def Kadane(self, nums):
        cursum, maxsum = nums[0], nums[0]
        for n in nums[1:]:
            cursum = max(n, cursum + n)
            maxsum = max(cursum, maxsum)
        return maxsum
    
