def rule_score(domain: dict, user_skills: list) -> float:
    """
    Checks mandatory skills and boosts score logically
    """
    score = 0.0
    skills = [s.lower() for s in user_skills]

    for req in domain["required_skills"]:
        if req in skills:
            score += 0.4
        else:
            # Missing mandatory skill → heavy penalty
            score -= 0.5

    return max(score, 0.0)
