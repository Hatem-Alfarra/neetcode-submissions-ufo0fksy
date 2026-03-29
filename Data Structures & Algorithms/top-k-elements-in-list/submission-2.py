class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        pair = []
        for counted_number, counted_count in count.items():
            pair.append([counted_count, counted_number])
        pair.sort()

        answer = []
        while len(answer) < k:
            answer.append(pair.pop()[1])
        
        return answer


