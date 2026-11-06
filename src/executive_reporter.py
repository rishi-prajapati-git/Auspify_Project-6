"""
Executive Report Synthesis Module.
Generates comprehensive executive summary covering findings from Task 1 through Task 5
and delivers high-impact strategic business roadmaps.
"""

from pathlib import Path
import json


def generate_executive_report(dashboard_payload: dict, output_path: str = "reports/executive_business_report.json"):
    out_file = Path(output_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    
    report = {
        "title": "Netflix Global Content Strategy & Business Insights Report",
        "program": "Auspify Technologies Data Science Internship",
        "task_name": "Task 6: Data Science Business Insights Dashboard",
        "author": "Rishi Prajapati",
        "executive_summary": (
            "This capstone project synthesizes end-to-end data analytics, machine learning classification, "
            "recommendation intelligence, and statistical forecasting into a strategic decision-making dashboard. "
            "Key strategic imperatives focus on increasing multi-season serial productions, expanding localized Asian and "
            "Latin American episodic content, and implementing family-oriented ad-tier monetization."
        ),
        "key_performance_indicators": dashboard_payload["kpis"],
        "content_mix_analysis": dashboard_payload["format_split"],
        "top_content_producers": dashboard_payload["top_countries"],
        "top_demographics": dashboard_payload["audience_demographics"],
        "growth_projections": dashboard_payload["five_year_forecast"],
        "strategic_pillars": dashboard_payload["business_recommendations"]
    }
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)
        
    print(f"[SUCCESS] Executive business report saved to: {out_file.resolve()}")
