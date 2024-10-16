import logging
import random
import re
from collections import defaultdict, Counter
from logging.config import dictConfig

import requests
from bs4 import BeautifulSoup


def plot_resumes(plt):
    data = [
        ("big data", 100, 15),
        ("Hadoop", 95, 25),
        ("Python", 75, 50),
        ("R", 50, 40),
        ("machine learning", 80, 20),
        ("statistics", 20, 60),
        ("data science", 60, 70),
        ("analytics", 90, 3),
        ("team player", 85, 85),
        ("dynamic", 2, 90),
        ("synergies", 70, 0),
        ("actionable insights", 40, 30),
        ("think out of the box", 45, 10),
        ("self-starter", 30, 50),
        ("customer focus", 65, 15),
        ("thought leadership", 35, 35),
    ]

    def text_size(total):
        """equals 8 if total is 0, 28 if total is 200"""
        return 8 + total / 200 * 20

    for word, job_popularity, resume_popularity in data:
        plt.text(
            job_popularity,
            resume_popularity,
            word,
            ha="center",
            va="center",
            size=text_size(job_popularity + resume_popularity),
        )
    plt.xlabel("Popularity on Job Postings")
    plt.ylabel("Popularity on Resumes")
    plt.axis([0, 100, 0, 100])
    plt.show()


#
# n-gram models
#


def fix_unicode(text):
    return text.replace(u"\u2019", "'")


def get_document():
    url = "http://radar.oreilly.com/2010/06/what-is-data-science.html"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html5lib")

    content = soup.find("div", "article-body")  # find article-body div
    regex = r"[\w']+|[\.]"  # matches a word or a period

    document = []

    for paragraph in content("p"):
        words = re.findall(regex, fix_unicode(paragraph.text))
        document.extend(words)

    return document


def generate_using_bigrams(transitions):
    current = "."  # this means the next word will start a sentence
    result = []
    while True:
        next_word_candidates = transitions[current]  # bigrams (current, _)
        current = random.choice(next_word_candidates)  # choose one at random
        result.append(current)  # append it to results
        if current == ".":
            return " ".join(result)  # if "." we're done


def generate_using_trigrams(_starts, _trigram_transitions):
    _current_ = random.choice(_starts)  # choose a random starting word
    _prev = "."  # and precede it with a '.'
    result = [_current_]
    while True:
        next_word_candidates = _trigram_transitions[(_prev, _current_)]
        next_word = random.choice(next_word_candidates)

        _prev, _current_ = _current_, next_word
        result.append(_current_)

        if _current_ == ".":
            return " ".join(result)


def is_terminal(token):
    return token[0] != "_"


def expand(_grammar, tokens):
    for _i, token in enumerate(tokens):

        # ignore terminals
        if is_terminal(token):
            continue

        # choose a replacement at random
        replacement = random.choice(_grammar[token])

        if is_terminal(replacement):
            tokens[_i] = replacement
        else:
            tokens = tokens[:_i] + replacement.split() + tokens[(_i + 1):]
        return expand(_grammar, tokens)

    # if we get here we had all terminals and are done
    return tokens


def generate_sentence(_grammar):
    return expand(_grammar, ["_S"])


#
# Gibbs Sampling
#


def roll_a_die():
    return random.choice([1, 2, 3, 4, 5, 6])


def direct_sample():
    d1 = roll_a_die()
    d2 = roll_a_die()
    return d1, d1 + d2


def random_y_given_x(x):
    """equally likely to be x + 1, x + 2, ... , x + 6"""
    return x + roll_a_die()


def random_x_given_y(y):
    if y <= 7:
        # if the total is 7 or less, the first die is equally likely to be
        # 1, 2, ..., (total - 1)
        return random.randrange(1, y)
    else:
        # if the total is 7 or more, the first die is equally likely to be
        # (total - 6), (total - 5), ..., 6
        return random.randrange(y - 6, 7)


def gibbs_sample(num_iters=100):
    x, y = 1, 2  # doesn't really matter
    for _ in range(num_iters):
        x = random_x_given_y(y)
        y = random_y_given_x(x)
    return x, y


def compare_distributions(num_samples=1000):
    counts = defaultdict(lambda: [0, 0])
    for _ in range(num_samples):
        counts[gibbs_sample()][0] += 1
        counts[direct_sample()][1] += 1
    return counts


#
# TOPIC MODELING
#


def sample_from(weights):
    total = sum(weights)
    rnd = total * random.random()  # uniform between 0 and total
    for _i, w in enumerate(weights):
        rnd -= w  # return the smallest _i such that
        if rnd <= 0:
            return _i  # sum(weights[:(_i+1)]) >= rnd


big_data_str = "Big Data"
documents = [
    ["Hadoop", big_data_str, "HBase", "Java", "Spark", "Storm", "Cassandra"],
    ["NoSQL", "MongoDB", "Cassandra", "HBase", "Postgres"],
    ["Python", "scikit-learn", "scipy", "numpy", "statsmodels", "pandas"],
    ["R", "Python", "statistics", "regression", "probability"],
    ["machine learning", "regression", "decision trees", "libsvm"],
    ["Python", "R", "Java", "C++", "Haskell", "programming languages"],
    ["statistics", "probability", "mathematics", "theory"],
    ["machine learning", "scikit-learn", "Mahout", "neural networks"],
    ["neural networks", "deep learning", big_data_str, "artificial intelligence"],
    ["Hadoop", "Java", "MapReduce", big_data_str],
    ["statistics", "R", "statsmodels"],
    ["C++", "deep learning", "artificial intelligence", "probability"],
    ["pandas", "R", "Python"],
    ["databases", "HBase", "Postgres", "MySQL", "MongoDB"],
    ["libsvm", "regression", "support vector machines"],
]

