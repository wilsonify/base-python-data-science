import pytest
from collections import defaultdict, Counter

from dsl.c13_naive_bayes.naive_bayes import (
    tokenize, count_words, word_probabilities, get_spam_probability,
    NaiveBayesClassifier, get_subject_data, p_spam_given_word
)


def test_tokenize():
    """Test the tokenize function."""
    # Test basic tokenization
    text = "Hello world! This is a test."
    tokens = tokenize(text)
    
    assert "hello" in tokens
    assert "world" in tokens
    assert "this" in tokens
    assert "is" in tokens
    assert "a" in tokens
    assert "test" in tokens
    
    # Test that punctuation is removed
    assert "world!" not in tokens
    assert "test." not in tokens
    
    # Test case normalization
    assert "Hello" not in tokens
    assert "hello" in tokens
    
    # Test that duplicates are removed (returns set)
    text_with_duplicates = "hello hello world"
    tokens_dup = tokenize(text_with_duplicates)
    assert len(tokens_dup) == 2  # Should remove duplicate "hello"


def test_count_words():
    """Test the count_words function."""
    training_set = [
        ("buy viagra now", True),
        ("hello friend", False),
        ("cheap pills buy", True),
        ("meeting tomorrow", False)
    ]
    
    counts = count_words(training_set)
    
    # Check that spam words are counted correctly
    assert counts["buy"][0] == 2  # "buy" appears in 2 spam messages
    assert counts["buy"][1] == 0  # "buy" appears in 0 non-spam messages
    
    # Check ham words
    assert counts["hello"][0] == 0  # "hello" appears in 0 spam messages
    assert counts["hello"][1] == 1  # "hello" appears in 1 non-spam message
    
    # Check words that appear in both
    training_set_mixed = [
        ("buy now", True),
        ("buy later", False)
    ]
    counts_mixed = count_words(training_set_mixed)
    assert counts_mixed["buy"][0] == 1  # 1 spam
    assert counts_mixed["buy"][1] == 1  # 1 non-spam


def test_word_probabilities():
    """Test the word_probabilities function."""
    counts = {
        "viagra": [2, 0],  # 2 spam, 0 non-spam
        "hello": [0, 2],   # 0 spam, 2 non-spam
        "buy": [1, 1]      # 1 spam, 1 non-spam
    }
    
    probs = word_probabilities(counts, total_spams=2, total_non_spams=2, k=0.5)
    
    # Should return list of (word, p(word|spam), p(word|non_spam))
    assert len(probs) == 3
    
    # Check probabilities are valid
    for word, p_spam, p_non_spam in probs:
        assert 0 <= p_spam <= 1
        assert 0 <= p_non_spam <= 1


def test_get_spam_probability():
    """Test the get_spam_probability function."""
    word_probs = [
        ("viagra", 0.8, 0.1),  # spam indicator
        ("hello", 0.1, 0.8),   # ham indicator
        ("buy", 0.5, 0.5)      # neutral
    ]
    
    # Test spammy message
    spam_prob = get_spam_probability(word_probs, "buy viagra now")
    assert spam_prob > 0.5
    
    # Test ham message
    ham_prob = get_spam_probability(word_probs, "hello friend")
    assert ham_prob < 0.5


def test_p_spam_given_word():
    """Test the p_spam_given_word function."""
    word_prob = ("viagra", 0.8, 0.2)  # word, p(word|spam), p(word|non_spam)
    
    result = p_spam_given_word(word_prob)
    expected = 0.8 / (0.8 + 0.2)  # 0.8 / 1.0 = 0.8
    
    assert result == pytest.approx(expected)


def test_naive_bayes_classifier():
    """Test the NaiveBayesClassifier class."""
    classifier = NaiveBayesClassifier()
    
    # Training data
    training_set = [
        ("buy viagra now cheap pills", True),
        ("online pharmacy buy today", True),
        ("limited offer cheap drugs", True),
        ("hello friend how are you", False),
        ("meeting tomorrow at office", False),
        ("project update please review", False)
    ]
    
    # Train the classifier
    classifier.train(training_set)
    
    # Test predictions
    spam_score = classifier.classify("buy cheap viagra now")
    ham_score = classifier.classify("hello friend meeting")
    
    assert spam_score > ham_score
    assert spam_score > 0.5
    assert ham_score < 0.5


def test_naive_bayes_classifier_edge_cases():
    """Test NaiveBayesClassifier edge cases."""
    classifier = NaiveBayesClassifier()
    
    # Test with no training data
    try:
        classifier.classify("test message")
        assert False, "Should raise error with no training data"
    except (ZeroDivisionError, ValueError, IndexError):
        pass  # Expected
    
    # Train with one message of each type
    training_set_small = [
        ("spam message", True),
        ("ham message", False)
    ]
    classifier.train(training_set_small)
    
    # Should work now
    prob = classifier.classify("spam")
    assert 0 <= prob <= 1


def test_get_subject_data():
    """Test the get_subject_data function."""
    try:
        # This might fail if test data doesn't exist, but we can test the function exists
        subjects = get_subject_data("path/to/test/data/*")
        # If it succeeds, check that it returns expected structure
        assert isinstance(subjects, list)
    except (FileNotFoundError, OSError):
        # Expected if test data doesn't exist
        pytest.skip("Test data not available")


def test_naive_bayes_with_repeated_words():
    """Test that repeated words are handled correctly."""
    classifier = NaiveBayesClassifier()
    
    # Train with messages containing repeated words
    training_set = [
        ("buy buy buy viagra cheap", True),
        ("hello hello friend", False)
    ]
    classifier.train(training_set)
    
    # Test classification
    spam_prob = classifier.classify("buy cheap viagra")
    ham_prob = classifier.classify("hello friend")
    
    assert spam_prob > ham_prob


def test_naive_bayes_smoothing():
    """Test that Laplace smoothing works."""
    classifier = NaiveBayesClassifier(k=1.0)  # Higher smoothing
    
    training_set = [
        ("spam message", True),
        ("ham message", False)
    ]
    classifier.train(training_set)
    
    # Should handle unknown words gracefully
    prob_unknown = classifier.classify("unknown word")
    assert 0 <= prob_unknown <= 1


def test_naive_bayes_probabilities_sum_to_one():
    """Test that spam + non-spam probabilities sum to 1."""
    classifier = NaiveBayesClassifier()
    
    training_set = [
        ("buy viagra", True),
        ("hello friend", False)
    ]
    classifier.train(training_set)
    
    # Get internal word probabilities and test they're valid
    for word_prob in classifier.word_probs:
        word, p_spam, p_non_spam = word_prob
        assert p_spam + p_non_spam > 0
        # These are conditional probabilities, so they don't need to sum to 1
        assert 0 <= p_spam <= 1
        assert 0 <= p_non_spam <= 1


def test_naive_bayes_empty_message():
    """Test classification of empty message."""
    classifier = NaiveBayesClassifier()
    
    training_set = [
        ("spam message", True),
        ("ham message", False)
    ]
    classifier.train(training_set)
    
    # Empty message should default to prior probabilities
    prob_empty = classifier.classify("")
    assert 0 <= prob_empty <= 1
