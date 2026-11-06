"""
End-to-End Task 6 Pipeline Runner.
Synthesizes analytics, generates structured JSON metrics, produces executive business reports,
and prepares the interactive dashboard environment.
"""

from pathlib import Path
import json
from dashboard_data_builder import build_dashboard_data
from executive_reporter import generate_executive_report


def run_pipeline(
    data_path: str = "data/netflix_cleaned.csv",
    metrics_path: str = "reports/dashboard_metrics.json",
    report_path: str = "reports/executive_business_report.json"
):
    print("=" * 70)
    print("AUSPIFY TECHNOLOGIES INTERNSHIP: TASK 6 - BUSINESS INSIGHTS DASHBOARD")
    print("=" * 70)
    
    # 1. Build and export structured dashboard payload
    print("\n[STEP 1/3] Synthesizing end-to-end analytics and KPIs...")
    payload = build_dashboard_data(data_path, output_path=metrics_path)
    
    # Copy payload into web_dashboard folder so UI can access directly if needed
    web_json = Path("web_dashboard/dashboard_metrics.json")
    with open(web_json, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=4)
    print(f"[INFO] Copied live metrics to: {web_json.resolve()}")
    
    # 2. Executive Report Generation
    print("\n[STEP 2/3] Generating executive business report and strategic roadmap...")
    generate_executive_report(payload, output_path=report_path)
    
    # 3. Summary confirmation
    print("\n[STEP 3/3] Dashboard environment ready!")
    print(f"Total Titles Tracked: {payload['kpis']['total_titles']:,}")
    print(f"Projected 2026 Library: {payload['kpis']['projected_library_2026']:,}")
    print("To view interactive dashboard in browser, execute: python src/server.py")
    
    print("\n" + "=" * 70)
    print("TASK 6 CAPSTONE DASHBOARD PIPELINE COMPLETED SUCCESSFULLY!")
    print("=" * 70)
    return payload


if __name__ == "__main__":
    run_pipeline()
