from datetime import datetime
import random
import string
from tkinter import *
import mysql.connector
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkinter import ttk, messagebox

import AD_AccessControl
import AD_DeleteAccount
import AD_History
import AD_Home
import AD_InforAccount
import AD_PassWord
import AD_ResetPassword
import ConnectionToMySQL
import History
import User

data = []


def ad_createaccount():

    # Tạo canvas và scrollbar
    canvas = Canvas(User.ad_root_homepage, borderwidth=0)
    scrollbar = Scrollbar(User.ad_root_homepage, orient=VERTICAL, command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Tạo một frame bên trong canvas với kích thước cố định
    frame_hp = Frame(canvas, width=290, height=1000, borderwidth=0, bg="#34495E")
    canvas.create_window((0, 0), window=frame_hp, anchor='nw')

    # Đặt canvas và scrollbar vào cửa sổ chính
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Ngăn frame điều chỉnh kích thước theo các widget bên trong
    frame_hp.pack_propagate(0)

    # Cập nhật kích thước canvas khi nội dung thay đổi
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_hp.bind("<Configure>", on_frame_configure)

    def create_image(file_name, x, y):
        # Mở ảnh với Pillow
        image = Image.open(file_name)

        # Thay đổi kích thước ảnh
        resized_image = image.resize((x, y))

        # Chuyển đổi ảnh sang định dạng có thể sử dụng bởi Tkinter
        photo = ImageTk.PhotoImage(resized_image)

        return photo

    image_hp = create_image("./icon/time-to-study.png",
                            120, 120)
    image_home = create_image("./icon/home.png", 45, 45)
    image_tk = create_image("./icon/user.png", 45, 45)
    image_kqht = create_image("./icon/kqht.png", 45, 45)
    image_hdnk = create_image("./icon/extraact.png", 45, 45)
    image_kehoach = create_image("./icon/learning.png", 45, 45)
    image_hocphi = create_image("./icon/tuitionfee.png", 45, 45)
    image_logout = create_image("./icon/logout.png", 45, 45)
    image_hethong = create_image("./icon/system.png", 45, 45)
    image_bt = create_image("./icon/system.png", 45, 45)

    label_hp = Label(frame_hp, width=290, height=150, image=image_hp, anchor=CENTER,
                     borderwidth=0, bg="#34495E")
    label_hp.image = image_hp
    label_hp.pack()

    def atv_ad_button_tk():
        History.save_user(User.user_input, f"Truy cập \"Tài khoản\"")

        ad_button_ht.pack_forget()
        ad_button_ht_ctk.pack_forget()
        ad_button_ht_xtk.pack_forget()
        ad_button_ht_clmk.pack_forget()
        ad_button_ht_xlshd.pack_forget()
        ad_button_ht_pq.pack_forget()
        ad_button_dx.pack_forget()
        ad_label_none.pack_forget()

        ad_button_tk_tttk.pack(anchor='w', padx=0, pady=5)
        ad_button_tk_dmk.pack(anchor='w', padx=0, pady=5)
        ad_button_ht.pack(anchor='w', padx=0, pady=5)
        ad_button_dx.pack(anchor='w', padx=0, pady=5)
        ad_label_none.pack()

    def select_homepage():
        History.save_user(User.user_input, f"Truy cập \"Trang chủ\"")
        # Xóa tất cả các widget trong root (ví dụ: User.ad_root_homepage)
        for widget in User.ad_root_homepage.winfo_children():
            widget.destroy()
        AD_Home.ad_home()

    ad_button_home = Button(frame_hp, text="    Trang chủ", font=("Arial", 14, "bold"),
                            fg="white", bg="#34495E", borderwidth=0, compound="left",
                            image=image_home, width=290, height=50, anchor="w", padx=10, command=select_homepage)
    ad_button_home.image = image_home
    ad_button_home.pack(anchor='w', padx=0, pady=5)

    ad_button_tk = Button(frame_hp, text="    Tài khoản", font=("Arial", 14, "bold"),
                          fg="white", bg="#34495E", borderwidth=0, compound="left",
                          image=image_tk, width=290, height=50, anchor="w", padx=10,
                          command=atv_ad_button_tk)
    ad_button_tk.image = image_tk
    ad_button_tk.pack(anchor='w', padx=0, pady=5)

    def select_ad_button_tk_tttk():
        History.save_user(User.user_input, "Truy cập \"Thông tin tài khoản\"")
        # Xóa tất cả các widget trong root (ví dụ: User.ad_root_homepage)
        for widget in User.ad_root_homepage.winfo_children():
            widget.destroy()
        AD_InforAccount.ad_inforaccount()

    ad_button_tk_tttk = Button(frame_hp, text="    Thông tin tài khoản", font=("Arial", 14, "bold"),
                               fg="white", bg="#34495E", borderwidth=0, compound="left",
                               width=290, height=1, anchor="w", padx=64, command=select_ad_button_tk_tttk)

    def select_ad_button_tk_dmk():
        History.save_user(User.user_input, "Truy cập \"Đổi mật khẩu\"")
        # Xóa tất cả các widget trong root (ví dụ: User.ad_root_homepage)
        for widget in User.ad_root_homepage.winfo_children():
            widget.destroy()
        AD_PassWord.ad_password()

    ad_button_tk_dmk = Button(frame_hp, text="    Đổi mật khẩu", font=("Arial", 14, "bold"),
                              fg="white", bg="#34495E", borderwidth=0, compound="left",
                              width=290, height=1, anchor="w", padx=64, command=select_ad_button_tk_dmk)

    def atv_ad_button_ht():
        History.save_user(User.user_input, "Truy cập \"Hệ thống\"")
        ad_button_tk_tttk.pack_forget()
        ad_button_tk_dmk.pack_forget()
        ad_button_dx.pack_forget()
        ad_label_none.pack_forget()

        ad_button_ht_ctk.pack(anchor='w', padx=0, pady=5)
        ad_button_ht_xtk.pack(anchor='w', padx=0, pady=5)
        ad_button_ht_clmk.pack(anchor='w', padx=0, pady=5)
        ad_button_ht_xlshd.pack(anchor='w', padx=0, pady=5)
        ad_button_ht_pq.pack(anchor='w', padx=0, pady=5)

        ad_button_dx.pack(anchor='w', padx=0, pady=5)
        ad_label_none.pack()

    ad_button_ht = Button(frame_hp, text="    Hệ thống", font=("Arial", 14, "bold"),
                          fg="white", bg="#34495E", borderwidth=0, compound="left", image=image_hethong,
                          width=290, height=50, anchor="w", padx=10, command=atv_ad_button_ht)
    ad_button_ht.image = image_hethong
    ad_button_ht.pack(anchor='w', padx=0, pady=5)

    ad_button_ht_ctk = Button(frame_hp, text="    Cấp tài khoản", font=("Arial", 14, "bold"),
                              fg="#34495E", bg="white", borderwidth=0, compound="left",
                              width=290, height=1, anchor="w", padx=64)
    ad_button_ht_ctk.pack(anchor='w', padx=0, pady=5)

    def select_ad_button_ht_xtk():
        History.save_user(User.user_input, "Truy cập \"Xóa tài khoản\"")
        # Xóa tất cả các widget trong root (ví dụ: User.ad_root_homepage)
        for widget in User.ad_root_homepage.winfo_children():
            widget.destroy()
        AD_DeleteAccount.ad_deleteaccount()

    ad_button_ht_xtk = Button(frame_hp, text="    Xóa tài khoản", font=("Arial", 14, "bold"),
                              fg="white", bg="#34495E", borderwidth=0, compound="left",
                              width=290, height=1, anchor="w", padx=64, command=select_ad_button_ht_xtk)
    ad_button_ht_xtk.pack(anchor='w', padx=0, pady=5)

    def select_ad_button_ht_clmk():
        History.save_user(User.user_input, "Truy cập \"Cấp lại mật khẩu\"")
        # Xóa tất cả các widget trong root (ví dụ: User.ad_root_homepage)
        for widget in User.ad_root_homepage.winfo_children():
            widget.destroy()
        AD_ResetPassword.ad_resetpassword()

    ad_button_ht_clmk = Button(frame_hp, text="    Cấp lại mật khẩu", font=("Arial", 14, "bold"),
                               fg="white", bg="#34495E", borderwidth=0, compound="left",
                               width=290, height=1, anchor="w", padx=64, command=select_ad_button_ht_clmk)
    ad_button_ht_clmk.pack(anchor='w', padx=0, pady=5)

    def select_ad_button_history():
        History.save_user(User.user_input, "Truy cập \"Lịch sử hoạt động\"")
        # Xóa tất cả các widget trong root (ví dụ: User.ad_root_homepage)
        for widget in User.ad_root_homepage.winfo_children():
            widget.destroy()
        AD_History.ad_history()

    ad_button_ht_xlshd = Button(frame_hp, text="    Lịch sử hoạt động", font=("Arial", 14, "bold"),
                                fg="white", bg="#34495E", borderwidth=0, compound="left",
                                width=290, height=1, anchor="w", padx=64, command=select_ad_button_history)
    ad_button_ht_xlshd.pack(anchor='w', padx=0, pady=5)

    def select_ad_access_control():
        History.save_user(User.user_input, "Truy cập \"Phân quyền\"")
        # Xóa tất cả các widget trong root (ví dụ: User.ad_root_homepage)
        for widget in User.ad_root_homepage.winfo_children():
            widget.destroy()
        AD_AccessControl.ad_accesscontrol()

    ad_button_ht_pq = Button(frame_hp, text="    Phân quyền", font=("Arial", 14, "bold"),
                             fg="white", bg="#34495E", borderwidth=0, compound="left",
                             width=290, height=1, anchor="w", padx=64, command=select_ad_access_control)
    ad_button_ht_pq.pack(anchor='w', padx=0, pady=5)
    ad_button_dx = Button(frame_hp, text="    Đăng xuất", font=("Arial", 14, "bold"),
                          fg="white", bg="#34495E", borderwidth=0, compound="left", image=image_logout,
                          width=290, height=50, anchor="w", padx=10)
    ad_button_home.image = image_logout
    ad_button_dx.pack(anchor='w', padx=0, pady=5)

    ad_label_none = Label(frame_hp, bg="#34495E", borderwidth=0, height=1000)
    ad_label_none.pack()

    ad_label = Label(User.ad_root_homepage, text="   Cấp tài khoản", fg="#34495E", font=("Arial", 16, "bold"),
                     borderwidth=0, relief=RAISED, width=81, height=2, anchor='w', bg="#DEE3EB")
    ad_label.place(x=292, y=0)

    ad_label_find = Label(User.ad_root_homepage, text="Tra cứu", font=("Arial", 14, "bold"),
                          fg="black", borderwidth=0)
    ad_label_find.place(x=310, y=80)

    ad_frame_find = Frame(User.ad_root_homepage, width=1015, height=200, borderwidth=2, relief=RAISED)
    ad_frame_find.place(x=310, y=110)

    ad_label_find_date = Label(User.ad_root_homepage, text="Ngày: ", font=("Arial", 12, "bold"),
                               fg="black", borderwidth=0)
    ad_label_find_date.place(x=350, y=140)

    ad_text_find_date = DateEntry(User.ad_root_homepage, width=20, height=2)
    ad_text_find_date.place(x=520, y=140)

    ad_label_find_moment = Label(User.ad_root_homepage, text="Thời điểm: ", font=("Arial", 12, "bold"),
                                 fg="black", borderwidth=0)
    ad_label_find_moment.place(x=850, y=140)

    # Tạo Spinbox cho giờ, phút, giây
    hour_spinbox = Spinbox(User.ad_root_homepage, from_=0, to=23, wrap=True, width=2, format="%02.0f")
    minute_spinbox = Spinbox(User.ad_root_homepage, from_=0, to=59, wrap=True, width=2, format="%02.0f")
    second_spinbox = Spinbox(User.ad_root_homepage, from_=0, to=59, wrap=True, width=2, format="%02.0f")

    # Đặt vị trí các Spinbox
    hour_spinbox.place(x=1000, y=140)
    minute_spinbox.place(x=1080, y=140)
    second_spinbox.place(x=1170, y=140)

    # Thêm nhãn chỉ dẫn (hh:mm:ss)
    Label(User.ad_root_homepage, text="Giờ", font=("Arial", 11, "bold")).place(x=1030, y=137)
    Label(User.ad_root_homepage, text="Phút", font=("Arial", 11, "bold")).place(x=1110, y=137)
    Label(User.ad_root_homepage, text="Giây", font=("Arial", 11, "bold")).place(x=1200, y=137)

    ad_label_user = Label(User.ad_root_homepage, text="Đối tượng sử dụng: ", font=("Arial", 12, "bold"),
                          fg="black", borderwidth=0)
    ad_label_user.place(x=350, y=230)

    # Tạo combo box đối tượng sử dụng
    ad_combobox_find_user_options = ["Admin", "Cán bộ phòng đào tạo",
                                     "Cán bộ phòng CTSV", "Sinh viên", "Giảng viên"]
    ad_combobox_find_user = Combobox(User.ad_root_homepage,
                                     values=ad_combobox_find_user_options, width=20, state="readonly")
    ad_combobox_find_user.set("Admin")

    ad_combobox_find_user.place(x=520, y=230)

    ad_label_find_student = Label(User.ad_root_homepage, text="MSSV / Họ và tên: ", font=("Arial", 12, "bold"),
                                  fg="black", borderwidth=0)
    ad_label_find_student.place(x=850, y=230)

    ad_text_find_student = Text(User.ad_root_homepage, width=29, height=1)
    ad_text_find_student.place(x=1000, y=230)

    ad_label_list_create = Label(User.ad_root_homepage, text="Danh sách người dùng cần tạo tài khoản",
                                 font=("Arial", 14, "bold"),
                                 fg="black", borderwidth=0)
    ad_label_list_create.place(x=310, y=350)

    # Hàm kết nối đến MySQL và lấy dữ liệu từ bảng 'list_create'
    def fetch_data_from_mysql(query, params=None):
        try:
            connection = ConnectionToMySQL.connection_to_mysql()

            # Tạo con trỏ và thực thi câu truy vấn
            cursor = connection.cursor()
            cursor.execute(query, params)  # Sử dụng params trong execute

            # Lấy tất cả các hàng dữ liệu
            rows = cursor.fetchall()

            # Đóng kết nối
            cursor.close()
            connection.close()

            return rows
        except mysql.connector.Error as error:
            print(f"Lỗi kết nối MySQL: {error}")
            return []

    # Hàm sinh mật khẩu ngẫu nhiên
    def generate_random_password(length=10):
        characters = string.digits  # Chỉ sử dụng chữ số
        return ''.join(random.choice(characters) for _ in range(length))

    # Hàm tạo bảng và chèn tài khoản vào bảng list_account
    def create_and_insert_accounts(selected_accounts):
        try:
            # Kết nối đến MySQL
            connection = ConnectionToMySQL.connection_to_mysql()
            cursor = connection.cursor()

            # Tạo bảng list_account nếu chưa tồn tại
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS list_account (
                MaTK VARCHAR(255) PRIMARY KEY,
                MatKhau VARCHAR(255)
            )
            """)

            # Chèn tài khoản đã chọn vào bảng
            for account in selected_accounts:
                password = generate_random_password()  # Sinh mật khẩu ngẫu nhiên
                cursor.execute("INSERT INTO list_account (MaTK, MatKhau) VALUES (%s, %s)", (account, password))

                # Xóa tài khoản khỏi list_create sau khi cấp tài khoản
                cursor.execute("DELETE FROM list_create WHERE MaSo = %s", (account,))

            connection.commit()  # Lưu các thay đổi
            print("Đã thêm các tài khoản vào bảng list_account và xóa khỏi list_create.")

        except mysql.connector.Error as error:
            print(f"Lỗi khi tạo bảng hoặc chèn dữ liệu: {error}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    # Khởi tạo style
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Treeview.Heading", font=("Arial", 12, "bold"),
                    background="#34495E", foreground="white")
    style.configure("Treeview", font=("Arial", 12), rowheight=25)
    style.configure("Treeview", highlightthickness=0, bd=0, font=('Arial', 12))
    style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

    query = "SELECT * from list_create"
    data = fetch_data_from_mysql(query)

    # Tạo danh sách để lưu trạng thái của các checkbox
    checked_state = [False] * len(data)

    # Các ký tự Unicode cho checkbox
    unchecked_char = '\u2610'  # '☐'
    checked_char = '\u2611'  # '☑'

    # Tạo widget Treeview với cột bổ sung cho checkbox
    tree = ttk.Treeview(User.ad_root_homepage,
                        columns=("Mã số", "Thời gian", "Đối tượng sử dụng", "Họ và tên", "Cấp tài khoản"),
                        show="headings")

    # Đặt tên tiêu đề cho các cột
    tree.heading("Mã số", text="Mã số")
    tree.heading("Thời gian", text="Thời gian")
    tree.heading("Đối tượng sử dụng", text="Đối tượng sử dụng")
    tree.heading("Họ và tên", text="Họ và tên")
    tree.heading("Cấp tài khoản", text="Cấp tài khoản")  # Di chuyển xuống cuối

    columns_width = 203
    for col in ["Mã số", "Thời gian", "Đối tượng sử dụng", "Họ và tên"]:
        tree.column(col, anchor="center", width=columns_width)

    tree.column("Cấp tài khoản", anchor="center", width=204)  # Đặt lại cột "Cấp tài khoản"

    # Thêm dữ liệu vào Treeview
    for index, row in enumerate(data):
        check = checked_char if checked_state[index] else unchecked_char
        tree.insert("", "end", values=(*row, check))  # Di chuyển checkbox xuống cuối

    # Tạo thanh cuộn dọc
    tree_scroll_vertical = Scrollbar(User.ad_root_homepage, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=tree_scroll_vertical.set)

    # Đặt vị trí Treeview và các thanh cuộn
    tree.place(x=310, y=400)
    tree_scroll_vertical.place(x=1310, y=400, height=300)

    # Hàm xử lý khi click vào Treeview
    def on_treeview_click(event):
        # Lấy vùng được click
        region = tree.identify('region', event.x, event.y)
        if region == 'cell':
            # Lấy cột được click
            column = tree.identify_column(event.x)
            if column == '#5':  # Cột '#5' là cột "Cấp tài khoản"
                # Lấy item được click
                rowid = tree.identify_row(event.y)
                if rowid:
                    index = tree.index(rowid)
                    # Thay đổi trạng thái checkbox
                    checked_state[index] = not checked_state[index]
                    # Cập nhật hiển thị
                    check = checked_char if checked_state[index] else unchecked_char
                    values = tree.item(rowid, 'values')
                    new_values = values[:-1] + (check,)  # Cập nhật cột "Cấp tài khoản"
                    tree.item(rowid, values=new_values)

    tree.bind('<Button-1>', on_treeview_click)

    # Hàm hiển thị các tài khoản đã chọn và cập nhật giao diện
    def show_selected():
        # Lấy danh sách các tài khoản đã Cấp tài khoản
        selected_accounts = [data[i][0] for i in range(len(data)) if checked_state[i]]
        for str in selected_accounts:
            History.save_user(User.user_input, f"Cấp TK cho mã TK {str}")

        # Gọi hàm tạo và chèn tài khoản vào bảng list_account
        create_and_insert_accounts(selected_accounts)

        # Cập nhật giao diện: Xóa các tài khoản đã cấp khỏi Treeview
        for i in reversed(range(len(data))):
            if checked_state[i]:  # Nếu tài khoản được chọn
                rowid = tree.get_children()[i]
                tree.delete(rowid)  # Xóa khỏi Treeview
                del data[i]  # Xóa khỏi danh sách dữ liệu
                del checked_state[i]  # Xóa trạng thái checkbox tương ứng

    def select_all():
        for i in range(len(checked_state)):
            checked_state[i] = True
            check = checked_char
            rowid = tree.get_children()[i]
            values = tree.item(rowid, 'values')
            new_values = values[:-1] + (check,)  # Cập nhật cột "Cấp tài khoản"
            tree.item(rowid, values=new_values)

    def delete_all():
        for i in range(len(checked_state)):
            checked_state[i] = False
            check = unchecked_char
            rowid = tree.get_children()[i]
            values = tree.item(rowid, 'values')
            new_values = values[:-1] + (check,)  # Cập nhật cột "Cấp tài khoản"
            tree.item(rowid, values=new_values)

    def ad_query():
        # Lấy dữ liệu từ các widget
        date = ad_text_find_date.get()  # Lấy ngày từ DateEntry
        hour = hour_spinbox.get()  # Lấy giờ từ Spinbox
        minute = minute_spinbox.get()  # Lấy phút từ Spinbox
        second = second_spinbox.get()  # Lấy giây từ Spinbox

        # Chuyển đổi định dạng ngày từ mm/dd/yy sang mm-dd-yyyy
        date_obj = datetime.strptime(date, "%m/%d/%y")  # Sử dụng %y cho năm 2 chữ số
        formatted_date = date_obj.strftime("%Y-%m-%d")  # Định dạng lại thành mm-dd-yyyy

        # Tạo chuỗi datetime
        datetime_str = f"{formatted_date} {hour}:{minute}:{second}"  # Tạo chuỗi datetime

        user_type = ad_combobox_find_user.get()  # Lấy đối tượng sử dụng từ Combobox
        student_info = ad_text_find_student.get("1.0", "end-1c").strip()  # Lấy MSSV/họ tên từ Text widget

        History.save_user(User.user_input, f"Tra cứu {datetime_str}, \n{user_type}, {student_info}")

        query = """
                SELECT MaSo, ThoiGian, DoiTuongSuDung, HoVaTen 
                FROM list_create 
                WHERE ThoiGian = %s AND DoiTuongSuDung = %s AND (MaSo = %s OR HoVaTen LIKE %s)
                """
        params = (datetime_str, user_type, student_info, f"%{student_info}%")  # Cập nhật tham số cho truy vấn
        data = fetch_data_from_mysql(query, params)  # Giả định rằng hàm này nhận params

        # Xóa tất cả các mục hiện tại trong Treeview
        for item in tree.get_children():
            tree.delete(item)

        # Thêm dữ liệu mới vào Treeview
        for index, row in enumerate(data):
            check = checked_char if checked_state[index] else unchecked_char
            tree.insert("", "end", values=(*row, check))  # Thêm dữ liệu mới

        # Điều chỉnh kích thước Treeview
        max_visible_rows = 10  # Số dòng tối đa mà bạn muốn hiển thị
        row_count = len(data)  # Đếm số dòng trả về

        # Nếu số dòng trả về nhỏ hơn max_visible_rows, điều chỉnh kích thước Treeview
        if row_count < max_visible_rows:
            tree.config(height=row_count)  # Đặt chiều cao tương ứng với số dòng trả về
        else:
            tree.config(
                height=max_visible_rows)  # Giữ kích thước tối đa nếu số dòng trả về lớn hơn hoặc bằng max_visible_rows

    ad_button_find = Button(User.ad_root_homepage, text="Tìm kiếm", font=("Arial", 12, "bold"),
                            fg="white",
                            bg="#34495E", command=ad_query)
    ad_button_find.place(x=1241, y=275)

    ad_button_select_all = Button(User.ad_root_homepage, text="Chọn tất cả", font=("Arial", 12, "bold"),
                                  fg="white",
                                  bg="#34495E", command=select_all)
    ad_button_select_all.place(x=1095, y=350)

    ad_button_delete_all = Button(User.ad_root_homepage, text="Bỏ chọn tất cả", font=("Arial", 12, "bold"),
                                  fg="white",
                                  bg="#34495E", command=delete_all)
    ad_button_delete_all.place(x=1200, y=350)

    ad_button_delete_account = Button(User.ad_root_homepage, text="Cấp tài khoản", font=("Arial", 12, "bold"),
                                      fg="white",
                                      bg="#34495E", command=show_selected)
    ad_button_delete_account.place(x=1205, y=700)
    User.ad_root_homepage.mainloop()