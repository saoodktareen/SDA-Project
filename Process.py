def process(df, config: dict):
    gdp_series = df["GDP"]

    operations = {
        "sum": lambda x: x.sum(),
        "average": lambda x: x.sum() / len(x)
    }

    op = config.get("operation")

    if op not in operations:
        raise ValueError("Invalid operation")

    result = operations[op](gdp_series)

    print(f"{op.capitalize()} GDP for year {config.get('year')}: {result}")
    return result
