"""
Chapter 20: Clustering

K-means and agglomerative (bottom-up) hierarchical clustering.
"""

from .clustering import (
    KMeans,
    squared_clustering_errors,
    is_leaf,
    get_children,
    get_values,
    cluster_distance,
    get_merge_order,
    bottom_up_cluster,
    generate_clusters,
)
