import matplotlib.pyplot as plt
plt.style.use("dark_background")
import seaborn as sns
from Process import process

def visualize_regions(df, config):
    years = config["year"]
    focus_regions = config["region"]
    operation = config["operation"]

    print("\n===== REGION RESULTS =====")

    for year in years:
        year_df = df[df["Year"] == year]

        region_gdp = process(year_df, config, "Continent")
        region_gdp = region_gdp.sort_values("GDP", ascending=False)

        # ---------- TERMINAL OUTPUT ----------
        print(f"\nYear: {year}")

        if operation == "sum":
            for _, row in region_gdp.iterrows():
                if row["Continent"] in focus_regions:
                    print(f"  {row['Continent']} → Total GDP: {row['GDP']:.2f}")

        elif operation == "average":
            avg_gdp = region_gdp["GDP"].mean()
            print(f"  Average GDP across all regions: {avg_gdp:.2f}")

        # ---------- VISUAL HIGHLIGHT ----------
        colors = [
            "#FF8C00" if r in focus_regions else "#4C72B0"
            for r in region_gdp["Continent"]
        ]

        # ---------- BAR ----------
        plt.figure(figsize=(9, 5))
        plt.bar(region_gdp["Continent"], region_gdp["GDP"], color=colors)
        plt.title(f"{operation.capitalize()} GDP by Region ({year})")
        plt.xlabel("Region")
        plt.ylabel(f"{operation.capitalize()} GDP Value (x10¹²)")
        plt.xticks(rotation=30)

        ax = plt.gca()
        for label in ax.get_xticklabels():
            if label.get_text() in focus_regions:
                label.set_color("#FFD700")      # gold
                label.set_fontweight("bold")
                label.set_fontsize(12)
            else:
                label.set_color("white")

        plt.tight_layout()
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')   # Windows

        plt.show()

       # ---------- PIE ----------
        plt.figure(figsize=(7, 7))
        wedges, texts, autotexts = plt.pie(
            region_gdp["GDP"],
            labels=region_gdp["Continent"],
            autopct="%1.1f%%",
            colors=colors,
            startangle=140
        )

        for text in texts:
            if text.get_text() in focus_regions:
                text.set_color("#FFD700")
                text.set_fontweight("bold")
                text.set_fontsize(12)
            else:
                text.set_color("white")

        plt.title(f"{operation.capitalize()} GDP Share by Region ({year})")
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        plt.show()


        # ---------- HEATMAP ----------
        plt.figure(figsize=(6, 4))
        sns.heatmap(
            region_gdp.set_index("Continent"),
            annot=True,
            fmt=".2e",
            cmap="coolwarm"
        )

        ax = plt.gca()  
        for label in ax.get_yticklabels():
            if label.get_text() in focus_regions:
                label.set_color("#FFD700")
                label.set_fontweight("bold")
                label.set_fontsize(12)
            else:
                label.set_color("white")

        plt.title(f"{operation.capitalize()} GDP Heatmap ({year})")
        plt.xlabel("GDP Value")
        plt.ylabel("Region")
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')   # Windows
        plt.show()
