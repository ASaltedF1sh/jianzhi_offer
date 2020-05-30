class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        ans = { _: -1 for _ in nums1}
        stack = [nums2[0]]

        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                if stack[-1] in ans:
                    ans[stack[-1]] = nums2[i]
                stack.pop(-1)
            stack.append(nums2[i])

        return [ans[i] for i in nums1]
