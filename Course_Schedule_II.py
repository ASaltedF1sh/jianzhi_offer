class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        #入度
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = []
        class_order = []

        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)

        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        while queue != []:
            cur_class = queue[0]
            class_order.append(cur_class)
            queue.pop(0)
            numCourses -= 1
            for ind in adjacency[cur_class]:
                indegrees[ind] -= 1
                if not indegrees[ind]:
                    queue.append(ind)

        if not numCourses:
        	return class_order
        else:
        	return []
