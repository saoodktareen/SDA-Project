import pandas as pd

def clean_data(df: pd.DataFrame):
    # Work on a copy
    df = df.copy()

    # ---------- ERROR LOG ----------
    error_log = {
        "text_errors": [],
        "empty_country": [],
        "gdp_alpha": [],
        "empty_gdp": [],
        "invalid_continent": []
    }

    # Text columns
    text_cols = [
        "Country Name",
        "Country Code",
        "Indicator Name",
        "Indicator Code",
        "Continent"
    ]

    # GDP columns
    gdp_cols = df.columns.difference(text_cols)

    # ---------- REMOVE DUPLICATES ----------
    df = df.drop_duplicates()

    # ---------- TEXT CLEANING ----------
    df[text_cols] = df[text_cols].astype("string").fillna("")

    # ---------- TEXT VALIDATION ----------
    bad_text_rows = df[text_cols].apply(
        lambda c: c.str.contains(r"\d")
    ).any(axis=1)

    error_log["text_errors"] = (df.index[bad_text_rows] + 2).tolist()
    df = df[~bad_text_rows]

    # ---------- EMPTY COUNTRY ----------
    bad_country_rows = df["Country Name"].str.strip().eq("")
    error_log["empty_country"] = (df.index[bad_country_rows] + 2).tolist()
    df = df[~bad_country_rows]

    # ---------- GDP LETTER CHECK ----------
    bad_gdp_rows = df[gdp_cols].astype(str).apply(
        lambda c: c.str.contains(r"[A-Za-z]")
    ).any(axis=1)

    error_log["gdp_alpha"] = (df.index[bad_gdp_rows] + 2).tolist()

    # Convert GDP columns to numeric
    df[gdp_cols] = (
        df[gdp_cols]
        .apply(pd.to_numeric, errors="coerce")
        .fillna(0.0)
        .astype(float)
    )

    # ---------- EMPTY GDP ----------
    empty_gdp_rows = (df[gdp_cols] == 0).all(axis=1)
    error_log["empty_gdp"] = (df.index[empty_gdp_rows] + 2).tolist()
    df = df[~empty_gdp_rows]

    # ---------- CONTINENT VALIDATION ----------
    valid_continents = {
        "Asia", "Europe", "Africa",
        "North America", "South America",
        "Oceania", "Global"
    }

    bad_continent_rows = ~df["Continent"].isin(valid_continents)
    error_log["invalid_continent"] = (df.index[bad_continent_rows] + 2).tolist()
    df = df[~bad_continent_rows]

    # ---------- RETURN ----------
    return df.reset_index(drop=True), error_log
