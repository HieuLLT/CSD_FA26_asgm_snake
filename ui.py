from engine import GameEngine
from models import Snapshot

class SnakeApp:
    def __init__(self, engine: GameEngine):
        """TODO 5: tạo cửa sổ Tkinter, Canvas, label điểm; bind bàn phím.
        UI chỉ gọi engine, không sửa body/occupied/score trực tiếp.
        """
        raise NotImplementedError("TODO 5")

    def on_key(self, event) -> None:
        """IN: Tkinter event.keysym; ánh xạ Up/Down/Left/Right -> hướng.
        R/r -> reset rồi vẽ; Escape -> đóng cửa sổ. Phím khác bỏ qua.
        OUT: None. Không tạo thêm vòng tick khi reset.
        """
        raise NotImplementedError("TODO 5")

    def render(self, state: Snapshot) -> None:
        """IN: Snapshot; OUT: None; vẽ ô (x,y) tại pixel
        (x*CELL_SIZE, y*CELL_SIZE), hiển thị điểm/trạng thái.
        apple=None thì không vẽ táo. Không thay đổi engine.
        """
        raise NotImplementedError("TODO 5")

    def tick(self) -> None:
        """OUT: None; step -> snapshot -> render -> root.after(TICK_MS, tick).
        Chỉ tồn tại một chuỗi after; game kết thúc thì vẫn cho phép nhấn R.
        """
        raise NotImplementedError("TODO 5")

    def run(self) -> None:
        """OUT: None; bắt đầu một chuỗi tick và gọi root.mainloop()."""
        raise NotImplementedError("TODO 5")
