import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# ==================== SETUP ====================
def setup_style():
    """Setup plot style"""
    plt.style.use("dark_background")
    plt.rcParams["font.size"] = 11
    plt.rcParams["figure.facecolor"] = "#1a1a1a"

# ==================== JSON ERRORS ====================
def show_json_errors(json_errors):
    """Show JSON configuration errors"""
    setup_style()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('off')
    
    # Create error message
    error_text = "\n".join(json_errors)
    
    # Title
    ax.text(0.5, 0.75, "🚨 JSON CONFIGURATION ERROR",
            ha="center", va="center", fontsize=22, fontweight="bold",
            color="#EF4444", transform=ax.transAxes)
    
    # Error message
    ax.text(0.5, 0.45, error_text,
            ha="center", va="center", fontsize=13,
            color="#FFFFFF", transform=ax.transAxes,
            bbox=dict(facecolor="#2a2a2a", edgecolor="#EF4444",
                     boxstyle="round,pad=1.5", linewidth=3))
    
    # Close button
    ax_button = plt.axes([0.44, 0.08, 0.12, 0.08])
    btn = Button(ax_button, 'Close', color='#EF4444', hovercolor='#DC2626')
    btn.label.set_color('white')
    btn.label.set_fontweight('bold')
    btn.label.set_fontsize(11)
    btn.on_clicked(lambda event: plt.close('all'))
    
    plt.tight_layout()
    plt.show()

# ==================== CSV ERRORS ====================
def show_csv_errors(csv_errors):
    """Show CSV data errors"""
    setup_style()
    
    # Filter only errors that have data
    error_list = []
    for error_type, rows in csv_errors.items():
        if rows:
            clean_name = error_type.replace('_', ' ').title()
            error_list.append(f"{clean_name}: {len(rows)} rows")
    
    if not error_list:
        return
    
    error_text = "\n\n".join(error_list)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('off')
    
    # Title
    ax.text(0.5, 0.72, "⚠️ CSV DATA ERRORS",
            ha="center", va="center", fontsize=22, fontweight="bold",
            color="#06B6D4", transform=ax.transAxes)
    
    # Error message
    ax.text(0.5, 0.45, error_text,
            ha="center", va="center", fontsize=14,
            color="#FFFFFF", transform=ax.transAxes,
            bbox=dict(facecolor="#2a2a2a", edgecolor="#06B6D4",
                     boxstyle="round,pad=1.5", linewidth=3))
    
    # Close button
    ax_button = plt.axes([0.44, 0.08, 0.12, 0.08])
    btn = Button(ax_button, 'Close', color='#06B6D4', hovercolor='#0891B2')
    btn.label.set_color('white')
    btn.label.set_fontweight('bold')
    btn.label.set_fontsize(11)
    btn.on_clicked(lambda event: plt.close('all'))
    
    plt.tight_layout()
    plt.show()

# ==================== MAIN FUNCTION ====================
def visualize_errors(csv_errors, json_errors):
    """Main function - shows errors if any exist"""
    setup_style()
    
    # JSON errors are critical - show and stop
    if json_errors:
        show_json_errors(json_errors)
        return
    
    # CSV errors are warnings - show but continue
    if csv_errors and any(csv_errors.values()):
        show_csv_errors(csv_errors)