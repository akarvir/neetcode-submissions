from collections import deque, defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        d = defaultdict(list)
        indegrees = {c:0 for word in words for c in word}
        res = []
        deq = deque()
        for i in range(n-1):
            s = words[i]
            w = words[i+1]
            minlen = min(len(s),len(w))
            if len(s) > len(w) and s[:minlen] == w[:minlen]:
                return ""
            for k in range(minlen):
                if s[k]!=w[k]:
                    if w[k] not in d[s[k]]:
                        d[s[k]].append(w[k])
                        indegrees[w[k]]+=1
                    break
        for k in indegrees:
            if indegrees[k] == 0:
                deq.append(k)
        while deq:
            a = deq.popleft()
            res.append(a)
            for k in d[a]:
                indegrees[k]-=1
                if indegrees[k] == 0:
                    deq.append(k)
        return "".join(res) if len(res) == len(indegrees) else ""

                    
                
                
            

