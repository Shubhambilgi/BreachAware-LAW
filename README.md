🛡️ BreachAware-LAW

A cybersecurity + legal intelligence project that detects data breach types from logs and automatically maps them to applicable Indian and global data protection laws like DPDP Act 2023, IT Act 2000, HIPAA, and GDPR — with PDF report generation.

------------------------------------------------------------
🚀 WHAT IT DOES

1. Reads system/server logs
2. Detects breach types:
   - unauthorized_access
   - phi_leak
   - ransomware_attack
   - data_exfiltration
   - pii_leak
3. Maps to relevant laws
4. Generates legal PDF reports

------------------------------------------------------------
📌 WHY THIS PROJECT?

Most breach detection tools only alert. This tool also shows what **laws** apply and what to do — useful for:

- Cybersecurity students
- Legal auditors
- Startups handling data

------------------------------------------------------------
💻 HOW TO RUN

1. Clone the repo
   git clone https://github.com/shubhambilgi/BreachAware-LAW.git
   cd BreachAware-LAW

2. Install requirements
   pip install -r requirements.txt

3. Run the script
   python3 main.py

Output:
- Breach types
- Legal suggestions
- PDF report generated

------------------------------------------------------------
🧠 IMPORTANT COMPONENTS

- logs/         → Sample logs
- laws/         → JSON file for law mapping
- parser/       → Parses logs and maps laws
- reporter/     → PDF report generation
- main.py       → Main program

------------------------------------------------------------
📷 SCREENSHOTS

(pictures/Screenshot_*.png)

------------------------------------------------------------
📚 LEGAL REFERENCES COVERED

| Breach Type         | Laws Applied                        |
|---------------------|-------------------------------------|
| PHI Leak            | HIPAA, DPDP Act 2023                |
| Unauthorized Access | IT Act 2000, DPDP Act 2023          |
| Ransomware Attack   | CERT-In, HIPAA                      |
| Data Exfiltration   | GDPR, CERT-In                       |
| PII Leak            | GDPR, DPDP Act 2023                 |

------------------------------------------------------------
📦 DEPENDENCIES

- Python 3.8+
- fpdf
- json, os, datetime

Install using:
pip install -r requirements.txt

------------------------------------------------------------
🙋 ABOUT ME

Shubham Bilgi  
B.E (IT)  
Cybersecurity & Legal Compliance Enthusiast  
GitHub: @shubhambilgi

------------------------------------------------------------
⭐ GIVE IT A STAR

If helpful, please ⭐ on GitHub and share.

------------------------------------------------------------
🔗 LICENSE

Educational/research purpose only. Not for production use without legal review.
