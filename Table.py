import tkinter as tk
from tkinter import ttk
from tkinter import *
def toggle_checkbutton(index):
    # Chức năng thay đổi trạng thái của Checkbutton
    current_value = check_vars[index].get()
    check_vars[index].set(not current_value)

def on_double_click(event):
    # Lấy chỉ số hàng được nhấp đúp
    item = tree.selection()[0]
    index = tree.index(item)
    toggle_checkbutton(index)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Bảng với Checkbutton")

# Tạo widget Treeview
tree = ttk.Treeview(root,
                    columns=("Thời gian", "Đối tượng sử dụng", "Mã số", "Họ và tên", "Cấp tài khoản"),
                    show="headings")

# Đặt tên tiêu đề cho các cột
tree.heading("Thời gian", text="Thời gian")
tree.heading("Đối tượng sử dụng", text="Đối tượng sử dụng")
tree.heading("Mã số", text="Mã số")
tree.heading("Họ và tên", text="Họ và tên")
tree.heading("Cấp tài khoản", text="Cấp tài khoản")

# Định kích thước và căn giữa các cột
columns_width = 203
for col in ["Thời gian", "Đối tượng sử dụng", "Mã số", "Họ và tên", "Cấp tài khoản"]:
    tree.column(col, anchor="center", width=columns_width)

# Dữ liệu mẫu
sample_data = [
    ("08:00", "Nguyễn Văn A", "001", "Nguyễn Văn A", "Admin"),
    ("09:00", "Trần Thị B", "002", "Trần Thị B", "User"),
    ("10:00", "Lê Văn C", "003", "Lê Văn C", "User"),
    ("11:01", "Phạm Thị D", "004", "Phạm Thị D", "User"),
]

# Thêm dữ liệu vào Treeview
for row in sample_data:
    tree.insert("", "end", values=row)

# Đặt Treeview vào cửa sổ
tree.place(x=50, y=50)

# Tạo biến cho các Checkbutton
check_vars = [tk.BooleanVar() for _ in sample_data]

# Thêm Checkbutton bên cạnh Treeview
for index in range(len(sample_data)):
    checkbutton = tk.Checkbutton(root, variable=check_vars[index])
    checkbutton.place(x=columns_width + 60, y=70 + index * 25)

# Gán sự kiện nhấp đúp chuột
tree.bind("<Double-1>", on_double_click)

def print_value():
    for item in check_vars:
        print(item.get())

button = Button(root, text="Click", command=print_value)
button.pack()
# Chạy vòng lặp chính
root.mainloop()
