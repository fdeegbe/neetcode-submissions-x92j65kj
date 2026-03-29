class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0 , len(matrix)-1
        m = l + (r-l) // 2

        while l <= r:
            print(l,r,m)
            if matrix[m][0] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            else:
                return True
            print(l,r,m)
            m = l + (r-l) // 2
        print(matrix[m])

        # check matrix at l and r to see if it exists
        check = []
        check.append(l) if l < len(matrix) else None
        check.append(r) if r < len(matrix) else None
        print(check)
        for x in check:
            l, r = 0 , len(matrix[0])-1
            m = l + (r-l) // 2

            while l <= r:
                print(l,r,m,x)
                if matrix[x][m] < target:
                    l = m + 1
                elif matrix[x][m] > target:
                    r = m - 1
                else:
                    return True
                print(l,r,m)
                m = l + (r-l) // 2
        return False