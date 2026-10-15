# Bộ ca nghiệm thu — thành viên D

Đây là đặc tả kiểm thử, chưa phải kết quả đã chạy. Khi viết test dùng unittest;
logic không import Tkinter. Mỗi ca tạo trạng thái riêng. Test được quyền thiết
lập snake, apple, score, status để tạo tình huống; UI không được quyền đó.

| ID | Thiết lập / input | Kết quả mong đợi |
|---|---|---|
| T01 | reset trên bàn 20x15 | body=((2,1),(1,1),(0,1)); RIGHT; 0; RUNNING; táo ngoài rắn |
| T02 | body T01, apple=(8,8), step | body=((3,1),(2,1),(1,1)); điểm 0; MOVE |
| T03 | body T01, apple=(3,1), step | body=((3,1),(2,1),(1,1),(0,1)); điểm 10; EAT; táo mới ngoài rắn |
| T04 | body=((19,1),(18,1),(17,1)), RIGHT, step | GAME_OVER/WALL; body, táo, điểm không đổi |
| T05 | body=((2,1),(2,2),(1,2),(1,1),(1,0)), UP; nhận LEFT; step | đầu mới (1,1) chạm thân: GAME_OVER/SELF; body không đổi |
| T06 | body=((1,1),(1,2),(0,2),(0,1)), UP; nhận LEFT; apple=(3,3); step trên bàn 4x4 | đầu vào đuôi cũ (0,1) hợp lệ; body=((0,1),(1,1),(1,2),(0,2)); MOVE |
| T07 | đang RIGHT; change_direction(LEFT) | False; vẫn RIGHT |
| T08 | đang RIGHT; nhận UP rồi LEFT trước step | True rồi False; tick đi UP; sau tick được đổi hướng tiếp |
| T09 | change_direction('DIAGONAL') | ValueError; trạng thái không đổi |
| T10 | spawn_apple(2,2,{(0,0),(1,0),(0,1)},rng) | (1,1) |
| T11 | spawn_apple(2,2, toàn bộ 4 ô,rng) | None |
| T12 | bàn 4x3; body=((2,0),(1,0),(0,0),(0,1),(1,1),(2,1),(3,1),(3,2),(2,2),(1,2),(0,2)); RIGHT; táo=(3,0); điểm 80; step | dài 12; điểm 90; apple=None; WON/BOARD_FULL; ate=True |
| T13 | status GAME_OVER hoặc WON; step | NO_CHANGE; ate=False; body/táo/điểm/trạng thái giữ nguyên |
| T14 | reset sau chết | giống T01; điểm 0; xóa khóa đổi hướng; không có nhiều vòng tick |
| T15 | snapshot rồi engine di chuyển | snapshot cũ không đổi |
| T16 | Snake có ô trùng, ô không liên tiếp, hoặc hướng trái với đầu | ValueError |

Sau mỗi lần di chuyển hợp lệ: set(body)==occupied, len(body)==len(occupied),
không ô nào ngoài bàn, apple không thuộc occupied nếu apple khác None.
UI kiểm tra thủ công: mũi tên, R, Escape, điểm, thông báo thua/thắng,
không tăng tốc ngoài ý muốn sau khi nhấn R nhiều lần.
