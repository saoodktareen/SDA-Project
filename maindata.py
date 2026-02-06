from load_data import load_data
from cleaner import clean_data

def main():
    df = load_data(r"C:\Users\LENOVOI\OneDrive\Desktop\SDA Project Phase 1\SDA-Project\gdp_with_continent_filled.csv")
    cleaned_df = clean_data(df)
    print(cleaned_df)

if __name__ == "__main__":
    main()
