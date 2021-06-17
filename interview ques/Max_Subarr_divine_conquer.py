class Solution:
    def max_crossing_subarr(self, nums, l, m, r):
        arr = nums
        left_sum = -100000
        sum_ = 0 
        for i in range(m, l-1, -1):
            sum_ += arr[i]
            if (sum_ > left_sum):
                left_sum = sum_
        right_sum = -100000
        sum_ = 0
        for i in range (m+1, r+1):
            sum_ += arr[i]
            if (sum_ > right_sum):
                right_sum = sum_
        return (left_sum + right_sum)
    def maxSubArray(self, nums, l, r) -> int:
        arr = nums 
        if (l == r):
            return arr[l]
        else:
            m = (l+r)//2
            max_left = self.maxSubArray(arr, l, m)
            max_right = self.maxSubArray(arr, m +1, r)
            max_cross = self.max_crossing_subarr(arr, l, m, r)
        return max(max_left, max_right, max_cross)

arr = [-2,1,0,4,-1,2,1,-5,7]
n = len(arr) - 1
kq = Solution()
print (kq.maxSubArray(arr, 0, n))