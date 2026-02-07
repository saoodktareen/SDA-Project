import matplotlib.pyplot as plt

def visualize_countries(df, config):
    countries = config["country"]
    operation = config["operation"].capitalize()

    for country in countries:
        country_df = df[df["Country Name"] == country]

        yearly_gdp = (
            country_df
            .groupby("Year")["GDP"]
            .agg("sum" if config["operation"] == "sum" else "mean")
            .reset_index()
        )

        years = yearly_gdp["Year"]
        gdp = yearly_gdp["GDP"]

        # ---------- LINE ----------
        plt.figure(figsize=(9, 5))
        plt.plot(years, gdp, marker="o")
        plt.title(f"{operation} GDP Trend of {country}")
        plt.xlabel("Year")
        plt.ylabel(f"{operation} GDP")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        # ---------- SCATTER ----------
        plt.figure(figsize=(9, 5))
        plt.scatter(years, gdp)
        plt.title(f"{operation} GDP Scatter Plot of {country}")
        plt.xlabel("Year")
        plt.ylabel(f"{operation} GDP")
        plt.tight_layout()
        plt.show()

        # ---------- HISTOGRAM ----------
        plt.figure(figsize=(8, 5))
        plt.hist(gdp, bins=12, edgecolor="black")
        plt.title(f"{operation} GDP Distribution of {country}")
        plt.xlabel(f"{operation} GDP")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()
