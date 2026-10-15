from random import Random
from models import Position

def spawn_apple(cols: int, rows: int, occupied: set[Position], rng: Random) -> Position | None:
    """IN: kích thước dương; occupied gồm các ô trong bàn; rng được truyền từ engine.
    OUT: một ô trống chọn đều; None khi kín bàn. Không sửa occupied.
    Sai kích thước/ô ngoài bàn: ValueError.
    Duyệt theo y rồi x để lập danh sách ô trống và dùng rng.choice.
    Chi phí O(cols*rows), tránh thử ngẫu nhiên lặp vô hạn khi bàn gần kín.
    """
    raise NotImplementedError("TODO 3")
