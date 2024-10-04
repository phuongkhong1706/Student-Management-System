import tkinter as tk
from tkinter import font

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Vẽ bảng với ô tự động mở rộng theo kích thước chữ")

# Dữ liệu bảng
data = [
    ["ID", "Tên", "Tuổi", "Địa chỉ"],
    [1, "Alice", 24, "Hà Nội"],
    [2, "Bob", 30, "Hồ Chí Minhhhhhhhhhhhhhhhhhhhhhhhhhhhh"],
    [3, "Charlie", 22, "Đà Nẵng"],
    [4, "David", 28, "Cần Thơ"]
]

# Tạo font chữ để đo kích thước
canvas_font = font.Font(family="Arial", size=12)


# Đo kích thước chữ lớn nhất trong từng cột
def calculate_column_widths(data, canvas_font):
    column_widths = []
    for col in range(len(data[0])):  # Duyệt qua tất cả các cột
        max_width = 0
        for row in range(len(data)):  # Duyệt qua từng hàng để tìm độ rộng lớn nhất của mỗi cột
            text_width = canvas_font.measure(str(data[row][col]))
            if text_width > max_width:
                max_width = text_width
        column_widths.append(max_width + 20)  # Thêm một khoảng cách padding
    return column_widths


# Tính toán kích thước của từng cột
column_widths = calculate_column_widths(data, canvas_font)
cell_height = 40  # Chiều cao của mỗi ô

# Tính tổng chiều rộng và chiều cao
total_width = sum(column_widths)
total_height = len(data) * cell_height

# Tạo Canvas
canvas = tk.Canvas(root, width=total_width, height=total_height)
canvas.pack()

# Vẽ các ô của bảng
for row in range(len(data)):
    for col in range(len(data[0])):
        x1 = sum(column_widths[:col])
        y1 = row * cell_height
        x2 = x1 + column_widths[col]
        y2 = y1 + cell_height

        # Vẽ hình chữ nhật cho mỗi ô
        canvas.create_rectangle(x1, y1, x2, y2)

        # Chèn chữ vào giữa ô
        canvas.create_text(x1 + column_widths[col] // 2, y1 + cell_height // 2,
                           text=str(data[row][col]), font=canvas_font)

# Chạy vòng lặp chính của Tkinter
root.mainloop()
