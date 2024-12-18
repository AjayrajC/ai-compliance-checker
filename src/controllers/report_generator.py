import json

def generate_report(context):
    """Generate a summary report based on context retrieval."""
    report = {
        "status": "Success",
        "context_details": context,
        "summary": "Compliance details and applicable laws matched successfully."
    }
    report_file = "data/generated_report.json"
    with open(report_file, "w") as file:
        json.dump(report, file, indent=4)
    print(f"Report generated: {report_file}")
    return report_file
