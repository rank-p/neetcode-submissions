class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += "#"
            res += s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            l = ""
            while s[i] != "#":
                l += s[i]
                i += 1
            # skip #
            i += 1
            t = ""
            for _ in range(int(l)):
                t += s[i]
                i += 1
            res.append(t)
        return res
