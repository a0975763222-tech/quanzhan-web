import json, os, gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

def run_crawler():
    # 1. 取得 Google 鑰匙
    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds_json = json.loads(os.environ['GOOGLE_CREDENTIALS'])
    creds = Credentials.from_service_account_info(creds_json, scopes=scopes)
    client = gspread.authorize(creds)

    # 2. 開啟表格
    spreadsheet_id = "1gyMPDvsarOcT-yQj6_2M4_d7YdPnWnMSAmmBtm73IIk" 
    sheet = client.open_by_key(spreadsheet_id).sheet1
    all_data = sheet.get_all_records()

    # 3. 轉換為網頁需要的格式
    products = []
    for row in all_data:
        if str(row.get("顯示狀態")).strip() == "顯示":
            color_list = []
            hex_str = str(row.get("官方色碼 (Hex)", ""))
            if hex_str:
                for h in hex_str.split(','):
                    color_list.append({"hex": h.strip(), "name": ""})
            
            products.append({
                "brand": row.get("品牌與型號", ""),
                "model": row.get("品牌與型號", ""),
                "specs": row.get("加購備註 (預留 3)", ""),
                "msrp": str(row.get("官方售價", "0")),
                "price": str(row.get("銓展最終價") or row.get("行情基準", "0")),
                "colors": color_list,
                "img": row.get("圖片手動校正 (預留1)") or "https://via.placeholder.com/300?text=銓展通訊"
            })

    # 4. 存檔到 prices.json (修正 ensure_ascii)
    output = {
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "products": products
    }
    with open("prices.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    run_crawler()
