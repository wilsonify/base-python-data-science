
#include "linear_algebra.h"

double populate_endorsements(users_dict);
double get_page_ranks(pr_result);
double get_eigenvector_centrality(eigenvector_centralities);
double populate_endorsments(users_dict, endorsements);
double compute_eigenvectors(adjacency_matrix);
double construct_adjacency(users_dict, friendships);
double get_closeness(users_dict);
double get_betweeness(users_dict);
double populate_closeness(users_dict);
double populate_shortest_paths(users_dict);
double populate_betweeness(users_dict);
double populate_friends(users_dict, friendships);
double shortest_paths_from(from_user_graph);
double farness(user);
double matrix_product_entry(a_matrix, b_matrix, i, j);
double matrix_multiply(a_matrix, b_matrix);
double vector_as_matrix(v);
double vector_from_matrix(v_as_matrix);
double matrix_operate(a_matrix, v);
double find_eigenvector(a_matrix, tolerance = 0.00001);
double page_rank(users, damping = 0.85, num_iters = 100);