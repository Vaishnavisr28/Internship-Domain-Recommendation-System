#Internship Domain Recommendation System (with Real-Time Job Search)
#Overview

Choosing the right internship domain is a major challenge for students because skills, interests, and project experience are often scattered and difficult to map to suitable career paths.

This project presents a Skill-Aware Internship Domain Recommendation System that:

Analyzes a student’s skills, interests, and projects

Recommends the most suitable internship domains

Fetches real-time internship opportunities using Google Jobs via SerpAPI

Provides direct application links

The system is designed as a final-year academic project with a strong emphasis on explainability, real-world relevance, and reliability.

#Objectives

Recommend internship domains based on user profile

Use a hybrid approach (rule-based + similarity scoring)

Provide real-time internship listings

Keep the system simple, explainable, and extensible

#Key Features

Hybrid recommendation logic (rules + ML similarity)

Domain-first recommendation (academically correct)

Real-time internship data using SerpAPI (Google Jobs)

Clear and explainable output

CLI-based (easy to demo, easy to extend)

#System Architecture
User Input (Skills, Interests, Projects)
            ↓
Hybrid Recommendation Engine
(Rule-based + Similarity Scoring)
            ↓
Top Internship Domains
            ↓
SerpAPI (Google Jobs)
            ↓
Live Internship Roles + Apply Links

#Project Structure
internship-domain-recommender/
│
├── app.py                  # Main application
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
│
├── engine/
│   ├── rules.py            # Rule-based scoring
│   ├── similarity.py       # TF-IDF + cosine similarity
│   ├── scorer.py           # Final score computation
│   └── job_fetcher.py      # SerpAPI integration
│
├── data/
│   └── domains.json        # Internship domain definitions
│
├── .gitignore              # Ignored files (venv, .env)

#Technologies Used

Python

Scikit-learn (TF-IDF & cosine similarity)

SerpAPI (Google Jobs)

Requests

python-dotenv

#API Used

SerpAPI – Google Jobs Search

Provides reliable real-time internship listings

Handles scraping and compliance internally

Free tier sufficient for demos and evaluation

#Setup Instructions
1️) Clone the Repository
git clone https://github.com/yourusername/internship-domain-recommender.git
cd internship-domain-recommender

2️) Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate # macOS/Linux

3️) Install Dependencies
pip install -r requirements.txt

4️) Configure SerpAPI Key

Create a .env file in the project root:

SERPAPI_KEY=your_serpapi_key_here


 .env is ignored by Git for security reasons.

5️) Run the Application
python app.py

# Sample Input
Skills: Python, Machine Learning
Interests: AI
Projects: Chatbot

# Sample Output
 Recommended Internship Domains with LIVE Roles:

 AI / Machine Learning (Score: 0.84)
   • Machine Learning Intern – Google
     Location: India
     Apply: https://www.google.com/jobs/...

 Data Science (Score: 0.71)
   • Data Science Intern – Deloitte
     Location: Remote
     Apply: https://www.google.com/jobs/...

# Recommendation Logic

Final score is calculated using a hybrid model:

Final Score =
0.6 × Similarity Score (TF-IDF + Cosine)
+ 0.4 × Rule-Based Skill Matching


This ensures:

Mandatory skills are respected

Interests and projects influence ranking

Results remain explainable

#Academic Significance

Solves a real student problem

Uses industry-relevant techniques

Avoids unreliable scraping

Demonstrates clean software design

Easy to extend for future research

#Future Enhancements

Resume PDF parsing

Web UI (Streamlit / React)

User feedback loop

Automation & alerts

Multi-country job search
