import requests
from bs4 import BeautifulSoup
import json
import time
import random
from datetime import datetime

class QuanzhanCrawler:
    def __init__(self):
        self.results = []
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Referer': 'https://www.google.com/'
        }

    def fetch_landtop(self):
        """抓取地標網通報價"""
        url = "https://www.landtop.com.tw/product_categories/phones"
        try:
            response = requests.get(url, headers=self.headers, timeout=15)
            response.encoding = 'utf-8'
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # 2026 網頁結構：選取產品卡片 (請依實際結構微調)
                items = soup.select('.product-card') 
                for item in items:
                    name_full = item.select_one('.product-name').text.strip()
                    # 簡易邏輯：將名稱拆分，例如 "Apple iPhone 15 Pro 256G"
                    parts = name_full.split(' ')
                    data = {
                        "source": "地標網通",
                        "brand": parts[0] if len(parts) > 0 else "其他",
                        "model": parts[1] if len(parts) > 1 else name_full,
                        "specs": parts[-1] if len(parts) > 2 else "標準規格",
                        "msrp": item.select_one('.price-original').text.replace('$', '').replace(',', '').strip(),
                        "price": item.select_one('.price-sale').text.replace('$', '').replace(',', '').strip(),
                        "updated_at": self.timestamp
                    }
                    self.results.append(data)
                return True
        except Exception as e:
            print(f"地標抓取失敗: {e}")
            return False

    def fetch_sogi(self):
        """抓取手機王熱門報價 (熱門排行榜)"""
        url = "https://www.sogi.com.tw/prices"
        try:
            response = requests.get(url, headers=self.headers, timeout=15)
            response.encoding = 'utf-8'
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # 抓取排行榜區域
                items = soup.select('.price-item')
                for item in items:
                    data = {
                        "source": "手機王",
                        "brand": item.get('data-brand', '未知'),
                        "model": item.select_one('.name').text.strip(),
                        "specs": "依官網為準",
                        "msrp": "參考手機王",
                        "price": item.select_one('.price').text.replace('$', '').replace(',', '').strip(),
                        "updated_at": self.timestamp
                    }
                    self.results.append(data)
                return True
        except Exception as e:
            print(f"手機王抓取失敗: {e}")
            return False

    def save_data(self):
        # 如果 list 是空的，寫入備用訊息防止網頁壞掉
        if not self.results:
            self.results = [{
                "brand": "系統通知",
                "model": "報價更新失敗",
                "specs": "請聯繫後台",
                "msrp": "-",
                "price": "請洽門市",
                "updated_at": self.timestamp,
                "note": "目前目標網站結構變更或連線逾時"
            }]
        
        with open("prices.json", "w", encoding="utf-8") as f:
            json.dump(self.results, f, ensure_ascii=False, indent=4)
        print(f"✅ 已成功儲存 {len(self.results)} 筆資料至 prices.json")

if __name__ == "__main__":
    crawler = QuanzhanCrawler()
    
    # 執行抓取任務
    success_landtop = crawler.fetch_landtop()
    time.sleep(random.uniform(3, 7)) # 避免過快請求被封 IP
    success_sogi = crawler.fetch_sogi()
    
    # 儲存結果
    crawler.save_data()
