class Twitter:

    def __init__(self):
        self.tweet_dict = defaultdict(list)
        self.followee_dict = defaultdict(list)
        self.order = 0
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.order += 1
        self.tweet_dict[userId].append((tweetId, self.order, userId))
        for i in self.followee_dict[userId]:
            self.tweet_dict[i].append((tweetId, self.order, userId))


    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = sorted(self.tweet_dict[userId], key = lambda x: x[1], reverse=True)
        return [x for x,_, _ in tweets[:10]]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followee_dict[followeeId]:
            self.followee_dict[followeeId].append(followerId)
        for i in self.tweet_dict[followeeId]:
            if i[2] == followeeId and i not in self.tweet_dict[followerId]:
                self.tweet_dict[followerId].append(i)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followee_dict[followeeId]:
            self.followee_dict[followeeId].remove(followerId)
        self.tweet_dict[followerId] = [t for t in self.tweet_dict[followerId] if t[2]!= followeeId]   

            
        
