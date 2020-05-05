class Solution:
    def sort(self, array):
        if len(array) <= 1:
            return array
        else:
            listA = array[:len(array) // 2]
            listB = array[len(array) // 2:]

            a = self.sort(listA)
            b = self.sort(listB)
            c = self.merge(a, b)

            return c

    def merge(self, A, B):

        lenA = len(A)
        lenB = len(B)

        merged_list = []
        i = 0
        j = 0

        while j < lenB and i < lenA:
            if B[j] <= A[i]:
                merged_list.append(B[j])
                j += 1
            else:
                merged_list.append(A[i])
                i += 1
                
        if i == lenA:
            merged_list.extend(B[j:])
            return merged_list
        else:
            merged_list.extend(A[i:])
            return merged_list
