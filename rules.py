"""Người 2 — các luật thuần; không import snake/engine/ui để tránh import vòng."""
from models import Position, Direction

def is_inside(pos: Position, cols: int, rows: int) -> bool:
    """IN: (x,y), cols/rows nguyên dương. OUT: 0<=x<cols và 0<=y<rows.
    Ví dụ: ((19,14),20,15)->True; ((20,1),20,15)->False. O(1).
    """
    raise NotImplementedError("TODO 2: kiểm tra biên")

def is_opposite(current: Direction, requested: Direction) -> bool:
    """IN: hai hướng trong UP/DOWN/LEFT/RIGHT; sai chuỗi: ValueError.
    OUT: True nếu đối nhau 180 độ. RIGHT/LEFT->True; RIGHT/UP->False.
    Cùng hướng trả False. Không xử lý khóa đổi hướng của engine. O(1).
    """
    raise NotImplementedError("TODO 2: kiểm tra hướng")

def hits_body(next_head: Position, tail: Position,
              occupied: set[Position], grow: bool) -> bool:
    """IN: đầu dự kiến, đuôi hiện tại, set thân, có tăng chiều dài không.
    OUT: next_head thuộc occupied, trừ trường hợp next_head==tail và not grow.
    Không sửa occupied. Trung bình O(1); xấu nhất O(L).
    """
    raise NotImplementedError("TODO 2: kiểm tra thân")
