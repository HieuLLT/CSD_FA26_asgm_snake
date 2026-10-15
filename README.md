# SNAKE EATS APPLES — KHUNG PROJECT PYTHON / CSD203

## 1. Mục tiêu và phạm vi
Xây dựng trò chơi rắn ăn táo có giao diện Tkinter: di chuyển bằng mũi tên,
ăn táo tăng chiều dài và điểm, đụng tường/thân thì thua, kín bàn thì thắng,
R để chơi lại, Escape để thoát. Bản khung này CỐ Ý chưa triển khai thuật toán:
các TODO ném NotImplementedError; không phải game hoàn chỉnh.

Đề xuất Python >=3.10. Tkinter thường đi kèm bản Python Windows; thử
`python -m tkinter` để kiểm tra. Sau khi hoàn thiện chạy `python main.py`.
Không cần pygame hoặc thư viện pip cho phạm vi này.

Đây là khung đề xuất theo nội dung môn học, chưa đối chiếu rubric của thầy.
Nếu thầy yêu cầu tự cài đặt Linked List/Queue, cần thay deque bằng cấu trúc tự
viết có cùng thao tác thêm đầu/bỏ đuôi; không gọi deque là danh sách do nhóm tự cài.

## 2. Cấu trúc dữ liệu và giải thuật có thể trình bày
| Thành phần | Lựa chọn | Vai trò / độ phức tạp |
|---|---|---|
| Thân rắn | collections.deque | Thứ tự đầu -> đuôi; Thêm đầu bằng appendleft, bỏ đuôi bằng pop; O(1) |
| Ô rắn chiếm | set[tuple[int,int]] | Kiểm tra thân / thêm / xóa: trung bình O(1), xấu nhất O(L) |
| Vị trí | tuple[int,int] | Tọa độ bất biến, dùng được làm khóa set |
| Bàn cờ | Lưới logic COLS x ROWS | Không bắt buộc lưu ma trận; kiểm tra biên O(1) |
| Sinh táo | Duyệt ô trống + chọn ngẫu nhiên | O(COLS*ROWS) thời gian và bộ nhớ phụ, chỉ khi reset/ăn táo |
| Trạng thái | RUNNING, GAME_OVER, WON | Quản lý điều kiện cập nhật |

L là chiều dài rắn. Tick không ăn táo: phần cập nhật logic trung bình O(1).
Nếu ăn táo: thêm chi phí O(COLS*ROWS). Snapshot và vẽ rắn O(L);
không khẳng định toàn bộ một khung hình là O(1). Bộ nhớ game O(L),
riêng danh sách tạm sinh táo tối đa O(COLS*ROWS).

## 3. Quy ước input/output chung — thống nhất trước khi chia việc
- Position = (x,y), đơn vị Ô, không phải pixel. Gốc (0,0) trên trái;
  x tăng sang phải, y tăng xuống dưới. 0<=x<COLS và 0<=y<ROWS.
- body[0] là đầu; body[-1] là đuôi. body và occupied luôn biểu diễn cùng các ô.
- UP=(0,-1), DOWN=(0,1), LEFT=(-1,0), RIGHT=(1,0).
- Mỗi tick đi đúng 1 ô. Táo không nằm trên rắn. Mỗi táo +10 điểm.
- Chỉ nhận tối đa một lần đổi hướng thực sự giữa hai tick, cấm quay ngược.
  Nhấn cùng hướng không khóa tick; phím bị từ chối không khóa tick.
- None nghĩa là không có táo khi kín bàn. Không dùng (-1,-1) thay None.
- Input người chơi là sự kiện bàn phím. Input/output bên dưới là THAM SỐ và
  GIÁ TRỊ TRẢ VỀ của hàm; logic không gọi input(), không dùng print() thay return.
