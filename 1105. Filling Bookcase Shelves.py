class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        cache = {}
        def helper(i):
            if i == len(books):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = float("inf")
            max_height = 0
            rem_width = shelfWidth
            for j in range(i, len(books)):
                width, height = books[j]
                if width > rem_width:
                    break
                rem_width -= width
                max_height = max(max_height, height)
                cache[i] = min(cache[i], helper(j + 1) + max_height) 
            return cache[i]
        return helper(0)
