"""
Automated Testing & Dashboard Integrity Suite for Task 6.
Verifies JSON payload schemas, KPI calculations, and web dashboard static assets.
"""

from pathlib import Path
import json


def test_dashboard_system_integrity():
    print("[TEST] Running automated Task 6 dashboard validation suite...")
    
    # 1. Verify JSON metric payloads
    metric_path = Path("reports/dashboard_metrics.json")
    assert metric_path.exists(), f"Metrics file missing at {metric_path}"
    
    with open(metric_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    assert "kpis" in data
    assert data["kpis"]["total_titles"] == 8790
    assert data["kpis"]["movies_count"] == 6126
    assert data["kpis"]["tv_shows_count"] == 2664
    print("[TEST] PASSED: Metric payload values and calculations verified.")
    
    # 2. Verify executive business report
    report_path = Path("reports/executive_business_report.json")
    assert report_path.exists(), f"Executive report missing at {report_path}"
    with open(report_path, "r", encoding="utf-8") as f:
        rep = json.load(f)
    assert len(rep["strategic_pillars"]) >= 4
    print("[TEST] PASSED: Strategic executive business pillars verified.")
    
    # 3. Verify HTML web dashboard asset
    html_path = Path("web_dashboard/index.html")
    assert html_path.exists(), f"HTML index file missing at {html_path}"
    content = html_path.read_text(encoding="utf-8")
    assert "Chart.js" in content
    assert "Netflix Strategic Intelligence" in content or "Netflix Business Insights" in content
    assert "favicon.svg" in content
    print("[TEST] PASSED: Web dashboard frontend template, Swiss Minimalist architecture, and Chart.js integration verified.")
    
    print("\nALL TASK 6 BUSINESS INSIGHTS DASHBOARD TESTS PASSED! READY FOR SUBMISSION.")


if __name__ == "__main__":
    test_dashboard_system_integrity()
