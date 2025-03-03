from openai import OpenAI
from dotenv import load_dotenv
from tavily import TavilyClient
from firecrawl import FirecrawlApp

# Upload the api keys
load_dotenv()


class WebTools:
    def __init__(self) -> None:
        self.client = OpenAI()
        self.tavily_client = TavilyClient()
        self.firecrawl = FirecrawlApp()

    def search(self, query: str):
        try:
            response = self.firecrawl.search(query)
            return response
        except Exception as e:
            return f"Error performing search: {str(e)}"

    def crawl(self, url: str, maxDepth: int, limit: int):
        try:
            crawl_page = self.firecrawl.crawl_url(
                url,
                params={
                    "limit": limit,
                    "maxDepth": maxDepth,
                    "scrapeOptions": {"formats": ["markdown", "html"]},
                },
                poll_interval=30,
            )
            return crawl_page
        except Exception as e:
            return f"Error crawling pages: {str(e)}"

    def extract_info(
        self, url: list[str], enableWebSearch: bool, prompt: str, showSources: bool
    ):
        try:
            info_extracted = self.firecrawl.extract(
                url,
                {
                    "prompt": prompt,
                    "enableWebSearch": enableWebSearch,
                    "showSources": showSources,
                    "scrapeOptions": {
                        "formats": ["markdown"],
                        "blockAds": True,
                    },
                },
            )
            return info_extracted
        except Exception as e:
            return f"Error extracting information from page {url}: {str(e)}"

    def scrape_urls(self, url: list[str]):
        try:
            urls_scraped = self.firecrawl.scrape_url(
                url,
                params={
                    "formats": ["markdown", "html"],
                    "actions": [
                        {"type": "screenshot"},
                    ],
                },
            )
            return urls_scraped
        except Exception as e:
            return f"Error scrapping ulr {url}: {str(e)}"
