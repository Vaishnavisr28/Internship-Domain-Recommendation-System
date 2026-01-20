import json
from engine.scorer import compute_final_score
from engine.job_fetcher import fetch_internships

DOMAIN_QUERY_MAP = {
    "AI / Machine Learning": "machine learning",
    "Data Science": "data science",
    "Web Development": "web developer",
    "RPA / Automation": "automation",
    "Cyber Security": "cyber security"
}

def get_user_profile():
    print("\nEnter your details\n")

    skills = input("Skills (comma separated): ").split(",")
    interests = input("Interests (comma separated): ").split(",")
    projects = input("Projects (comma separated): ").split(",")

    return {
        "skills": [s.strip() for s in skills if s.strip()],
        "interests": [i.strip() for i in interests if i.strip()],
        "projects": [p.strip() for p in projects if p.strip()]
    }

def main():
    with open("data/domains.json") as f:
        domains = json.load(f)

    profile = get_user_profile()
    results = []

    for domain in domains:
        score = compute_final_score(domain, profile)
        results.append({
            "domain": domain["domain"],
            "score": score
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    print("\nRecommended Internship Domains with LIVE Roles:\n")

    for r in results[:2]:
        print(f"\n🔹 {r['domain']} (Score: {r['score']})")

        keyword = DOMAIN_QUERY_MAP.get(r["domain"], "intern")
        jobs = fetch_internships(keyword)

        if not jobs:
            print("   No internships found.")
        else:
            for job in jobs:
                print(f"   • {job['title']} – {job['company']}")
                print(f"     Location: {job['location']}")
                print(f"     Apply: {job['apply_link']}")

if __name__ == "__main__":
    main()
