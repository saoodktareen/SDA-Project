import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# ---------- HELPER FUNCTIONS ----------

def set_modern_style():
    """Apply modern, professional styling for all plots."""
    plt.style.use("default")
    plt.rcParams.update({
        "font.family": "Arial",
        "font.size": 18,
        "axes.labelweight": "bold",
        "axes.titleweight": "bold",
        "axes.edgecolor": "white",
        "axes.linewidth": 2,
        "figure.facecolor": "#1B2A41",
        "figure.autolayout": True
    })

def format_json_errors(json_errors):
    msg = "🚨 JSON ERRORS FOUND 🚨\n\n"
    for i, err in enumerate(json_errors, 1):
        msg += f"{err}\n" # Removed "i)" to help visual centering
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
    fig.patch.set_facecolor("#1B2A41")

    # The key fix for centering: multialignment="center"
    ax.text(
        0.5, 0.5, message,
        ha="center", va="center",
        multialignment="center",  # <--- Fixes the right-shift issue
        fontsize=20, fontweight="bold",
        color=text_color,
        linespacing=1.6,
        transform=ax.transAxes,
        bbox=dict(facecolor=box_color, edgecolor=title_color, boxstyle="round,pad=1.2")
    )

    ax.set_title(title, fontsize=28, fontweight="bold", color=title_color, pad=30)
    ax.axis("off")

    # --- ADDING THE BUTTON ---
    # Position: [left, bottom, width, height]
    ax_button = plt.axes([0.05, 0.05, 0.12, 0.06]) 
    btn_next = Button(
        ax_button, 'Next →', 
        color='#34495E', hovercolor='#1ABC9C'
    )
    btn_next.label.set_color('white')
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
        pass

    plt.show()

# ---------- MAIN FUNCTION ----------

def visualize_errors(csv_errors: dict, json_errors: list):
    set_modern_style()

    if json_errors:
        msg = format_json_errors(json_errors)
        display_message(
            "JSON CONFIGURATION ERROR",
            msg,
            title_color="#FF4C4C",
            box_color="#3B1F1F",
            text_color="#FFDADA"
        )
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
        print("No CSV errors found ✔")