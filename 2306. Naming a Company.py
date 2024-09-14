class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        wmap = defaultdict(set)

        for word in ideas:
            wmap[word[0]].add(word[1:])

        res = 0
        
        for char1 in wmap:
            for char2 in wmap:
                if char1 == char2:
                    continue
                duplicate = 0
                for w in wmap[char1]:
                    if w in wmap[char2]:
                        duplicate += 1 
                distinict1 = len(wmap[char1]) - duplicate
                distinict2 = len(wmap[char2]) - duplicate
                res += distinict1 * distinict2

        return res
        
