from collections import defaultdict
names = 'bob julian tim martin rod sara joyce nick beverly kevin'.split()
ids = range(len(names))
users = dict(zip(ids, names))  # 0: bob, 1: julian, etc

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
               (3, 4), (4, 5), (5, 6), (5, 7), (5, 9),
               (6, 8), (7, 8), (8, 9)]


def get_friend_with_most_friends(friendships=friendships):
    """Receives the friendships list of user ID pairs,
       parse it to see who has most friends, return a tuple
       of (name_friend_with_most_friends, his_or_her_friends)"""
    friends = defaultdict(set)
    for f1, f2 in friendships:
        friend1 = users[f1]
        friend2 = users[f2]
        friends[friend1].add(friend2)
        friends[friend2].add(friend1)

    friend_with_most = sorted(friends,key=lambda k:len(friends[k]),reverse=True)[0]
    return (friend_with_most,friends[friend_with_most])
