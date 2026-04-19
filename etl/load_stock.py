import sqlite3
from pathlib import Path

from scrapers.stock_scraper import fetch_stock_data

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "data" / "aca.db"


def load_stock(symbol="MSFT"):
    df = fetch_stock_data(symbol)

    conn = sqlite3.connect(DB_PATH)
    df.to_sql("stock_prices", conn, if_exists="replace", index=False)
    conn.close()


if __name__ == "__main__":
    load_stock()