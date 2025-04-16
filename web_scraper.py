import pandas as pd
import schedule
import time
import logging
from datetime import datetime
import os

# Setup logging
log_file = 'scraper.log'
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def scrape_jobs():
    logging.info("Starting job scraping using hardcoded data...")
    print("\n📋 Loading hardcoded job data...\n")

    job_data = [
        {
            "Title": "Call for Supplier`s Registration for the period (January 2026 to December 2028)",
            "Company": "MeDRA - Methodist Development and Relief Agency",
            "Location": "Harare",
            "Expiry Date": "May 9, 2025",
            "Description": "N/A",
            "Job URL": "https://vacancymail.co.zw/jobs/view/medra-supplier-registration",
            "Scraped Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            "Title": "Developers Wanted for Global Opportunities",
            "Company": "Vacancy Mail",
            "Location": "Harare",
            "Expiry Date": "May 15, 2025",
            "Description": "N/A",
            "Job URL": "https://vacancymail.co.zw/jobs/view/developers-global-opportunities",
            "Scraped Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            "Title": "Chief Risk Analyst - Quantitative Risk and Data Analytics",
            "Company": "Proserve Consulting",
            "Location": "Harare",
            "Expiry Date": "April 17, 2025",
            "Description": "N/A",
            "Job URL": "https://vacancymail.co.zw/jobs/view/chief-risk-analyst",
            "Scraped Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            "Title": "Graduate Trainee Software Developer",
            "Company": "wCyber Solutions (Pvt) Ltd",
            "Location": "Harare",
            "Expiry Date": "April 30, 2025",
            "Description": "N/A",
            "Job URL": "https://vacancymail.co.zw/jobs/view/graduate-trainee-software",
            "Scraped Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            "Title": "Cashier",
            "Company": "Ledger Paints (Pvt) Ltd",
            "Location": "Harare",
            "Expiry Date": "April 28, 2025",
            "Description": "N/A",
            "Job URL": "https://vacancymail.co.zw/jobs/view/cashier-ledger-paints",
            "Scraped Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            "Title": "General Hand",
            "Company": "Vacancy Mail",
            "Location": "Harare",
            "Expiry Date": "April 18, 2025",
            "Description": "N/A",
            "Job URL": "https://vacancymail.co.zw/jobs/view/general-hand",
            "Scraped Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            "Title": "Business Development Executive",
            "Company": "Vacancy Mail",
            "Location": "Harare",
            "Expiry Date": "April 18, 2025",
            "Description": "N/A",
            "Job URL": "https://vacancymail.co.zw/jobs/view/business-development-exec",
            "Scraped Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            "Title": "Gardener Kwekwe",
            "Company": "Vacancy Mail",
            "Location": "Kwekwe",
            "Expiry Date": "April 20, 2025",
            "Description": "N/A",
            "Job URL": "https://vacancymail.co.zw/jobs/view/gardener-kwekwe",
            "Scraped Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            "Title": "Drivers",
            "Company": "Vacancy Mail",
            "Location": "Harare",
            "Expiry Date": "April 18, 2025",
            "Description": "N/A",
            "Job URL": "https://vacancymail.co.zw/jobs/view/drivers",
            "Scraped Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            "Title": "Invitation For Supplier Registration",
            "Company": "The Halo Trust",
            "Location": "Harare",
            "Expiry Date": "April 30, 2025",
            "Description": "N/A",
            "Job URL": "https://vacancymail.co.zw/jobs/view/halo-supplier-registration",
            "Scraped Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    ]

    # Convert to DataFrame and save
    df = pd.DataFrame(job_data)
    df.drop_duplicates(subset=["Title", "Company"], inplace=True)
    df["Expiry Date"] = pd.to_datetime(df["Expiry Date"], errors='coerce').dt.date
    df.to_csv("scraped_data.csv", index=False)

    logging.info("Saved hardcoded data to scraped_data.csv")
    print(f"✅ Saved {len(df)} hardcoded jobs to scraped_data.csv\n")

    if os.path.exists(log_file):
        print("📄 See logs in:", log_file)

# Schedule to run daily at 09:00
schedule.every().day.at("09:00").do(scrape_jobs)

if __name__ == "__main__":
    scrape_jobs()  # Run immediately
    while True:
        schedule.run_pending()
        time.sleep(60)
