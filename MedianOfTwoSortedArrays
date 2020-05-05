class Solution:
    def findMedianSortedArrays(self, ArrayA, ArrayB):
        lenA = len(ArrayA)
        lenB = len(ArrayB)
        if lenA == 0:
            return self.median_normal(ArrayB)
        if lenB == 0:
            return self.median_normal(ArrayA)
        if lenA > lenB:
            ArrayA, ArrayB = ArrayB, ArrayA
            lenA, lenB = lenB, lenA

        odd = (lenA + lenB) % 2 !=0
        if not odd:
            index = 0
            if ArrayA[0] <= ArrayB[0]:
                ArrayA.pop(0)
                lenA -= 1
            else:
                ArrayB.pop(0)
                lenB -= 1
        
        target_num = [(lenA + lenB + 1) // 2]

        result = self.binary_search(ArrayA, ArrayB, target_num, odd)
        if result:
            return result
        else:
            return self.binary_search(ArrayB, ArrayA, target_num, odd)

    def binary_search(self, ArrayA, ArrayB, target_num, odd):

        l = 0
        r = len(ArrayA) -1
        lenA = len(ArrayA)
        lenB = len(ArrayB)

        while l <= r:
            mid = l + (r - l) // 2
            LA = len([x for x in ArrayA if x < ArrayA[mid]])
            RA = len([x for x in ArrayA if x > ArrayA[mid]])
            LB = len([x for x in ArrayB if x < ArrayA[mid]])
            RB = len([x for x in ArrayB if x > ArrayA[mid]])
            check_list = [x for x in range(LA + LB + 1, lenA + lenB - RA - RB + 1)]

            if target_num in check_list:
                median = ArrayA[mid]
                if not odd:
                    index = mid
                    width = target_num[0] - (LA + LB)
                    if width >= 2:
                        return median
                    else:
                        j = 1
                        current = median
                        while mid - j >= 0:
                            if ArrayA[mid-j] == median:
                                j += 1
                            else:
                                current = ArrayA[mid-j]
                                break
                        return (self.search_nearest(ArrayB, median, current) + median) / 2
                else:
                    return median
            else:
                if lenA + lenB - RA - RB < min(target_num):
                    l = mid + 1
                else:
                    r = mid - 1

    def search_nearest(self, arr, target, current):
        arr = [x - target for x in arr]

        if arr[0] >= 0:
            return current
        else:
            l = 0
            r = len(arr) - 1
            best = 1
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] >= 0:
                    r = mid -1
                else:
                    if best > 0:
                        best = arr[mid]
                    else:
                        if arr[mid] > best:
                            best = arr[mid]
                    l = mid + 1

            if target == current:
                return min(current, best + target)
            else:
                return max(current, best + target)

    def median_normal(a):
        length = len(a)
        if len(a) % 2 == 0:
            return (a[length//2] + a[length//2 + 1]) / 2
        else:
            return a[(length + 1) // 2]
