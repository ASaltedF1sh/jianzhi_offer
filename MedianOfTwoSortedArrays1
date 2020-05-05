class Solution:
    def findMedianSortedArrays(self, A, B):
        lenA = len(A)
        lenB = len(B)

        if lenA > lenB:
            A, B = B, A
            lenA, lenB = lenB, lenA

        len_total = lenA + lenB

        begin = 0
        end = lenA

        while begin <= end:
            i = (begin + end) // 2
            j = (len_total + 1) // 2 - i

            if i > 0 and j < lenB and A[i-1] > B[j]:
                #如果A[i-1] > B[j]，可知此时全部数组中，小于等于A[i-1]的至少有i+j个，此时必不可能是目标点
                #此时显然是i过大造成分界过分偏右，因此下次向左修正
                end = i - 1
            elif i < lenA and j > 0 and B[j-1] > A[i]:
                #此时全部数组中，小于等于B[j-1]的至少有i+j个，同理此时也不可能是目标点
                #此时是i偏小，向右修正
                begin = i + 1
            else:
                #满足条件了，如果是奇数的话中位数是二者之一，
                #如果是偶数的话二者之一将是左边的那个中间数，需要分情况讨论
                if i == 0:
                    #可知此时中位数左边的数应该全在B中
                    left = B[j-1]
                elif j == 0:
                    left = A[i-1]
                else:
                    #中位数左边的数一部分在A中，一部分在B中
                    #应是二者中最大的
                    left = max(A[i-1], B[j-1])

                if len_total & 1:
                    #使用位运算判断奇偶
                    #为奇
                    return left

                if i == lenA:
                    #A中所有的数都小于等于中位数
                    #如果数组总长度为偶的话，有右边的中间数
                    right = B[j]
                elif j == lenB:
                    right = A[i]
                else:
                    right = min(A[i], B[j])
                return (left + right) / 2.
        return 0
