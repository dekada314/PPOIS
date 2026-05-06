from pathlib import Path

from .config import load_json, save_json

ScoreEntry = dict[str, int | str]


def _normalize_entry(entry: object) -> ScoreEntry | None:
    if not isinstance(entry, dict):
        return None
    name = entry.get("name")
    score = entry.get("score")
    if not isinstance(name, str):
        return None
    if not isinstance(score, int):
        return None
    return {"name": name[:16].strip() or "PLAYER", "score": max(0, score)}


def load_highscores(path: Path) -> list[ScoreEntry]:
    if not path.exists():
        return []

    try:
        raw = load_json(path)
    except Exception:
        return []

    if not isinstance(raw, list):
        return []

    normalized = []
    for item in raw:
        entry = _normalize_entry(item)
        if entry is not None:
            normalized.append(entry)

    normalized.sort(key=lambda item: int(item["score"]), reverse=True)
    return normalized


def save_highscores(path: Path, entries: list[ScoreEntry], limit: int) -> None:
    ranked = sorted(entries, key=lambda item: int(item["score"]), reverse=True)
    save_json(path, ranked[:limit])


def is_new_top_score(score: int, entries: list[ScoreEntry]) -> bool:
    if not entries:
        return True
    return score > int(entries[0]["score"])


def insert_score(entries: list[ScoreEntry], name: str, score: int, limit: int) -> list[ScoreEntry]:
    cleaned_name = (name.strip() or "PLAYER")[:16]
    updated = list(entries)
    updated.append({"name": cleaned_name, "score": max(0, score)})
    updated.sort(key=lambda item: int(item["score"]), reverse=True)
    return updated[:limit]
