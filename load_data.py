import pandas as pd # Importing Panda Library

def load_data(file_path):
    df = pd.read_csv(file_path) # df = DataFrame (Like Excel sheet)
    return df


df = load_data(r"C:\Users\LENOVOI\OneDrive\Desktop\SDA Project Phase 1\SDA-Project\gdp_with_continent_filled.xlsx.csv") 
print(df.head())