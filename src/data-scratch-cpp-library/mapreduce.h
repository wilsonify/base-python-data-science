#include "naive_bayes.h"

double word_count_old(documents);
double wc_mapper(document);
double wc_reducer(word, counts);
double word_count(documents);
double map_reduce(inputs, mapper, reducer);
double reduce_with(aggregation_fn, key, values);
double values_reducer(aggregation_fn);
double most_popular_word_reducer(user, words_and_counts);
double most_popular_word_reducer(user, words_and_counts);
double liker_mapper(status_update);
double matrix_multiply_mapper(m, element);
double matrix_multiply_reducer(m, key, indexed_values);