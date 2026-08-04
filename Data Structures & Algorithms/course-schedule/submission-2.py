class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adj list
        adj = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)
        
        visiting = set()
        visited = set()

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course) 

            for pre in adj[course]:
                if not dfs(pre):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            return True
        
        for course, pre in prerequisites:
            if not dfs(course):
                return False
        return True

