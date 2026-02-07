from load_data import load_data
from cleaner import clean_data
from load_json import load_json
from filter_by_region import filter_by_region
from filter_by_country import filter_by_country
from Process import process   
from visualize_regions import visualize_regions
from visualize_countries import visualize_countries

def main():
    df = load_data("gdp_with_continent_filled.csv")
    cleaned_df = clean_data(df)

    df_long = cleaned_df.melt(
        id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code", "Continent"],
        var_name="Year",
        value_name="GDP"
    )
    df_long["Year"] = df_long["Year"].astype(int)

    config = load_json("config.json")

    # ================= REGIONS =================
    filtered_regions = filter_by_region(df_long, config)
    print("Filtered region rows:", len(filtered_regions))

    # statistics only
    process(filtered_regions, config)

    # visualization MUST get a DataFrame
    visualize_regions(df_long, config)

    # ================= COUNTRIES =================
    # filtered_countries = filter_by_country(df_long, config)
    # print("Filtered country rows:", len(filtered_countries))

    # process(filtered_countries, config)
    # visualize_countries(filtered_countries, config)

if __name__ == "__main__":
    main()
