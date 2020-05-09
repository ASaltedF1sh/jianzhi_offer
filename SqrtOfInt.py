class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        else:
            start = 0
            end = x // 2

            while(start <= end):
                mid = (start + end) // 2
                square = mid ** 2

                if square == x:
                    return mid
                elif square > x:
                    end = mid - 1
                else:
                    square_ = (mid + 1) ** 2
                    
                    if square_ == x:
                        return mid + 1
                    elif square_ > x:
                        return mid
                    else:
                        start = mid + 1
