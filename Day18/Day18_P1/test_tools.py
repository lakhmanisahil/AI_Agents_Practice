"""
Manual test for tools.py.

Run from this folder:
    python test_tools.py
"""

import sys

from tools import ToolError, read_webpage, search_web


QUERY = "robotics engineer roadmap"


def test_search():
    print(f"\nSEARCH RESULTS for: {QUERY!r}\n")

    results = search_web(QUERY, max_results=3)

    # Fail loudly instead of printing an empty list silently.
    if not results:
        raise ToolError("Search returned 0 results.")

    for number, result in enumerate(results, start=1):
        print(f"{number}. {result['title']}")
        print(f"   {result['url']}")
        print(f"   {result['snippet']}")
        print()

    return results


def test_read_webpage(results):
    # Try each result until one page can be read.
    # Some sites block scripts (403), so one failure is normal.
    for result in results:
        url = result["url"]

        try:
            text = read_webpage(url)
        except ToolError as error:
            print(f"Skipping: {error}")
            continue

        print(f"\nWEBPAGE TEXT from {url}\n")
        print(text[:2000])
        return

    raise ToolError("Could not read any of the result pages.")


def main():
    try:
        results = test_search()
        test_read_webpage(results)
    except ToolError as error:
        print(f"\nFAILED: {error}")
        sys.exit(1)

    print("\nALL CHECKS PASSED")


if __name__ == "__main__":
    main()
