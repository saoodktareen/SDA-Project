import matplotlib.pyplot as plt

def visualize_errors(csv_errors: dict, json_errors: list):

    # ===============================
    # JSON ERRORS (STOP EXECUTION)
    # ===============================
    if json_errors:
        plt.figure(figsize=(10,5))

        msg = "JSON ERRORS FOUND\n\n"

        for i, err in enumerate(json_errors, 1):
            msg += f"{i}) {err}\n"

        plt.text(0.5, 0.5, msg,
                 ha="center",
                 va="center",
                 fontsize=13,
                 color="red")

        plt.title("JSON CONFIGURATION ERROR", fontsize=16)
        plt.axis("off")
        plt.show()
        return


    # ===============================
    # CSV ERRORS (SHOW ARRAYS)
    # ===============================
    error_text = "CSV DATA ERRORS\n\n"
    has_error = False

    for error_type, rows in csv_errors.items():
        if rows:   # only show if exists
            has_error = True

            nice_name = error_type.replace("_", " ").title()

            error_text += f"{nice_name} → {rows}\n\n"

    if not has_error:
        print("No CSV errors found ✔")
        return

    # ---------- DISPLAY ----------
    plt.figure(figsize=(10,6))

    plt.text(0.5, 0.5,
             error_text,
             ha="center",
             va="center",
             fontsize=12,
             bbox=dict(facecolor="black", alpha=0.1))

    plt.title("CSV ERROR REPORT (Row Numbers)", fontsize=15)
    plt.axis("off")
    plt.show()
