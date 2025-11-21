"""Shared constants used across modules to avoid duplicated string literals.

Placing these constants in a single module reduces duplicated literal occurrences
and makes it easier to update canonical module paths in one place.
"""

# Working-with-data module base
WORKING_DATA_MODULE = 'dsl.c10_working_with_data'

# Common working-data suffixes used multiple times in the codebase
E1004 = '.e1004_named_tuples'
E1006 = '.e1006_cleaning'
E1007 = '.e1007_manipulation'
E1008 = '.e1008_rescaling'
E1009 = '.e1009_dimensionality_reduction'

# Fully qualified working-data module constants
WORKING_E1004 = WORKING_DATA_MODULE + E1004
WORKING_E1006 = WORKING_DATA_MODULE + E1006
WORKING_E1007 = WORKING_DATA_MODULE + E1007
WORKING_E1008 = WORKING_DATA_MODULE + E1008
WORKING_E1009 = WORKING_DATA_MODULE + E1009
