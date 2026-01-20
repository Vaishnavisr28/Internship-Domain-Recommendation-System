from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def similarity_score(domain_text: str, user_text: str) -> float:
    """
    Computes cosine similarity between domain and user profile
    """
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([domain_text, user_text])
    return cosine_similarity(vectors[1], vectors[0])[0][0]
