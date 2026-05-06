import sys
from typing import Final

import pygame
from src.audio import AudioManager
from src.config import HIGHSCORES_PATH, MUSIC_PATH, SOUNDS_DIR, load_all_configs
from src.highscores import (
    insert_score,
    is_new_top_score,
    load_highscores,
    save_highscores,
)
from src.tetris import TetrisGame

STATE_MENU: Final[str] = "menu"
STATE_PLAYING: Final[str] = "playing"
STATE_HIGHSCORES: Final[str] = "highscores"
STATE_HELP: Final[str] = "help"
STATE_NEW_RECORD: Final[str] = "new_record"


class TetrisApp:
    def __init__(self) -> None:
        pygame.init()

        configs = load_all_configs()
        self.game_cfg = configs["game"]
        self.text_cfg = configs["texts"]
        self.piece_cfg = configs["pieces"]

        window = self.game_cfg["window"]
        self.fps = int(self.game_cfg["timings"]["fps"])

        self.screen = pygame.display.set_mode((int(window["width"]), int(window["height"])))
        pygame.display.set_caption(str(window["title"]))
        self.clock = pygame.time.Clock()

        self.colors = {name: tuple(value) for name, value in self.game_cfg["colors"].items()}
        self.fonts = {
            "title": pygame.font.SysFont("dejavusans", 44, bold=True),
            "body": pygame.font.SysFont("dejavusans", 28),
            "small": pygame.font.SysFont("dejavusans", 22),
            "mono": pygame.font.SysFont("dejavusansmono", 24),
        }

        audio_cfg = self.game_cfg["audio"]
        self.audio = AudioManager(
            music_path=MUSIC_PATH,
            sounds_dir=SOUNDS_DIR,
            music_volume=float(audio_cfg["music_volume"]),
            effects_volume=float(audio_cfg["effects_volume"]),
        )

        self.game = TetrisGame(self.game_cfg, self.piece_cfg)

        hs_cfg = self.game_cfg["highscores"]
        self.highscore_limit = int(hs_cfg["limit"])
        self.default_name = str(hs_cfg["default_name"])
        self.highscores = load_highscores(HIGHSCORES_PATH)

        self.menu_items: list[str] = list(self.text_cfg["menu"])
        self.menu_index = 0

        self.state = STATE_MENU
        self.running = True

        self.pending_record_score = 0
        self.name_input = ""

        self.message = ""
        self.message_time_ms = 0

    def run(self) -> None:
        while self.running:
            dt_ms = self.clock.tick(self.fps)
            self._process_events()
            self._update(dt_ms)
            self._draw()
            pygame.display.flip()

        pygame.quit()

    def _process_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                continue

            if self.state == STATE_MENU:
                self._handle_menu_event(event)
            elif self.state == STATE_PLAYING:
                self._handle_game_event(event)
            elif self.state in (STATE_HIGHSCORES, STATE_HELP):
                self._handle_back_event(event)
            elif self.state == STATE_NEW_RECORD:
                self._handle_record_event(event)

    def _update(self, dt_ms: int) -> None:
        if self.message_time_ms > 0:
            self.message_time_ms = max(0, self.message_time_ms - dt_ms)
            if self.message_time_ms == 0:
                self.message = ""

        if self.state != STATE_PLAYING:
            return

        self.game.update(dt_ms)
        self._play_pending_audio()

        if self.game.finished:
            self._on_game_finished()

    def _draw(self) -> None:
        self.screen.fill(self.colors["background"])

        if self.state == STATE_MENU:
            self._draw_menu()
        elif self.state == STATE_PLAYING:
            self._draw_game()
        elif self.state == STATE_HIGHSCORES:
            self._draw_highscores()
        elif self.state == STATE_HELP:
            self._draw_help()
        elif self.state == STATE_NEW_RECORD:
            self._draw_game()
            self._draw_record_dialog()

        if self.message:
            self._draw_message()

    def _handle_menu_event(self, event: pygame.event.Event) -> None:
        if event.type != pygame.KEYDOWN:
            return

        if event.key in (pygame.K_UP, pygame.K_w):
            self.menu_index = (self.menu_index - 1) % len(self.menu_items)
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self.menu_index = (self.menu_index + 1) % len(self.menu_items)
        elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
            self._activate_menu_item()
        elif event.key == pygame.K_ESCAPE:
            self.running = False

    def _activate_menu_item(self) -> None:
        if self.menu_index == 0:
            self.game.reset()
            self._play_pending_audio()
            self.state = STATE_PLAYING
        elif self.menu_index == 1:
            self.highscores = load_highscores(HIGHSCORES_PATH)
            self.state = STATE_HIGHSCORES
        elif self.menu_index == 2:
            self.state = STATE_HELP
        elif self.menu_index == 3:
            self.running = False

    def _handle_game_event(self, event: pygame.event.Event) -> None:
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_ESCAPE:
            self.state = STATE_MENU
            return

        if event.key == pygame.K_p:
            self.game.toggle_pause()
            return

        if event.key in (pygame.K_LEFT, pygame.K_a):
            self.game.move(-1)
        elif event.key in (pygame.K_RIGHT, pygame.K_d):
            self.game.move(1)
        elif event.key in (pygame.K_UP, pygame.K_w):
            self.game.rotate()
        elif event.key == pygame.K_DOWN:
            self.game.soft_drop(manual=True)
        elif event.key == pygame.K_SPACE:
            self.game.hard_drop()

        self._play_pending_audio()

    def _handle_back_event(self, event: pygame.event.Event) -> None:
        if event.type != pygame.KEYDOWN:
            return
        if event.key in (pygame.K_ESCAPE, pygame.K_RETURN, pygame.K_KP_ENTER):
            self.state = STATE_MENU

    def _handle_record_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.key.stop_text_input()
                self.state = STATE_MENU
                return
            if event.key == pygame.K_BACKSPACE:
                self.name_input = self.name_input[:-1]
                return
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                self._save_record()
                return

        if event.type == pygame.TEXTINPUT and len(self.name_input) < 16:
            if event.text.isprintable():
                self.name_input += event.text

    def _on_game_finished(self) -> None:
        score = self.game.score
        self.highscores = load_highscores(HIGHSCORES_PATH)

        if is_new_top_score(score, self.highscores):
            self.pending_record_score = score
            self.name_input = ""
            self.state = STATE_NEW_RECORD
            pygame.key.start_text_input()
            return

        self.message = f"Игра окончена. Очки: {score}"
        self.message_time_ms = 2500
        self.state = STATE_MENU

    def _save_record(self) -> None:
        name = self.name_input.strip() or self.default_name
        self.highscores = insert_score(self.highscores, name, self.pending_record_score, self.highscore_limit)
        save_highscores(HIGHSCORES_PATH, self.highscores, self.highscore_limit)

        pygame.key.stop_text_input()
        self.name_input = ""
        self.state = STATE_HIGHSCORES

        self.message = "Рекорд сохранен"
        self.message_time_ms = 2000

    def _play_pending_audio(self) -> None:
        for event_name in self.game.pop_events():
            self.audio.play(event_name)

    def _draw_menu(self) -> None:
        w = self.screen.get_width()
        title = self.fonts["title"].render("TETRIS", True, self.colors["text"])
        subtitle = self.fonts["small"].render("", True, self.colors["muted_text"])

        self.screen.blit(title, title.get_rect(center=(w // 2, 110)))
        self.screen.blit(subtitle, subtitle.get_rect(center=(w // 2, 150)))

        y = 250
        for i, item in enumerate(self.menu_items):
            active = i == self.menu_index
            color = self.colors["accent"] if active else self.colors["text"]
            text = self.fonts["body"].render(item, True, color)
            text_rect = text.get_rect(center=(w // 2, y + i * 60))

            if active:
                box = pygame.Rect(text_rect.left - 14, text_rect.top - 8, text_rect.width + 28, text_rect.height + 16)
                pygame.draw.rect(self.screen, self.colors["panel_alt"], box)
                pygame.draw.rect(self.screen, self.colors["accent"], box, 2)

            self.screen.blit(text, text_rect)

        hint = self.fonts["small"].render("↑/↓ выбор, Enter подтверждение", True, self.colors["muted_text"])
        self.screen.blit(hint, hint.get_rect(center=(w // 2, self.screen.get_height() - 50)))

    def _draw_game(self) -> None:
        self.game.draw(self.screen, self.text_cfg["labels"], self.colors, self.fonts)

    def _draw_highscores(self) -> None:
        self._draw_simple_panel("Таблица рекордов")
        panel = pygame.Rect(80, 120, self.screen.get_width() - 160, self.screen.get_height() - 190)

        if not self.highscores:
            txt = self.fonts["body"].render("Пока нет результатов", True, self.colors["muted_text"])
            self.screen.blit(txt, txt.get_rect(center=panel.center))
        else:
            y = panel.top + 20
            for i, row in enumerate(self.highscores[: self.highscore_limit], start=1):
                rank = self.fonts["mono"].render(f"{i:>2}", True, self.colors["accent"])
                name = self.fonts["body"].render(str(row["name"]), True, self.colors["text"])
                score = self.fonts["mono"].render(f"{int(row['score']):>6}", True, self.colors["text"])

                self.screen.blit(rank, (panel.left + 30, y))
                self.screen.blit(name, (panel.left + 90, y))
                self.screen.blit(score, (panel.right - 150, y))
                y += 42

        self._draw_back_hint()

    def _draw_help(self) -> None:
        help_cfg = self.text_cfg["help"]
        self._draw_simple_panel(help_cfg["title"])

        y = 140
        for line in help_cfg["lines"]:
            txt = self.fonts["small"].render(line, True, self.colors["text"])
            self.screen.blit(txt, (100, y))
            y += 34

        y += 10
        controls_title = self.fonts["body"].render("Управление", True, self.colors["accent"])
        self.screen.blit(controls_title, (100, y))
        y += 40

        for line in help_cfg["controls"]:
            txt = self.fonts["small"].render(line, True, self.colors["text"])
            self.screen.blit(txt, (110, y))
            y += 32

        self._draw_back_hint()

    def _draw_simple_panel(self, title: str) -> None:
        title_txt = self.fonts["title"].render(title, True, self.colors["text"])
        self.screen.blit(title_txt, (80, 50))

        panel = pygame.Rect(80, 120, self.screen.get_width() - 160, self.screen.get_height() - 190)
        pygame.draw.rect(self.screen, self.colors["panel"], panel)
        pygame.draw.rect(self.screen, self.colors["grid_line"], panel, 2)

    def _draw_back_hint(self) -> None:
        hint = self.fonts["small"].render("Esc или Enter: назад в меню", True, self.colors["muted_text"])
        self.screen.blit(hint, (80, self.screen.get_height() - 50))

    def _draw_record_dialog(self) -> None:
        shade = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        shade.fill((0, 0, 0, 150))
        self.screen.blit(shade, (0, 0))

        dialog = pygame.Rect(220, 200, self.screen.get_width() - 440, 240)
        pygame.draw.rect(self.screen, self.colors["panel_alt"], dialog)
        pygame.draw.rect(self.screen, self.colors["accent"], dialog, 2)

        labels = self.text_cfg["labels"]
        title = self.fonts["body"].render(labels["new_record"], True, self.colors["text"])
        score = self.fonts["small"].render(f"{labels['score']}: {self.pending_record_score}", True, self.colors["muted_text"])
        prompt = self.fonts["small"].render(labels["enter_name"], True, self.colors["text"])

        self.screen.blit(title, title.get_rect(center=(dialog.centerx, dialog.top + 45)))
        self.screen.blit(score, score.get_rect(center=(dialog.centerx, dialog.top + 82)))
        self.screen.blit(prompt, prompt.get_rect(center=(dialog.centerx, dialog.top + 116)))

        input_rect = pygame.Rect(dialog.left + 70, dialog.top + 145, dialog.width - 140, 55)
        pygame.draw.rect(self.screen, self.colors["panel"], input_rect)
        pygame.draw.rect(self.screen, self.colors["accent"], input_rect, 2)

        value = self.name_input or "_"
        value_txt = self.fonts["body"].render(value, True, self.colors["text"])
        self.screen.blit(value_txt, (input_rect.left + 12, input_rect.top + 12))

    def _draw_message(self) -> None:
        text = self.fonts["small"].render(self.message, True, self.colors["text"])
        box = pygame.Rect(text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() - 24)))
        box.inflate_ip(26, 16)

        pygame.draw.rect(self.screen, self.colors["panel_alt"], box)
        pygame.draw.rect(self.screen, self.colors["grid_line"], box, 1)
        self.screen.blit(text, text.get_rect(center=box.center))


def main() -> None:
    try:
        app = TetrisApp()
        app.run()
    except Exception as exc:
        print(f"Ошибка запуска: {exc}", file=sys.stderr)
        raise


if __name__ == "__main__":
    main()