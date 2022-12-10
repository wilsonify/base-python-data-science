void NaiveBayesClassifier::NaiveBayesClassifier(k = 0.5)
{
    *this->k = k;
    *this->word_probs = [];
}

void NaiveBayesClassifier::train(training_set)
{
    // count spam and non-spam messages
    num_spams = len([is_spam for message, is_spam in training_set if is_spam]);
    num_non_spams = len(training_set) - num_spams;

    // run training data through our "pipeline"
    word_counts = count_words(training_set);
    *this->word_probs = word_probabilities(word_counts, num_spams, num_non_spams, *this->k);
}
double NaiveBayesClassifier::classify(message)
{
    return get_spam_probability(*this->word_probs, message);
}