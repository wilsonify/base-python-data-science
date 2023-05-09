import glob
import re


def source_to_header(source_str):
    regex = r"{(.*?)}"
    subst = r";"
    result = re.sub(
        pattern=regex,
        repl=subst,
        string=source_str,
        count=0,
        flags=re.DOTALL
    )
    return result


def main():
    for f in glob.glob("*.h"):
        test_str = open(f, "r").read()
        test_result_str = source_to_header(test_str)
        with open(f, 'w') as output:
            output.writelines(test_result_str)


if __name__ == "__main__":
    main()
