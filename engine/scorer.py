from engine.rules import rule_score
from engine.similarity import similarity_score

def compute_final_score(domain: dict, profile: dict) -> float:
    """
    Combines rule-based score and ML similarity
    """

    user_text = " ".join(
        profile["skills"] +
        profile["projects"] +
        profile["interests"]
    ).lower()

    domain_text = " ".join(
        domain["required_skills"] +
        domain["keywords"]
    ).lower()

    rule = rule_score(domain, profile["skills"])
    similarity = similarity_score(domain_text, user_text)

    final_score = (0.6 * similarity) + (0.4 * rule)
    return round(final_score, 2)
