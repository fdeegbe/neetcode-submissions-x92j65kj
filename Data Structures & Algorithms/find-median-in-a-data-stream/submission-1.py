import bisect as bs
class MedianFinder:

    def __init__(self):
        self.lst = []

    def addNum(self, num: int) -> None:
        bs.insort(self.lst,num)
        print(self.lst)

    def findMedian(self) -> float:
        if len(self.lst) & 1:
            m = len(self.lst) // 2
            return self.lst[m]
        else:
            m = len(self.lst) // 2
            n = (len(self.lst) // 2) + 1
            print(m,n)
            return (self.lst[m-1] + self.lst[n-1])/2

        return 1.0