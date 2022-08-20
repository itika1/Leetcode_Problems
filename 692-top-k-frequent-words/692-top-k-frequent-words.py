class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = Counter(words)
        keys = list(d.keys())
        keys.sort(key=lambda x: (- d[x], x))
        return keys[:k]
        