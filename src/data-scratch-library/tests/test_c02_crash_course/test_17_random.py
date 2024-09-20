import random

from dsl.c02_crash_course.e0217_random import (
    generate_uniform_randoms,
    random_choice_with_replacement,
    random_from_range,
    random_choice,
    random_sample, shuffle_list
)


def test_generate_uniform_randoms():
    random.seed(10)
    # uniform random numbers with seed 10
    random_numbers = generate_uniform_randoms(10, 4)
    expected_result = [0.5714025946899135, 0.4288890546751146, 0.5780913011344704, 0.20609823213950174]
    assert random_numbers == expected_result, f"Expected {expected_result}, got {random_numbers}"


def test_random_from_range():
    random.seed(10)
    # Test: Generate a random number from range(10) with seed 10
    random_num = random_from_range(10, 10)
    assert random_num == 9, f"Expected 9, got {random_num}"


def test_random_from_range2():
    # Test: Generate a random number from range(3, 6) with seed 10
    random.seed(10)
    random_num = random_from_range(10, 3, 6)
    assert random_num == 5, f"Expected 4, got {random_num}"


def test_shuffle_list():
    # Test: Shuffle a list with seed 10
    random.seed(10)
    up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffled_list = shuffle_list(10, up_to_ten)
    expected_shuffle = [6, 3, 8, 2, 9, 5, 4, 7, 1, 10]
    assert shuffled_list == expected_shuffle, f"Expected {expected_shuffle}, got {shuffled_list}"


def test_random_choice():
    # Test: Random choice from a list with seed 10
    random.seed(10)
    friend = random_choice(10, ["Alice", "Bob", "Charlie"])
    assert friend == 'Charlie', f"Expected 'Bob', got {friend}"


def test_random_sample():
    # Test: Random sample of 6 elements from a range of 60 with seed 10
    random.seed(10)
    lottery_numbers = range(60)
    winning_numbers = random_sample(10, lottery_numbers, 6)
    expected_numbers = [36, 2, 27, 30, 59, 0]
    assert winning_numbers == expected_numbers, f"Expected {expected_numbers}, got {winning_numbers}"


def test_random_choice_with_replacement():
    # Test: Random choice with replacement from range(10) with seed 10
    random.seed(10)
    choices = random_choice_with_replacement(10, range(10), 4)
    expected_choices = [9, 0, 6, 7]
    assert choices == expected_choices, f"Expected {expected_choices}, got {choices}"
