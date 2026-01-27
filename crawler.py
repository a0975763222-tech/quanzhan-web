import requests
import json
from datetime import datetime

def crawl_prices():
    # Target: Landtop (Sample)
    results = []
    
    # Static Data for Testing
    mock_data = [
        {"brand": "Apple", "model": "iPhone 15 Pro", "specs": "256G", "msrp": "40400", "price": "36500"},
        {"brand": "Samsung", "model": "S24 Ultra", "specs": "512G", "msrp": "47900", "price": "41200"}
    ]
    
    for item in mock_data:
        item["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        results.append(item)

    with open("prices.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    print("Success: prices.json updated")

if __name__ == "__main__":
    crawl_prices()
