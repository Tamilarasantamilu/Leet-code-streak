class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0

        for x in range(len(tickets)):
            if tickets[x] >= tickets[k]:
                time += tickets[k]
            elif tickets[x] < tickets[k]:
                time += tickets[x]

            if x > k and tickets[x] >= tickets[k]:
                time -= 1

        return time
        
