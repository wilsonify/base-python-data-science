# Chapter 9 – Getting Data (Library)

Utilities for reading, writing, and parsing files in various formats.

---

## Module Contents

### Scripts

| Script | Description |
|---|---|
| `e0901_stdin_stdout_egrep.py` | Filter stdin lines matching a regex (egrep clone) |
| `e0902_line_count.py` | Count lines from stdin |
| `e0903_most_common_words.py` | Print the *n* most common words from stdin |
| `e0904_reading_files.py` | File I/O helpers: read, write, append, count lines, parse emails |
| `e0905_delimited_files.py` | Read/write tab-, colon-, and comma-delimited files |

### Key Functions (`e0904_reading_files`)

| Function | Description |
|---|---|
| `get_file_path` | Resolve a filename to an absolute path in the `data/` directory |
| `write_to_file` | Write a string to a file |
| `append_to_file` | Append a string to a file |
| `read_file` | Read all lines from a file |
| `count_lines_starting_with_hash` | Count lines that begin with `#` |
| `get_domain` | Extract the domain from an email address |
| `count_email_domains` | Tally domains in an email-address file |

### Key Functions (`e0905_delimited_files`)

| Function | Description |
|---|---|
| `read_tab_delimited_file` | Parse a tab-separated file into a list of rows |
| `read_colon_delimited_file` | Parse a colon-separated file into a list of dicts |
| `write_comma_delimited_file` | Write a dict as a CSV file |
| `write_bad_csv_file` | Write a list of lists as CSV (demonstrates quoting issues) |

---

## Further Reading

- [csv module – Python docs](https://docs.python.org/3/library/csv.html)
- *Data Science from Scratch*, Chapter 9
