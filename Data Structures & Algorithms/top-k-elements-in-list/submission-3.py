class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            num = str(num)
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1 
        
        answer = []
        while k > 0:
            cur_max = max(my_dict.values())    
            for key, value in my_dict.items():
                if value == cur_max:
                    answer.append(key)
                    k -= 1
                    my_dict.pop(key)
                    break
        return answer


        
