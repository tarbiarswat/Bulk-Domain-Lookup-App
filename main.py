import pandas as pd
import whois
import time

def check_domain_availability(domain_name):
    try:
        result = whois.whois(domain_name)

        # Some WHOIS servers return lowercase strings, some lists
        domain_exists = result.domain_name is not None

        if domain_exists:
            print(f"❌ Taken: {domain_name}")
        else:
            print(f"✅ Available: {domain_name}")

    except Exception:
        # Hide verbose WHOIS error and show clean fallback
        print(f"✅ Probably Available: {domain_name}")

def main():
    try:
        df = pd.read_csv("domains.csv")
    except FileNotFoundError:
        print("❗ Error: 'domains.csv' not found.")
        return

    if "domain" not in df.columns:
        print("❗ Error: CSV must have a column named 'domain'")
        return

    for domain in df['domain']:
        domain = domain.strip()
        if domain:
            check_domain_availability(domain)
            time.sleep(1)  # optional delay to avoid rate limit

if __name__ == "__main__":
    main()
