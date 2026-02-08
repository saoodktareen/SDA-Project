from load_data import load_data
from cleaner import clean_data
from load_json import load_json
from validate_json import validate_json
from filter_by_region import filter_by_region
from filter_by_country import filter_by_country
from transform import transform_to_long
from visualize_regions import visualize_regions
from visualize_countries import visualize_countries

def main():
    df = load_data("gdp_with_continent_filled.csv")
    cleaned_df = clean_data(df)

    config = load_json("config.json")
    validated_config = validate_json(config, cleaned_df)

    if validated_config is None:
        print("Execution stopped due to invalid JSON configuration.")
        return

    df_long = transform_to_long(cleaned_df)

    # Filter ONLY countries (regions must stay global)
    filtered_countries = filter_by_country(df_long, validated_config)

    # ---- VISUALIZATION ----
    visualize_regions(df_long, validated_config)
    visualize_countries(filtered_countries, validated_config)

if __name__ == "__main__":
    main()
