"""
Scrapers package
Contains base scraper and specific scraper implementations
"""

from .base_scraper import BaseScraper
from .quotes_scraper import QuotesScraper

__all__ = ['BaseScraper', 'QuotesScraper']