K = 4

document_topic_counts = [Counter() for _ in documents]

topic_word_counts = [Counter() for _ in range(K)]

topic_counts = [0 for _ in range(K)]

document_lengths = [len(d) for d in documents]

distinct_words = set(word for document in documents for word in document)
W = len(distinct_words)

D = len(documents)


def p_topic_given_document(topic, d, alpha=0.1):
    """the fraction of words in document _d_
    that are assigned to _topic_ (plus some smoothing)"""

    return (document_topic_counts[d][topic] + alpha) / (document_lengths[d] + K * alpha)


def p_word_given_topic(word, topic, beta=0.1):
    """the fraction of words assigned to _topic_
    that equal _word_ (plus some smoothing)"""

    return (topic_word_counts[topic][word] + beta) / (topic_counts[topic] + W * beta)


def topic_weight(d, word, k):
    """given a document and a word in that document,
    return the weight for the k-th topic"""

    return p_word_given_topic(word, k) * p_topic_given_document(k, d)


def choose_new_topic(d, word):
    return sample_from([topic_weight(d, word, k) for k in range(K)])


random.seed(0)
document_topics = [[random.randrange(K) for word in document] for document in documents]

for d in range(D):
    for word, _topic in zip(documents[d], document_topics[d]):
        document_topic_counts[d][_topic] += 1
        topic_word_counts[_topic][word] += 1
        topic_counts[_topic] += 1

for iteration in range(1000):
    for d in range(D):
        for i, (word, _topic) in enumerate(zip(documents[d], document_topics[d])):
            # remove this word / topic from the counts
            # so that it doesn't influence the weights
            document_topic_counts[d][_topic] -= 1
            topic_word_counts[_topic][word] -= 1
            topic_counts[_topic] -= 1
            document_lengths[d] -= 1

            # choose a new topic based on the weights
            new_topic = choose_new_topic(d, word)
            document_topics[d][i] = new_topic

            # and now add it back to the counts
            document_topic_counts[d][new_topic] += 1
            topic_word_counts[new_topic][word] += 1
            topic_counts[new_topic] += 1
            document_lengths[d] += 1

if __name__ == "__main__":
    dictConfig(dict(
        version=1,
        formatters={"simple": {"format": """%(asctime)s | %(name)s | %(lineno)s | %(levelname)s | %(message)s"""}},
        handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
        root={"handlers": ["console"], "level": logging.DEBUG},
    ))
    document = get_document()

    bigrams = list(zip(document, document[1:]))
    _transitions = defaultdict(list)
    for prev, _current in bigrams:
        _transitions[prev].append(_current)

    random.seed(0)
    logging.info("bigram sentences")
    for i in range(10):
        logging.debug("i = {}".format(i))
        logging.info("%r", "generate_using_bigrams(_transitions) {}".format(generate_using_bigrams(_transitions)))

    # trigrams

    trigrams = list(zip(document, document[1:], document[2:]))
    trigram_transitions = defaultdict(list)
    starts = []

    for prev, _current, next_gram in trigrams:

        if prev == ".":  # if the previous "word" was a period
            starts.append(_current)  # then this is a start word

        trigram_transitions[(prev, _current)].append(next_gram)

    logging.info("trigram sentences")
    for i in range(10):
        logging.debug("%r", "i={}".format(i))
        logging.info(
            "%r",
            " generate_using_trigrams(starts, trigram_transitions) {}".format(
                generate_using_trigrams(starts, trigram_transitions)
            )
        )

    grammar = {
        "_S": ["_NP _VP"],
        "_NP": ["_N", "_A _NP _P _A _N"],
        "_VP": ["_V", "_V _NP"],
        "_N": ["data science", "Python", "regression"],
        "_A": ["big", "linear", "logistic"],
        "_P": ["about", "near"],
        "_V": ["learns", "trains", "tests", "is"],
    }

    logging.info("grammar sentences")
    for i in range(10):
        logging.debug("%r", "i = {}".format(i))
        logging.info("%r", "generate_sentence(grammar) ={}".format(" ".join(generate_sentence(grammar))))

    logging.info("gibbs sampling")
    comparison = compare_distributions()
    for roll, (gibbs, direct) in comparison.items():
        logging.info("%r", "roll {}, gibbs {}, direct {}".format(roll, gibbs, direct))

    # topic MODELING

    for kth, word_counts in enumerate(topic_word_counts):
        for word, count in word_counts.most_common():
            if count > 0:
                logging.info("%r", "kth {}, word {}, count {}".format(kth, word, count))

    topic_names = [
        "Big Data and programming languages",
        "databases",
        "machine learning",
        "statistics",
    ]

    for document, topic_counts in zip(documents, document_topic_counts):
        logging.info("%r", "document ={}  ".format(document))
        for _topic, count in topic_counts.most_common():
            if count > 0:
                logging.debug("%r", "count={}".format(count))
                logging.info("%r", "topic_names[_topic] = {}".format(topic_names[_topic]))
