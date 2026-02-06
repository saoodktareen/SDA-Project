import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()

    categorical_cols = [
        "Country Name",
        "Country Code",
        "Indicator Name",
        "Indicator Code",
        "Continent"
    ]

    numeric_cols = df.columns.difference(categorical_cols)

    df[categorical_cols] = df[categorical_cols].astype("string").fillna("")

    df[numeric_cols] = (
        df[numeric_cols]
        .apply(pd.to_numeric, errors="coerce")
        .fillna(0.0)
        .astype(float)
    )

    return df
