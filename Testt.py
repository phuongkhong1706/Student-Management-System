import mysql.connector
from tkinter import *
from tkinter import ttk


# Hàm kết nối đến MySQL và lấy dữ liệu từ bảng 'list_create'
def fetch_data_from_mysql():
    try:
        # Kết nối đến MySQL
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='dotrungquan183@',  # Đặt mật khẩu của bạn
            database='student_management'  # Tên database
        )

        # Tạo con trỏ và thực thi câu truy vấn
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM list_create")

        # Lấy tất cả các hàng dữ liệu
        rows = cursor.fetchall()

        # Đóng kết nối
        cursor.close()
        connection.close()

        return rows
    except mysql.connector.Error as error:
        print(f"Lỗi kết nối MySQL: {error}")
        return []


# Hàm để hiển thị dữ liệu vào Treeview
def display_data_in_treeview():
    # Lấy dữ liệu từ MySQL
    data = fetch_data_from_mysql()

    # Xóa dữ liệu hiện tại trong Treeview
    for row in tree.get_children():
        tree.delete(row)

    # Thêm dữ liệu mới từ MySQL vào Treeview
    for row in data:
        tree.insert("", "end", values=row)


# Tạo cửa sổ giao diện chính
ad_root_createaccount = Tk()
ad_root_createaccount.title("Quản lý tài khoản")
ad_root_createaccount.geometry("1300x800")

# Khởi tạo style
style = ttk.Style()
style.theme_use('clam')
style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#34495E", foreground="white")
style.configure("Treeview", font=("Arial", 12), rowheight=25)

# Tạo widget Treeview
tree = ttk.Treeview(ad_root_createaccount,
                    columns=("Thời gian", "Đối tượng sử dụng", "Mã số", "Họ và tên", "Cấp tài khoản"),
                    show="headings")

# Đặt tên tiêu đề cho các cột
tree.heading("Thời gian", text="Thời gian")
tree.heading("Đối tượng sử dụng", text="Đối tượng sử dụng")
tree.heading("Mã số", text="Mã số")
tree.heading("Họ và tên", text="Họ và tên")
tree.heading("Cấp tài khoản", text="Cấp tài khoản")

# Đặt độ rộng cho các cột
columns_width = 203
for col in ["Thời gian", "Đối tượng sử dụng", "Mã số", "Họ và tên", "Cấp tài khoản"]:
    tree.column(col, anchor="center", width=columns_width)

# Đặt Treeview vào cửa sổ
tree.place(x=310, y=100)

# Gọi hàm hiển thị dữ liệu từ MySQL vào Treeview
display_data_in_treeview()

# Chạy vòng lặp chính của giao diện
ad_root_createaccount.mainloop()
