import pandas as pd


def add_growth_metrics(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values("date").copy()
    df["daily_change"] = df["close"].diff()
    df["daily_pct_change"] = df["close"].pct_change() * 100
    return df