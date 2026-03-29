class Solution:

    def encode(self, strs: List[str]) -> str:
        # we can store the length of the strings at the start
        result = ""
        result += ','.join([str(len(a)) for a in strs])
        result += '#' + ''.join(strs)
        return result

    def decode(self, s: str) -> List[str]:
        print(s)
        if s == "#":
            return []
        marker = s.find('#')
        lengths = s[:marker].split(',')
        res = []
        for i in lengths:
            i = int(i)
            res.append(s[marker+1:i+1+marker])
            marker += i

        return res

