from collections import Counter, defaultdict
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

friendships = {user["id"]: [] for user in users}
# print(friendships)

for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

# print(friendships)


def number_of_friends(user):
    """How many friends does user have?"""
    user_id = user["id"]
    friends_id = friendships[user_id]
    return len(friends_id)


# print(number_of_friends(users[0]))
total_connections = sum(number_of_friends(user) for user in users)
# print(total_connections)

assert total_connections == 24

num_users = len(users)
avg_connections = total_connections/num_users

assert num_users == 10
assert avg_connections == 2.4

# Create a list (user_id,number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
print(num_friends_by_id)

num_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1], reverse=True)
# Each pair is (user_id, num_friends):
# [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3),
#  (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]


assert num_friends_by_id[0][1] == 3     # several people have 3 friends
assert num_friends_by_id[-1] == (9, 1)  # user 9 has only 1 friend


def foaf_ids_bad(user):
    """ Foaf is short form for "friends of a friend" """
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]


assert foaf_ids_bad(users[0]) == [0, 2, 3, 0, 1, 3]


def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id and foaf_id not in friendships[user_id]
    )


print(friends_of_friends(users[3]))
assert friends_of_friends(users[3]) == Counter({0: 2, 5: 1})
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


def data_scientist_who_like(target_interest):
    """ Find the ids of all users who like the target interests"""
    return [user_id for user_id, user_interest in interests if user_interest == target_interest]
