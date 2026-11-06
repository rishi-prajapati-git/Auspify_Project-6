"""
Export Static Visual Snapshot for Offline Viewers.
Renders summary analytical charts into static/ folder for portfolio previews.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


sns.set_theme(style="darkgrid")
plt.rcParams.update({"text.color": "white", "axes.labelcolor": "white", "xtick.color": "white", "ytick.color": "white"})


def export_dashboard_preview(data_path: str = "data/netflix_cleaned.csv", out_dir: str = "static"):
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    
    df = pd.read_csv(data_path)
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), facecolor="#0f172a")
    for ax in axes:
        ax.set_facecolor("#1e293b")
        
    # 1. Format
    counts = df["type"].value_counts()
    axes[0].bar(counts.index, counts.values, color=["#E50914", "#475569"], edgecolor="black", width=0.5)
    axes[0].set_title("Catalog Format Breakdown", color="white", fontweight="bold")
    axes[0].set_ylabel("Titles Count")
    for idx, v in enumerate(counts.values):
        axes[0].text(idx, v + 100, f"{v:,}", ha="center", color="white", fontweight="bold")
        
    # 2. Audience Demographics
    aud = df["target_audience"].value_counts()
    axes[1].pie(aud.values, labels=aud.index, colors=["#E50914", "#3b82f6", "#f59e0b", "#10b981", "#64748b"], autopct="%1.1f%%", startangle=140)
    axes[1].set_title("Demographic Distribution", color="white", fontweight="bold")
    
    plt.tight_layout()
    preview_file = out_path / "dashboard_preview.png"
    fig.savefig(preview_file, dpi=300, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print(f"[SUCCESS] Dashboard preview saved to: {preview_file.resolve()}")


if __name__ == "__main__":
    export_dashboard_preview()
