from load_data import load_data
from cleaner import clean_data
from load_json import load_json

def filter_data(df, config:dict):
    if "region" in config:
        df = df[df["Continent"] == config["region"]]
    if "year" in config:
        df = df[df["Year"] == config["year"]]
    return df

df = load_data(r"C:\Users\LENOVOI\OneDrive\Desktop\SDA Project Phase 1\SDA-Project\gdp_with_continent_filled.csv")
cleaned_df = clean_data(df)


config = load_json(r"C:\Users\LENOVOI\OneDrive\Desktop\SDA Project Phase 1\SDA-Project\config.json")
filtered = filter_data(df, config)
print(filtered.head())