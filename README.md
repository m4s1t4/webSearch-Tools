# WebSearch - Advanced Web Search and Content Extraction Tool

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Firecrawl](https://img.shields.io/badge/firecrawl-latest-green)
![uv](https://img.shields.io/badge/uv-latest-purple)

A powerful web search and content extraction tool built with Python, leveraging the Firecrawl API for advanced web scraping, searching, and content analysis capabilities.

## 🚀 Features

- **Advanced Web Search**: Perform intelligent web searches with customizable parameters
- **Content Extraction**: Extract specific information from web pages using natural language prompts
- **Web Crawling**: Crawl websites with configurable depth and limits
- **Web Scraping**: Scrape web pages with support for various output formats
- **MCP Integration**: Built as a Model Context Protocol (MCP) server for seamless integration

## 📋 Prerequisites

- Python 3.8 or higher
- uv package manager
- Firecrawl API key
- OpenAI API key (optional, for enhanced features)
- Tavily API key (optional, for additional search capabilities)

## 🛠️ Installation

1. Install uv:

```bash
# On Windows (using pip)
pip install uv

# On Unix/MacOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add uv to PATH (Unix/MacOS)
export PATH="$HOME/.local/bin:$PATH"

# Add uv to PATH (Windows - add to Environment Variables)
# Add: %USERPROFILE%\.local\bin
```

2. Clone the repository:

```bash
git clone https://github.com/yourusername/websearch.git
cd websearch
```

3. Create and activate a virtual environment with uv:

```bash
# Create virtual environment
uv venv

# Activate on Windows
.\.venv\Scripts\activate.ps1

# Activate on Unix/MacOS
source .venv/bin/activate
```

4. Install dependencies with uv:

```bash
# Install from requirements.txt
uv sync
```

5. Set up environment variables:

```bash
# Create .env file
touch .env

# Add your API keys
FIRECRAWL_API_KEY=your_firecrawl_api_key
OPENAI_API_KEY=your_openai_api_key
```

## 🎯 Usage

### Starting the Server

Run the MCP server:

```bash
python main.py
```

### Available Tools

1. **Search**

```python
# Perform a web search
await search(query="your search query")
```

2. **Extract Information**

```python
# Extract specific information from URLs
await extract(
    urls=["https://example.com"],
    prompt="Extract main topics",
    enableWebSearch=True,
    showSources=True
)
```

3. **Crawl Websites**

```python
# Crawl a website with specific parameters
await crawl(
    url="https://example.com",
    maxDepth=2,
    limit=10
)
```

4. **Scrape Content**

```python
# Scrape content from a URL
await scrape(url="https://example.com")
```

## 📚 API Reference

### Search

- `query` (str): The search query
- Returns: Search results in JSON format

### Extract

- `urls` (List[str]): List of URLs to extract information from
- `prompt` (str): Instructions for extraction
- `enableWebSearch` (bool): Enable supplementary web search
- `showSources` (bool): Include source references
- Returns: Extracted information in specified format

### Crawl

- `url` (str): Starting URL
- `maxDepth` (int): Maximum crawl depth
- `limit` (int): Maximum pages to crawl
- Returns: Crawled content in markdown/HTML format

### Scrape

- `url` (str): Target URL
- Returns: Scraped content with optional screenshots

## 🔧 Configuration

### Environment Variables

The tool requires certain API keys to function. We provide a `.env.example` file that you can use as a template:

1. Copy the example file:

```bash
# On Unix/MacOS
cp .env.example .env

# On Windows
copy .env.example .env
```

2. Edit the `.env` file with your API keys:

```env
# OpenAI API key - Required for AI-powered features
OPENAI_API_KEY=your_openai_api_key_here

# Firecrawl API key - Required for web scraping and searching
FIRECRAWL_API_KEY=your_firecrawl_api_key_here
```

### Getting the API Keys

1. **OpenAI API Key**:

   - Visit [OpenAI's platform](https://platform.openai.com/)
   - Sign up or log in
   - Navigate to API keys section
   - Create a new secret key

2. **Firecrawl API Key**:
   - Visit [Firecrawl's website](https://docs.firecrawl.dev/)
   - Create an account
   - Navigate to your dashboard
   - Generate a new API key

### Verifying Configuration

To verify your configuration is working:

```bash
# Start the server
python main.py

# Try a simple search query
curl -X POST http://localhost:3000/search -d '{"query": "test query"}'
```

If everything is configured correctly, you should receive a JSON response with search results.

### Troubleshooting

If you encounter errors:

1. Ensure all required API keys are set in your `.env` file
2. Verify the API keys are valid and have not expired
3. Check that the `.env` file is in the root directory of the project
4. Make sure the environment variables are being loaded correctly

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Firecrawl](https://docs.firecrawl.dev/) for their powerful web scraping API
- [OpenAI](https://openai.com/) for AI capabilities
- [Tavily](https://tavily.com/) for search functionality
- The MCP community for the protocol specification

## 📬 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter) - email@example.com

Project Link: [https://github.com/yourusername/websearch](https://github.com/yourusername/websearch)

---

Made with ❤️ using Python and Firecrawl
