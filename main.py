#!/usr/bin/env python3
"""
Web Scraping Sample - Main Entry Point
Demonstrates web scraping with Python
"""

import os
from scrapers.quotes_scraper import QuotesScraper
from utils.logger import setup_logger

def main():
    """Main function to run the web scraper"""
    
    # Setup logger
    logger = setup_logger()
    
    logger.info("Starting Web Scraping Sample Project")
    logger.info("=" * 50)
    
    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    
    # Example 1: Scrape quotes from quotes.toscrape.com
    logger.info("Example 1: Scraping quotes...")
    quotes_url = "http://quotes.toscrape.com/"
    
    try:
        scraper = QuotesScraper(quotes_url)
        quotes = scraper.scrape()
        
        if quotes:
            logger.info(f"Successfully scraped {len(quotes)} quotes")
            scraper.save_data(quotes, "quotes")
            logger.info("Data saved successfully!")
            
            # Display first 3 quotes
            logger.info("\nFirst 3 quotes:")
            for i, quote in enumerate(quotes[:3], 1):
                logger.info(f"\n{i}. \"{quote['text']}\"")
                logger.info(f"   - {quote['author']}")
                logger.info(f"   Tags: {', '.join(quote['tags'])}")
        else:
            logger.warning("No quotes were scraped")
            
    except Exception as e:
        logger.error(f"Error during scraping: {e}")
    
    logger.info("\n" + "=" * 50)
    logger.info("Scraping completed!")

if __name__ == "__main__":
    main()
