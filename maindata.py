from load_data import load_data
from cleaner import clean_data
from load_json import load_json
from filter_data import filter_data
from Process import process   

def main():
        
    df = load_data("gdp_with_continent_filled.csv")
    cleaned_df = clean_data(df)

    print(cleaned_df)

if __name__ == "__main__":
    main()
