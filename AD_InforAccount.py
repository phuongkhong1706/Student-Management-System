from tkinter import *
from tkinter import messagebox

import mysql
from PIL import Image, ImageTk
from tkcalendar import DateEntry

import AD_AccessControl
import AD_CreateAccount
import AD_DeleteAccount
import AD_History
import AD_Home
import AD_PassWord
import AD_ResetPassword
import ConnectionToMySQL
import History
import User


def ad_inforaccount():

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

    label_hp = Label(frame_hp, width=200, height=150, image=image_hp, anchor=CENTER,
                     borderwidth=0, bg="#34495E")
    label_hp.image = image_hp
    label_hp.pack()

    def atv_ad_button_tk():
        History.save_user(User.user_input, "Truy cập \"Tài khoản\"")
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
        History.save_user(User.user_input, "Truy cập \"Trang chủ\"")
        # Xóa tất cả các widget trong root (ví dụ: User.ad_root_homepage)
        for widget in User.ad_root_homepage.winfo_children():
            widget.destroy()
        AD_Home.ad_home()

    ad_button_home = Button(frame_hp, text="    Trang chủ", font=("Arial", 14, "bold"),
                            fg="white", bg="#34495E", borderwidth=0, compound="left",
                            image=image_home, width=290, height=50, anchor="w", padx=10,
                            command=select_homepage)
    ad_button_home.image = image_home
    ad_button_home.pack(anchor='w', padx=0, pady=5)

    ad_button_tk = Button(frame_hp, text="    Tài khoản", font=("Arial", 14, "bold"),
                          fg="white", bg="#34495E", borderwidth=0, compound="left",
                          image=image_tk, width=290, height=50, anchor="w", padx=10,
                          command=atv_ad_button_tk)
    ad_button_tk.pack(anchor='w', padx=0, pady=5)

    ad_button_tk_tttk = Button(frame_hp, text="    Thông tin tài khoản", font=("Arial", 14, "bold"),
                               fg="#34495E", bg="white", borderwidth=0, compound="left",
                               width=290, height=1, anchor="w", padx=64)
    ad_button_tk_tttk.pack(anchor='w', padx=0, pady=5)

    def select_ad_button_tk_dmk():
        History.save_user(User.user_input, "Truy cập \"Đổi mật khẩu\"")
        # Xóa tất cả các widget trong root (ví dụ: User.ad_root_homepage)
        for widget in User.ad_root_homepage.winfo_children():
            widget.destroy()
        AD_PassWord.ad_password()

    ad_button_tk_dmk = Button(frame_hp, text="    Đổi mật khẩu", font=("Arial", 14, "bold"),
                              fg="white", bg="#34495E", borderwidth=0, compound="left",
                              width=290, height=1, anchor="w", padx=64, command=select_ad_button_tk_dmk)
    ad_button_tk_dmk.pack(anchor='w', padx=0, pady=5)

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

    def select_ad_button_ht_ctk():
        History.save_user(User.user_input, "Truy cập \"Cấp tài khoản\"")
        # Xóa tất cả các widget trong root (ví dụ: User.ad_root_homepage)
        for widget in User.ad_root_homepage.winfo_children():
            widget.destroy()
        AD_CreateAccount.ad_createaccount()

    ad_button_ht_ctk = Button(frame_hp, text="    Cấp tài khoản", font=("Arial", 14, "bold"),
                              fg="white", bg="#34495E", borderwidth=0, compound="left",
                              width=290, height=1, anchor="w", padx=64, command=select_ad_button_ht_ctk)

    def select_ad_button_ht_xtk():
        History.save_user(User.user_input, "Truy cập \"Xoá tài khoản\"")
        # Xóa tất cả các widget trong root (ví dụ: User.ad_root_homepage)
        for widget in User.ad_root_homepage.winfo_children():
            widget.destroy()
        AD_DeleteAccount.ad_deleteaccount()

    ad_button_ht_xtk = Button(frame_hp, text="    Xóa tài khoản", font=("Arial", 14, "bold"),
                              fg="white", bg="#34495E", borderwidth=0, compound="left",
                              width=290, height=1, anchor="w", padx=64, command=select_ad_button_ht_xtk)

    def select_ad_button_ht_clmk():
        History.save_user(User.user_input, "Truy cập \"Cấp lại mật khẩu\"")
        # Xóa tất cả các widget trong root (ví dụ: User.ad_root_homepage)
        for widget in User.ad_root_homepage.winfo_children():
            widget.destroy()
        AD_ResetPassword.ad_resetpassword()

    ad_button_ht_clmk = Button(frame_hp, text="    Cấp lại mật khẩu", font=("Arial", 14, "bold"),
                               fg="white", bg="#34495E", borderwidth=0, compound="left",
                               width=290, height=1, anchor="w", padx=64, command=select_ad_button_ht_clmk)

    def select_ad_button_history():
        History.save_user(User.user_input, "Truy cập \"Lịch sử hoạt động\"")
        # Xóa tất cả các widget trong root (ví dụ: User.ad_root_homepage)
        for widget in User.ad_root_homepage.winfo_children():
            widget.destroy()
        AD_History.ad_history()

    ad_button_ht_xlshd = Button(frame_hp, text="    Lịch sử hoạt động", font=("Arial", 14, "bold"),
                                fg="white", bg="#34495E", borderwidth=0, compound="left",
                                width=290, height=1, anchor="w", padx=64, command=select_ad_button_history)

    def select_ad_access_control():
        History.save_user(User.user_input, "Truy cập \"Phân quyền\"")
        # Xóa tất cả các widget trong root (ví dụ: User.ad_root_homepage)
        for widget in User.ad_root_homepage.winfo_children():
            widget.destroy()
        AD_AccessControl.ad_accesscontrol()

    ad_button_ht_pq = Button(frame_hp, text="    Phân quyền", font=("Arial", 14, "bold"),
                             fg="white", bg="#34495E", borderwidth=0, compound="left",
                             width=290, height=1, anchor="w", padx=64, command=select_ad_access_control)

    ad_button_dx = Button(frame_hp, text="    Đăng xuất", font=("Arial", 14, "bold"),
                          fg="white", bg="#34495E", borderwidth=0, compound="left", image=image_logout,
                          width=290, height=50, anchor="w", padx=10)
    ad_button_dx.image = image_logout
    ad_button_dx.pack(anchor='w', padx=0, pady=5)

    ad_label_none = Label(frame_hp, bg="#34495E", borderwidth=0, height=1000)
    ad_label_none.pack()

    ad_label = Label(User.ad_root_homepage, text="   Thông tin tài khoản", fg="#34495E", font=("Arial", 16, "bold"),
                     borderwidth=0, relief=RAISED, width=81, height=2, anchor='w', bg="#DEE3EB")
    ad_label.place(x=292, y=0)

    ad_label_matk = Label(User.ad_root_homepage, text="Mã tài khoản", fg="#34495E", font=("Arial", 12, "bold"),
                          borderwidth=0, width=10, height=1, anchor='w')
    ad_label_matk.place(x=450, y=175)

    ad_text_matk = Text(User.ad_root_homepage, borderwidth=2, relief=RAISED, width=70, height=1)
    ad_text_matk.place(x=600, y=173)

    ad_label_ht = Label(User.ad_root_homepage, text="Họ và tên", fg="#34495E", font=("Arial", 12, "bold"),
                        borderwidth=0, width=10, height=1, anchor='w')
    ad_label_ht.place(x=450, y=235)

    ad_text_ht = Text(User.ad_root_homepage, borderwidth=2, relief=RAISED, width=70, height=1)
    ad_text_ht.place(x=600, y=233)

    ad_label_ns = Label(User.ad_root_homepage, text="Ngày sinh", fg="#34495E", font=("Arial", 12, "bold"),
                        borderwidth=0, width=10, height=1, anchor='w')
    ad_label_ns.place(x=450, y=295)

    ad_text_ns = DateEntry(User.ad_root_homepage, borderwidth=2, relief=RAISED, width=90, height=2)
    ad_text_ns.place(x=600, y=293)

    ad_label_qq = Label(User.ad_root_homepage, text="Quê quán", fg="#34495E", font=("Arial", 12, "bold"),
                        borderwidth=0, width=10, height=1, anchor='w')
    ad_label_qq.place(x=450, y=355)

    ad_text_qq = Text(User.ad_root_homepage, borderwidth=2, relief=RAISED, width=70, height=1)
    ad_text_qq.place(x=600, y=353)

    ad_label_sodt = Label(User.ad_root_homepage, text="Số điện thoại", fg="#34495E", font=("Arial", 12, "bold"),
                          borderwidth=0, width=10, height=1, anchor='w')
    ad_label_sodt.place(x=450, y=415)

    ad_text_sodt = Text(User.ad_root_homepage, borderwidth=2, relief=RAISED, width=70, height=1)
    ad_text_sodt.place(x=600, y=413)

    ad_label_cccd = Label(User.ad_root_homepage, text="CMT / CCCD", fg="#34495E", font=("Arial", 12, "bold"),
                          borderwidth=0, width=10, height=1, anchor='w')
    ad_label_cccd.place(x=450, y=475)

    ad_text_cccd = Text(User.ad_root_homepage, borderwidth=2, relief=RAISED, width=70, height=1)
    ad_text_cccd.place(x=600, y=473)

    # Kết nối với cơ sở dữ liệu MySQL
    def get_user_data(user_input):
        try:
            connection = ConnectionToMySQL.connection_to_mysql()
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM user_information WHERE MaSo = %s"
            cursor.execute(query, (user_input,))
            user_data = cursor.fetchone()
            return user_data
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    # Hàm để bật/tắt chỉnh sửa các widget
    def enable_widgets(state):
        ad_text_matk.config(state=state)
        ad_text_ht.config(state=state)
        ad_text_ns.config(state=state)
        ad_text_qq.config(state=state)
        ad_text_sodt.config(state=state)
        ad_text_cccd.config(state=state)

    # Hàm để hiển thị dữ liệu người dùng
    def display_user_data(user_data):
        if user_data:
            ad_text_matk.insert(END, user_data['MaSo'])
            ad_text_ht.insert(END, user_data['HoVaTen'])
            ad_text_ns.set_date(user_data['NgaySinh'])
            ad_text_qq.insert(END, user_data['QueQuan'])
            ad_text_sodt.insert(END, user_data['SoDienThoai'])
            ad_text_cccd.insert(END, user_data['CMT_CCCD'])

    # Hàm cập nhật thông tin người dùng
    def update_user_data():
        enable_widgets(NORMAL)
        ad_text_matk.config(state=DISABLED)

    ad_button_capnhat = Button(User.ad_root_homepage, text="Cập nhật thông tin", fg="#34495E",
                               font=("Arial", 10, "bold"),
                               borderwidth=2, relief=RAISED, width=15, height=1, anchor=CENTER, bg="white",
                               command=update_user_data)

    ad_button_capnhat.place(x=940, y=535)

    # Lấy mã tài khoản từ input của người dùng (ví dụ)
    user_data = get_user_data(User.user_input)

    # Hiển thị dữ liệu người dùng
    display_user_data(user_data)

    # Không cho phép chỉnh sửa các widget
    enable_widgets(DISABLED)


    # Hàm lưu dữ liệu sau khi nhấn nút "Lưu"
    def save_user_data(user_input):
        try:
            History.save_user(User.user_input, "Cập nhật thông tin cá nhân")
            # Không cho phép chỉnh sửa các widget
            enable_widgets(DISABLED)
            connection = ConnectionToMySQL.connection_to_mysql()
            cursor = connection.cursor()

            # Lấy giá trị từ các widget
            maso = ad_text_matk.get("1.0", END).strip()
            hovaten = ad_text_ht.get("1.0", END).strip()
            ngaysinh = ad_text_ns.get_date()
            quequan = ad_text_qq.get("1.0", END).strip()
            sodienthoai = ad_text_sodt.get("1.0", END).strip()
            cmt_cccd = ad_text_cccd.get("1.0", END).strip()

            # Câu lệnh cập nhật
            update_query = """
            UPDATE user_information
            SET HoVaTen = %s, NgaySinh = %s, QueQuan = %s, SoDienThoai = %s, CMT_CCCD = %s
            WHERE MaSo = %s
            """
            cursor.execute(update_query, (hovaten, ngaysinh, quequan, sodienthoai, cmt_cccd, user_input))

            # Xác nhận thay đổi
            connection.commit()
            print("Dữ liệu đã được cập nhật thành công!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def confirm_save():
        # Hiển thị hộp thoại xác nhận với Yes/No
        result = messagebox.askyesno("Xác nhận", "Bạn có muốn lưu thay đổi?")

        if result:  # Nếu người dùng chọn Yes
            save_user_data(User.user_input)  # Gọi hàm lưu thông tin
            messagebox.showinfo("Thông báo", "Cập nhật thông tin thành công")  # Hiển thị thông báo thành công
        # Nếu người dùng chọn No, không làm gì cả

    def event_save():
        save_user_data(User.user_input)
        confirm_save()

    ad_button_luu = Button(User.ad_root_homepage, text="Lưu", fg="#34495E", font=("Arial", 10, "bold"),
                           borderwidth=2, relief=RAISED, width=6, height=1, anchor=CENTER, bg="white",
                           command=event_save)

    ad_button_luu.place(x=1107, y=535)

    User.ad_root_homepage.mainloop()