- Logic không vẽ; UI chỉ lấy Snapshot để vẽ. Không đổi tên hàm/kiểu trả về khi
  chưa thông báo nhóm. None ở hàm cập nhật nghĩa là hàm có thay đổi đối tượng.

## 4. Phân công cho 6 người
| Người | Phần phụ trách | File bàn giao | Điều kiện hoàn thành |
|---|---|---|---|
| 1 | Cấu trúc thân rắn, deque + set; thêm đầu/bỏ đuôi | snake.py | Khởi tạo hợp lệ; di chuyển/tăng chiều dài; giữ body và occupied đồng bộ |
| 2 | Luật hướng, biên bàn và va chạm thân | rules.py | Các hàm thuần không sửa input; xử lý được ô đuôi sắp rời |
| 3 | Sinh táo, cấu hình và kiểu dữ liệu chung | food.py; quản lý config.py, models.py | Táo ngoài rắn, kín bàn trả None; test sinh táo; giữ hợp đồng chung |
| 4 | Điều phối logic, điểm, trạng thái game | engine.py | Ghép 1–3; step đúng thứ tự; reset và khóa đổi hướng đúng |
| 5 | Giao diện và bàn phím Tkinter | ui.py | Chỉ dùng API engine; vẽ đúng tọa độ; R/Escape và một chuỗi after |
| 6 | Tích hợp, kiểm thử hệ thống, demo và tổng hợp báo cáo | main.py, tests/, báo cáo | Bộ ca nghiệm thu có kết quả thực tế; hướng dẫn chạy; tổng hợp phần viết của 1–5 |

Mỗi bạn viết test cho phần mình và mô tả cấu trúc/thuật toán/input/output của
phần đó. Người 6 tổng hợp báo cáo, không phải tự viết toàn bộ báo cáo cho nhóm.
Người 3 quản lý file dùng chung nhưng mọi thay đổi chữ ký phải thống nhất cả nhóm.
Chi tiết đầu vào/đầu ra bàn giao và thứ tự tích hợp ở PHAN_CONG_6_NGUOI.md.

## 5. Bảng hợp đồng hàm
| File / hàm | Input | Output | Có sửa trạng thái? |
|---|---|---|---|
| is_inside(pos,cols,rows) | Position, kích thước bàn | bool trong biên | Không |
| is_opposite(current,requested) | Hai hướng hợp lệ | bool đối nhau | Không |
| hits_body(pos,tail,occupied,grow) | Đầu dự kiến, đuôi hiện tại, set, bool | bool chạm thân | Không |
| Snake(body,direction) | list tọa độ, hướng | Snake mới; sai dữ liệu: ValueError | Khởi tạo |
| Snake.next_head() | direction và đầu hiện tại | Position | Không |
| Snake.would_hit_self(pos,grow) | đầu dự kiến, bool ăn táo | bool | Không |
| Snake.advance(pos,grow) | đầu hợp lệ, bool | None | body, occupied |
| spawn_apple(cols,rows,occupied,rng) | kích thước, set ô rắn, Random | Position hoặc None | Không sửa input; rng tiến trạng thái |
| GameEngine(cols,rows,seed) | số ô, seed tùy chọn | Engine mới | Khởi tạo |
| reset() | Không | None | Đưa game về trạng thái đầu |
| change_direction(direction) | một trong 4 hướng | bool nhận/từ chối; sai chuỗi: ValueError | Hướng và khóa đổi hướng nếu nhận |
| step() | Trạng thái engine hiện tại | StepResult | Theo trình tự dưới đây |
| snapshot() | Trạng thái engine | Snapshot | Không |
| SnakeApp(engine) | Engine | UI mới | Tạo cửa sổ |
| on_key(event) | Tkinter event | None | Thông qua engine |
| render(snapshot) | Snapshot | None | Chỉ UI |
| tick() / run() | Không | None | Điều phối |

