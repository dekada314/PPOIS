from pathlib import Path

import pygame


class AudioManager:
    def __init__(self, music_path: Path, sounds_dir: Path, music_volume: float, effects_volume: float) -> None:
        self.enabled = False
        self.sounds: dict[str, pygame.mixer.Sound] = {}

        try:
            if pygame.mixer.get_init() is None:
                pygame.mixer.init()
        except pygame.error:
            return

        self.enabled = True

        for key in ("move", "rotate", "soft_drop", "hard_drop", "line_clear", "game_over"):
            path = sounds_dir / f"{key}.wav"
            if not path.exists():
                continue

            try:
                sound = pygame.mixer.Sound(str(path))
                sound.set_volume(effects_volume)
                self.sounds[key] = sound
            except pygame.error:
                pass

        if music_path.exists():
            try:
                pygame.mixer.music.load(str(music_path))
                pygame.mixer.music.set_volume(music_volume)
                pygame.mixer.music.play(-1)
            except pygame.error:
                pass

    def play(self, key: str) -> None:
        if not self.enabled:
            return

        sound = self.sounds.get(key)
        if sound is not None:
            sound.play()
