# Web Scraping Sample Project

A professional Python web scraping project demonstrating best practices for extracting data from websites.

## Features

- 🔍 Scrape data from websites using BeautifulSoup and Requests
- 📊 Export data to CSV and JSON formats
- ⚙️ Configurable settings via YAML
- 🛡️ Rate limiting and respectful scraping
- 📝 Comprehensive logging
- 🧪 Example scraper for quotes

## Project Structure

```
web-scraping-sample/
├── scrapers/
│   ├── __init__.py
│   ├── base_scraper.py      # Base scraper class
│   └── quotes_scraper.py    # Example: scrape quotes
├── utils/
│   ├── __init__.py
│   ├── logger.py            # Logging configuration
│   └── file_handler.py      # Save data to files
├── data/                    # Output directory
├── config.yaml              # Configuration file
├── requirements.txt         # Python dependencies
├── main.py                  # Entry point
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/bunnydevv/web-scraping-sample.git
cd web-scraping-sample
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Run the example quotes scraper:
```bash
python main.py
```

### Configuration

Edit `config.yaml` to customize scraping behavior:
```yaml
scraping:
  delay: 1  # Delay between requests (seconds)
  timeout: 10  # Request timeout
  user_agent: "Mozilla/5.0 (compatible; WebScraper/1.0)"

output:
  format: "both"  # csv, json, or both
  directory: "data"
```

### Creating Custom Scrapers

Extend the `BaseScraper` class to create your own scrapers:

```python
from scrapers.base_scraper import BaseScraper

class MyCustomScraper(BaseScraper):
    def __init__(self, url):
        super().__init__(url)
    
    def parse(self, soup):
        # Your parsing logic here
        data = []
        # Extract data from soup
        return data
```

## Example Output

The scraper will create files in the `data/` directory:
- `quotes_YYYYMMDD_HHMMSS.csv`
- `quotes_YYYYMMDD_HHMMSS.json`

## Best Practices

✅ **Respect robots.txt**: Always check the website's robots.txt file  
✅ **Rate limiting**: Include delays between requests  
✅ **User-Agent**: Identify your scraper  
✅ **Error handling**: Handle network errors gracefully  
✅ **Legal compliance**: Only scrape publicly available data and respect terms of service  

## Legal Notice

This project is for educational purposes. When scraping websites:
- Review and comply with the website's Terms of Service
- Check the robots.txt file
- Don't overload servers with requests
- Respect copyright and data privacy laws

## Dependencies

- `requests`: HTTP library for making requests
- `beautifulsoup4`: HTML/XML parsing
- `lxml`: Fast XML and HTML parser
- `pyyaml`: YAML configuration file support

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use this project for learning and development.
