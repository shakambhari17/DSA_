import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):

        graph = defaultdict(list)

        # Build graph
        for u, v, w in times:
            graph[u].append((v, w))

        # Min Heap (distance, node)
        heap = [(0, k)]

        # Shortest distance
        distance = {}

        while heap:

            dist, node = heapq.heappop(heap)

            if node in distance:
                continue

            distance[node] = dist

            for neighbor, weight in graph[node]:

                if neighbor not in distance:
                    heapq.heappush(heap,
                                   (dist + weight, neighbor))

        if len(distance) != n:
            return -1

        return max(distance.values())