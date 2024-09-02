
/* class KMeans: performs k-means clustering */

void KMeans::KMeans(integer k)
{
    this->k = k;        // number of clusters
    this->means = None; // means of clusters
}

double KMeans::classify(*this, inputs)
{
    /* return the index of the cluster closest to the input */
    return min(range(*this->k), key = lambda i
               : squared_distance(inputs, *this->means[i]))
}

double KMeans::train(*this, inputs)
{

        *this->means = random.sample(inputs, *this->k)
        assignments = None

        while True:
            // Find new assignments
            new_assignments = list(map(*this->classify, inputs))

            // If no assignments have changed, we're done.
            if assignments == new_assignments:
                return

            // Otherwise keep the new assignments,
            assignments = new_assignments

            for i in range(*this->k):
                i_points = [p for p, a in zip(inputs, assignments) if a == i]
                // avoid divide-by-zero if i_points is empty
                if i_points:
                    *this->means[i] = vector_mean(i_points)
}