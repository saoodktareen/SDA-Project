from load_data import load_data
from cleaner import clean_data
from load_json import load_json
from validate_json import validate_json
from filter_by_region import filter_by_region
from filter_by_country import filter_by_country
from transform import transform_to_long
from visualize_regions import visualize_regions
from visualize_countries import visualize_countries
from visualize_errors import visualize_errors


def main():

    # ---------- LOAD CSV ----------
    df = load_data("gdp_with_continent_filled.csv")

    # ---------- CLEAN CSV ----------
    cleaned_df, csv_errors = clean_data(df)

    # ---------- LOAD JSON ----------
    config = load_json("config.json")

    # ---------- VALIDATE JSON ----------
    validated_config, json_errors = validate_json(config, cleaned_df)

    # ---------- SHOW ERRORS VISUALLY ----------
    visualize_errors(csv_errors, json_errors)

    # STOP if JSON invalid
    if json_errors:
        return

    # ---------- TRANSFORM ----------
    df_long = transform_to_long(cleaned_df)

    # ---------- FILTER ----------
    filtered_countries = filter_by_country(df_long, validated_config)

    # ---------- VISUALIZE ----------
    visualize_regions(df_long, validated_config)
    visualize_countries(filtered_countries, validated_config)


if __name__ == "__main__":
    main()
