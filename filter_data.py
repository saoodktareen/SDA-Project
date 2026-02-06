from load_data import load_data
from cleaner import clean_data
from load_json import load_json

def filter_data(df, config:dict):
    if "region" in config:
        if isinstance(config["region"], list): 
            df = df[df["Continent"].isin(config["region"])] 
        else: 
            df = df[df["Continent"] == config["region"]]
    if "year" in config:
        df = df[df["Year"] == config["year"]]
    df = df.dropna(subset=["GDP"])
    return df