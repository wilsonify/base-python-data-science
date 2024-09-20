from dsl.c02_crash_course.e0216_oop import CountingClicker, NoResetClicker


def test_case_1():
    # Initialize clicker to 0 and check count
    clicker = CountingClicker()
    assert clicker.read() == 0, "Clicker should start with count 0"


def test_case_2():
    # Click twice and check the count
    clicker = CountingClicker()
    clicker.click()
    clicker.click()
    assert clicker.read() == 2, "After two clicks, count should be 2"


def test_case_3():
    # Reset the clicker and check the count
    clicker = CountingClicker()
    clicker.reset()
    assert clicker.read() == 0, "After reset, count should be 0"


def test_case_4():
    # Click multiple times at once
    clicker = CountingClicker()
    clicker.click(3)
    assert clicker.read() == 3, "After clicking 3 times, count should be 3"


def test_case_5():
    # Test case 1: Initialize and click once
    no_reset_clicker = NoResetClicker()
    assert no_reset_clicker.read() == 0, "NoResetClicker should start with count 0"
    no_reset_clicker.click()
    assert no_reset_clicker.read() == 1, "After one click, count should be 1"


def test_case_6():
    # Test case 2: Try to reset (which should not affect the count)
    no_reset_clicker = NoResetClicker()
    assert no_reset_clicker.read() == 0, "NoResetClicker should start with count 0"
    no_reset_clicker.click()
    assert no_reset_clicker.read() == 1, "After one click, count should be 1"
    no_reset_clicker.reset()
    assert no_reset_clicker.read() == 1, "Reset shouldn't affect count in NoResetClicker"
