class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        edges = defaultdict(list)
        indegrees = [0] * n
        for parent, child in relations:
            edges[parent - 1].append(child - 1)
            indegrees[child - 1] += 1
        
        courses = [(time[i], i) for i, indeg in enumerate(indegrees) if indeg == 0]
        heapify(courses)

        res = 0
        while courses:
            duration, course = heappop(courses)
            res = duration
            for child in edges[course]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    heappush(courses, (duration + time[child], child))
        return res
        
