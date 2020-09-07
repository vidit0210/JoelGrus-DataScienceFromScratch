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
print(friendships)

# And loop over the friendsip pairs to populate it
for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)


def number_of_friends(user):
    """How many friends does this user have """
    user_id = user["id"]
    friends_ids = friendships[user_id]
    return len(friends_ids)


total_connections = sum(number_of_friends(user) for user in users)

num_users = len(users)
avg_connections = total_connections / num_users

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

num_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1], reverse=True)


def foaf_ids_bad(user):
    """foaf is short for "friend of a friends " """
    return [foaf_id for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]
