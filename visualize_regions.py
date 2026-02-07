import matplotlib.pyplot as plt
import seaborn as sns
from Process import process

def visualize_regions(df, config):
    years = config["year"]
    focus_regions = config["region"]
    operation = config["operation"].capitalize()

    for year in years:
        year_df = df[df["Year"] == year]

        region_gdp = process(year_df, config, "Continent")
        region_gdp = region_gdp.sort_values("GDP", ascending=False)

        colors = [
            "#FF8C00" if r in focus_regions else "#4C72B0"
            for r in region_gdp["Continent"]
        ]

        # ---------- BAR CHART ----------
        plt.figure(figsize=(9, 5))
        plt.bar(region_gdp["Continent"], region_gdp["GDP"], color=colors)
        plt.title(f"{operation} GDP by Region ({year})")
        plt.xlabel("Region")
        plt.ylabel(f"{operation} GDP")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

        # ---------- PIE CHART ----------
        plt.figure(figsize=(7, 7))
        plt.pie(
            region_gdp["GDP"],
            labels=region_gdp["Continent"],
            autopct="%1.1f%%",
            colors=colors,
            startangle=140
        )
        plt.title(f"{operation} GDP Share by Region ({year})")
        plt.show()

        # ---------- HEATMAP ----------
        plt.figure(figsize=(6, 4))
        sns.heatmap(
            region_gdp.set_index("Continent"),
            annot=True,
            fmt=".2e",
            cmap="coolwarm"
        )
        plt.title(f"{operation} GDP Heatmap ({year})")
        plt.xlabel("GDP")
        plt.ylabel("Region")
        plt.show()
