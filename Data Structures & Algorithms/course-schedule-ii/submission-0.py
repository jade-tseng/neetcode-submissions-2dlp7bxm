from collections import deque 

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses

        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1
        
        # seed q with nodes without prerequisites
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []

        while q:
            node = q.popleft()
            order.append(node)
            for pre in adj[node]:
                in_degree[pre] -= 1
                if in_degree[pre] == 0:
                    q.append(pre)

        # if we processed all nodes, no cycle
        if len(order) == numCourses:
            return order
        return []  # cycle exists