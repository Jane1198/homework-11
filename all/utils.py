import json


def load_candidates():
    """"Получает список всех кандидатов"""
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)
    return candidates


def get_candidate_by_id(id):
    """Получает словарь с данными о кандидате по его id."""
    candidates = load_candidates()
    for candidate in candidates:
        if candidate["id"] == id:
            return candidate


def get_candidates_by_name(candidate_name):
    """"Возвращает кандидатов по имени"""
    candidates = load_candidates()
    candidates_found = []
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            candidates_found.append(candidate)
    return candidates_found


def get_candidates_by_skill(skill):
    """Отбирает кандидатов по навыкам"""
    skilled_candidates = []
    skill_lower = skill.lower()
    candidates = load_candidates()
    for candidate in candidates:
        skills = candidate["skills"].lower().strip().split(", ")
        if skill_lower in skills:
            skilled_candidates.append(candidate)
    return skilled_candidates


