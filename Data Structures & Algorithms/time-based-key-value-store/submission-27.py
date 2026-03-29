class TimeMap:
    # Note: For all calls to set, the timestamps are in strictly increasing order.
    def __init__(self):
        self.memo = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.memo[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        print("========================", timestamp)
        lst = self.memo[key]
        res = ""
        if not lst or timestamp < lst[0][0]:
            return res
        l, r = 0, len(lst)-1
        while l <= r:
            m = l + (r-l) // 2
            if lst[m][0] <= timestamp:
                # move l
                l = m + 1
            elif lst[m][0] > timestamp:
                r = m - 1
        print(lst,l,m,r)
        # if l == len(lst):
        #     return lst[-1][1]
        return lst[r][1]
        return ""
        
        
