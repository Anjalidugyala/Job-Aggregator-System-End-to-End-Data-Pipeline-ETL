import requests
from bs4 import BeautifulSoup

def scrape_jobs():
    url = "https://example-job-site.com"   # Replace later
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    for job in soup.find_all("div", class_="job-card"):
        title = job.find("h2").text if job.find("h2") else "N/A"
        company = job.find("span", class_="company").text if job.find("span", class_="company") else "N/A"
        location = job.find("span", class_="location").text if job.find("span", "location") else "N/A"

        jobs.append({
            "title": title,
            "company": company,
            "location": location
        })

    return jobs
