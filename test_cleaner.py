import pandas as pd
from cleaner import clean_data

test_df = pd.DataFrame({

    "Country Name": ["ValidCountry", "Bad1Country", "ValidCountry", "ValidCountry"],
    "Country Code": ["VC", "C0D3", "VC", "VC"],
    "Indicator Name": ["GDP", "GDP", "GDP1", "GDP"],
    "Indicator Code": ["NY.GDP", "NY.GDP", "NY.GDP", "NY.GDP"],

    "Continent": ["Asia", "Asia", "Asia", "WrongContinent"],

    "1962": [1000, 2000, 3000, 4000],
    "1963": ["500A", 6000, 7000, None],
    "1964": [2000, 3000, 4000, None]

})

print("Original DF:")
print(test_df)

print("\nCleaned DF:")
print(clean_data(test_df))
