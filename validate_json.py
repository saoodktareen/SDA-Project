import pandas as pd

def validate_json(config: dict, clean_df: pd.DataFrame):
    errors = []

    required_keys = {"operation", "output", "country", "region", "year"}

    # ---------- 1. STRUCTURE CHECK ----------
    if not isinstance(config, dict):
        errors.append("JSON must be a dictionary")
        return None, errors

    missing_keys = required_keys - config.keys()
    extra_keys = config.keys() - required_keys

    if missing_keys:
        errors.append(f"Missing keys: {list(missing_keys)}")

    if extra_keys:
        errors.append(f"Extra keys not allowed: {list(extra_keys)}")

    # ---------- 2. NULL / EMPTY CHECK ----------
    for key in required_keys:
        value = config.get(key)

        if value is None:
            errors.append(f"'{key}' cannot be null")

        if isinstance(value, str) and not value.strip():
            errors.append(f"'{key}' cannot be empty")

        if isinstance(value, list) and not value:
            errors.append(f"'{key}' list cannot be empty")

    # ---------- 3. OPERATION ----------
    operation = str(config.get("operation", "")).lower()
    if operation not in {"sum", "average"}:
        errors.append("Operation must be 'sum' or 'average'")

    # ---------- 4. OUTPUT ----------
    output = str(config.get("output", "")).lower()
    if output != "dashboard":
        errors.append("Output must be 'dashboard'")

    # ---------- 5. DF REFERENCES ----------
    df_countries = set(clean_df["Country Name"].str.strip())
    df_regions = set(clean_df["Continent"].str.strip())
    df_years = {int(col) for col in clean_df.columns if col.isdigit()}

    # ---------- 6. COUNTRY ----------
    countries = config.get("country", [])
    if isinstance(countries, str):
        countries = [countries]

    invalid_countries = [c for c in countries if c not in df_countries]
    if invalid_countries:
        errors.append(f"Invalid country names: {invalid_countries}")

    # ---------- 7. REGION ----------
    regions = config.get("region", [])
    if isinstance(regions, str):
        regions = [regions]

    invalid_regions = [r for r in regions if r not in df_regions]
    if invalid_regions:
        errors.append(f"Invalid regions: {invalid_regions}")

    # ---------- 8. YEAR ----------
    years = config.get("year", [])
    if isinstance(years, int):
        years = [years]

    invalid_years = [
        y for y in years
        if not isinstance(y, int) or y not in df_years or y < 1960 or y > 2024
    ]

    if invalid_years:
        errors.append(f"Invalid years: {invalid_years}")

    # ---------- 9. RETURN ----------
    if errors:
        return None, errors

    validated = {
        "operation": operation,
        "output": output,
        "country": countries,
        "region": regions,
        "year": years
    }

    return validated, []
