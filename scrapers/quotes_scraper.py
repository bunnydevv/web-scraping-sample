"""
Quotes Scraper
Example scraper for quotes.toscrape.com
"""

from .base_scraper import BaseScraper

class QuotesScraper(BaseScraper):
    """Scraper for quotes from quotes.toscrape.com"""
    
    def __init__(self, url="http://quotes.toscrape.com/"): 
        """Initialize the quotes scraper"""
        super().__init__(url)
    
    def parse(self, soup):
        """Parse quotes from the page"""
        
        Args:
            soup (BeautifulSoup): Parsed HTML content
            
        Returns:
            list: List of dictionaries containing quote data
        """
        quotes_data = []
        
        # Find all quote containers
        quotes = soup.find_all('div', class_='quote')
        
        for quote in quotes:
            try:
                # Extract quote text
                text = quote.find('span', class_='text').get_text(strip=True)
                
                # Extract author
                author = quote.find('small', class_='author').get_text(strip=True)
                
                # Extract tags
                tags = [tag.get_text(strip=True) for tag in quote.find_all('a', class_='tag')]
                
                quotes_data.append({
                    'text': text,
                    'author': author,
                    'tags': tags
                })
                
            except AttributeError as e:
                self.logger.warning(f"Error parsing quote: {e}")
                continue
        
        return quotes_data
    
    def scrape_multiple_pages(self, max_pages=5):
        """Scrape multiple pages"""
        
        Args:
            max_pages (int): Maximum number of pages to scrape
            
        Returns:
            list: All scraped quotes
        """
        all_quotes = []
        page = 1
        
        while page <= max_pages:
            page_url = f"{self.url}page/{page}/"
            self.logger.info(f"Scraping page {page}...")
            
            soup = self.fetch_page(page_url)
            if not soup:
                break
            
            quotes = self.parse(soup)
            if not quotes:
                self.logger.info("No more quotes found")
                break
            
            all_quotes.extend(quotes)
            page += 1
        
        return all_quotes
