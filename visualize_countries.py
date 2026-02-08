import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button

# ==================== COLORS ====================
COLORS = ["#3B82F6", "#10B981", "#F59E0B", "#8B5CF6", "#EF4444", "#06B6D4", "#EC4899", "#14B8A6"]

# ==================== SETUP ====================
def setup_style():
    """Setup plot style - dark background"""
    plt.style.use("dark_background")
    plt.rcParams["font.size"] = 10
    plt.rcParams["figure.facecolor"] = "#1a1a1a"
    plt.rcParams["axes.facecolor"] = "#262626"

# ==================== HELPER FUNCTIONS ====================
def get_country_data(df, country, operation):
    """Get GDP data for one country"""
    country_df = df[df["Country Name"] == country]
    
    if operation == "sum":
        result = country_df.groupby("Year")["GDP"].sum().reset_index()
    else:
        result = country_df.groupby("Year")["GDP"].mean().reset_index()
    
    return result

def print_stats(country, data, operation):
    """Print stats for one country"""
    if operation == "sum":
        total = data["GDP"].sum()
        print(f"{country:>20} → Total GDP: ${total:,.2f}T")
    else:
        avg = data["GDP"].mean()
        print(f"{country:>20} → Avg GDP: ${avg:,.2f}T")

# ==================== CHART DRAWING FUNCTIONS ====================
def draw_line_chart(ax, country_data_list, countries):
    """Draw line chart"""
    ax.clear()
    
    for i, (country, data) in enumerate(zip(countries, country_data_list)):
        color = COLORS[i % len(COLORS)]
        ax.plot(data["Year"], data["GDP"], marker="o", linewidth=2,
               markersize=5, color=color, label=country, alpha=0.9)
    
    ax.set_title("GDP Trends Over Time", fontsize=16, fontweight="bold", pad=10)
    ax.set_xlabel("Year", fontsize=11, fontweight="bold")
    ax.set_ylabel("GDP (Trillions USD)", fontsize=11, fontweight="bold")
    ax.legend(loc="upper left", fontsize=9, framealpha=0.9)
    ax.grid(True, alpha=0.3, linestyle="--")

def draw_bar_chart(ax, country_data_list, countries, operation):
    """Draw bar chart"""
    ax.clear()
    
    if operation == "sum":
        values = list(map(lambda data: data["GDP"].sum(), country_data_list))
        title = "Total GDP Comparison"
    else:
        values = list(map(lambda data: data["GDP"].mean(), country_data_list))
        title = "Average GDP Comparison"
    
    colors_list = [COLORS[i % len(COLORS)] for i in range(len(countries))]
    bars = ax.bar(countries, values, color=colors_list, edgecolor="white",
                 linewidth=1.2, alpha=0.85, width=0.6)
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height, f'${height:.2f}T',
               ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    ax.set_title(title, fontsize=16, fontweight="bold", pad=10)
    ax.set_ylabel("GDP (Trillions USD)", fontsize=11, fontweight="bold")
    ax.set_xlabel("Country", fontsize=11, fontweight="bold")
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    ax.grid(axis='y', alpha=0.3, linestyle="--")

def draw_area_chart(ax, country_data_list, countries):
    """Draw area chart"""
    ax.clear()
    
    years = country_data_list[0]["Year"].values
    gdp_matrix = np.column_stack([data["GDP"].values for data in country_data_list])
    
    colors_list = [COLORS[i % len(COLORS)] for i in range(len(countries))]
    ax.stackplot(years, gdp_matrix.T, labels=countries, colors=colors_list,
                alpha=0.7, edgecolor='white', linewidth=0.5)
    
    ax.set_title("Cumulative GDP Over Time", fontsize=16, fontweight="bold", pad=10)
    ax.set_xlabel("Year", fontsize=11, fontweight="bold")
    ax.set_ylabel("Cumulative GDP (Trillions USD)", fontsize=11, fontweight="bold")
    ax.legend(loc="upper left", fontsize=9, framealpha=0.9)
    ax.grid(True, alpha=0.3, linestyle="--")

def draw_scatter_chart(ax, country_data_list, countries):
    """Draw scatter plot"""
    ax.clear()
    
    for i, (country, data) in enumerate(zip(countries, country_data_list)):
        color = COLORS[i % len(COLORS)]
        years = data["Year"].values
        gdp = data["GDP"].values
        
        ax.scatter(years, gdp, s=80, color=color, label=country,
                  alpha=0.7, edgecolors='white', linewidth=1)
        
        trend = np.poly1d(np.polyfit(years, gdp, 2))
        ax.plot(years, trend(years), color=color, linestyle='--',
               linewidth=2, alpha=0.5)
    
    ax.set_title("GDP Scatter with Trend Lines", fontsize=16, fontweight="bold", pad=10)
    ax.set_xlabel("Year", fontsize=11, fontweight="bold")
    ax.set_ylabel("GDP (Trillions USD)", fontsize=11, fontweight="bold")
    ax.legend(loc="upper left", fontsize=9, framealpha=0.9)
    ax.grid(True, alpha=0.3, linestyle="--")

# ==================== MAIN VISUALIZATION ====================
def visualize_countries(df, config):
    """Main function - creates all visualizations with Next button"""
    setup_style()
    
    countries = config["country"]
    operation = config["operation"]
    
    # Get data for each country
    country_data_list = list(map(lambda c: get_country_data(df, c, operation), countries))
    
    # Print summary
    print("\n" + "="*60)
    print("📊 COUNTRY GDP ANALYSIS".center(60))
    print("="*60 + "\n")
    
    for country, data in zip(countries, country_data_list):
        print_stats(country, data, operation)
    
    print("\n" + "="*60 + "\n")
    print("✨ Use Next button to navigate between charts\n")
    
    # Create figure with consistent size
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.subplots_adjust(bottom=0.15)
    
    # Chart list
    charts = [
        lambda: draw_line_chart(ax, country_data_list, countries),
        lambda: draw_bar_chart(ax, country_data_list, countries, operation),
        lambda: draw_area_chart(ax, country_data_list, countries),
        lambda: draw_scatter_chart(ax, country_data_list, countries)
    ]
    
    # State
    state = {'current': 0}
    
    def next_chart(event):
        """Show next chart"""
        state['current'] = (state['current'] + 1) % len(charts)
        charts[state['current']]()
        counter_text.set_text(f"Chart {state['current'] + 1} of {len(charts)}")
        plt.draw()
    
    # Draw first chart
    charts[0]()
    
    # Add Next button
    button_ax = plt.axes([0.44, 0.02, 0.12, 0.06])
    btn = Button(button_ax, 'Next →', color='#10B981', hovercolor='#059669')
    btn.label.set_color('white')
    btn.label.set_fontweight('bold')
    btn.label.set_fontsize(11)
    btn.on_clicked(next_chart)
    
    # Add counter text
    counter_text = fig.text(0.5, 0.01, f'Chart 1 of {len(charts)}',
                           ha='center', fontsize=10, color='#AAAAAA', fontweight='bold')
    
    plt.show()
    
    print("\n✅ All visualizations complete!\n")