import pytest

from dsl.c25_mapreduce.mapreduce import (
    count_distinct_reducer,
    liker_mapper,
    map_reduce,
    max_reducer,
    min_reducer,
    most_popular_word_reducer,
    reduce_with,
    sum_reducer,
    values_reducer,
    wc_mapper,
    wc_reducer,
    word_count,
    word_count_old,
)


@pytest.fixture
def sample_documents():
    return ["data science is fun", "data is the new oil"]


class TestWordCountOld:
    def test_basic_count(self, sample_documents):
        result = word_count_old(sample_documents)
        assert result["data"] == 2
        assert result["is"] == 2

    def test_empty_documents(self):
        result = word_count_old([])
        assert len(result) == 0

    def test_single_document(self):
        result = word_count_old(["hello world hello"])
        assert result["hello"] == 1  # tokenize returns a set, so deduped per doc
        assert result["world"] == 1


class TestWcMapper:
    def test_yields_pairs(self):
        results = list(wc_mapper("hello world"))
        assert all(isinstance(pair, tuple) and len(pair) == 2 for pair in results)

    def test_count_is_one(self):
        results = list(wc_mapper("hello world"))
        assert all(count == 1 for _, count in results)

    def test_words_lowercased(self):
        results = list(wc_mapper("Hello World"))
        words = [word for word, _ in results]
        assert all(w == w.lower() for w in words)


class TestWcReducer:
    def test_sums_counts(self):
        results = list(wc_reducer("hello", [1, 1, 1]))
        assert results == [("hello", 3)]

    def test_single_count(self):
        results = list(wc_reducer("word", [1]))
        assert results == [("word", 1)]


class TestWordCount:
    def test_basic_count(self, sample_documents):
        result = dict(word_count(sample_documents))
        assert result["data"] == 2
        assert result["is"] == 2

    def test_empty_documents(self):
        result = word_count([])
        assert len(result) == 0

    def test_single_word_doc(self):
        result = dict(word_count(["hello"]))
        assert result["hello"] == 1


class TestMapReduce:
    def test_with_wc(self, sample_documents):
        result = dict(map_reduce(sample_documents, wc_mapper, wc_reducer))
        assert result["data"] == 2

    def test_empty_inputs(self):
        result = map_reduce([], wc_mapper, wc_reducer)
        assert result == []

    def test_custom_mapper_reducer(self):
        def char_mapper(word):
            for c in word:
                yield (c, 1)

        def char_reducer(char, counts):
            yield (char, sum(counts))

        result = dict(map_reduce(["aab", "abc"], char_mapper, char_reducer))
        assert result["a"] == 3
        assert result["b"] == 2
        assert result["c"] == 1


class TestReduceWith:
    def test_sum(self):
        results = list(reduce_with(sum, "key", [1, 2, 3]))
        assert results == [("key", 6)]

    def test_max(self):
        results = list(reduce_with(max, "key", [1, 5, 3]))
        assert results == [("key", 5)]

    def test_len(self):
        results = list(reduce_with(len, "key", [1, 2, 3]))
        assert results == [("key", 3)]


class TestValuesReducer:
    def test_creates_reducer(self):
        my_reducer = values_reducer(sum)
        results = list(my_reducer("key", [1, 2, 3]))
        assert results == [("key", 6)]

    def test_with_custom_fn(self):
        avg_reducer = values_reducer(lambda vals: sum(vals) / len(vals))
        results = list(avg_reducer("key", [2, 4, 6]))
        assert results == [("key", 4.0)]


class TestBuiltinReducers:
    def test_sum_reducer(self):
        results = list(sum_reducer("total", [10, 20, 30]))
        assert results == [("total", 60)]

    def test_max_reducer(self):
        results = list(max_reducer("max", [10, 50, 30]))
        assert results == [("max", 50)]

    def test_min_reducer(self):
        results = list(min_reducer("min", [10, 50, 30]))
        assert results == [("min", 10)]

    def test_count_distinct_reducer(self):
        results = list(count_distinct_reducer("distinct", [1, 2, 2, 3, 3, 3]))
        assert results == [("distinct", 3)]

    def test_count_distinct_all_same(self):
        results = list(count_distinct_reducer("distinct", [5, 5, 5]))
        assert results == [("distinct", 1)]


class TestMostPopularWordReducer:
    def test_basic(self):
        words_and_counts = [("python", 3), ("java", 1), ("python", 2)]
        results = list(most_popular_word_reducer("user1", words_and_counts))
        assert len(results) == 1
        user, (word, count) = results[0]
        assert user == "user1"
        assert word == "python"
        assert count == 5

    def test_single_word(self):
        results = list(most_popular_word_reducer("user", [("sql", 10)]))
        user, (word, count) = results[0]
        assert word == "sql"
        assert count == 10


class TestLikerMapper:
    def test_yields_user_liker_pairs(self):
        status = {"username": "alice", "liked_by": ["bob", "charlie"]}
        results = list(liker_mapper(status))
        assert ("alice", "bob") in results
        assert ("alice", "charlie") in results

    def test_no_likers(self):
        status = {"username": "alice", "liked_by": []}
        results = list(liker_mapper(status))
        assert results == []


class TestMapReduceIntegration:
    def test_sum_reducer_with_map_reduce(self):
        def number_mapper(n):
            yield ("sum", n)

        result = dict(map_reduce([1, 2, 3, 4, 5], number_mapper, sum_reducer))
        assert result["sum"] == 15

    def test_max_reducer_with_map_reduce(self):
        def number_mapper(n):
            yield ("max", n)

        result = dict(map_reduce([1, 5, 3, 2, 4], number_mapper, max_reducer))
        assert result["max"] == 5

    def test_grouping(self):
        def parity_mapper(n):
            yield ("even" if n % 2 == 0 else "odd", n)

        result = dict(map_reduce([1, 2, 3, 4, 5], parity_mapper, sum_reducer))
        assert result["even"] == 6
        assert result["odd"] == 9
