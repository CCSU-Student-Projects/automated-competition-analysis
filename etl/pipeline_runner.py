from etl.init_db import init_db
from etl.load_stock import load_stock


def run_pipeline():
    init_db()
    load_stock("MSFT")


if __name__ == "__main__":
    run_pipeline()