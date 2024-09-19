from collections import Counter

# Function to count words using Counter
def count_words_with_counter(document):
    """Counts the occurrences of each word in the document using Counter."""
    return Counter(document)

# Function to get the most common words
def most_common_words(word_counts, n=10):
    """Returns the n most common words from the word_counts Counter."""
    return word_counts.most_common(n)
