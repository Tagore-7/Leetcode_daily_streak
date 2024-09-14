class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums, l , m, r):
            left, right = nums[l:m+1], nums[m+1:r + 1]
            i, j, k = l, 0, 0
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    nums[i] = left[j]
                    j += 1
                else:
                    nums[i] = right[k]
                    k += 1
                i += 1
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, left, right):
            if left == right:
                return arr
            middle = (left + right) // 2
            mergeSort(arr, left, middle)
            mergeSort(arr, middle + 1, right)
            merge(arr, left, middle, right)

            return arr
        
        return mergeSort(nums, 0, len(nums))
