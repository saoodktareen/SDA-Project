import matplotlib.pyplot as plt

def visualize(df, config, result):

    print("\nStatistical Result:", result)

    # -----------------------------
    # REGION-WISE VISUALIZATION
    # -----------------------------
    if "region" in config:
        region_df = df.copy()

        grouped = region_df.groupby("Country Name")["GDP"].mean()

        # BAR CHART
        plt.figure()
        grouped.plot(kind="bar")
        plt.title(f"Region-wise GDP Comparison ({config['region']})")
        plt.xlabel("Country")
        plt.ylabel("Average GDP")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # PIE CHART
        plt.figure()
        grouped.plot(kind="pie", autopct="%1.1f%%")
        plt.title(f"GDP Share in {config['region']}")
        plt.ylabel("")
        plt.show()

    # -----------------------------
    # YEAR-WISE VISUALIZATION
    # -----------------------------
    if "country" in config:
        country_df = df[df["Country Name"] == config["country"]]

        year_group = country_df.groupby("Year")["GDP"].mean()

        # LINE GRAPH
        plt.figure()
        plt.plot(year_group.index, year_group.values, marker="o")
        plt.title(f"GDP Trend for {config['country']}")
        plt.xlabel("Year")
        plt.ylabel("Average GDP")
        plt.grid(True)
        plt.show()

        # SCATTER PLOT
        plt.figure()
        plt.scatter(year_group.index, year_group.values)
        plt.title(f"GDP Scatter for {config['country']}")
        plt.xlabel("Year")
        plt.ylabel("Average GDP")
        plt.show()
