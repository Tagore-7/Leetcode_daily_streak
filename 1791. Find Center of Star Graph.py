class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        element_seen = set()
        for u, v in edges:
            if u in element_seen:
                return u
            if v in element_seen:
                return v
            element_seen.add(u)
            element_seen.add(v)
