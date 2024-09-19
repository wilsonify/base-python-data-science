from collections import Counter

from dsl.c02_crash_course.e0209_counters import count_words_with_counter, most_common_words


def test_count_words_with_counter():
    document = ["data", "science", "data", "awesome", "science", "science"]
    word_counts = count_words_with_counter(document)
    assert word_counts == {"data": 2, "science": 3, "awesome": 1}


def test_most_common_words():
    word_counts = Counter({"data": 2, "science": 3, "awesome": 1})
    top_two = most_common_words(word_counts, 2)
    assert top_two == [("science", 3), ("data", 2)]
