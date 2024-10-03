from bs4 import BeautifulSoup
import requests
from typing import List, Optional, Dict

def fetch_html(url: str) -> str:
    """Fetch HTML content from a URL."""
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_html(html: str) -> BeautifulSoup:
    """Parse the HTML content using BeautifulSoup."""
    return BeautifulSoup(html, 'html5lib')

def get_first_paragraph(soup: BeautifulSoup) -> str:
    """Return the text content of the first <p> tag."""
    first_paragraph = soup.find('p')
    return first_paragraph.text if first_paragraph else ""

def get_paragraph_text_and_words(soup: BeautifulSoup) -> Dict[str, List[str]]:
    """Return the text of the first <p> tag and a list of its words."""
    first_paragraph = soup.p
    if first_paragraph:
        paragraph_text = first_paragraph.text
        paragraph_words = first_paragraph.text.split()
        return {"text": paragraph_text, "words": paragraph_words}
    return {"text": "", "words": []}

def get_paragraph_id(soup: BeautifulSoup) -> Optional[str]:
    """Return the id of the first <p> tag, or None if no id exists."""
    return soup.p.get('id') if soup.p else None

def find_all_paragraphs(soup: BeautifulSoup) -> List[str]:
    """Return a list of all paragraphs' text content."""
    return [p.text for p in soup.find_all('p')]

def find_paragraphs_with_ids(soup: BeautifulSoup) -> List[str]:
    """Return a list of paragraphs' text content that have ids."""
    return [p.text for p in soup.find_all('p') if p.get('id')]

def find_important_paragraphs(soup: BeautifulSoup) -> List[str]:
    """Return a list of paragraphs with the class 'important'."""
    return [p.text for p in soup.find_all('p', {'class': 'important'})]

def find_spans_inside_divs(soup: BeautifulSoup) -> List[str]:
    """Return a list of text content from all <span> elements inside <div>s."""
    return [span.text for div in soup.find_all('div') for span in div.find_all('span')]




