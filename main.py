from parser.log_parser import parse_log
from parser.law_mapper import load_law_mapping, map_breaches_to_laws
from reporter.pdf_reporter import generate_pdf_report


def main():
    log_path = "logs/breach_log1.txt"
    law_map_path = "laws/law_mapping.json"

    breaches = parse_log(log_path)

    if not breaches:
        print("\n[INFO] No breaches detected. Nothing to report.")
        return

    law_data = load_law_mapping(law_map_path)
    actions = map_breaches_to_laws(breaches, law_data)

    print("\n=== Legal Compliance Suggestions ===")

    for breach, laws in actions.items():
        print(f"\n[!] Breach Type: {breach}")

        for law, instruction in laws.items():
            print(f"   - {law}: {instruction}")

    generate_pdf_report(breaches, actions)


if __name__ == "__main__":
    main()