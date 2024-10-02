from dsl.c09_getting_data.e0904_reading_files import (
    get_domain,
    count_email_domains,
    write_to_file,
    count_lines_starting_with_hash
)


def test_get_domain():
    assert get_domain('joelgrus@gmail.com') == 'gmail.com'
    assert get_domain('joel@m.datasciencester.com') == 'm.datasciencester.com'


def test_count_lines_starting_with_hash():
    # Create a temporary file for testing
    write_to_file('test_file.txt', "# First line\nSecond line\n# Third line")
    assert count_lines_starting_with_hash('test_file.txt') == 2


def test_count_email_domains():
    # Create a temporary file with email addresses for testing
    write_to_file('email_addresses.txt', "joelgrus@gmail.com\njoel@m.datasciencester.com")
    domain_counts = count_email_domains('email_addresses.txt')
    assert domain_counts['gmail.com'] == 1
    assert domain_counts['m.datasciencester.com'] == 1
