import matplotlib.pyplot as plt
plt.style.use("dark_background")

def visualize_countries(df, config):
    countries = config["country"]
    operation = config["operation"]

    print("\n===== COUNTRY RESULTS =====")

    # Strong, distinct colors (cycle automatically if many countries)
    color_palette = [
        "#EF4444",  # red
        "#3B82F6",  # blue
        "#22C55E",  # green
        "#F59E0B",  # yellow
        "#A855F7",  # purple
        "#EC4899",  # pink
        "#06B6D4"   # cyan
    ]

    country_data = {}

    # ---------- DATA + TERMINAL OUTPUT ----------
    for country in countries:
        country_df = df[df["Country Name"] == country]

        yearly_gdp = (
            country_df
            .groupby("Year")["GDP"]
            .agg("sum" if operation == "sum" else "mean")
            .reset_index()
        )

        country_data[country] = yearly_gdp

        if operation == "sum":
            print(f"{country} → Total GDP (all years): {yearly_gdp['GDP'].sum():.2f}")
        else:
            print(f"{country} → Average GDP (1940–2024): {yearly_gdp['GDP'].mean():.2f}")

    # ---------- LINE PLOT (COMBINED) ----------
    plt.figure(figsize=(10, 6))

    for i, (country, data) in enumerate(country_data.items()):
        plt.plot(
            data["Year"],
            data["GDP"],
            marker="o",
            color=color_palette[i % len(color_palette)],
            label=country
        )

    plt.title("Annual GDP Trend of Selected Countries")
    plt.xlabel("Year")
    plt.ylabel("GDP Value (x10¹²)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.get_current_fig_manager().window.state('zoomed')
    plt.show()

    # ---------- SCATTER PLOT (COMBINED) ----------
    plt.figure(figsize=(10, 6))

    for i, (country, data) in enumerate(country_data.items()):
        plt.scatter(
            data["Year"],
            data["GDP"],
            color=color_palette[i % len(color_palette)],
            label=country
        )

    plt.title("Annual GDP Scatter Plot of Selected Countries")
    plt.xlabel("Year")
    plt.ylabel("GDP Value (x10¹²)")
    plt.legend()
    plt.tight_layout()
    plt.get_current_fig_manager().window.state('zoomed')
    plt.show()

    # ---------- HISTOGRAM (SEPARATE PER COUNTRY) ----------
    for country, data in country_data.items():
        plt.figure(figsize=(9, 5))
        plt.hist(
            data["GDP"],
            bins=12,
            color="#F59E0B",
            edgecolor="white",
            alpha=0.9
        )
        plt.title(f"Annual GDP Distribution of {country}")
        plt.xlabel("GDP Value (x10¹²)")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.get_current_fig_manager().window.state('zoomed')
        plt.show()
