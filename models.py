from dataclasses import dataclass
from typing import Literal

Position = tuple[int, int]  # (x, y), đơn vị ô
Direction = Literal["UP", "DOWN", "LEFT", "RIGHT"]
Status = Literal["RUNNING", "GAME_OVER", "WON"]
Reason = Literal["MOVE", "EAT", "WALL", "SELF", "BOARD_FULL", "NO_CHANGE"]

@dataclass(frozen=True)
class StepResult:
    status: Status
    score: int
    ate: bool
    reason: Reason

@dataclass(frozen=True)
class Snapshot:
    body: tuple[Position, ...]  # đầu -> đuôi; bản sao không sửa được
    apple: Position | None
    direction: Direction
    score: int
    status: Status
