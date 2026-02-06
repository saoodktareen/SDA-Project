import pandas as pd
from cleaner import clean_data

test_df = pd.DataFrame({
    "Country Name": ["Pakistan", 123],
    "Country Code": ["PAK", "IND"],
    "Indicator Name": ["GDP", "GDP"],
    "Indicator Code": ["NY.GDP", "NY.GDP"],
    "Continent": ["Asia", None],
    "1960": ["123abc", 500],
    "1961": [None, "700"]
})

print(clean_data(test_df))
