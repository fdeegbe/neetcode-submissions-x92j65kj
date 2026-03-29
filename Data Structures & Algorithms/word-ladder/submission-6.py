class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        else:
            endwordIdx = wordList.index(endWord)
        print(endwordIdx)
        wordList.append(beginWord)
        beginwordIdx = len(wordList)-1
        num_words = len(wordList)
        # construct the adjacency list
        adj = defaultdict(list)
        for i in range(num_words):
            for j in range(i + 1, num_words):
                word1 = wordList[i]
                word2 = wordList[j]

                diff = 0
                for k in range(len(word1)):
                    if word1[k] != word2[k]:
                        diff += 1
                
                if diff == 1:
                    adj[i].append(j)
                    adj[j].append(i) # Add both directions
        print(adj.items())
        visited = set()
        if beginwordIdx in adj:
            q = deque([(beginwordIdx,1)])
            print(q)
            while q:
                curr, jumps = q.popleft()
                print(curr,jumps)
                visited.add(curr)

                if curr == endwordIdx:
                    print("Lol")
                    return int(jumps)

                for nei in adj[curr]:
                    if nei not in visited:
                        q.append((nei, jumps+1))
            return 0
        return 0

                    
