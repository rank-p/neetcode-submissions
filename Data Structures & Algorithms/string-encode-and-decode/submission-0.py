class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += str(len(s))
            enc += "#"
            enc += s
        return enc

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        curr = ""
        length = ""
        i = 0
        decode_len = True
        while i < len(s):
            if s[i] != '#':
                length += s[i]
                i += 1
            elif s[i] == '#':
                length = int(length)
                i += 1
                for _ in range(length):
                    curr += s[i]
                    i += 1
                res.append(curr)
                length = ""
                curr = ""            
        return res
