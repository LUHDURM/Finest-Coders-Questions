class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        rows , cols = len(matrix),len(matrix[0])
        left , right = 0,rows * cols - 1
        while(left<=right):
            mid = (left+right) // 2
            mid_point = matrix[mid // cols][mid % cols]

            if target == mid_point:
                return True
            elif target < mid_point:
                right = mid - 1
            elif target > mid_point:
                left = mid + 1

        return False 
