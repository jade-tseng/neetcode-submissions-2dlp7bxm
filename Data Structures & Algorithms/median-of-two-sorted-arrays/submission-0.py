class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        nums1:  [1, 3 | 8, 9, 15]        ← 2 on left
        nums2:  [7, 11, 18, 19 | 21, 25] ← 4 on left
                 LEFT half      | RIGHT half
        right partition:
        nums1:  [1, 3, 8, 9 | 15]        ← 4 on left
        nums2:  [7, 11 | 18, 19, 21, 25] ← 2 on left
        # median of 11 numbers is the 6th, max of Aleft and Bleft ? 9 or 11, its 11
        # say only 10 numbers, then we want 1234 56 78910. (5+6 / 2)

        3 <= 21 and 19 <= 8 -> not true, so we go to elif

        9 <= 18 and 11 <= 15 -> true, so we check if our nums1 + nums 2 are even
        this is not even, so we want median to be 
        
        nums1 move to right, nums2 move to left
        """
        # we know (index of the median, how many nums on the left of partition):
        total = len(nums1) + len(nums2)
        half = (total + 1) // 2

        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1
            
        # Together they contribute (i+1) + (j+1) = half elements to the left half
        # That's why j = half - i - 2
        while True:
            i = (l + r) // 2          # partition index in A
            j = half - i - 2          # partition index in B (forced by i)
        
            Aleft  = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if i+1 < len(A) else float("inf")
            Bleft  = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if j+1 < len(B) else float("inf")

            # binary search, when is the correct partition found?
            if Aleft <= Bright and Bleft <= Aright:
                # we found the right partition
                # if len of arrays is even, median is just / 2

                if total % 2 == 0:  # even
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else: # odd
                    return max(Aleft, Bleft) # min(Aright, Bright)
            elif Bleft > Aright:
                l = i + 1 
            else:
                r = i - 1 


        

