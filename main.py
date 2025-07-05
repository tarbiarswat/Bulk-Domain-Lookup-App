import pandas as pd
import whois
import time

def check_domain_availability(domain_name):
    try:
        result = whois.whois(domain_name)
        domain_exists = result.domain_name is not None

        if domain_exists:
            status = "Taken"
            print(f"❌ Taken: {domain_name}")
        else:
            status = "Available"
            print(f"✅ Available: {domain_name}")
    except Exception:
        status = "Probably Available"
        print(f"✅ Probably Available: {domain_name}")
    return status

def main():
    try:
        df = pd.read_csv("domains.csv")
    except FileNotFoundError:
        print("❗ Error: 'domains.csv' not found.")
        return

    if "domain" not in df.columns:
        print("❗ Error: CSV must have a column named 'domain'")
        return

    results = []

    for domain in df['domain']:
        domain = domain.strip()
        if domain:
            status = check_domain_availability(domain)
            results.append({
                "Domain": domain,
                "Availability Status": status
            })
            time.sleep(1)  # polite delay

    # Save results to Excel
    output_df = pd.DataFrame(results)
    output_df.to_excel("domain_results.xlsx", index=False)
    print("\n✅ Results exported to 'domain_results.xlsx'")

if __name__ == "__main__":
    main()
