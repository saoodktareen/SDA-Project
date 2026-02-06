from load_data import load_data
from cleaner import clean_data
from load_json import load_json

def filter_data(df, config:dict):
    if "region" in config:
        df = df[df["Continent"] == config["region"]]
    if "year" in config:
        df = df[df["Year"] == config["year"]]
    return df

df = load_data("gdp_with_continent_filled.csv")
cleaned_df = clean_data(df)


df_long = df.melt(
    id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code", "Continent"],
    var_name="Year",
    value_name="GDP"
)
df_long["Year"] = df_long["Year"].astype(int)

config = load_json("config.json")
filtered = filter_data(df_long, config)
print(filtered)
print("Total Rows: ", len(filtered))