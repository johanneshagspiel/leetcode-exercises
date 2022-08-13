import heapq


class Twitter:

    def __init__(self):
        self.user_post_dic = {}
        self.follower_dic = {}

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId not in self.user_post_dic:
            self.user_post_dic[userId] = []

        self.user_post_dic[userId].append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:

        tweet_list = []

        if userId in self.follower_dic:
            for followeeId in self.follower_dic[userId].values():
                tweet_list.extend(self.user_post_dic[followeeId])

        tweet_list.extend(self.user_post_dic[userId])

        return heapq.nlargest(10, tweet_list)

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.follower_dic:
            self.follower_dic[followerId] = {}

        self.follower_dic[followeeId][followerId] = True

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower_dic[followeeId].pop(followerId)
