import json
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "config"
DATA_DIR = BASE_DIR / "data"
ASSETS_DIR = BASE_DIR / "assets"

GAME_CONFIG_PATH = CONFIG_DIR / "game_config.json"
PIECES_CONFIG_PATH = CONFIG_DIR / "pieces.json"
TEXTS_CONFIG_PATH = CONFIG_DIR / "texts.json"
HIGHSCORES_PATH = DATA_DIR / "highscores.json"

MUSIC_PATH = ASSETS_DIR / "music" / "background.wav"
SOUNDS_DIR = ASSETS_DIR / "sounds"


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, ensure_ascii=False, indent=2)


def load_all_configs() -> dict[str, Any]:
    return {
        "game": load_json(GAME_CONFIG_PATH),
        "pieces": load_json(PIECES_CONFIG_PATH),
        "texts": load_json(TEXTS_CONFIG_PATH),
    }
