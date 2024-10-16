from tkinter import *

from tkcalendar import DateEntry
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkinter import ttk

import AD_AccessControl
import AD_CreateAccount
import AD_DeleteAccount
import AD_History
import AD_Home
import AD_InforAccount
import AD_PassWord
import History
import User


def ad_resetpassword():
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

    # điều chỉnh button
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

    def select_ad_button_ht_ctk():
        History.save_user(User.user_input, "Truy cập \"Cấp tài khoản\"")
        # Xóa tất cả các widget trong root (ví dụ: User.ad_root_homepage)
        for widget in User.ad_root_homepage.winfo_children():
            widget.destroy()
        AD_CreateAccount.ad_createaccount()

    ad_button_ht_ctk = Button(frame_hp, text="    Cấp tài khoản", font=("Arial", 14, "bold"),
                              fg="white", bg="#34495E", borderwidth=0, compound="left",
                              width=290, height=1, anchor="w", padx=64, command=select_ad_button_ht_ctk)
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
    ad_button_ht_clmk = Button(frame_hp, text="    Cấp lại mật khẩu", font=("Arial", 14, "bold"),
                               fg="#34495E", bg="white", borderwidth=0, compound="left",
                               width=290, height=1, anchor="w", padx=64)
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
    ad_button_dx.image = image_logout
    ad_button_dx.pack(anchor='w', padx=0, pady=5)

    ad_label_none = Label(frame_hp, bg="#34495E", borderwidth=0, height=1000)
    ad_label_none.pack()

    ad_label = Label(User.ad_root_homepage, text="   Cấp lại mật khẩu", fg="#34495E", font=("Arial", 16, "bold"),
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
    ad_combobox_find_user_options = ["Quản trị viên", "Cán bộ phòng đào tạo",
                                     "Cán bộ phòng CTSV", "Sinh viên", "Giảng viên"]
    ad_combobox_find_user = Combobox(User.ad_root_homepage,
                                     values=ad_combobox_find_user_options, width=20, state="readonly")
    ad_combobox_find_user.set("Quản trị viên")

    ad_combobox_find_user.place(x=520, y=230)

    ad_label_find_student = Label(User.ad_root_homepage, text="MSSV / Họ và tên: ", font=("Arial", 12, "bold"),
                                  fg="black", borderwidth=0)
    ad_label_find_student.place(x=850, y=230)

    ad_text_find_student = Text(User.ad_root_homepage, width=29, height=1)
    ad_text_find_student.place(x=1000, y=230)

    ad_label_list_create = Label(User.ad_root_homepage, text="Danh sách người dùng cần cấp lại mật khẩu",
                                 font=("Arial", 14, "bold"),
                                 fg="black", borderwidth=0)
    ad_label_list_create.place(x=310, y=350)

    # Khởi tạo style
    style = ttk.Style()

    # Sử dụng theme 'clam' để hỗ trợ thay đổi màu nền tiêu đề
    style.theme_use('clam')

    # Đặt tên style cho tiêu đề cột với nền xanh dương và chữ trắng
    style.configure("Treeview.Heading", font=("Arial", 12, "bold"),
                    background="#34495E", foreground="white")

    # Đặt style cho các hàng với cỡ chữ
    style.configure("Treeview", font=("Arial", 12), rowheight=25)

    # Hiển thị đường kẻ giữa các hàng và cột
    style.configure("Treeview", highlightthickness=0, bd=0, font=('Arial', 12))
    style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

    def show_selected():
        # Lấy danh sách các tài khoản đã chọn
        selected_accounts = [data[i][1] for i in range(len(data)) if check_vars[i].get()]
        print("Tài khoản đã chọn:", selected_accounts)

    # Tạo widget Treeview
    tree = ttk.Treeview(User.ad_root_homepage,
                        columns=("Thời gian", "Đối tượng sử dụng", "Mã số", "Họ và tên", "Cấp lại mật khẩu"),
                        show="headings")

    # Đặt tên tiêu đề cho các cột
    tree.heading("Thời gian", text="Thời gian")
    tree.heading("Đối tượng sử dụng", text="Đối tượng sử dụng")
    tree.heading("Mã số", text="Mã số")
    tree.heading("Họ và tên", text="Họ và tên")
    tree.heading("Cấp lại mật khẩu", text="Cấp lại mật khẩu")
    columns_width = 203
    for col in ["Thời gian", "Đối tượng sử dụng", "Mã số", "Họ và tên", "Cấp lại mật khẩu"]:
        tree.column(col, anchor="center", width=columns_width)

    # Dữ liệu mẫu
    data = [
        ("08:00", "Nguyễn Văn A", "001", "Nguyễn Văn A"),
        ("09:00", "Trần Thị B", "002", "Trần Thị B"),
        ("10:00", "Lê Văn C", "003", "Lê Văn C"),
        ("11:01", "Phạm Thị D", "004", "Phạm Thị D"),
        ("11:01", "Phạm Thị D", "004", "Phạm Thị D"),
        ("11:01", "Phạm Thị D", "004", "Phạm Thị D")
    ]

    # Thêm dữ liệu vào Treeview
    for row in data:
        tree.insert("", "end", values=row)

    # Đặt Treeview vào cửa sổ
    tree.place(x=310, y=400)

    # Tạo biến cho các Checkbutton
    check_vars = [BooleanVar() for _ in data]

    # Thêm Checkbutton bên cạnh Treeview
    for index in range(len(data)):
        checkbutton = Checkbutton(User.ad_root_homepage, variable=check_vars[index])
        checkbutton.place(x=columns_width + 1000, y=430 + index * 25)

    def select_all():
        # Đánh dấu tất cả Checkbutton là True
        for var in check_vars:
            var.set(True)

    def delete_all():
        # Đánh dấu tất cả Checkbutton là True
        for var in check_vars:
            var.set(False)

    ad_button_select_all = Button(User.ad_root_homepage, text="Chọn tất cả", font=("Arial", 12, "bold"), fg="white",
                                  bg="#34495E", command=select_all)
    ad_button_select_all.place(x=1095, y=350)

    ad_button_delete_all = Button(User.ad_root_homepage, text="Bỏ chọn tất cả", font=("Arial", 12, "bold"), fg="white",
                                  bg="#34495E", command=delete_all)
    ad_button_delete_all.place(x=1200, y=350)

    ad_button_delete_account = Button(User.ad_root_homepage, text="Cấp lại mật khẩu", font=("Arial", 12, "bold"),
                                      fg="white",
                                      bg="#34495E", command=show_selected)
    ad_button_delete_account.place(x=1184, y=700)

    User.ad_root_homepage.mainloop()
