class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
        flowers.sort()
        sorted_people = sorted([ [people[i], i] for i in range(len(people))])
        res = [None] * len(people)
        curr = 0
        heap = []

        for i in range(len(people)):
            person, index = sorted_people[i]
            while curr < len(flowers) and person >= flowers[curr][0]:
                if person <= flowers[curr][1]:
                    heappush(heap, flowers[curr][1])
                curr += 1
            while heap and person > heap[0]:
                heappop(heap)
            res[index] = len(heap)
        return res

        
