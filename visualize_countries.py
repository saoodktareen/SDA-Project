import matplotlib.pyplot as plt
plt.style.use("dark_background")

def visualize_countries(df, config):
    countries = config["country"]
    operation = config["operation"]

    print("\n===== COUNTRY RESULTS =====")

    for country in countries:
        country_df = df[df["Country Name"] == country]

        yearly_gdp = (
            country_df
            .groupby("Year")["GDP"]
            .agg("sum" if operation == "sum" else "mean")
            .reset_index()
        )

        # ---------- TERMINAL OUTPUT ----------
        if operation == "sum":
            total_gdp = yearly_gdp["GDP"].sum()
            print(f"{country} → Total GDP (all years): {total_gdp:.2f}")

        elif operation == "average":
            avg_gdp = yearly_gdp["GDP"].mean()
            print(f"{country} → Average GDP (1940–2024): {avg_gdp:.2f}")

        years = yearly_gdp["Year"]
        gdp = yearly_gdp["GDP"]

        # ---------- LINE ----------
        plt.figure(figsize=(9, 5))
        plt.plot(years, gdp, marker="o")
        plt.title(f"Annual GDP Trend of {country}") #{operation.capitalize()} before GDP Trend
        plt.xlabel("Year")
        plt.ylabel(f" GDP Value (x10¹²)") #{operation.capitalize()} before GDP Value
        plt.grid(True)
        plt.tight_layout()
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')   # Windows
        plt.show()

        # ---------- SCATTER ----------
        plt.figure(figsize=(9, 5))
        plt.scatter(years, gdp)
        plt.title(f"Annual GDP Scatter Plot of {country}") #{operation.capitalize()}
        plt.xlabel("Year")
        plt.ylabel(f" GDP Value (x10¹²)") #{operation.capitalize()}
        plt.tight_layout()
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')   # Windows
        plt.show()

        # ---------- HISTOGRAM ----------
        plt.figure(figsize=(8, 5))
        plt.hist(
            gdp,
            bins=12,
            color="#F59E0B",      # bar color
            edgecolor="white",   # outline for visibility
            alpha=0.9
        )
        plt.title(f"Annual GDP Distribution of {country}")
        plt.xlabel("GDP Value (x10¹²)")
        plt.ylabel("Frequency")
        plt.tight_layout()

        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        plt.show()

