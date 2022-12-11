
double tokenize(message);
double count_words(training_set);
double word_probabilities(counts, total_spams, total_non_spams, k=0.5);
double get_spam_probability(word_probs, message);
double get_subject_data(path);
double p_spam_given_word(word_prob);