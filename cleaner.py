import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    text_cols = [
        "Country Name",
        "Country Code",
        "Indicator Name",
        "Indicator Code",
        "Continent"
    ]

    gdp_cols = df.columns.difference(text_cols)

    df = df.drop_duplicates()

    df[text_cols] = df[text_cols].astype("string").fillna("")

    bad_text_rows = df[text_cols].apply(
        lambda c: c.str.contains(r"\d")
    ).any(axis=1)

    if bad_text_rows.any():
        print(" Text column error rows:", df.index[bad_text_rows].tolist())

    df = df[~bad_text_rows]

    bad_gdp_rows = df[gdp_cols].astype(str).apply(
        lambda c: c.str.contains(r"[A-Za-z]")
    ).any(axis=1)

    if bad_gdp_rows.any():
        print(" GDP alphabet error rows:", df.index[bad_gdp_rows].tolist())

    df[gdp_cols] = (
        df[gdp_cols]
        .apply(pd.to_numeric, errors="coerce")
        .fillna(0.0)
        .astype(float)
    )

    empty_gdp_rows = (df[gdp_cols] == 0).all(axis=1)

    if empty_gdp_rows.any():
        print(" Empty GDP rows:", df.index[empty_gdp_rows].tolist())

    df = df[~empty_gdp_rows]

    valid_continents = {
        "Asia", "Europe", "Africa",
        "North America", "South America",
        "Oceania", "Global"
    }

    bad_continent_rows = ~df["Continent"].isin(valid_continents)

    if bad_continent_rows.any():
        print(" Invalid continent rows:", df.index[bad_continent_rows].tolist())

    df = df[~bad_continent_rows]

    return df.reset_index(drop=True)
