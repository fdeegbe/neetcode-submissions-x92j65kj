class CountSquares:

    def __init__(self):
        self.memo = {}
    def add(self, point: List[int]) -> None:
        self.memo[(point[0], point[1])] = self.memo.get((point[0], point[1]), 0) + 1
    def count(self, point: List[int]) -> int:
        # use the law of diagonals to lookup the other two potential points.
        total = 0
        x, y = point[0], point[1]
        for qx, qy in self.memo.keys():
            if (abs(qx - x) != abs(qy - y)) or x == qx or y == qy:
                continue
            if (x,qy) in self.memo and (qx, y) in self.memo:
                total += self.memo[(x,qy)] * self.memo[(qx, y)] * self.memo[(qx, qy)]
        return total

#     def count(self, point: List[int]) -> int:
#         res = 0
#         px, py = point
#         print('New')
#         for x, y in self.pts:
#             if (abs(px - x) != abs(py - y)) or x == px or y == py:
#                 continue
#             if (px, y) in self.pts and (x, py) in self.pts:
#                 # Multiply with the number of occurrences of the repeated point represented by self.pts[(x, y)]
#                 res += self.pts[(px, y)] * self.pts[(x, py)] * self.pts[(x, y)]
#         return res
# # class DetectSquares:

#     def __init__(self):
#         self.pts = defaultdict(int)

#     def add(self, point: List[int]) -> None:
#         self.pts[tuple(point)] += 1

#     def count(self, point: List[int]) -> int:
#         res = 0
#         px, py = point
#         print('New')
#         for x, y in self.pts:
#             if (abs(px - x) != abs(py - y)) or x == px or y == py:
#                 continue
#             if (px, y) in self.pts and (x, py) in self.pts:
#                 # Multiply with the number of occurrences of the repeated point represented by self.pts[(x, y)]
#                 res += self.pts[(px, y)] * self.pts[(x, py)] * self.pts[(x, y)]
#         return res

        
