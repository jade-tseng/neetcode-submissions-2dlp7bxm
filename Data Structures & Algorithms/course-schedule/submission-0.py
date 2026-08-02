from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adj list
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for course, prereq in prerequisites:
            indegree[course] += 1
            adj[prereq].append(course)

        q = deque([])
        
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0        
        while q:
            curr = q.popleft()
            finish += 1
            for nei in adj[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return finish == numCourses
