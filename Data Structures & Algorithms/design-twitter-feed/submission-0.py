class Twitter:

    def __init__(self):
        self.ts = 0
        self.follower = defaultdict(set)
        self.tweets = {}


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId] = self.tweets.get(userId, [])
        self.tweets[userId].append((self.ts, tweetId))
        self.ts -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        mh = []
        res = []
        self.follower[userId].add(userId)
        print(self.follower)
        for ppl in self.follower[userId]:
            if ppl in self.tweets:
                print(self.tweets[ppl])
                idx = len(self.tweets[ppl]) - 1
                ts, tweet = self.tweets[ppl][idx]
                heapq.heappush(mh, (ts,tweet,idx,ppl))
        while mh and len(res) < 10:
            ts, tweet, idx, person = heapq.heappop(mh)
            res.append(tweet)
            if idx > 0:
                idx -= 1
                ts, tweet = self.tweets[person][idx]
                heapq.heappush(mh, (ts, tweet, idx, person))
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower[followerId]:
            self.follower[followerId].remove(followeeId)
        

        
