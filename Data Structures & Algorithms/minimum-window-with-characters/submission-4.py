class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        countT, countS = Counter(t), defaultdict(int)
        need, have = len(countT), 0
        print(need, have)
        
        l = 0
        min_len = float("inf")
        res = [-1,-1]
        for r, char in enumerate(s):
            if char in countT:
                countS[char] += 1
                if countS[char] == countT[char]:
                    have += 1
                # print(s[l:r+1], countS, have)
                while have == need:
                    if (r-l+1) < min_len:
                        min_len = r-l+1
                        res = [l,r]
                    old = s[l]
                    if old in countT:
                        countS[old] -= 1
                        if countS[old] < countT[old]:
                            have -= 1
                    l += 1
                
        l,r = res
        return s[l:r+1]