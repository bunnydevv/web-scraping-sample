"""
Base Scraper Class
Provides common functionality for all scrapers
"""

import time
import yaml
import requests
from bs4 import BeautifulSoup
from utils.logger import setup_logger
from utils.file_handler import save_to_csv, save_to_json

class BaseScraper:
    """Base class for all web scrapers"""
    
    def __init__(self, url):
        """
        Initialize the scraper
        
        Args:
            url (str): The URL to scrape
        """
        self.url = url
        self.logger = setup_logger()
        self.config = self._load_config()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': self.config['scraping']['user_agent']
        })
    
    def _load_config(self):
        """Load configuration from YAML file"""
        try:
            with open('config.yaml', 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            self.logger.warning("config.yaml not found, using defaults")
            return {
                'scraping': {
                    'delay': 1,
                    'timeout': 10,
                    'user_agent': 'WebScraper/1.0',
                    'max_retries': 3
                },
                'output': {
                    'format': 'both',
                    'directory': 'data'
                }
            }
    
    def fetch_page(self, url=None):
        """Fetch a web page"""
        
        Args:
            url (str): URL to fetch (defaults to self.url)
            
        Returns:
            BeautifulSoup: Parsed HTML content
        """
        if url is None:
            url = self.url
        
        try:
            self.logger.info(f"Fetching: {url}")
            response = self.session.get(
                url,
                timeout=self.config['scraping']['timeout']
            )
            response.raise_for_status()
            
            # Be respectful - add delay
            time.sleep(self.config['scraping']['delay'])
            
            soup = BeautifulSoup(response.content, 'lxml')
            return soup
            
        except requests.RequestException as e:
            self.logger.error(f"Error fetching {url}: {e}")
            return None
    
    def parse(self, soup):
        """Parse the HTML content (to be overridden by subclasses)"""
        
        Args:
            soup (BeautifulSoup): Parsed HTML content
            
        Returns:
            list: Extracted data
        """
        raise NotImplementedError("Subclasses must implement parse()")
    
    def scrape(self):
        """Main scraping method"""
        
        Returns:
            list: Scraped data
        """
        soup = self.fetch_page()
        if soup:
            return self.parse(soup)
        return []
    
    def save_data(self, data, filename_prefix):
        """Save scraped data to file(s)"""
        
        Args:
            data (list): Data to save
            filename_prefix (str): Prefix for output filename
        """
        output_format = self.config['output']['format']
        output_dir = self.config['output']['directory']
        
        if output_format in ['csv', 'both']:
            save_to_csv(data, filename_prefix, output_dir)
        
        if output_format in ['json', 'both']:
            save_to_json(data, filename_prefix, output_dir)
