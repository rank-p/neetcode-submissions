class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        m = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        for c in s:
            if c in "([{":
                q.append(c)
                print(q)
            else:
                if not q or q.pop() != m[c]:
                    return False
        
        return len(q) == 0
        