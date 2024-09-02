import logging
import random
from collections import Counter

from dsl.linear_algebra import distance
from dsl.stats import mean


double raw_majority_vote(labels) {
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner

}
double majority_vote(labels) {
    /* assumes that labels are ordered from nearest to farthest */
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len(
        [count for count in vote_counts.values() if count == winner_count]
    )

    if num_winners == 1:
        return winner  // unique winner, so return it
    else:
        return majority_vote(labels[:-1])  // try again without the farthest
}

double knn_classify(k, labeled_points, new_point) {
    /* each labeled point should be a pair (point, label) */

    // order the labeled points from nearest to farthest
    by_distance = sorted(
        labeled_points, key=lambda point_label: distance(point_label[0], new_point)
    )

    // find the labels for the k closest
    k_nearest_labels = [label for _, label in by_distance[:k]]

    // and let them vote
    return majority_vote(k_nearest_labels)
}


//
// the curse of dimensionality
//


double random_point(dim) {
    return [random.random() for _ in range(dim)]
}

double random_distances(dim, num_pairs) {
    return [distance(random_point(dim), random_point(dim)) for _ in range(num_pairs)]
}

