from collections import deque
from models import Position, Direction
from rules import hits_body

class Snake:
    def __init__(self, body: list[Position], direction: Direction):
        """IN: >=2 ô khác nhau, liên tiếp Manhattan=1, đầu->đuôi.
        direction phải phù hợp hướng đầu so với đốt thứ hai.
        OUT: đối tượng có body: deque[Position], occupied: set[Position], direction.
        Dữ liệu sai: ValueError. Tạo bản sao input, không giữ alias.
        """
        raise NotImplementedError("TODO 1: khởi tạo và kiểm tra dữ liệu")

    def next_head(self) -> Position:
        """OUT: ô đầu tiếp theo theo direction; không thay đổi dữ liệu."""
        raise NotImplementedError("TODO 1")

    def would_hit_self(self, next_head: Position, grow: bool) -> bool:
        """OUT: True nếu đụng thân. Khi grow=False, được vào ô đuôi sắp rời.
        Gọi rules.hits_body(next_head, self.body[-1], self.occupied, grow);
        người 1 viết lớp bao, người 2 viết thuật toán va chạm, không viết lặp."""
        raise NotImplementedError("TODO 1")

    def advance(self, next_head: Position, grow: bool) -> None:
        """IN: next_head đã được engine xác nhận hợp lệ.
        OUT: None; thêm đầu, chỉ bỏ đuôi khi grow=False; đồng bộ occupied.
        Khi vào đuôi cũ, phải bỏ đuôi khỏi set trước khi thêm đầu mới.
        """
        raise NotImplementedError("TODO 1")
