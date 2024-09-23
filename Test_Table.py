import tkinter as tk

def draw_table(canvas, data, row_height, col_width):
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            x0 = j * col_width
            y0 = i * row_height
            x1 = x0 + col_width
            y1 = y0 + row_height

            # Vẽ ô
            canvas.create_rectangle(x0, y0, x1, y1, outline='black')
            # Vẽ dữ liệu trong ô
            canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=item)

root = tk.Tk()
root.title("Bảng với viền giữa các ô")

# Tạo Canvas để vẽ bảng
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# Dữ liệu mẫu
data = [
    [1, 'Nguyễn Văn A', 28],
    [2, 'Trần Thị B', 22],
    [3, 'Phạm Văn C', 25],
]

# Vẽ bảng với viền giữa các ô
draw_table(canvas, data, row_height=50, col_width=100)

root.mainloop()
