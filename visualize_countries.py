import matplotlib.pyplot as plt

def visualize_countries(df, config):
    countries = config.get("country", [])

    for country in countries:
        country_df = df[df["Country Name"] == country].sort_values("Year")

        years = country_df["Year"]
        gdp = country_df["GDP"]

        # ---------------- LINE GRAPH ----------------
        plt.figure(figsize=(9, 5))
        plt.plot(
            years,
            gdp,
            marker="o",
            color="#1f77b4",   # blue
            linewidth=2
        )
        plt.title(f"GDP Trend of {country}")
        plt.xlabel("Year")
        plt.ylabel("GDP")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

        # ---------------- SCATTER PLOT ----------------
        plt.figure(figsize=(9, 5))
        plt.scatter(
            years,
            gdp,
            color="#2ca02c",  # green
            alpha=0.7
        )
        plt.title(f"GDP Scatter Plot of {country}")
        plt.xlabel("Year")
        plt.ylabel("GDP")
        plt.tight_layout()
        plt.show()

        # ---------------- HISTOGRAM ----------------
        plt.figure(figsize=(8, 5))
        plt.hist(
            gdp,
            bins=12,
            color="#ff7f0e",   # orange
            edgecolor="black",
            alpha=0.75
        )
        plt.title(f"GDP Distribution of {country}")
        plt.xlabel("GDP")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()
