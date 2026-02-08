import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# ---------- HELPER FUNCTIONS ----------

def set_modern_style():
    """Apply modern, professional styling matching other diagrams."""
    plt.style.use("dark_background")
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
        "font.size": 18,
        "axes.labelweight": "bold",
        "axes.titleweight": "bold",
        "axes.edgecolor": "#555555",
        "axes.linewidth": 2,
        "figure.facecolor": "#1a1a1a",
        "axes.facecolor": "#262626",
        "figure.autolayout": False
    })

def format_json_errors(json_errors):
    msg = "🚨 JSON ERRORS FOUND 🚨\n\n"
    for i, err in enumerate(json_errors, 1):
        msg += f"{err}\n"
    return msg

def format_csv_errors(csv_errors):
    msg = "⚠ CSV DATA ERRORS ⚠\n\n"
    has_error = False
    for error_type, rows in csv_errors.items():
        if rows:
            has_error = True
            nice_name = error_type.replace("_", " ").title()
            msg += f"{nice_name} → {rows}\n\n"
    return msg if has_error else None

def display_message(title, message, title_color="white", box_color="#2C3E50", text_color="white"):
    """Display a centered message with a 'Next' button."""
    fig, ax = plt.subplots(figsize=(14, 8))
    fig.patch.set_facecolor("#1a1a1a")
    ax.set_facecolor("#262626")

    # Centered text with proper alignment - white background box with dark text
    ax.text(
        0.5, 0.5, message,
        ha="center", va="center",
        multialignment="center",
        fontsize=20, fontweight="bold",
        color="#1a1a1a",  # Dark text color (same as screen background)
        linespacing=1.6,
        transform=ax.transAxes,
        bbox=dict(facecolor="white", edgecolor=title_color, boxstyle="round,pad=1.2", linewidth=2)
    )

    # Title positioned lower to avoid collision with top border
    ax.set_title(title, fontsize=28, fontweight="bold", color=title_color, pad=30, y=0.98)
    ax.axis("off")

    # Adjust layout to match other diagrams with more top margin
    plt.subplots_adjust(left=0.1, right=0.95, top=0.88, bottom=0.18)

    # Add Next button - SAME position and style as other diagrams
    ax_button = plt.axes([0.02, 0.02, 0.1, 0.05])
    btn_next = Button(
        ax_button, 'Next →', 
        color='white', hovercolor='#E5E7EB'
    )
    btn_next.label.set_color('black')
    btn_next.label.set_fontweight('bold')

    # Function to close the screen
    def next_screen(event):
        plt.close(fig)

    btn_next.on_clicked(next_screen)

    # Auto-maximize window
    mng = plt.get_current_fig_manager()
    try:
        mng.window.state('zoomed')
    except Exception:
        try:
            mng.window.showMaximized()
        except:
            pass

    plt.show()

# ==================== MAIN FUNCTION ====================
def visualize_errors(csv_errors, json_errors):
    """Main function - shows errors if any exist"""
    setup_style()
    
    # JSON errors are critical - show and stop
    if json_errors:
        show_json_errors(json_errors)
        return

    msg = format_csv_errors(csv_errors)
    if msg:
        display_message(
            "CSV ERROR REPORT (Row Numbers)",
            msg,
            title_color="#00CED1",
            box_color="#2C3E50",
            text_color="#E0FFFF"
        )
    else:
        print("✔ No CSV errors found")