from load_data import load_data
from cleaner import clean_data
from load_json import load_json
from filter_by_region import filter_by_region
from filter_by_country import filter_by_country
from Process import process
from transform import transform_to_long

def main():
    df = load_data("gdp_with_continent_filled.csv")
    cleaned_df = clean_data(df)
    df_long = transform_to_long(cleaned_df)

    config = load_json("config.json")
    filtered_regions = filter_by_region(df_long, config)
    print(filtered_regions)
    print("Total Rows: ", len(filtered_regions))

    filtered_country = filter_by_country(df_long, config)
    print(filtered_country)

if __name__ == "__main__":
    main()
