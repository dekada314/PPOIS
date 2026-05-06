import random
from dataclasses import dataclass
from typing import Iterable

import pygame

Color = tuple[int, int, int]
Matrix = tuple[tuple[int, ...], ...]


@dataclass(frozen=True)
class PieceDef:
    piece_id: str
    color: Color
    shape: Matrix


@dataclass
class ActivePiece:
    piece: PieceDef
    shape: Matrix
    x: int
    y: int


class TetrisGame:
    def __init__(self, game_config: dict, piece_config: dict) -> None:
        board_cfg = game_config["board"]
        timing_cfg = game_config["timings"]
        score_cfg = game_config["scoring"]
        colors_cfg = game_config["colors"]

        self.cols = int(board_cfg["cols"])
        self.rows = int(board_cfg["rows"])
        self.cell_size = int(board_cfg["cell_size"])
        self.offset_x = int(board_cfg["offset_x"])
        self.offset_y = int(board_cfg["offset_y"])

        self.base_fall_ms = int(timing_cfg["base_fall_delay_ms"])
        self.min_fall_ms = int(timing_cfg["min_fall_delay_ms"])
        self.level_speed_step_ms = int(timing_cfg["level_speed_step_ms"])
        self.line_anim_ms = int(timing_cfg["line_clear_animation_ms"])
        self.game_over_step_ms = int(timing_cfg["game_over_row_step_ms"])

        self.soft_drop_points = int(score_cfg["soft_drop_per_cell"])
        self.hard_drop_points = int(score_cfg["hard_drop_per_cell"])
        self.line_points = [int(v) for v in score_cfg["line_clear_points"]]
        self.level_up_every = int(score_cfg["level_up_every_lines"])

        self.grid_color: Color = tuple(colors_cfg["grid_line"])
        self.clear_color: Color = tuple(colors_cfg["clear_flash"])
        self.danger_color: Color = tuple(colors_cfg["danger"])

        self.pieces = self._load_pieces(piece_config)
        self.random = random.Random()
        self.bag: list[PieceDef] = []

        self.events: list[str] = []
        self.reset()

    def _load_pieces(self, piece_config: dict) -> list[PieceDef]:
        result: list[PieceDef] = []
        for entry in piece_config.get("pieces", []):
            matrix_rows = entry["matrix"]
            shape = tuple(tuple(1 if c != "." else 0 for c in row) for row in matrix_rows)
            result.append(
                PieceDef(
                    piece_id=str(entry["id"]),
                    color=tuple(entry["color"]),
                    shape=shape,
                )
            )

        if len(result) < 5:
            raise ValueError("Нужно минимум 5 фигур")
        return result

    def reset(self) -> None:
        self.board: list[list[Color | None]] = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.current: ActivePiece | None = None
        self.next_piece: PieceDef | None = None

        self.score = 0
        self.lines = 0
        self.level = 1

        self.paused = False
        self.finished = False

        self.fall_elapsed_ms = 0
        self.clear_elapsed_ms = 0
        self.game_over_elapsed_ms = 0

        self.clearing_rows: list[int] = []
        self.game_over_anim = False
        self.game_over_rows = 0

        self.events.clear()
        self.bag.clear()

        self.next_piece = self._take_piece()
        self._spawn_next()

    def _emit(self, name: str) -> None:
        self.events.append(name)

    def pop_events(self) -> list[str]:
        items = list(self.events)
        self.events.clear()
        return items

    def _take_piece(self) -> PieceDef:
        if not self.bag:
            self.bag = list(self.pieces)
            self.random.shuffle(self.bag)
        return self.bag.pop()

    def _spawn_next(self) -> None:
        piece = self.next_piece if self.next_piece is not None else self._take_piece()
        self.next_piece = self._take_piece()

        spawn_x = self.cols // 2 - len(piece.shape) // 2
        spawn_y = -1
        candidate = ActivePiece(piece=piece, shape=piece.shape, x=spawn_x, y=spawn_y)

        if self._collides(candidate.shape, candidate.x, candidate.y):
            self._start_game_over()
            return

        self.current = candidate

    def _start_game_over(self) -> None:
        self.current = None
        self.game_over_anim = True
        self.game_over_rows = 0
        self.game_over_elapsed_ms = 0
        self._emit("game_over")

    def _fall_delay_ms(self) -> int:
        value = self.base_fall_ms - (self.level - 1) * self.level_speed_step_ms
        return max(self.min_fall_ms, value)

    def _rotate_clockwise(self, shape: Matrix) -> Matrix:
        size = len(shape)
        return tuple(tuple(shape[size - 1 - row][col] for row in range(size)) for col in range(size))

    def _iter_cells(self, shape: Matrix, x: int, y: int) -> Iterable[tuple[int, int]]:
        for row_index, row in enumerate(shape):
            for col_index, value in enumerate(row):
                if value:
                    yield x + col_index, y + row_index

    def _collides(self, shape: Matrix, x: int, y: int) -> bool:
        for cell_x, cell_y in self._iter_cells(shape, x, y):
            if cell_x < 0 or cell_x >= self.cols:
                return True
            if cell_y >= self.rows:
                return True
            if cell_y >= 0 and self.board[cell_y][cell_x] is not None:
                return True
        return False

    def _can_control(self) -> bool:
        return not self.finished and not self.paused and not self.game_over_anim and not self.clearing_rows

    def toggle_pause(self) -> None:
        if self.finished or self.game_over_anim:
            return
        self.paused = not self.paused

    def move(self, dx: int) -> bool:
        if not self._can_control() or self.current is None:
            return False

        new_x = self.current.x + dx
        if self._collides(self.current.shape, new_x, self.current.y):
            return False

        self.current.x = new_x
        self._emit("move")
        return True

    def rotate(self) -> bool:
        if not self._can_control() or self.current is None:
            return False

        rotated = self._rotate_clockwise(self.current.shape)
        for kick_x in (0, -1, 1):
            new_x = self.current.x + kick_x
            if not self._collides(rotated, new_x, self.current.y):
                self.current.shape = rotated
                self.current.x = new_x
                self._emit("rotate")
                return True
        return False

    def soft_drop(self, manual: bool = False) -> bool:
        if not self._can_control() or self.current is None:
            return False

        new_y = self.current.y + 1
        if self._collides(self.current.shape, self.current.x, new_y):
            self._lock_piece()
            return False

        self.current.y = new_y
        if manual:
            self.score += self.soft_drop_points
            self._emit("soft_drop")
        return True

    def hard_drop(self) -> None:
        if not self._can_control() or self.current is None:
            return

        dropped = 0
        while self.soft_drop(manual=False):
            dropped += 1

        self.score += dropped * self.hard_drop_points
        self._emit("hard_drop")

    def _lock_piece(self) -> None:
        if self.current is None:
            return

        for cell_x, cell_y in self._iter_cells(self.current.shape, self.current.x, self.current.y):
            if cell_y >= 0:
                self.board[cell_y][cell_x] = self.current.piece.color

        self.current = None

        rows = [row_index for row_index, row in enumerate(self.board) if all(cell is not None for cell in row)]
        if rows:
            self.clearing_rows = rows
            self.clear_elapsed_ms = 0
            self._emit("line_clear")
            return

        self._spawn_next()

    def _apply_cleared_rows(self) -> None:
        removed = len(self.clearing_rows)
        for row_index in sorted(self.clearing_rows, reverse=True):
            del self.board[row_index]
            self.board.insert(0, [None for _ in range(self.cols)])

        self.clearing_rows = []
        self.clear_elapsed_ms = 0

        self.lines += removed
        self.level = 1 + self.lines // self.level_up_every

        points_idx = min(removed, len(self.line_points) - 1)
        self.score += self.line_points[points_idx] * self.level

        self._spawn_next()

    def update(self, dt_ms: int) -> None:
        if self.finished:
            return

        if self.game_over_anim:
            self.game_over_elapsed_ms += dt_ms
            if self.game_over_elapsed_ms >= self.game_over_step_ms:
                self.game_over_elapsed_ms -= self.game_over_step_ms
                self.game_over_rows += 1
                if self.game_over_rows >= self.rows:
                    self.game_over_anim = False
                    self.finished = True
            return

        if self.paused:
            return

        if self.clearing_rows:
            self.clear_elapsed_ms += dt_ms
            if self.clear_elapsed_ms >= self.line_anim_ms:
                self._apply_cleared_rows()
            return

        self.fall_elapsed_ms += dt_ms
        if self.fall_elapsed_ms >= self._fall_delay_ms():
            self.fall_elapsed_ms = 0
            self.soft_drop(manual=False)

    def draw(
        self,
        surface: pygame.Surface,
        labels: dict[str, str],
        colors: dict[str, Color],
        fonts: dict[str, pygame.font.Font],
    ) -> None:
        board_w = self.cols * self.cell_size
        board_h = self.rows * self.cell_size
        board_rect = pygame.Rect(self.offset_x, self.offset_y, board_w, board_h)

        pygame.draw.rect(surface, colors["panel"], board_rect)
        pygame.draw.rect(surface, self.grid_color, board_rect, 2)

        self._draw_grid(surface, board_rect)
        self._draw_locked_cells(surface)
        self._draw_current_piece(surface)

        if self.clearing_rows:
            self._draw_clear_animation(surface)

        if self.game_over_anim:
            self._draw_game_over_animation(surface, board_rect)

        self._draw_info_panel(surface, labels, colors, fonts)

        if self.paused and not self.finished:
            text = fonts["title"].render(labels["paused"], True, colors["text"])
            rect = text.get_rect(center=(board_rect.centerx, board_rect.centery))
            surface.blit(text, rect)

    def _draw_grid(self, surface: pygame.Surface, board_rect: pygame.Rect) -> None:
        for col in range(1, self.cols):
            x = board_rect.left + col * self.cell_size
            pygame.draw.line(surface, self.grid_color, (x, board_rect.top), (x, board_rect.bottom), 1)
        for row in range(1, self.rows):
            y = board_rect.top + row * self.cell_size
            pygame.draw.line(surface, self.grid_color, (board_rect.left, y), (board_rect.right, y), 1)

    def _draw_block(self, surface: pygame.Surface, x: int, y: int, color: Color) -> None:
        if y < 0:
            return

        px = self.offset_x + x * self.cell_size + 2
        py = self.offset_y + y * self.cell_size + 2
        rect = pygame.Rect(px, py, self.cell_size - 4, self.cell_size - 4)

        pygame.draw.rect(surface, color, rect)
        border = tuple(min(255, v + 35) for v in color)
        pygame.draw.rect(surface, border, rect, 2)

    def _draw_locked_cells(self, surface: pygame.Surface) -> None:
        for row_idx, row in enumerate(self.board):
            for col_idx, cell in enumerate(row):
                if cell is not None:
                    self._draw_block(surface, col_idx, row_idx, cell)

    def _draw_current_piece(self, surface: pygame.Surface) -> None:
        if self.current is None:
            return

        for cell_x, cell_y in self._iter_cells(self.current.shape, self.current.x, self.current.y):
            self._draw_block(surface, cell_x, cell_y, self.current.piece.color)

    def _draw_clear_animation(self, surface: pygame.Surface) -> None:
        alpha = 170 if (self.clear_elapsed_ms // 70) % 2 == 0 else 80
        for row in self.clearing_rows:
            row_rect = pygame.Rect(
                self.offset_x,
                self.offset_y + row * self.cell_size,
                self.cols * self.cell_size,
                self.cell_size,
            )
            flash = pygame.Surface((row_rect.width, row_rect.height), pygame.SRCALPHA)
            flash.fill((*self.clear_color, alpha))
            surface.blit(flash, row_rect.topleft)

    def _draw_game_over_animation(self, surface: pygame.Surface, board_rect: pygame.Rect) -> None:
        for row in range(min(self.game_over_rows, self.rows)):
            row_rect = pygame.Rect(
                board_rect.left,
                board_rect.top + row * self.cell_size,
                board_rect.width,
                self.cell_size,
            )
            overlay = pygame.Surface((row_rect.width, row_rect.height), pygame.SRCALPHA)
            overlay.fill((*self.danger_color, 140))
            surface.blit(overlay, row_rect.topleft)

    def _draw_info_panel(
        self,
        surface: pygame.Surface,
        labels: dict[str, str],
        colors: dict[str, Color],
        fonts: dict[str, pygame.font.Font],
    ) -> None:
        panel_x = self.offset_x + self.cols * self.cell_size + 30
        panel = pygame.Rect(panel_x, self.offset_y, 220, self.rows * self.cell_size)

        pygame.draw.rect(surface, colors["panel_alt"], panel)
        pygame.draw.rect(surface, self.grid_color, panel, 2)

        y = panel.top + 20
        for line in [
            f"{labels['score']}: {self.score}",
            f"{labels['lines']}: {self.lines}",
            f"{labels['level']}: {self.level}",
        ]:
            txt = fonts["body"].render(line, True, colors["text"])
            surface.blit(txt, (panel.left + 12, y))
            y += 34

        next_title = fonts["small"].render(labels["next"], True, colors["muted_text"])
        surface.blit(next_title, (panel.left + 12, y + 6))

        preview = pygame.Rect(panel.left + 12, y + 36, 130, 130)
        pygame.draw.rect(surface, colors["panel"], preview)
        pygame.draw.rect(surface, self.grid_color, preview, 1)

        if self.next_piece is None:
            return

        size = len(self.next_piece.shape)
        cell = 26
        start_x = preview.centerx - (size * cell) // 2
        start_y = preview.centery - (size * cell) // 2

        for r, row in enumerate(self.next_piece.shape):
            for c, value in enumerate(row):
                if not value:
                    continue
                rect = pygame.Rect(start_x + c * cell + 2, start_y + r * cell + 2, cell - 4, cell - 4)
                pygame.draw.rect(surface, self.next_piece.color, rect)
                border = tuple(min(255, v + 35) for v in self.next_piece.color)
                pygame.draw.rect(surface, border, rect, 1)
