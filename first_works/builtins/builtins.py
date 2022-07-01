
#  you give it something, and it returns everything back to you
from functools import reduce


print(list(map(lambda x: x ** 2, [2, 3, 4, 5])))


# filters out the number lesser than 2
print(list(filter(lambda x: x < 2, [3, 4, 2, 0])))


#  you can do filter modulos when looking for even numbers
print(list(filter(lambda x: x % 2 == 0, [3, 4, 2, 0])))


# reduce will take the function, the list of the iterable and the string reduce will do whatever you ask it to do and
# return the result, you can use it for max and min and for sum, even product and so on
print(reduce(lambda x, y: x + y, [1, 2, 3, 4], 10))


"""ASSIGNMENTS"""
"""twitter_user = []
{   name:
    user_name:
    age:
    tweets: [contents, likes, comments: tweets]
    followers:
    followings:
    verification_status: [verified and non verified users]
    statistics:
        average age:
        number of tweets:
        tweets with most likes
        tweets with most comments
        list of active tweeter users
        list of non active tweeters users
}"""