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

# initialize the dict iwth an empty list for each user id
friendships = {user["id"]: [] for user in users}
print(friendships)

# And Loop over the fiendship pair to populate it
for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)
print(friendships)


def number_of_friends(user):
    """How many friends does the user have """
    user_id = user["id"]
    friends_id = friendships[user_id]
    return len(friends_id)


assert number_of_friends(users[0]) == 2

total_connections = sum(number_of_friends(user) for user in users)
assert total_connections == 24

num_users = len(users)
avg_connections = total_connections / num_users

assert num_users == 10, "Length of users should be 10"
assert avg_connections == 2.4, "Average Connection length should be 2.4"

# create a list of use_id , number_of_friends
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
print(num_friends_by_id)
