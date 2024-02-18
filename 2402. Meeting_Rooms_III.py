class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        openM = [i for i in range(n)]
        closedM = {}
        meetingArray = [0] * n
        time = 0
        while meetings:
            if time in closedM:
                for room in closedM[time]:
                    openM.append(room)
                del closedM[time]
                openM.sort()
            while meetings and meetings[0][0] <= time and openM:
                start, end = meetings.pop(0)
                nextTime = end - start + time
                room = openM.pop(0)
                meetingArray[room] += 1
                if nextTime in closedM:
                    closedM[nextTime].append(room)
                else:
                    closedM[nextTime] = [room]
            if not openM:
                time = min(closedM.keys())
            else:
                time += 1
        maxRoom = max(range(n), key=meetingArray.__getitem__)
        return maxRoom
