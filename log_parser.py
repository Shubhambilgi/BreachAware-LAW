import os

def parse_log(file_path):
    breach_types = {
        "unauthorized access": "unauthorized_access",
        "patient_data": "phi_leak",
        "confidential": "pii_leak",
        "ransomware": "ransomware_attack",
        "data transfer": "data_exfiltration"
    }

    detected = set()

    try:
        with open(file_path, 'r') as log_file:
            for line in log_file:
                lower_line = line.lower()
                for keyword, breach in breach_types.items():
                    if keyword in lower_line:
                        detected.add(breach)

        if detected:
            print(f"[✓] Breach types detected: {', '.join(detected)}")
        else:
            print("[!] No breach indicators found in log.")

        return list(detected)

    except FileNotFoundError:
        print("[X] Log file not found.")
        return []
