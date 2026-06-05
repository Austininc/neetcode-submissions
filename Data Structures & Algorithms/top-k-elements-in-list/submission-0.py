class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #number of times a number shows up in the array
        count = {}
        #new array for the length of nums + 1 to store values based on how many times they appear
        frequency =[[] for i in range(len(nums)+ 1)]

        #looping through nums 
        for n in nums: 
            #
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            frequency[c].append(n)

        res = []
        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                    return res