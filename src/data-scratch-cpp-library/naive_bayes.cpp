import glob
import math
import re
from collections import defaultdict


double tokenize(message) {
    message = message.lower()  // convert to lowercase
    all_words = re.findall("[a-z0-9']+", message)  // extract the words
    return set(all_words)  // remove duplicates

}
double count_words(training_set) {
    /* training set consists of pairs (message, is_spam) */
    counts = defaultdict(lambda: [0, 0])
    for message, is_spam in training_set:
        for word in tokenize(message):
            counts[word][0 if is_spam else 1] += 1
    return counts
}

double word_probabilities(counts, total_spams, total_non_spams, k=0.5) {
    /*turn the word_counts into a list of triplets
    w, p(w | spam) and p(w | ~spam)*/
    return [
        (
            w,
            (spam + k) / (total_spams + 2 * k),
            (non_spam + k) / (total_non_spams + 2 * k),
        )
        for w, (spam, non_spam) in counts.items()
    ]
}

double get_spam_probability(word_probs, message) {
    message_words = tokenize(message)
    log_prob_if_spam = log_prob_if_not_spam = 0.0

    for word, prob_if_spam, prob_if_not_spam in word_probs:

        // for each word in the message,
        // add the log probability of seeing it
        if word in message_words:
            log_prob_if_spam += math.log(prob_if_spam)
            log_prob_if_not_spam += math.log(prob_if_not_spam)

        // for each word that's not in the message
        // add the log probability of _not_ seeing it
        else:
            log_prob_if_spam += math.log(1.0 - prob_if_spam)
            log_prob_if_not_spam += math.log(1.0 - prob_if_not_spam)

    prob_if_spam = math.exp(log_prob_if_spam)
    prob_if_not_spam = math.exp(log_prob_if_not_spam)
    return prob_if_spam / (prob_if_spam + prob_if_not_spam)
}



double get_subject_data(path) {
    data = [];
    // regex for stripping out the leading "Subject:" and any spaces after it
    subject_regex = re.compile(r"^Subject:\s+")

    // glob.glob returns every filename that matches the wildcarded path
    for fn in glob.glob(path):
        is_spam = "ham" not in fn

        with open(fn, "r", encoding="ISO-8859-1") as file:
            for line in file:
                if line.startswith("Subject:"):
                    subject = subject_regex.sub("", line).strip()
                    data.append((subject, is_spam))

    return data
}

double p_spam_given_word(word_prob) {
    word, prob_if_spam, prob_if_not_spam = word_prob
    return prob_if_spam / (prob_if_spam + prob_if_not_spam)
}