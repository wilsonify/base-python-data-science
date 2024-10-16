import csv
import json
import re
from collections import Counter
from os.path import dirname, abspath
from time import sleep

import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse

path_to_here = abspath(dirname(__file__))
path_to_data = abspath(f"{path_to_here}/../../../data")

github_endpoint = "https://api.github.com/users/joelgrus/repos"

serialized_example = """{
"title" : "Data Science Book",
"author" : "Joel Grus",
"publicationYear" : 2014,
"topics" : [ "data", "science", "data science"] }
"""


def is_video(td):
    """it's a video if it has exactly one pricelabel, and if
    the stripped text inside that pricelabel starts with 'Video'"""
    pricelabels = td("span", "pricelabel")
    return len(pricelabels) == 1 and pricelabels[0].text.strip().startswith("Video")


def book_info(td):
    """given a BeautifulSoup <td> Tag representing a book,
    extract the book's details and return a dict"""

    title = td.find("div", "thumbheader").a.text
    by_author = td.find("div", "AuthorName").text
    authors = [x.strip() for x in re.sub("^By ", "", by_author).split(",")]
    isbn_link = td.find("div", "thumbheader").a.get("href")
    isbn = re.match("/product/(.*)\.do", isbn_link).groups()[0]
    date = td.find("span", "directorydate").text.strip()

    return {"title": title, "authors": authors, "isbn": isbn, "date": date}


def scrape(num_pages=31):
    # BOOKS ABOUT DATA
    base_url = "http://shop.oreilly.com/category/browse-subjects/data.do?sortby=publicationDate&page="
    books = []
    for page_num in range(1, num_pages + 1):
        print("souping page", page_num)
        url = base_url + str(page_num)
        soup = BeautifulSoup(requests.get(url).text, "html5lib")

        for td in soup("td", "thumbtext"):
            if not is_video(td):
                books.append(book_info(td))

        # now be a good citizen and respect the robots.txt!
        sleep(30)

    return books


def get_year(book):
    """book["date"] looks like 'November 2014' so we need to
    split on the space and then take the second piece"""
    return int(book["date"].split()[1])


def plot_years(plt, books):
    # 2014 is the last complete year of data (when I ran this)
    year_counts = Counter(get_year(book) for book in books if get_year(book) <= 2014)

    years = sorted(year_counts)
    book_counts = [year_counts[year] for year in years]
    plt.bar([x - 0.5 for x in years], book_counts)
    plt.xlabel("year")
    plt.ylabel("# of data books")
    plt.title("Data is Big!")
    plt.show()


def main_tab_delimited():
    print("tab delimited stock prices:")
    with open(f"{path_to_data}/tab_delimited_stock_prices.txt", "r", encoding="utf8", newline="") as f:
        reader = csv.reader(f, delimiter="\t")
        # reader = csv.reader(codecs.iterdecode(f, 'utf-8'), delimiter='\t')
        for row in reader:
            date = row[0]
            symbol = row[1]
            closing_price = float(row[2])
            print(date, symbol, closing_price)


def main_colon_delimited():
    print("colon delimited stock prices:")
    with open(f"{path_to_data}/colon_delimited_stock_prices.txt", "r", encoding="utf8", newline="") as f:
        reader = csv.DictReader(f, delimiter=":")
        # reader = csv.DictReader(codecs.iterdecode(f, 'utf-8'), delimiter=':')
        for row in reader:
            date = row["date"]
            symbol = row["symbol"]
            closing_price = float(row["closing_price"])
            print(date, symbol, closing_price)


def write_comma_delimited():
    print("writing out comma_delimited_stock_prices.txt")
    today_prices = {"AAPL": 90.91, "MSFT": 41.68, "FB": 64.5}
    with open(f"{path_to_data}/comma_delimited_stock_prices.txt", "w", encoding="utf8", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        for stock, price in today_prices.items():
            writer.writerow([stock, price])


def example_soup():
    print("BeautifulSoup")
    html = requests.get("http://www.example.com").text
    soup = BeautifulSoup(html)
    print(soup)


def parse_serialized_example():
    print("parse the JSON to create a Python object")
    deserialized = json.loads(serialized_example)
    if "data science" in deserialized["topics"]:
        print(deserialized)


def main():
    print("GitHub API")
    repos = json.loads(requests.get(github_endpoint).text)
    dates = [parse(repo["created_at"]) for repo in repos]
    print("dates", dates)

    month_counts = Counter(date.month for date in dates)
    print("month_counts", month_counts)

    weekday_counts = Counter(date.weekday() for date in dates)
    print("weekday_count", weekday_counts)

    last_5_repositories = sorted(repos, key=lambda r: r["created_at"], reverse=True)[:5]

    print("last five languages", [repo["language"] for repo in last_5_repositories])


if __name__ == "__main__":
    main()
