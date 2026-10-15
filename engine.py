from random import Random
from models import Direction, Position, Snapshot, StepResult
from snake import Snake
from food import spawn_apple
from rules import is_inside, is_opposite

class GameEngine:
    def __init__(self, cols: int = 20, rows: int = 15, seed: int | None = None):
        """IN: cols>=4, rows>=3, số nguyên; sai: ValueError.
        OUT: lưu kích thước, Random(seed), sau đó reset().
        """
        raise NotImplementedError("TODO 4")

    def reset(self) -> None:
        """OUT: None; rắn [(2,1),(1,1),(0,1)], hướng RIGHT,
        score=0, status=RUNNING, sinh táo mới. Xóa khóa đổi hướng.
        Giữ rng hiện có, không khởi tạo lại seed mỗi lần reset.
        """
        raise NotImplementedError("TODO 4")

    def change_direction(self, new_direction: Direction) -> bool:
        """OUT: True khi nhận hướng mới; False khi cùng hướng, ngược 180 độ,
        game đã kết thúc hoặc đã nhận một lần đổi hướng trước step tiếp theo.
        Chuỗi ngoài 4 hướng: ValueError. Từ chối không làm thay đổi trạng thái.
        """
        raise NotImplementedError("TODO 4")

    def step(self) -> StepResult:
        """Một tick logic. Xem README mục trình tự và bảng kết quả.
        OUT: StepResult; đây là nơi duy nhất tăng điểm và thay trạng thái game.
        """
        raise NotImplementedError("TODO 4")

    def snapshot(self) -> Snapshot:
        """OUT: bản sao body dạng tuple và các giá trị hiện tại; O(L)."""
        raise NotImplementedError("TODO 4")
