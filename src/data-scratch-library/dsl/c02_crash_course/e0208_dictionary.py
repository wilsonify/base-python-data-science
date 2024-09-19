from collections import defaultdict

# Dictionary operations
def create_grades():
    """Creates a dictionary of grades."""
    return {"Joel": 80, "Tim": 95}

def get_grade(grades, student, default_value=0):
    """Returns the grade of a student, or a default value if not found."""
    return grades.get(student, default_value)

def update_grades(grades, student, grade):
    """Updates or adds a grade for a student."""
    grades[student] = grade
    return grades

def check_student_in_grades(grades, student):
    """Checks if a student is in the grades dictionary."""
    return student in grades

# defaultdict examples
def count_words(document):
    """Counts the occurrences of each word in the document using defaultdict."""
    word_counts = defaultdict(int)
    for word in document:
        word_counts[word] += 1
    return word_counts

def create_default_dict_list():
    """Creates a defaultdict with list as the default factory."""
    dd_list = defaultdict(list)
    dd_list[2].append(1)
    return dd_list

def create_default_dict_dict():
    """Creates a defaultdict with dict as the default factory."""
    dd_dict = defaultdict(dict)
    dd_dict["Joel"]["City"] = "Seattle"
    return dd_dict

def create_default_dict_pair():
    """Creates a defaultdict with a lambda function returning a [0, 0] list."""
    dd_pair = defaultdict(lambda: [0, 0])
    dd_pair[2][1] = 1
    return dd_pair
