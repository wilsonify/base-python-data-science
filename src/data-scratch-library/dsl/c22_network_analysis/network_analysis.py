import logging
from collections import deque
from functools import partial

from dsl.c04_linear_algebra.linear_algebra import (
    dot,
    get_row,
    get_column,
    make_matrix,
    magnitude,
    scalar_multiply,
    shape,
    distance,
)


def populate_endorsements(users_dict):
    result = []
    for user in users_dict:
        uid = user["id"]
        n_endorsements = len(user["endorsed_by"])
        result.append((uid, n_endorsements))
    return result


def get_page_ranks(pr_result):
    for user_id, pr in pr_result.items():
        logging.info("%r", f"user_id {user_id}, pr{pr}")


def get_eigenvector_centrality(eigenvector_centralities):
    logging.info("Eigenvector Centrality")
    for _user_id, centrality in enumerate(eigenvector_centralities):
        logging.info("%r", "user_id {}, centrality {}".format(_user_id, centrality))


def populate_endorsments(users_dict, endorsements):
    for user in users_dict:
        user["endorses"] = []  # add one list to track outgoing endorsements
        user["endorsed_by"] = []  # and another to track endorsements
    for source_id, target_id in endorsements:
        users_dict[source_id]["endorses"].append(users_dict[target_id])
        users_dict[target_id]["endorsed_by"].append(users_dict[source_id])
    return users_dict


def compute_eigenvectors(adjacency_matrix):
    eigenvector_centralities, _ = find_eigenvector(adjacency_matrix)
    return eigenvector_centralities


def construct_adjacency(users_dict, friendships):
    n = len(users_dict)

    def entry_fn_friendships(i, j):
        return 1 if (i, j) in friendships or (j, i) in friendships else 0

    adjacency_matrix = make_matrix(n, n, entry_fn_friendships)
    return adjacency_matrix


def get_closeness(users_dict):
    logging.info("Closeness Centrality")
    for user in users_dict:
        uid = user["id"]
        centrality = user["closeness_centrality"]
        logging.info("%r", f"user {uid}, closeness_centrality {centrality}")


def get_betweeness(users_dict):
    logging.info("Betweenness Centrality")
    for user in users_dict:
        uid = user["id"]
        centrality = user["betweenness_centrality"]
        logging.info("%r", f"user {uid}, betweenness {centrality}")


def populate_closeness(users_dict):
    eps = 0.001
    for user in users_dict:
        farness_user = farness(user)
        closeness_user = 1 / (farness_user + eps)
        user["closeness_centrality"] = closeness_user
    return users_dict


def populate_shortest_paths(users_dict):
    for user in users_dict:
        user["shortest_paths"] = shortest_paths_from(user)
    return users_dict


def populate_betweeness_v1(users_dict):
    for user in users_dict:
        user["betweenness_centrality"] = 0.0
    for source in users_dict:
        source_id = source["id"]
        for target_id, paths_item in source["shortest_paths"].items():
            if source_id < target_id:  # don't double count
                num_paths = len(paths_item)  # how many shortest paths?
                contrib = 1 / num_paths  # contribution to centrality
                for path in paths_item:
                    for identification in path:
                        if identification not in [source_id, target_id]:
                            users_dict[identification]["betweenness_centrality"] += contrib
    return users_dict


def initialize_centrality(users_dict):
    """Initialize betweenness centrality for all users."""
    if isinstance(users_dict,list):
        for user in users_dict:
            user["betweenness_centrality"] = 0.0
    else:
        for user in users_dict.values():
            user["betweenness_centrality"] = 0.0


def process_shortest_paths(source, users_dict):
    """Update centrality contributions based on shortest paths."""
    source_id = source["id"]
    for target_id, paths_item in source["shortest_paths"].items():
        if source_id < target_id:  # avoid double counting
            contrib = 1 / len(paths_item)  # contribution to centrality
            for path in paths_item:
                update_centrality(path, contrib, source_id, target_id, users_dict)


def update_centrality(path, contrib, source_id, target_id, users_dict):
    """Add contributions to centrality for each user in the path."""
    for identification in path:
        if identification not in (source_id, target_id):
            users_dict[identification]["betweenness_centrality"] += contrib


def populate_betweeness(users_dict):
    """Calculate and populate betweenness centrality for users."""
    initialize_centrality(users_dict)
    if isinstance(users_dict,list):
        for source in users_dict:
            process_shortest_paths(source, users_dict)
    else:
        for source in users_dict.values():
            process_shortest_paths(source, users_dict)
    return users_dict


def populate_friends(users_dict, friendships):
    # initialize friends list
    for user in users_dict:
        user["friends"] = []

    # populate friends list
    for friend_i, friend_j in friendships:
        # this works because users[i] is the user whose id is i
        users_dict[friend_i]["friends"].append(users_dict[friend_j])  # add i as a friend of j
        users_dict[friend_j]["friends"].append(users_dict[friend_i])  # add j as a friend of i
    return users_dict


def shortest_paths_from(from_user_graph):
    # a dictionary from "user_id" to *all* the shortest paths to that user
    shortest_paths_to = {from_user_graph["id"]: [[]]}

    # a queue of (previous user, next user) that we need to check.
    # starts out with all pairs (from_user, friend_of_from_user)
    frontier = deque((from_user_graph, friend) for friend in from_user_graph["friends"])

    # keep going until we empty the queue
    while frontier:

        prev_user, user = frontier.popleft()  # take from the beginning
        user_id = user["id"]

        # the fact that we're pulling from our queue means that
        # necessarily we already know the shortest path to prev_user
        paths_to_prev = shortest_paths_to[prev_user["id"]]
        paths_via_prev = [_ + [user_id] for _ in paths_to_prev]

        # it's possible we already know the shortest path to here as well
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
            if len(path_via_prev) <= min_path_length and path_via_prev not in old_paths_to_here
        ]

        shortest_paths_to[user_id] = old_paths_to_here + new_paths_to_here

        # add new neighbors to the frontier
        frontier.extend(
            (user, friend)
            for friend in user["friends"]
            if friend["id"] not in shortest_paths_to
        )

    return shortest_paths_to


def farness(user):
    """the sum of the lengths of the shortest paths to each other user"""
    return sum(len(paths[0]) for paths in user["shortest_paths"].values())


def matrix_product_entry(a_matrix, b_matrix, i, j):
    # matrix multiplication
    return dot(get_row(a_matrix, i), get_column(b_matrix, j))


def matrix_multiply(a_matrix, b_matrix):
    n1, k1 = shape(a_matrix)
    n2, k2 = shape(b_matrix)
    if k1 != n2:
        raise ArithmeticError("incompatible shapes!")

    return make_matrix(n1, k2, partial(matrix_product_entry, a_matrix, b_matrix))


def vector_as_matrix(v):
    """returns the vector v (represented as a list) as an n x 1 matrix"""
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


def page_rank(users, damping=0.85, num_iters=100):
    logging.info("page_rank")
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
