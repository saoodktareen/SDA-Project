import matplotlib.pyplot as plt
import seaborn as sns

def visualize_regions(df, config):
    years = config.get("year", [])
    focus_regions = config.get("region", [])

    base_colors = [
        "#4C72B0",  # blue
        "#55A868",  # green
        "#C44E52",  # red
        "#8172B3",  # purple
        "#CCB974",  # yellow
        "#64B5CD"   # cyan
    ]

    for year in years:
        year_df = df[df["Year"] == year]

        region_avg = (
            year_df
            .groupby("Continent")["GDP"]
            .mean()
            .sort_values(ascending=False)
        )

        colors = []
        for i, region in enumerate(region_avg.index):
            if region in focus_regions:
                colors.append("#FF8C00")   # highlight bars
            else:
                colors.append(base_colors[i % len(base_colors)])

        # ================= BAR CHART =================
        plt.figure(figsize=(9, 5))
        plt.bar(region_avg.index, region_avg.values, color=colors)
        plt.title(f"Average GDP by Region ({year})")
        plt.xlabel("Region")
        plt.ylabel("Average GDP")

        plt.xticks(rotation=30)
        
        plt.draw()

        ax = plt.gca()
        for label in ax.get_xticklabels():
            if label.get_text() in focus_regions:
                label.set_color("#FF8C00")
                label.set_fontweight("bold")
            else:
                label.set_color("black")

        plt.tight_layout()
        plt.show()


        # ================= PIE CHART =================
        plt.figure(figsize=(7, 7))
        plt.pie(
            region_avg.values,
            labels=region_avg.index,
            autopct="%1.1f%%",
            colors=colors,
            startangle=140
        )
        plt.title(f"Average GDP Share by Region ({year})")
        plt.show()

        # ================= HEATMAP =================
        heatmap_data = region_avg.to_frame(name=str(year))
        plt.figure(figsize=(6, 4))
        ax = sns.heatmap(
            heatmap_data,
            annot=True,
            fmt=".2e",
            cmap="coolwarm",
            linewidths=0.5
        )

        ax.set_xlabel("Year")
        ax.set_ylabel("Region")

        for label in ax.get_yticklabels():
            if label.get_text() in focus_regions:
                label.set_color("#FF8C00")
                label.set_fontweight("bold")
            else:
                label.set_color("black")

        plt.title(f"Average GDP Heatmap ({year})")
        plt.show()
