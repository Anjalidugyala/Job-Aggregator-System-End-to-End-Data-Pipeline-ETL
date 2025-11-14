from src.scraper import scrape_jobs
from src.transform import clean_jobs
from src.load import save_to_csv

def run_pipeline():
    print("🔍 Starting Job Aggregation Pipeline...")

    jobs = scrape_jobs()
    print(f"Scraped {len(jobs)} jobs")

    clean = clean_jobs(jobs)
    print("✨ Cleaned job data")

    save_to_csv(clean)
    print("📁 Saved processed jobs to data folder")

if __name__ == "__main__":
    run_pipeline()
