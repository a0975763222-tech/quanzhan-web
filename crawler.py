import requests
from bs4 import BeautifulSoup
import json
import time
import random
from datetime import datetime

class PriceCrawler:
    def __init__(self):
        self.results = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'
        }

    def fetch_landtop_prices(self):
        """抓取地標網通報價 (範例邏輯)"""
        url = "https://www.landtop.com.tw/product_categories/phones" # 實際路徑依官網為準
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # 假設資料結構在表格或特定 div 中
                items = soup.select('.product-item') 
                for item in items:
                    data = {
                        "brand": item.select_one('.brand').text.strip(),
                        "model": item.select_one('.name').text.strip(),
                        "specs": item.select_one('.spec').text.strip(),
                        "msrp": item.select_one('.original-price').text.replace('$', '').strip(),
                        "market_price": item.select_one('.sale-price').text.replace('$', '').strip(),
                        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    self.results.append(data)
            print(f"[{datetime.now()}] 地標網通抓取完成")
        except Exception as e:
            print(f"抓取失敗: {e}")

    def export_json(self, filename="prices.json"):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, ensure_ascii=False, indent=4)
        print(f"資料已儲存至 {filename}")

if __name__ == "__main__":
    crawler = PriceCrawler()
    # 執行抓取
    crawler.fetch_landtop_prices()
    # 隨機延遲 3-7 秒防止被鎖 IP
    time.sleep(random.uniform(3, 7))
    # 輸出結果
    crawler.export_json()