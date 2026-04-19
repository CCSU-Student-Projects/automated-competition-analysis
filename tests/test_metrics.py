import pandas as pd

from analysis.metrics import add_growth_metrics


def test_add_growth_metrics():
    df = pd.DataFrame({
        "date": pd.to_datetime(["2026-04-01", "2026-04-02", "2026-04-03"]),
        "close": [100, 110, 121]
    })

    result = add_growth_metrics(df)

    assert "daily_change" in result.columns
    assert "daily_pct_change" in result.columns
    assert round(result.iloc[1]["daily_pct_change"], 2) == 10.00