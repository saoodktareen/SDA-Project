import matplotlib.pyplot as plt
import seaborn as sns
<<<<<<< HEAD
from Process import process
from matplotlib.widgets import Button
=======
from process import process
>>>>>>> origin/Saood

# ==================== COLORS ====================
COLORS = ["#3B82F6", "#10B981", "#F59E0B", "#8B5CF6", "#EF4444", "#06B6D4", "#EC4899", "#14B8A6"]
DARK_COLORS = ["#1E3A8A", "#7F1D1D", "#064E3B", "#4C1D95", "#78350F", "#0F172A", "#374151", "#155E75"]

# ==================== SETUP ====================
def setup_style():
    """Setup plot style"""
    plt.style.use("dark_background")
    plt.rcParams["font.size"] = 10
    plt.rcParams["figure.facecolor"] = "#1a1a1a"
    plt.rcParams["axes.facecolor"] = "#262626"

# ==================== HELPER FUNCTIONS ====================
def get_bar_color(region, focus_regions):
    """Get color for a region - highlight if in focus"""
    if region in focus_regions:
        return "#F59E0B"  # Highlight color (orange)
    else:
        return "#3B82F6"  # Normal color (blue)

# ==================== CHART DRAWING FUNCTIONS ====================
def draw_bar_chart(ax, region_gdp, focus_regions, operation, year):
    """Draw bar chart"""
    ax.clear()
    
    regions = region_gdp["Continent"].tolist()
    gdp_values = region_gdp["GDP"].tolist()
    
    # Get colors for each region
    colors = list(map(lambda r: get_bar_color(r, focus_regions), regions))
    
    # Create bars
    bars = ax.bar(regions, gdp_values, color=colors, edgecolor="white",
                 linewidth=1.2, alpha=0.85, width=0.7)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height, f'${height:.2f}T',
               ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    # Styling
    title = f"{operation.capitalize()} GDP by Region ({year})"
    ax.set_title(title, fontsize=16, fontweight="bold", pad=10)
    ax.set_xlabel("Region", fontsize=11, fontweight="bold")
    ax.set_ylabel(f"{operation.capitalize()} GDP (Trillions USD)", fontsize=11, fontweight="bold")
    
    # Highlight focus region labels
    for label in ax.get_xticklabels():
        if label.get_text() in focus_regions:
            label.set_color("#FFD700")
            label.set_fontweight("bold")
            label.set_fontsize(10)
        else:
            label.set_color("white")
    
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    ax.grid(axis='y', alpha=0.3, linestyle="--")

def draw_pie_chart(ax, region_gdp, focus_regions, operation, year):
    """Draw pie chart"""
    ax.clear()
    
    regions = region_gdp["Continent"].tolist()
    gdp_values = region_gdp["GDP"].tolist()
    
    # Get colors for pie slices
    pie_colors = []
    dark_index = 0
    for region in regions:
        if region in focus_regions:
            pie_colors.append("#F59E0B")
        else:
            pie_colors.append(DARK_COLORS[dark_index % len(DARK_COLORS)])
            dark_index += 1
    
    # Explode focus regions
    explode = [0.05 if r in focus_regions else 0 for r in regions]
    
    # Create pie chart
    wedges, texts, autotexts = ax.pie(gdp_values, labels=regions, autopct="%1.1f%%",
                                        colors=pie_colors, startangle=90,
                                        explode=explode, shadow=True,
                                        textprops={'fontsize': 10, 'fontweight': 'bold'})
    
    # Highlight focus region labels
    for text in texts:
        if text.get_text() in focus_regions:
            text.set_color("#FFD700")
            text.set_fontweight("bold")
            text.set_fontsize(11)
        else:
            text.set_color("white")
            text.set_fontsize(10)
    
    # Make percentage text bold
    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_fontweight('bold')
        autotext.set_color('white')
    
    title = f"{operation.capitalize()} GDP Share by Region ({year})"
    ax.set_title(title, fontsize=16, fontweight="bold", pad=10)

def draw_heatmap(ax, region_gdp, focus_regions, operation, year):
    """Draw heatmap"""
    ax.clear()
    
    # Create heatmap
    sns.heatmap(region_gdp.set_index("Continent"), annot=True, fmt=".2f",
                cmap="YlOrRd", cbar_kws={'label': 'GDP (Trillions USD)'},
                linewidths=1.2, linecolor='white', ax=ax, 
                annot_kws={'fontsize': 10, 'fontweight': 'bold'})
    
    # Highlight focus region labels
    for label in ax.get_yticklabels():
        if label.get_text() in focus_regions:
            label.set_color("#FFD700")
            label.set_fontweight("bold")
            label.set_fontsize(11)
        else:
            label.set_color("white")
            label.set_fontsize(10)
    
    title = f"{operation.capitalize()} GDP Heatmap ({year})"
    ax.set_title(title, fontsize=16, fontweight="bold", pad=10)
    ax.set_xlabel("GDP Value", fontsize=11, fontweight="bold")
    ax.set_ylabel("Region", fontsize=11, fontweight="bold")
    
    # Style colorbar
    cbar = ax.collections[0].colorbar
    cbar.ax.tick_params(labelsize=9)

# ==================== PROCESS ONE YEAR ====================
def process_one_year(df, year, focus_regions, operation, config):
    """Process and visualize one year of data"""
    # Filter data for this year
    year_df = df[df["Year"] == year]
    
    # Process regional data
    region_gdp = process(year_df, config, "Continent")
    region_gdp = region_gdp.sort_values("GDP", ascending=False)
    
    # Print stats
    print(f"\n{'Year: ' + str(year):^60}")
    print("-" * 60)
    
    if operation == "sum":
        for _, row in region_gdp.iterrows():
            if row['Continent'] in focus_regions:
                print(f"  {row['Continent']:>20} → Total GDP: ${row['GDP']:,.2f}T")
    elif operation == "average":
        avg = region_gdp["GDP"].mean()
        print(f"  Average GDP across all regions: ${avg:,.2f}T")
    
    print(f"\n✨ Showing visualizations for {year} - Use Next button to navigate\n")
    
    # Create figure with consistent size
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.subplots_adjust(bottom=0.15)
    
    # Chart list
    charts = [
        lambda: draw_bar_chart(ax, region_gdp, focus_regions, operation, year),
        lambda: draw_pie_chart(ax, region_gdp, focus_regions, operation, year),
        lambda: draw_heatmap(ax, region_gdp, focus_regions, operation, year)
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

# ==================== MAIN FUNCTION ====================
def visualize_regions(df, config):
    """Main function - visualize regional GDP data"""
    setup_style()
    
    years = config["year"]
    focus_regions = config["region"]
    operation = config["operation"]
    
    print("\n" + "="*60)
    print("🌍 REGION GDP ANALYSIS".center(60))
    print("="*60)
    
    # Process each year
    for year in years:
        process_one_year(df, year, focus_regions, operation, config)
    