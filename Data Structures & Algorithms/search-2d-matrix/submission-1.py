class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        min = 0 # matrix[0][0] = first entry of matrix value, but we need the index
        max = rows - 1 # last entry of matrix value: matrix[rows - 1 ][cols - 1]

        while min <= max:
            mid = (min + max) // 2
            if target > matrix[mid][-1]: # target is bigger than last elem in this row, so must be in row below (upper bound)
                min = mid + 1
            elif target < matrix[mid][0]: # target is smaller than first elem, so must be in row above (lower bound)
                max = mid - 1
            else:
                # target is in this row, this is the row we binary search ! 
                mini = 0 #matrix[mid][0]
                maxi = cols - 1 # value = matrix[mid][-1]
                while mini <= maxi:
                    middle = (mini + maxi) // 2
                    val = matrix[mid][middle]  # look up the actual value
                    if target > val:
                        mini = middle + 1
                    elif target < val:
                        maxi = middle - 1
                    else:
                        return True  # found it!
                return False
        return False