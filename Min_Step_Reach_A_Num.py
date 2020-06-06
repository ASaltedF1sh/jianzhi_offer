#当sum - target是偶数的时候，一定可只通过将某一步变为向左走，从而最少步数到达target
class Solution:
    def reachNumber(self, target):
        target = abs(target)
        sum_ = 0
        step = 0
        while sum_ < target or (sum_ - target) % 2:
            sum_ += step
            step += 1
        return step - 1
