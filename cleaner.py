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

    # Remove any duplicate rows in the dataset
    df = df.drop_duplicates()

    # Ensure text columns are of type string and replace missing values with empty string
    df[text_cols] = df[text_cols].astype("string").fillna("")

    # Identify rows in text columns that contain any digits
    bad_text_rows = df[text_cols].apply(
        lambda c: c.str.contains(r"\d")
    ).any(axis=1)

    # If any bad rows exist, print their row numbers (+2 for Excel + header)
    if bad_text_rows.any():
        print(" Text column error rows:", (df.index[bad_text_rows] + 2).tolist())

    # Remove rows with invalid text
    df = df[~bad_text_rows]

    # Identify rows in numeric columns that contain letters
    bad_gdp_rows = df[gdp_cols].astype(str).apply(
        lambda c: c.str.contains(r"[A-Za-z]")
    ).any(axis=1)

    # Print bad GDP rows (+2 for Excel)
    if bad_gdp_rows.any():
        print(" GDP alphabet error rows:", (df.index[bad_gdp_rows] + 2).tolist())

    # Convert GDP columns to numeric, replace non-numeric with 0.0
    df[gdp_cols] = (
        df[gdp_cols]
        .apply(pd.to_numeric, errors="coerce")
        .fillna(0.0)
        .astype(float)
    )

    # Identify rows where all GDP columns are zero
    empty_gdp_rows = (df[gdp_cols] == 0).all(axis=1)

    # Print rows with empty GDP data (+2 for Excel)
    if empty_gdp_rows.any():
        print(" Empty GDP rows:", (df.index[empty_gdp_rows] + 2).tolist())

    # Remove rows with empty GDP
    df = df[~empty_gdp_rows]

    # Define valid continents
    valid_continents = {
        "Asia", "Europe", "Africa",
        "North America", "South America",
        "Oceania", "Global"
    }

    # Identify rows with invalid continent names
    bad_continent_rows = ~df["Continent"].isin(valid_continents)

    # Print invalid continent rows (+2 for Excel)
    if bad_continent_rows.any():
        print(" Invalid continent rows:", (df.index[bad_continent_rows] + 2).tolist())

    # Remove invalid continent rows
    df = df[~bad_continent_rows]

    # Reset index and return cleaned DataFrame
    return df.reset_index(drop=True)
