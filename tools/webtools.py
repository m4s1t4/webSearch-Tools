import json
from typing import List
from openai import OpenAI
from dotenv import load_dotenv
from tavily import TavilyClient
from dataclasses import dataclass
from firecrawl import FirecrawlApp

# Upload the api keys
load_dotenv()


@dataclass
class QueryResponse:
    response_text: str
    sources: List[str]


# Tool Schema:
tools = [
    {
        "type": "function",
        "function": {
            "name": "tavily_search",
            "description": "Perform a web search using Tavily API to get up-to-date information or additional context. Use this when you need current information or feel a search could provide a better answer.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The search query"},
                    "max_results": {
                        "type": "integer",
                        "description": "The maximun number of search results to return. It must be between 0 and 20",
                    },
                },
                "required": ["query", "max_results"],
            },
        },
    },
]


class WebTools:
    def __init__(self) -> None:
        self.client = OpenAI()
        self.tavily_client = TavilyClient()
        self.firecrawl = FirecrawlApp()
        self.model = "o3-mini"
        self.temperature = 0
        self.reasoning_effort = "high"
        self.messages = []
        self.current_conversation = []
        self.conversations_history = []
        self.tools = tools
        self.tool_choice = "required"

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
