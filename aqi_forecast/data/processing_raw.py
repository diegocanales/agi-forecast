import pandas as pd


def process_historical_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns={" pm10": "pm10", " pm25": "pm25", " no2": "no2", " co": "co"})
    df["date"] = pd.to_datetime(df["date"], format="%Y/%m/%d")
    df["pm25"] = pd.to_numeric(df["pm25"], errors="coerce")
    df["pm10"] = pd.to_numeric(df["pm10"], errors="coerce")
    df["no2"] = pd.to_numeric(df["no2"], errors="coerce")
    df["co"] = pd.to_numeric(df["co"], errors="coerce")
    df.sort_values("date", inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df
