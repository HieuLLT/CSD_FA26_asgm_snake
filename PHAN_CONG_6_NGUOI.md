# PHÂN CÔNG PROJECT RẮN ĂN TÁO — 6 NGƯỜI

Đây là mẫu phân công theo số thứ tự; nhóm điền tên thật vào khi chốt.
Các hàm chưa triển khai: đọc README và docstring trước khi code.

## Người 1 — Thân rắn (snake.py)
- Nhận: list Position đầu->đuôi và Direction từ engine.
- Làm: kiểm tra dữ liệu khởi tạo; deque body, set occupied; next_head;
  advance; lớp bao would_hit_self gọi thuật toán người 2.
- Trả: next_head -> Position; would_hit_self -> bool; advance -> None.
- Ví dụ: [(2,1),(1,1),(0,1)], RIGHT; advance((3,1),False)
  -> body=[(3,1),(2,1),(1,1)], occupied=set(body).
- Bàn giao cho người 4; test di chuyển, tăng chiều dài, set đồng bộ, ô đuôi cũ.
- Báo cáo: deque, set, thêm đầu/bỏ đuôi và chi phí thao tác.

## Người 2 — Luật và va chạm (rules.py)
- Nhận: tọa độ, kích thước bàn, hướng, set thân và cờ grow.
- Trả: is_inside -> bool; is_opposite -> bool; hits_body -> bool.
- Ví dụ: is_inside((20,1),20,15)->False;
  is_opposite('RIGHT','LEFT')->True.
- Với occupied={(1,1),(1,2),(0,2),(0,1)}, tail=(0,1):
  hits_body((0,1),tail,occupied,False)->False;
  cùng input nhưng grow=True -> True.
- Không sửa input; không tự đổi hướng, di chuyển rắn hay đặt GAME_OVER.
- Bàn giao hits_body cho người 1; is_inside/is_opposite cho người 4.
- Test đủ 4 biên, 4 cặp hướng đối nhau có thứ tự, hướng cùng/vuông góc,
  ô thân, ô đuôi; báo cáo thuật toán va chạm và trường hợp đặc biệt.

## Người 3 — Táo và hợp đồng dữ liệu (food.py, config.py, models.py)
- Nhận: cols, rows, occupied, rng: random.Random.
- Trả: spawn_apple -> Position trống hoặc None nếu kín bàn.
- Ví dụ: bàn 2x2, occupied={(0,0),(1,0),(0,1)} -> (1,1).
- Duyệt y rồi x, lập danh sách ô trống, rng.choice; kiểm tra input theo docstring.
- Bàn giao cho người 4; giữ tên Position/Direction/StepResult/Snapshot ổn định.
- Test một ô trống, kín bàn, táo không trùng thân và dữ liệu sai.
- Báo cáo: thuật toán sinh táo, O(COLS*ROWS), lý do không thử ngẫu nhiên mãi.

## Người 4 — Game engine (engine.py)
- Nhận: các hàm/lớp từ người 1–3; Direction từ UI.
- Làm: __init__, reset, change_direction, step, snapshot.
- Trả: change_direction -> bool; step -> StepResult; snapshot -> Snapshot;
  reset -> None. Xem bảng kết quả trong README.
- Ví dụ: rắn ban đầu, apple=(3,1), step()
  -> StepResult('RUNNING',10,True,'EAT'); rắn dài 4, sinh táo mới.
- Chỉ engine tăng điểm và chuyển trạng thái; tối đa một lần đổi hướng/tick.
- Bàn giao cho người 5 và 6; test tick thường, ăn, chết, thắng, khóa đổi hướng.
- Báo cáo: trình tự tick và độ phức tạp logic so với render.

## Người 5 — Giao diện (ui.py)
- Nhận: GameEngine; Snapshot(body,apple,direction,score,status).
- Input người chơi: Up/Down/Left/Right; R/r; Escape.
- Output: bàn cờ, rắn, táo, điểm, thông báo kết thúc trên cửa sổ;
  các hàm UI trả None.
- Ví dụ: ô (3,1), CELL_SIZE=30 -> góc trên trái pixel (90,30).
- Dùng Tkinter after, không time.sleep trong UI; không sửa dữ liệu engine.
- Có thể làm trước với Snapshot mẫu, sau đó nối engine thật của người 4.
- Bàn giao cho người 6; test thủ công phím, reset nhiều lần, đóng cửa sổ.
- Báo cáo: chuyển tọa độ ô sang pixel và điều phối sự kiện.

## Người 6 — Tích hợp và kiểm thử (main.py, tests/, báo cáo)
- Nhận: các module giữ nguyên API và test cục bộ của người 1–5.
- Làm: điểm vào main; unittest cho acceptance_cases.md; ghép module;
  tổng hợp mô tả/bằng chứng kiểm thử của từng người; chuẩn bị demo.
- Input chạy: python main.py. Output: cửa sổ game khi đã hoàn thành TODO.
- Input kiểm thử: python -m unittest discover -s tests -v
  (sau khi đã tự tạo tests/test_*.py). Output: kết quả pass/fail thực tế.
- Không ghi pass cho ca chưa chạy; ghi lỗi, người xử lý và kết quả chạy lại.
- Test thêm end-to-end: chơi -> ăn -> thua -> R -> chơi lại -> Escape.
- Bộ thư viện hiện có chưa chứa test thực thi, chỉ chứa đặc tả 16 ca.

## Ghép code và điều kiện nghiệm thu
1. Chốt models/config và chữ ký hàm; người 3 quản lý thay đổi chung.
2. Người 1–3 triển khai độc lập theo API. Người 4/5/6 có thể chuẩn bị bằng
   dữ liệu mẫu; không sửa chữ ký để chiều theo module riêng.
3. Ghép rules -> snake; rules + snake + food -> engine; engine -> UI -> main.
4. Người 6 chạy kiểm thử; lỗi module nào người phụ trách module đó sửa.
5. Cả 6 người thử bản ghép và giải thích được phần DSA của mình.

Mỗi bàn giao gồm: code, ví dụ input/output, test/kết quả, mô tả ngắn thuật toán
và độ phức tạp. Không thêm âm thanh, AI hoặc lưu điểm trước khi bản cơ bản ổn.
