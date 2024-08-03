class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count = defaultdict(int)
        for n1, n2 in zip(target, arr):
            count[n1] += 1
            count[n2] -= 1
        print(count)
        for i in range(len(arr)):
            if count[arr[i]] != 0:
                return False
        return True