### Ví dụ cụ thể
```python
# A: không ăn táo
s = Snake([(2,1),(1,1),(0,1)], 'RIGHT')
s.next_head()                         # (3,1), chưa di chuyển
s.would_hit_self((3,1), False)         # False
s.advance((3,1), False)               # None
list(s.body)                         # [(3,1),(2,1),(1,1)]
s.occupied                           # {(3,1),(2,1),(1,1)}

# B: táo nằm ngay trước đầu (trạng thái dựng riêng cho test)
game.apple = (3,1)
# Với rắn ở trạng thái ban đầu, game.step() trả:
StepResult(status='RUNNING', score=10, ate=True, reason='EAT')
# body: ((3,1),(2,1),(1,1),(0,1)); sinh táo mới ngoài thân
```
Ví dụ là kết quả yêu cầu sau triển khai, chưa chạy được với các TODO hiện tại.
Set không có thứ tự; test so sánh tập hợp, không so chuỗi in ra.

## 6. Trình tự step() bắt buộc
1. Nếu không RUNNING: trả NO_CHANGE, ate=False, giữ nguyên dữ liệu.
2. Tính next_head; grow = (next_head == apple).
3. Nếu đầu ngoài bàn: status=GAME_OVER, trả WALL; không di chuyển/tăng điểm.
4. Nếu would_hit_self(next_head,grow): status=GAME_OVER, trả SELF;
   không di chuyển/tăng điểm.
5. advance(next_head,grow). Nếu grow: cộng 10, sinh táo lại. Nếu sinh None:
   status=WON và reason=BOARD_FULL; nếu còn ô trống: reason=EAT.
   Không ăn: reason=MOVE.
6. Xóa khóa đổi hướng cho tick kế tiếp; trả StepResult theo trạng thái mới.
   Cũng xóa khóa trên nhánh kết thúc ở bước 3/4 để nhất quán.

| Tình huống | status | ate | reason | score |
|---|---|---|---|---|
| Di chuyển thường | RUNNING | False | MOVE | Giữ nguyên |
| Ăn táo, còn ô trống | RUNNING | True | EAT | +10 |
| Đụng tường | GAME_OVER | False | WALL | Giữ nguyên |
| Đụng thân | GAME_OVER | False | SELF | Giữ nguyên |
| Ăn táo cuối, kín bàn | WON | True | BOARD_FULL | +10 |
| Gọi sau khi kết thúc | Giữ nguyên | False | NO_CHANGE | Giữ nguyên |

Lưu ý quan trọng: được đi vào ô đuôi hiện tại khi KHÔNG tăng chiều dài vì đuôi
rời đi cùng tick. Khi advance, bỏ đuôi khỏi deque/set trước rồi thêm đầu mới
để không vô tình xóa ô đầu khỏi occupied.

## 7. Thứ tự làm và ghép bài
1. Cả nhóm chốt config/models/hợp đồng; giữ tên hàm và kiểu dữ liệu.
2. Người 1 làm Snake; người 2 làm rules; người 3 làm food và giữ models/config.
   Người 4 viết engine theo hợp đồng; người 5 dựng UI từ Snapshot mẫu;
   người 6 viết test từ acceptance_cases.md.
3. Ghép rules + Snake + food vào engine, chạy test logic trước; sau đó ghép UI.
4. Kiểm tra R nhiều lần, quay ngược, vào đuôi cũ, kín bàn; ghi kết quả thực tế.
5. Demo và báo cáo: mô tả bài toán, cấu trúc dữ liệu, trình tự thuật toán,
   input/output, độ phức tạp, phân công, kiểm thử và hạn chế.

## 8. Phạm vi mở rộng (chỉ sau bản chính)
Có thể thêm tự tìm đường đến táo bằng BFS với queue + visited + parent.
Đây là mở rộng riêng: đường ngắn nhất trên ảnh chụp bàn cờ chưa bảo đảm an toàn
khi thân rắn di chuyển. Không cần thêm AI để dự án cơ bản có nội dung DSA.
