class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for num in nums: 
            hashMap[num] = 1 + hashMap.get(num, 0)
        
        for key, value in hashMap.items(): 
            freq[value].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1): 
            for number in freq[i]: 
                res.append(number)
                if len(res) == k: 
                    return res