"""
Export Static Visual Snapshot for Offline Viewers.
Renders summary analytical charts into static/ folder for portfolio previews.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


sns.set_theme(style="whitegrid")
plt.rcParams.update({"text.color": "#000000", "axes.labelcolor": "#000000", "xtick.color": "#000000", "ytick.color": "#000000"})


def export_dashboard_preview(data_path: str = "data/netflix_cleaned.csv", out_dir: str = "static"):
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    
    df = pd.read_csv(data_path)
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), facecolor="#ffffff")
    for ax in axes:
        ax.set_facecolor("#f9f9f9")
        
    # 1. Format
    counts = df["type"].value_counts()
    axes[0].bar(counts.index, counts.values, color=["#000000", "#c90000"], edgecolor="#000000", width=0.45)
    axes[0].set_title("Catalog Format Breakdown (Swiss Style)", color="#000000", fontweight="bold")
    axes[0].set_ylabel("Titles Count")
    for idx, v in enumerate(counts.values):
        axes[0].text(idx, v + 100, f"{v:,}", ha="center", color="#000000", fontweight="bold")
        
    # 2. Audience Demographics with simplified age-group labels
    aud = df["target_audience"].value_counts().head(4)
    labels = [
        f"Adults (18+)\n{aud.iloc[0]:,}",
        f"Teens (13-17)\n{aud.iloc[1]:,}",
        f"Older Kids (7-12)\n{aud.iloc[2]:,}",
        f"Kids (All Ages)\n{aud.iloc[3]:,}"
    ]
    axes[1].pie(aud.values, labels=labels, colors=["#000000", "#555555", "#999999", "#c90000"], autopct="%1.1f%%", startangle=140, textprops={'fontsize': 9, 'weight': 'bold'})
    axes[1].set_title("Audience Age Demographics Distribution", color="#000000", fontweight="bold")
    
    plt.tight_layout()
    preview_file = out_path / "dashboard_preview.png"
    fig.savefig(preview_file, dpi=300, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print(f"[SUCCESS] Dashboard preview saved to: {preview_file.resolve()}")


if __name__ == "__main__":
    export_dashboard_preview()
