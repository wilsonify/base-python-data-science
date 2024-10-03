# Test functions
from data_scrape_from_scratch.c09_getting_data.e0906_scaping import find_spans_inside_divs, parse_html, fetch_html, \
    find_important_paragraphs, find_all_paragraphs, find_paragraphs_with_ids, get_paragraph_id, \
    get_paragraph_text_and_words, get_first_paragraph


def test_fetch_html():
    url = ("https://raw.githubusercontent.com/"
           "joelgrus/data/master/getting-data.html")
    html = fetch_html(url)
    assert "html" in html  # Basic sanity check


def test_get_first_paragraph():
    url = ("https://raw.githubusercontent.com/"
           "joelgrus/data/master/getting-data.html")
    html = fetch_html(url)
    soup = parse_html(html)
    first_paragraph = get_first_paragraph(soup)
    assert first_paragraph.startswith("Once upon a time")


def test_get_paragraph_text_and_words():
    url = ("https://raw.githubusercontent.com/"
           "joelgrus/data/master/getting-data.html")
    html = fetch_html(url)
    soup = parse_html(html)
    paragraph_info = get_paragraph_text_and_words(soup)
    assert paragraph_info["text"].startswith("Once upon a time")
    assert "time" in paragraph_info["words"]


def test_get_paragraph_id():
    url = ("https://raw.githubusercontent.com/"
           "joelgrus/data/master/getting-data.html")
    html = fetch_html(url)
    soup = parse_html(html)
    paragraph_id = get_paragraph_id(soup)
    assert paragraph_id is None or isinstance(paragraph_id, str)


def test_find_all_paragraphs():
    url = ("https://raw.githubusercontent.com/"
           "joelgrus/data/master/getting-data.html")
    html = fetch_html(url)
    soup = parse_html(html)
    paragraphs = find_all_paragraphs(soup)
    assert len(paragraphs) > 0


def test_find_paragraphs_with_ids():
    url = ("https://raw.githubusercontent.com/"
           "joelgrus/data/master/getting-data.html")
    html = fetch_html(url)
    soup = parse_html(html)
    paragraphs_with_ids = find_paragraphs_with_ids(soup)
    assert isinstance(paragraphs_with_ids, list)


def test_find_important_paragraphs():
    url = ("https://raw.githubusercontent.com/"
           "joelgrus/data/master/getting-data.html")
    html = fetch_html(url)
    soup = parse_html(html)
    important_paragraphs = find_important_paragraphs(soup)
    assert isinstance(important_paragraphs, list)


def test_find_spans_inside_divs():
    url = ("https://raw.githubusercontent.com/"
           "joelgrus/data/master/getting-data.html")
    html = fetch_html(url)
    soup = parse_html(html)
    spans = find_spans_inside_divs(soup)
    assert isinstance(spans, list)
