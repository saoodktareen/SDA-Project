import pandas as pd

def validate_json(config: dict, clean_df: pd.DataFrame) -> dict:
    required_keys = {"operation", "output", "country", "region", "year"}

    # ---------- 1. STRUCTURE CHECK ----------
    if not isinstance(config, dict):
        print("Invalid JSON: JSON must be a dictionary")
        return None

    missing_keys = required_keys - config.keys()
    extra_keys = config.keys() - required_keys

    if missing_keys:
        print(f"Invalid JSON: Missing keys -> {list(missing_keys)}")
        return None

    if extra_keys:
        print(f"Invalid JSON: Extra keys not allowed -> {list(extra_keys)}")
        return None

    # ---------- 2. NULL / EMPTY CHECK ----------
    for key in required_keys:
        value = config.get(key)

        if value is None:
            print(f"Invalid JSON: '{key}' cannot be null")
            return None

        if isinstance(value, str) and not value.strip():
            print(f"Invalid JSON: '{key}' cannot be empty")
            return None

        if isinstance(value, list) and not value:
            print(f"Invalid JSON: '{key}' list cannot be empty")
            return None

    # ---------- 3. OPERATION VALIDATION ----------
    operation = config["operation"].strip().lower()
    valid_operations = {"sum", "average"}

    if operation not in valid_operations:
        print("Invalid operation: Allowed values are 'sum' or 'average'")
        return None

    # ---------- 4. OUTPUT VALIDATION ----------
    output = config["output"].strip().lower()

    if output != "dashboard":
        print("Invalid output: Only 'dashboard' is supported")
        return None

    # ---------- 5. PREPARE DF REFERENCE SETS ----------
    df_countries = set(clean_df["Country Name"].str.strip())
    df_regions = set(clean_df["Continent"].str.strip())
    df_years = {int(col) for col in clean_df.columns if col.isdigit()}

    # ---------- 6. COUNTRY VALIDATION ----------
    countries = config["country"]
    if isinstance(countries, str):
        countries = [countries]

    invalid_countries = [c for c in countries if c not in df_countries]

    if invalid_countries:
        print(f"Invalid country names: {invalid_countries}")
        return None

    # ---------- 7. REGION VALIDATION ----------
    regions = config["region"]
    if isinstance(regions, str):
        regions = [regions]

    invalid_regions = [r for r in regions if r not in df_regions]

    if invalid_regions:
        print(f"Invalid regions: {invalid_regions}")
        return None

    # ---------- 8. YEAR VALIDATION ----------
    years = config["year"]
    if isinstance(years, int):
        years = [years]

    invalid_years = []
    for y in years:
        if not isinstance(y, int) or y not in df_years or y < 1960 or y > 2024:
            invalid_years.append(y)

    if invalid_years:
        print(f"Invalid years: {invalid_years}")
        return None

    # ---------- 9. NORMALIZED & VALIDATED OUTPUT ----------
    return {
        "operation": operation,
        "output": output,
        "country": countries,
        "region": regions,
        "year": years
    }
