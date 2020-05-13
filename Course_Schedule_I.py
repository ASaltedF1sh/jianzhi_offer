class Solution:
    def canFinish(self, numCourses, prerequisites):
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = []

        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)

        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        while queue != []:
            cur_class = queue[0]
            queue.pop(0)
            numCourses -= 1
            for ind in adjacency[cur_class]:
                indegrees[ind] -= 1
                if not indegrees[ind]:
                    queue.append(ind)

        return not numCourses
