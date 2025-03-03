import os
from typing import List
from dataclasses import dataclass
from tools.webtools import WebTools
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("webtools")

# CONSTANTS
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY ")
webtools = WebTools()


@dataclass
class QueryResponse:
    response_text: str
    sources: List[str]


@mcp.tool()
async def search(query: str) -> str:
    """Performs web searches and retrieves up-to-date information from the internet.
    Args:
    - prompt: Specific query or topic to search for on the internet
    - limit: Maximum number of results to return (between 1 and 20)

    Returns:
    - Search results with relevant information about the requested topic
    """
    try:
        search = webtools.search(query)
        return search
    except Exception as e:
        return f"Error performing search: {str(e)}"


@mcp.tool()
async def crawl(url: str, maxDepth: int, limit: int) -> str:
    """Crawls a website starting from the specified URL and extracts content from multiple pages.
    Args:
    - url: The complete URL of the web page to start crawling from
    - maxDepth: The maximum depth level for crawling linked pages
    - limit: The maximum number of pages to crawl

    Returns:
    - Content extracted from the crawled pages in markdown and HTML format
    """
    try:
        crawl_results = webtools.crawl(url, maxDepth, limit)
        return crawl_results
    except Exception as e:
        return f"Error crawling pages: {str(e)}"


@mcp.tool()
async def extract(
    url: list[str], prompt: str, enabaleWebSearch: bool, showSources: bool
) -> str:
    """Extracts specific information from a web page based on a prompt.
    Args:
    - url: The complete URL of the web page to extract information from
    - prompt: Instructions specifying what information to extract from the page
    - enabaleWebSearch: Whether to allow web searches to supplement the extraction
    - showSources: Whether to include source references in the response

    Returns:
    - Extracted information from the web page based on the prompt
    """
    try:
        info_extracted = webtools.extract_info(
            url, enabaleWebSearch, prompt, showSources
        )
        return info_extracted
    except Exception as e:
        return f"Error extracting information: {str(e)}"


@mcp.tool()
async def scrape(url: str) -> str:
    try:
        url_scraped = webtools.scrape_urls(url)
        return url_scraped
    except Exception as e:
        return f"Error scraping url {url}: {str(e)}"


if __name__ == "__main__":
    # Initialize and run server
    mcp.run(transport="stdio")
