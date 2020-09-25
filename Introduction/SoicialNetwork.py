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
    """ Foaf is hsort form for "friends of a friend" """
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]


assert foaf_ids_bad(users[0]) == [0, 2, 3, 0, 1, 3]
