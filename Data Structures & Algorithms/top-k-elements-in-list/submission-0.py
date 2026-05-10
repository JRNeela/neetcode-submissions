class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = []
        n = len(nums)
        buckets = [[] for _ in range(n+1)]
        freqs = Counter(nums)
        for key, val in freqs.items():
            buckets[val].append(key)
        print(buckets)
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                ret.append(num)
                if len(ret) == k:
                    return ret

                








        