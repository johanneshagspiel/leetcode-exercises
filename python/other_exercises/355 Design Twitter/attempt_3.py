import collections


class Twitter:

    def __init__(self):
        self.user_dic = {}
        self.tweet_list = []
        self.follower_dic = {}
        self.tweet_count = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_list.append(tweetId)

        if userId not in self.user_dic:
            self.user_dic[userId] = collections.deque()

        self.user_dic[userId].appendleft(self.tweet_count)
        self.tweet_count += 1

        if len(self.user_dic[userId]) > 10:
            self.user_dic[userId].pop()


    def getNewsFeed(self, userId: int) -> List[int]:
        cur_count = 0


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follower_dic:
            self.follower_dic[followerId] = {}

        self.follower_dic[followerId][followeeId] = True


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follower_dic:
            if followeeId in self.follower_dic[followerId]:
                self.follower_dic[followerId].pop(followeeId)
