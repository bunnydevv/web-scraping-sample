"""
File Handler
Functions to save scraped data to various formats
"""

import csv
import json
import os
from datetime import datetime
from utils.logger import setup_logger

logger = setup_logger()

def save_to_csv(data, filename_prefix, output_dir='data'):
    """Save data to CSV file"""
    
    Args:
        data (list): List of dictionaries to save
        filename_prefix (str): Prefix for the filename
        output_dir (str): Output directory
    """
    if not data:
        logger.warning("No data to save to CSV")
        return
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = os.path.join(output_dir, f"{filename_prefix}_{timestamp}.csv")
    
    try:
        # Get all unique keys from all dictionaries
        fieldnames = set()
        for item in data:
            fieldnames.update(item.keys())
        fieldnames = sorted(list(fieldnames))
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for item in data:
                # Convert lists to strings for CSV
                row = {}
                for key, value in item.items():
                    if isinstance(value, list):
                        row[key] = ', '.join(str(v) for v in value)
                    else:
                        row[key] = value
                writer.writerow(row)
        
        logger.info(f"Data saved to CSV: {filename}")
        
    except Exception as e:
        logger.error(f"Error saving to CSV: {e}")

def save_to_json(data, filename_prefix, output_dir='data'):
    """Save data to JSON file"""
    
    Args:
        data (list): List of dictionaries to save
        filename_prefix (str): Prefix for the filename
        output_dir (str): Output directory
    """
    if not data:
        logger.warning("No data to save to JSON")
        return
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = os.path.join(output_dir, f"{filename_prefix}_{timestamp}.json")
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Data saved to JSON: {filename}")
        
    except Exception as e:
        logger.error(f"Error saving to JSON: {e}")
