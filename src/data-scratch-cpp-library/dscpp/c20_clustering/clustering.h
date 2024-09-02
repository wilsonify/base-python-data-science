#include "linear_algebra.h"

double squared_clustering_errors(inputs, k);
double is_leaf(cluster_);
double get_children(cluster_);
double get_values(cluster_);
double cluster_distance(cluster1, cluster2, distance_agg=min);
double get_merge_order(cluster_);
double bottom_up_cluster(inputs, distance_agg=min);
double generate_clusters(base_cluster, num_clusters);