"""
Web tools for an AI agent: search the web and read a webpage.

Install dependencies (inside your venv):
    python -m pip install ddgs requests beautifulsoup4
"""

import requests
from bs4 import BeautifulSoup
from ddgs import DDGS


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}

MAX_PAGE_CHARS = 12000


class ToolError(Exception):
    """Raised when a tool cannot do its job, with a readable reason."""


def search_web(query, max_results=5):
    """
    Search the web using DuckDuckGo (via the ddgs library).

    Args:
        query: Search query.
        max_results: Maximum number of results.

    Returns:
        A list of dicts: {"title", "url", "snippet"}.

    Raises:
        ToolError: If the search fails.
    """

    if not query or not query.strip():
        raise ToolError("Search query is empty.")

    try:
        raw_results = DDGS().text(query, max_results=max_results)
    except Exception as error:
        raise ToolError(f"Search failed: {error}") from error

    results = []

    for item in raw_results or []:
        url = item.get("href", "")

        if not url:
            continue

        results.append({
            "title": item.get("title", ""),
            "url": url,
            "snippet": item.get("body", ""),
        })

    return results


def read_webpage(url):
    """
    Download a webpage and extract its readable text.

    Args:
        url: Webpage URL.

    Returns:
        Extracted webpage text (at most MAX_PAGE_CHARS characters).

    Raises:
        ToolError: If the page cannot be downloaded or has no text.
    """

    if url.startswith("//"):
        url = "https:" + url

    if not url.startswith(("http://", "https://")):
        raise ToolError(f"Not a valid web URL: {url!r}")

    try:
        response = requests.get(url, headers=HEADERS, timeout=20)
        response.raise_for_status()
    except requests.RequestException as error:
        raise ToolError(f"Could not download {url}: {error}") from error

    soup = BeautifulSoup(response.text, "html.parser")

    for element in soup(["script", "style", "noscript"]):
        element.decompose()

    text = soup.get_text("\n", strip=True)

    if not text:
        raise ToolError(f"No readable text found at {url}")

    return text[:MAX_PAGE_CHARS]
