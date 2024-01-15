class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = defaultdict(int)
        for player1, player2 in matches:
            players[player1] = players[player1]
            players[player2] += 1
        
        return [
            sorted([key for key in players if players[key] == 0]),
            sorted([key for key in players if players[key] == 1])
        ]
