from collections import deque
from functools import partial

from dsl.linear_algebra import (
    dot,
    get_row,
    get_column,
    make_matrix,
    magnitude,
    scalar_multiply,
    shape,
    distance,
)

users_dict = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

friendships = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (6, 8),
    (7, 8),
    (8, 9),
]

# give each user a friends list
for _user in users_dict:
    # noinspection PyTypeChecker
    _user["friends"] = []

# and populate it
for friend_i, friend_j in friendships:
    # this works because users[i] is the user whose id is i
    users_dict[friend_i]["friends"].append(
        users_dict[friend_j]
    )  # add i as a friend of j
    users_dict[friend_j]["friends"].append(
        users_dict[friend_i]
    )  # add j as a friend of i


#
# Betweenness Centrality
#


def shortest_paths_from(from_user):
    # a dictionary from "user_id" to *all* shortest paths to that user
    shortest_paths_to = {from_user["id"]: [[]]}

    # a queue of (previous user, next user) that we need to check.
    # starts out with all pairs (from_user, friend_of_from_user)
    frontier = deque((from_user, friend) for friend in from_user["friends"])

    # keep going until we empty the queue
    while frontier:

        prev_user, user = frontier.popleft()  # take from the beginning
        user_id = user["id"]

        # the fact that we're pulling from our queue means that
        # necessarily we already know a shortest path to prev_user
        paths_to_prev = shortest_paths_to[prev_user["id"]]
        paths_via_prev = [_ + [user_id] for _ in paths_to_prev]

        # it's possible we already know a shortest path to here as well
        old_paths_to_here = shortest_paths_to.get(user_id, [])

        # what's the shortest path to here that we've seen so far?
        if old_paths_to_here:
            min_path_length = len(old_paths_to_here[0])
        else:
            min_path_length = float("inf")

        # any new paths to here that aren't too long
        # noinspection PyPep8
        new_paths_to_here = [
            path_via_prev
            for path_via_prev in paths_via_prev
            if len(path_via_prev) <= min_path_length
               and path_via_prev not in old_paths_to_here
        ]

        shortest_paths_to[user_id] = old_paths_to_here + new_paths_to_here

        # add new neighbors to the frontier
        frontier.extend(
            (user, friend)
            for friend in user["friends"]
            if friend["id"] not in shortest_paths_to
        )

    return shortest_paths_to


for _user in users_dict:
    # noinspection PyTypeChecker
    _user["shortest_paths"] = shortest_paths_from(_user)

for _user in users_dict:
    # noinspection PyTypeChecker
    _user["betweenness_centrality"] = 0.0

for source in users_dict:
    source_id = source["id"]
    # noinspection PyUnresolvedReferences
    for target_id, paths_item in source["shortest_paths"].items():
        if source_id < target_id:  # don't double count
            num_paths = len(paths_item)  # how many shortest paths?
            contrib = 1 / num_paths  # contribution to centrality
            for path in paths_item:
                for identification in path:
                    if identification not in [source_id, target_id]:
                        users_dict[identification]["betweenness_centrality"] += contrib


#
# closeness centrality
#


def farness(user):
    """the sum of the lengths of the shortest paths to each other user"""
    return sum(len(paths[0]) for paths in user["shortest_paths"].values())


for _user in users_dict:
    # noinspection PyTypeChecker
    _user["closeness_centrality"] = 1 / farness(_user)


#
# matrix multiplication
#


def matrix_product_entry(a_matrix, b_matrix, i, j):
    return dot(get_row(a_matrix, i), get_column(b_matrix, j))


def matrix_multiply(a_matrix, b_matrix):
    n1, k1 = shape(a_matrix)
    n2, k2 = shape(b_matrix)
    if k1 != n2:
        raise ArithmeticError("incompatible shapes!")

    return make_matrix(n1, k2, partial(matrix_product_entry, a_matrix, b_matrix))


def vector_as_matrix(v):
    """returns the vector v (represented as a list) as a n x 1 matrix"""
    return [[v_i] for v_i in v]


def vector_from_matrix(v_as_matrix):
    """returns the n x 1 matrix as a list of values"""
    return [row[0] for row in v_as_matrix]


def matrix_operate(a_matrix, v):
    v_as_matrix = vector_as_matrix(v)
    product = matrix_multiply(a_matrix, v_as_matrix)
    return vector_from_matrix(product)


def find_eigenvector(a_matrix, tolerance=0.00001):
    guess = [1 for __ in a_matrix]

    while True:
        result = matrix_operate(a_matrix, guess)
        length = magnitude(result)
        next_guess = scalar_multiply(1 / length, result)

        if distance(guess, next_guess) < tolerance:
            return next_guess, length  # eigenvector, eigenvalue

        guess = next_guess


#
# eigenvector centrality
#


def entry_fn(i, j):
    return 1 if (i, j) in friendships or (j, i) in friendships else 0


n = len(users_dict)
adjacency_matrix = make_matrix(n, n, entry_fn)

eigenvector_centralities, _ = find_eigenvector(adjacency_matrix)

#
# directed graphs
#

endorsements = [
    (0, 1),
    (1, 0),
    (0, 2),
    (2, 0),
    (1, 2),
    (2, 1),
    (1, 3),
    (2, 3),
    (3, 4),
    (5, 4),
    (5, 6),
    (7, 5),
    (6, 8),
    (8, 7),
    (8, 9),
]

for _user in users_dict:
    # noinspection PyTypeChecker
    _user["endorses"] = []  # add one list to track outgoing endorsements
    # noinspection PyTypeChecker
    _user["endorsed_by"] = []  # and another to track endorsements

for source_id, target_id in endorsements:
    users_dict[source_id]["endorses"].append(users_dict[target_id])
    users_dict[target_id]["endorsed_by"].append(users_dict[source_id])

endorsements_by_id = [(user["id"], len(user["endorsed_by"])) for user in users_dict]

sorted(endorsements_by_id, key=lambda pair: pair[1], reverse=True)


def page_rank(users, damping=0.85, num_iters=100):
    # initially distribute PageRank evenly
    num_users = len(users)
    pr = {user["id"]: 1 / num_users for user in users}

    # this is the small fraction of PageRank
    # that each node gets each iteration
    base_pr = (1 - damping) / num_users

    for __ in range(num_iters):
        next_pr = {user["id"]: base_pr for user in users}
        for user in users:
            # distribute PageRank to outgoing links
            links_pr = pr[user["id"]] * damping
            for endorsee in user["endorses"]:
                next_pr[endorsee["id"]] += links_pr / len(user["endorses"])

        pr = next_pr

    return pr
