from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort()
        hmap=defaultdict(list)
        for i in strs:
            ss=''.join(sorted(i))
            hmap[ss].append(i)
        return list(hmap.values())
