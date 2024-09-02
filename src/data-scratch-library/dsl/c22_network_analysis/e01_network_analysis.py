import logging
from logging.config import dictConfig

from dsl.c22_network_analysis.network_analysis import (
    page_rank,
    populate_friends,
    populate_shortest_paths,
    populate_betweeness,
    populate_closeness,
    get_betweeness,
    get_closeness,
    construct_adjacency,
    compute_eigenvectors,
    get_eigenvector_centrality,
    populate_endorsments,
    get_page_ranks,
    populate_endorsements
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


def main():
    users_dict_outer = populate_friends(users_dict, friendships)
    users_dict_outer = populate_shortest_paths(users_dict_outer)
    users_dict_outer = populate_betweeness(users_dict_outer)
    users_dict_outer = populate_closeness(users_dict_outer)

    get_betweeness(users_dict_outer)
    get_closeness(users_dict_outer)

    adjacency_matrix = construct_adjacency(users_dict, friendships)
    eigenvector_centralities = compute_eigenvectors(adjacency_matrix)

    get_eigenvector_centrality(eigenvector_centralities)

    users_dict_outer = populate_endorsments(users_dict_outer, endorsements)
    page_rank_outer = page_rank(users_dict_outer)
    get_page_ranks(page_rank_outer)

    endorsements_list = populate_endorsements(users_dict_outer)
    endorsements_list_sorted = sorted(endorsements_list, key=lambda pair: pair[1], reverse=True)
    print(f"endorsements_list_sorted = {endorsements_list_sorted}")


if __name__ == "__main__":
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))
    main()
