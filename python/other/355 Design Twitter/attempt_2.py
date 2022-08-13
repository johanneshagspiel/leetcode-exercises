import collections
import heapq


class Twitter:

    def __init__(self):
        self.user_dic = {}
        self.follower_dic = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId not in self.user_dic:
            self.user_dic[userId] = collections.deque()

        self.user_dic[userId].appendleft((self.timestamp, tweetId))

        self.timestamp += 1

        if len(self.user_dic[userId]) > 10:
            self.user_dic[userId].pop()


    def getNewsFeed(self, userId: int) -> List[int]:
        tweet_list = []

        if userId in self.user_dic:
            user_tweet_list = list(self.user_dic[userId])
            tweet_list.extend(user_tweet_list)

        if userId in self.follower_dic:
            for followee_id in self.follower_dic[userId]:
                if followee_id in self.user_dic:
                    follower_tweet_list = list(self.user_dic[followee_id])
                    tweet_list.extend(follower_tweet_list)

        tweet_list.sort(key= lambda x:x[0], reverse=True)

        tweet_list =[x[1] for x in tweet_list]

        if len(tweet_list) > 10:
            return tweet_list[:10]
        else:
            return tweet_list


    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.follower_dic:
            self.follower_dic[followerId] = {}

        self.follower_dic[followerId][followeeId] = True


    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId in self.follower_dic:
            if followeeId in self.follower_dic[followerId]:
                self.follower_dic[followerId].pop(followeeId)
