import requests
import os
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def fetch_internships(keyword, location="India", limit=5):
    """
    Fetch real-time internships using Google Jobs via SerpAPI
    """
    if not SERPAPI_KEY:
        print("SERPAPI_KEY not set")
        return []

    url = "https://serpapi.com/search.json"

    params = {
        "engine": "google_jobs",
        "q": f"{keyword} internship",
        "location": location,
        "api_key": SERPAPI_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()

        data = response.json()
        jobs = data.get("jobs_results", [])

        internships = []

        for job in jobs[:limit]:
            internships.append({
                "title": job.get("title"),
                "company": job.get("company_name"),
                "location": job.get("location"),
                "apply_link": job.get("apply_options", [{}])[0].get("link")
            })

        return internships

    except Exception as e:
        print(" Error fetching jobs:", e)
        return []
