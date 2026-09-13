from fpdf import FPDF
from datetime import datetime
import os

def generate_pdf_report(breach_types, law_mappings, output_path="output/breach_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Cybersecurity Legal Compliance Report", ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)

    pdf.ln(10)
    for breach in breach_types:
        pdf.set_font("Arial", "B", 14)
        pdf.cell(200, 10, f"Breach Type: {breach}", ln=True)

        if breach in law_mappings:
            for law, instruction in law_mappings[breach].items():
                pdf.set_font("Arial", "I", 12)
                pdf.multi_cell(0, 10, f"- {law}: {instruction}")
        else:
            pdf.set_font("Arial", "", 12)
            pdf.cell(200, 10, "No legal mapping found.", ln=True)

        pdf.ln(5)

    # Ensure output directory exists
    os.makedirs("output", exist_ok=True)
    pdf.output(output_path)
    print(f"[✓] PDF report saved to: {output_path}")

