from load_data import load_data
from cleaner import clean_data
from load_json import load_json
from filter_by_region import filter_by_region
from filter_by_country import filter_by_country
from Process import process   
from visual import visualize

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
    filtered_regions = filter_by_region(df_long, config)
    print(filtered_regions)
    print("Total Rows: ", len(filtered_regions))
    filtered_country = filter_by_country(df_long, config)
    print(filtered_country)

    # result = process(filtered, config)  
    # visualize(filtered, config, result)

if __name__ == "__main__":
    main()
