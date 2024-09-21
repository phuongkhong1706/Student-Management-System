import tkinter as tk
from tkinter import ttk


# Hàm tạo giao diện và hiển thị bảng
def create_table():
    # Tạo cửa sổ tkinter
    root = tk.Tk()
    root.title("Giao diện Bảng")

    # Tạo widget Treeview
    tree = ttk.Treeview(root, columns=("ID", "Tên", "Tuổi", "Thành phố"), show="headings")

    # Đặt tên tiêu đề cho các cột
    tree.heading("ID", text="ID")
    tree.heading("Tên", text="Tên")
    tree.heading("Tuổi", text="Tuổi")
    tree.heading("Thành phố", text="Thành phố")

    # Định kích thước cho các cột
    tree.column("ID", width=50)
    tree.column("Tên", width=100)
    tree.column("Tuổi", width=50)
    tree.column("Thành phố", width=100)

    # Dữ liệu mẫu
    sample_data = [
        (1, "Nguyễn Văn A", 25, "Hà Nội"),
        (2, "Trần Thị B", 30, "Đà Nẵng"),
        (3, "Lê Văn C", 22, "Hồ Chí Minh"),
        (4, "Phạm Thị D", 28, "Cần Thơ"),
    ]

    # Thêm dữ liệu vào Treeview
    for row in sample_data:
        tree.insert("", "end", values=row)

    # Đặt Treeview vào cửa sổ
    tree.pack(expand=True, fill="both")

    # Chạy giao diện
    root.mainloop()


# Gọi hàm tạo bảng
create_table()
