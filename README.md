# Job Scraper Project

This Python script scrapes the **10 most recent job postings** from [https://vacancymail.co.zw/jobs/](https://vacancymail.co.zw/jobs/). It extracts the job title, company name, location, expiry date, and job description. The data is saved in a structured CSV file and updated daily through scheduling.

---

## 📦 Features

- ✅ Scrapes the 10 latest job posts
- ✅ Extracts title, company, location, deadline, and description
- ✅ Cleans and stores data using `pandas`
- ✅ Saves to `scraped_data.csv`
- ✅ Scheduled scraping using `schedule` (runs daily at 9:00 AM)
- ✅ Error handling and logging with `logging`

---

## 🛠 Requirements

Install the required libraries by running:

```bash
pip install -r requirements.txt

# scraped_data
