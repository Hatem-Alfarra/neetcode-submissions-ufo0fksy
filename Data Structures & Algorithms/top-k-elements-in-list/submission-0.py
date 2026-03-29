class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}
        nums = sorted(nums)
        nums_set = set(nums)
        answer = []
        temp_k = k

        for num in nums_set:
            count = nums.count(num)
            if count in frequency_dict.keys():
                frequency_dict[count].append(num)
            else:
                frequency_dict[count] = [num]

        keys = frequency_dict.keys()
        keys = sorted(keys, reverse=True)
        for key in keys:
            desired_inner_list = frequency_dict[key]
            inner_count = len(desired_inner_list)
            for number in desired_inner_list: 
                if temp_k > 0:
                    temp_k -= 1
                    answer.append(number)
                else:
                    answer.sort(reverse=True)
                    answer = sorted(answer)
                    return answer
        return answer



