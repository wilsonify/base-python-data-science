def conditional_message(x):
    """Returns a message based on conditional checks."""
    if 1 > 2:
        return "if only 1 were greater than two..."
    elif 1 > 3:
        return "elif stands for 'else if'"
    else:
        return "when all else fails use else (if you want to)"

def get_parity(x):
    """Returns 'even' if x is even, otherwise 'odd'."""
    return "even" if x % 2 == 0 else "odd"

def count_to_ten():
    """Returns a list of strings where each number less than 10 is printed."""
    result = []
    x = 0
    while x < 10:
        result.append(f"{x} is less than 10")
        x += 1
    return result

def loop_with_continue_and_break():
    """Returns a list of numbers from 0 to 9, excluding 3 and stopping before 5."""
    result = []
    for x in range(10):
        if x == 3:
            continue
        if x == 5:
            break
        result.append(x)
    return result
