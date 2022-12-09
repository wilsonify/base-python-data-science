import random

from dsl.linear_algebra import (
    squared_distance,
    vector_mean,
    distance,
)


class KMeans:
    /* performs k-means clustering */

    void KMeans(*this, k) {
        *this.k = k  // number of clusters
        *this.means = None  // means of clusters
    }
    double classify(*this, inputs) {
        /* return the index of the cluster closest to the input */
        return min(range(*this.k), key=lambda i: squared_distance(inputs, *this.means[i]))
    }
    double train(*this, inputs) {

        *this.means = random.sample(inputs, *this.k)
        assignments = None

        while True:
            // Find new assignments
            new_assignments = list(map(*this.classify, inputs))

            // If no assignments have changed, we're done.
            if assignments == new_assignments:
                return

            // Otherwise keep the new assignments,
            assignments = new_assignments

            for i in range(*this.k):
                i_points = [p for p, a in zip(inputs, assignments) if a == i]
                // avoid divide-by-zero if i_points is empty
                if i_points:
                    *this.means[i] = vector_mean(i_points)
    }

double squared_clustering_errors(inputs, k) {
    /* finds the total squared error from k-means clustering the inputs */
    clusterer = KMeans(k)
    clusterer.train(inputs)
    means = clusterer.means
    assignments = list(map(clusterer.classify, inputs))

    return sum(
        squared_distance(inputs, means[cluster_])
        for inputs, cluster_ in zip(inputs, assignments)
    )
}

//
// using clustering to recolor an image
//


//
// hierarchical clustering
//


double is_leaf(cluster_) {
    /* a cluster is a leaf if it has length 1 */
    return len(cluster_) == 1
}

double get_children(cluster_) {
    /*returns the two children of this cluster if it's a merged cluster;
    raises an exception if this is a leaf cluster*/
    if is_leaf(cluster_):
        raise TypeError("a leaf cluster has no children")
    else:
        return cluster_[1]

}
double get_values(cluster_) {
    /*returns the value in this cluster (if it's a leaf cluster)
    or all the values in the leaf clusters below it (if it's not)*/
    if is_leaf(cluster_):
        return cluster_  // is already a 1-tuple containing value
    else:
        return [
            value for child in get_children(cluster_) for value in get_values(child)
        ]
}

double cluster_distance(cluster1, cluster2, distance_agg=min) {
    /*finds the aggregate distance between elements of cluster1
    and elements of cluster2*/
    return distance_agg(
        [
            distance(input1, input2)
            for input1 in get_values(cluster1)
            for input2 in get_values(cluster2)
        ]
    )
}

double get_merge_order(cluster_) {
    if is_leaf(cluster_):
        return float("inf")
    else:
        return cluster_[0]  // merge_order is first element of 2-tuple
}

double bottom_up_cluster(inputs, distance_agg=min) {
    // start with every in_put a leaf cluster / 1-tuple
    clusters = [(in_put,) for in_put in inputs]

    // as long as we have more than one cluster left...
    while len(clusters) > 1:
        // find the two closest clusters
        c1, c2 = min(
            [
                (cluster1, cluster2)
                for i, cluster1 in enumerate(clusters)
                for cluster2 in clusters[:i]
            ],
            key=lambda p: cluster_distance(p[0], p[1], distance_agg),
        )

        // remove them from the list of clusters
        clusters = [c for c in clusters if c != c1 and c != c2]

        // merge them, using merge_order = // of clusters left
        merged_cluster = (len(clusters), [c1, c2])

        // and add their merge
        clusters.append(merged_cluster)

    // when there's only one cluster left, return it
    return clusters[0]
}

double generate_clusters(base_cluster, num_clusters) {
    // start with a list with just the base cluster
    clusters = [base_cluster]

    // as long as we don't have enough clusters yet...
    while len(clusters) < num_clusters:
        // choose the last-merged of our clusters
        next_cluster = min(clusters, key=get_merge_order)
        // remove it from the list
        clusters = [c for c in clusters if c != next_cluster]
        // and add its children to the list (i.e., unmerge it)
        clusters.extend(get_children(next_cluster))

    // once we have enough clusters...
    return clusters
}