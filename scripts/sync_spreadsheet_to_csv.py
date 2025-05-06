import json
import os
import time
from pathlib import Path

import gspread
import pandas as pd  # type:ignore
from oauth2client.service_account import ServiceAccountCredentials  # type:ignore

# --- 設定 ---
SPREADSHEET_NAME = "zenn_ideas"
CSV_PATH = Path("mst_zenn_ideas.csv")

# --- Google Sheets認証設定 ---
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

if "GSPREAD_SERVICE_ACCOUNT" in os.environ:
    json_content = json.loads(os.environ["GSPREAD_SERVICE_ACCOUNT"])
else:
    # ローカルでのテスト用(gitignoreする)
    with open("secrets/GSPREAD_SERVICE_ACCOUNT.json", "r") as f:
        json_content = json.load(f)

credentials = ServiceAccountCredentials.from_json_keyfile_dict(json_content, scope)
gc = gspread.authorize(credentials)

# --- スプレシート読み込み ---
for i in range(3):
    try:
        worksheet = gc.open(SPREADSHEET_NAME).sheet1
        break
    except Exception as e:
        print(f"[WARN] Attempt {i+1} failed: {e}")
        time.sleep(10)
else:
    raise RuntimeError("Failed to open spreadsheet after 3 retries.")

records = worksheet.get_all_records()
spread_df = pd.DataFrame(records)

# --- CSVの読み込み（存在しない場合は空で初期化） ---
if CSV_PATH.exists():
    csv_df = pd.read_csv(CSV_PATH)
else:
    csv_df = pd.DataFrame(columns=spread_df.columns)

# --- 差分チェック（internal_keyが新しいものだけ） ---
spread_df["internal_key"] = spread_df["internal_key"].astype(str)
csv_df["internal_key"] = csv_df["internal_key"].astype(str)

new_rows = spread_df.loc[~spread_df["internal_key"].isin(csv_df["internal_key"])]

if not new_rows.empty:
    print(f"\n[INFO] {len(new_rows)} new rows found. Appending to CSV...\n")
    updated_df = pd.concat([csv_df, new_rows], ignore_index=True)
    updated_df.to_csv(CSV_PATH, index=False)
else:
    print("\n[INFO] No new rows to append. CSV is up to date.\n")
