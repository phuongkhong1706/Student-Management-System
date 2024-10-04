import mysql.connector
from tkinter import Tk, BooleanVar, Checkbutton, Button
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

# Khởi tạo giao diện
ad_root_createaccount = Tk()
ad_root_createaccount.title("Quản lý tài khoản")
ad_root_createaccount.geometry("1300x800")

# Khởi tạo style
style = ttk.Style()
style.theme_use('clam')

# Đặt tên style cho tiêu đề cột với nền xanh dương và chữ trắng
style.configure("Treeview.Heading", font=("Arial", 12, "bold"),
                background="#34495E", foreground="white")

# Đặt style cho các hàng với cỡ chữ
style.configure("Treeview", font=("Arial", 12), rowheight=25)

# Lấy dữ liệu từ MySQL
data = fetch_data_from_mysql()

# Tạo Frame để chứa Treeview và Checkbuttons
frame = ttk.Frame(ad_root_createaccount)
frame.place(x=310, y=400)

# Tạo widget Treeview
tree = ttk.Treeview(frame,
                    columns=("Thời gian", "Đối tượng sử dụng", "Mã số", "Họ và tên", "Cấp tài khoản"),
                    show="headings", height=5)  # Height là số hàng hiển thị

# Đặt tên tiêu đề cho các cột
tree.heading("Thời gian", text="Thời gian")
tree.heading("Đối tượng sử dụng", text="Đối tượng sử dụng")
tree.heading("Mã số", text="Mã số")
tree.heading("Họ và tên", text="Họ và tên")
tree.heading("Cấp tài khoản", text="Cấp tài khoản")

# Điều chỉnh chiều rộng của các cột
columns_width = 203
for col in ["Thời gian", "Đối tượng sử dụng", "Mã số", "Họ và tên", "Cấp tài khoản"]:
    tree.column(col, anchor="center", width=columns_width)

# Thêm dữ liệu vào Treeview
for row in data:
    tree.insert("", "end", values=row)

# Đặt Treeview vào cửa sổ
tree.grid(row=0, column=0, sticky="nsew")

# Tạo biến cho các Checkbutton
check_vars = [BooleanVar() for _ in data]

# Tạo Frame để chứa các Checkbuttons
checkbutton_frame = ttk.Frame(frame)
checkbutton_frame.grid(row=0, column=1, sticky="ns")

# Thêm Scrollbar
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scrollbar.grid(row=0, column=2, sticky="ns")
tree.configure(yscrollcommand=scrollbar.set)

# Thêm Checkbutton bên cạnh mỗi hàng của Treeview
checkbuttons = []
for index, var in enumerate(check_vars):
    checkbutton = Checkbutton(checkbutton_frame, variable=var)
    checkbutton.grid(row=index, column=0, pady=1, padx=5, sticky="w")
    checkbuttons.append(checkbutton)

# Hàm cập nhật hiển thị các Checkbutton khi cuộn
def update_checkbuttons(*args):
    # Tính toán tỷ lệ cuộn hiện tại (vị trí cuộn và tầm nhìn của treeview)
    yview = tree.yview()

    # Tính toán số hàng đầu tiên và cuối cùng đang hiển thị dựa trên yview
    first_row = int(len(data) * yview[0])
    last_row = int(len(data) * yview[1])

    # Cập nhật hiển thị của các checkbuttons
    for i in range(len(checkbuttons)):
        if first_row <= i <= last_row:
            checkbuttons[i].grid(row=i, column=0, pady=1, padx=5, sticky="w")
        else:
            checkbuttons[i].grid_remove()

# Ràng buộc sự kiện thay đổi vị trí của thanh cuộn để cập nhật Checkbutton
def on_scroll(*args):
    tree.yview(*args)
    update_checkbuttons()

scrollbar.config(command=on_scroll)

# Ràng buộc các sự kiện cuộn để cập nhật Checkbutton
tree.bind("<MouseWheel>", update_checkbuttons)
tree.bind("<ButtonRelease-1>", update_checkbuttons)
tree.bind("<Configure>", update_checkbuttons)

# Hiển thị ban đầu
update_checkbuttons()

# Hàm hiển thị tài khoản đã chọn
def show_selected():
    selected_accounts = [data[i][1] for i in range(len(data)) if check_vars[i].get()]
    print("Tài khoản đã chọn:", selected_accounts)

# Hàm chọn tất cả Checkbutton
def select_all():
    for var in check_vars:
        var.set(True)
    update_checkbuttons()

# Hàm bỏ chọn tất cả Checkbutton
def delete_all():
    for var in check_vars:
        var.set(False)
    update_checkbuttons()

# Nút chọn tất cả
ad_button_select_all = Button(ad_root_createaccount, text="Chọn tất cả", font=("Arial", 12, "bold"), fg="white",
                              bg="#34495E", command=select_all)
ad_button_select_all.place(x=1095, y=350)

# Nút bỏ chọn tất cả
ad_button_delete_all = Button(ad_root_createaccount, text="Bỏ chọn tất cả", font=("Arial", 12, "bold"), fg="white",
                              bg="#34495E", command=delete_all)
ad_button_delete_all.place(x=1200, y=350)

# Nút cấp tài khoản
ad_button_delete_account = Button(ad_root_createaccount, text="Cấp tài khoản", font=("Arial", 12, "bold"),
                                  fg="white", bg="#34495E", command=show_selected)
ad_button_delete_account.place(x=1205, y=700)

ad_root_createaccount.mainloop()
