import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Work on a copy to avoid changing the original DataFrame
    df = df.copy()

    # Columns that are expected to have text data only
    text_cols = [
        "Country Name",
        "Country Code",
        "Indicator Name",
        "Indicator Code",
        "Continent"
    ]

    # All other columns are considered numeric (GDP) columns
    gdp_cols = df.columns.difference(text_cols)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Ensure text columns are string type and replace NaN with empty string
    df[text_cols] = df[text_cols].astype("string").fillna("")

    # ---------------- TEXT VALIDATION (digits not allowed) ----------------
    bad_text_rows = df[text_cols].apply(
        lambda c: c.str.contains(r"\d")
    ).any(axis=1)

    if bad_text_rows.any():
        print("Text column error rows:", (df.index[bad_text_rows] + 2).tolist())

    df = df[~bad_text_rows]

    # ---------------- COUNTRY NAME EMPTY CHECK ----------------
    bad_country_rows = df["Country Name"].str.strip().eq("")

    if bad_country_rows.any():
        print("Empty Country Name rows:", (df.index[bad_country_rows] + 2).tolist())

    df = df[~bad_country_rows]

    # ---------------- GDP VALIDATION (letters not allowed) ----------------
    bad_gdp_rows = df[gdp_cols].astype(str).apply(
        lambda c: c.str.contains(r"[A-Za-z]")
    ).any(axis=1)

    if bad_gdp_rows.any():
        print("GDP alphabet error rows:", (df.index[bad_gdp_rows] + 2).tolist())

    # Convert GDP columns to numeric
    df[gdp_cols] = (
        df[gdp_cols]
        .apply(pd.to_numeric, errors="coerce")
        .fillna(0.0)
        .astype(float)
    )

    # ---------------- EMPTY GDP CHECK ----------------
    empty_gdp_rows = (df[gdp_cols] == 0).all(axis=1)

    if empty_gdp_rows.any():
        print("Empty GDP rows:", (df.index[empty_gdp_rows] + 2).tolist())

    df = df[~empty_gdp_rows]

    # ---------------- CONTINENT VALIDATION ----------------
    valid_continents = {
        "Asia", "Europe", "Africa",
        "North America", "South America",
        "Oceania", "Global"
    }

    bad_continent_rows = ~df["Continent"].isin(valid_continents)

    if bad_continent_rows.any():
        print("Invalid continent rows:", (df.index[bad_continent_rows] + 2).tolist())

    df = df[~bad_continent_rows]

    # Reset index and return cleaned DataFrame
    return df.reset_index(drop=True)