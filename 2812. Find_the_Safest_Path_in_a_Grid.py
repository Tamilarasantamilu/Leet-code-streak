class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] or grid[m-1][n-1]:
            return 0

        steps = [[-1, 0],
                 [1, 0],
                 [0, -1],
                 [0, 1]]
    
        mh_dists = self.get_manhattan_dists(grid, m, n, steps)

        # run modified dijkstra's
        # max heap keys: (mh_dist, (i, j))
        path_mh_dists = [[None]*n for _ in range(m)]
        path_mh_dists[0][0] = mh_dists[0][0]
        pq = [(-mh_dists[0][0], (0, 0))]
        heapq.heapify(pq)

        # We greedily select the node we have seen so far that has the maximum path safeness factor
        # Then we visit the neighbours from there and calculate the new path safeness factor as: min(curr, new_cell_safety_factor)
        # This safeness factor is guaranteed to be the largest since we chose to visit it from the largest using priority queue.
        # All other paths must have a safeness factor <= this one because it was smaller in the priority queue.
        while pq:
            dist, idx = heapq.heappop(pq)
            dist = -dist

            for di, dj in steps:
                new_i = idx[0] + di
                new_j = idx[1] + dj

                if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and path_mh_dists[new_i][new_j] is None:
                    new_path_mh_dist = min(dist, mh_dists[new_i][new_j])
                    path_mh_dists[new_i][new_j] = new_path_mh_dist
                    heapq.heappush(pq, (-new_path_mh_dist, (new_i, new_j)))

        return path_mh_dists[m-1][n-1]

    def get_manhattan_dists(self, grid, m, n, steps):

        # calculate Manhattan distance to each cell from any thief
        mh_dists = [[None]*n for _ in range(m)]
        q = deque([])

        # find all thiefs
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    mh_dists[i][j] = 0
    
        # BFS starting at every thief
        path_length = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                
                for di, dj in steps:
                    new_i = i + di
                    new_j = j + dj

                    if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and mh_dists[new_i][new_j] is None:
                        # add this cell to the queue to visit
                        mh_dists[new_i][new_j] = path_length+1
                        q.append((new_i, new_j))

            path_length += 1
        return mh_dists
