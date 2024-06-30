class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # Sort edges by type
        edges.sort(key=lambda x: -x[0])

        # Initialize disjoint sets
        alice_set = list(range(n+1))
        bob_set = list(range(n+1))
        alice_count = 0
        bob_count = 0
        shared_count = 0

        # Helper function to find root of a node in a set
        def find_set(node, s):
            if s[node] != node:
                s[node] = find_set(s[node], s)
            return s[node]

        # Iterate over edges and add to sets if no cycle is created
        for edge in edges:
            t, u, v = edge
            if t == 3:
                # Check if edge can be added to both sets
                a = find_set(u, alice_set)
                b = find_set(v, alice_set)
                if a != b:
                    alice_set[b] = a
                    bob_set[b] = a
                    shared_count += 1
            elif t == 1:
                # Check if edge can be added to Alice's set
                a = find_set(u, alice_set)
                b = find_set(v, alice_set)
                if a != b:
                    alice_set[b] = a
                    alice_count += 1
            else:
                # Check if edge can be added to Bob's set
                a = find_set(u, bob_set)
                b = find_set(v, bob_set)
                if a != b:
                    bob_set[b] = a
                    bob_count += 1

        # Check if graph is fully traversable
        if alice_count + shared_count < n-1 or bob_count + shared_count < n-1:
            return -1

        # Calculate number of edges that can be removed
        return len(edges) - alice_count - bob_count - shared_count
