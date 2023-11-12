class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop_to_buses = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].add(i)
        
        if source not in stop_to_buses or target not in stop_to_buses:
            return -1

        visited_stops = set()
        visited_buses = set()
        queue = deque([[source, 0]])
        visited_stops.add(source)

        while queue:
            stop, bus_changes = queue.popleft()
            if stop == target:
                return bus_changes
            for bus in stop_to_buses[stop]:
                if bus not in visited_buses:
                    visited_buses.add(bus)
                    for next_stop in routes[bus]:
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append([next_stop, bus_changes + 1])
        return -1
