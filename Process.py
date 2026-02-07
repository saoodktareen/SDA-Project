import pandas as pd

def process(df: pd.DataFrame, config: dict):
    operation = config.get("operation")

    # -------------------------------
    # CASE 1: REGION + YEAR DATA
    # -------------------------------
    if "region" in config:
        grouped = df.groupby("Year")["GDP"]

        if operation == "sum":
            result_df = grouped.sum().reset_index(name="GDP")
            summary = result_df["GDP"].sum()

        elif operation == "average":
            result_df = grouped.mean().reset_index(name="GDP")
            summary = result_df["GDP"].mean()

        print(f"{operation.capitalize()} GDP for region {config['region']}")
        return {
            "type": "region",
            "data": result_df,
            "summary": summary
        }

    # -------------------------------
    # CASE 2: COUNTRY DATA
    # -------------------------------
    if "country" in config:
        grouped = df.groupby("Country Name")["GDP"]

        if operation == "sum":
            result_df = grouped.sum().reset_index(name="GDP")
            summary = result_df["GDP"].iloc[0]

        elif operation == "average":
            result_df = grouped.mean().reset_index(name="GDP")
            summary = result_df["GDP"].iloc[0]

        print(f"{operation.capitalize()} GDP for country {config['country']}")
        return {
            "type": "country",
            "data": result_df,
            "summary": summary
        }
