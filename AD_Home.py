from tkinter import *

from PIL import Image, ImageTk

import AD_AccessControl
import AD_CreateAccount
import AD_DeleteAccount
import AD_History
import AD_InforAccount
import AD_PassWord
import AD_ResetPassword
import History
import User


def ad_home():
    # Tạo canvas và scrollbar
    canvas = Canvas(User.ad_root_homepage, borderwidth=0)
    scrollbar = Scrollbar(User.ad_root_homepage, orient=VERTICAL, command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Tạo một frame bên trong canvas
    frame_hp = Frame(canvas, width=290, height=1000, borderwidth=0, bg="#34495E")
    frame_hp.pack_propagate(False)
    canvas.create_window((0, 0), window=frame_hp, anchor='nw')

    # Đặt canvas và scrollbar vào cửa sổ chính
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

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
    image_meoquan = create_image("./icon/meoqan.jpg", 200, 200)

    label_hp = Label(frame_hp, height=150, image=image_hp, anchor=CENTER,
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

    ad_button_home = Button(frame_hp, text="    Trang chủ", font=("Arial", 14, "bold"),
                            fg="white", bg="#34495E", borderwidth=0, compound="left",
                            image=image_home, width=290, height=50, anchor="w", padx=10)
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

    def select_ad_button_ht_xtk():
        History.save_user(User.user_input, "Truy cập \"Xóa tài khoản\"")
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

    ad_label = Label(User.ad_root_homepage, text="   Trang chủ", fg="#34495E", font=("Arial", 16, "bold"),
                     borderwidth=0, relief=RAISED, width=81, height=2, anchor='w', bg="#DEE3EB")
    ad_label.place(x=290, y=0)

    ad_label_content = Label(User.ad_root_homepage, text="  Tổ hợp cuti meo qăn",
                             fg="blue", font=("Arial", 16, "bold"),
                             borderwidth=0, relief=RAISED, width=81, height=30, anchor=CENTER)
    ad_label_content.place(x=290, y=50)

    ad_image = Label(User.ad_root_homepage, image=image_meoquan)
    ad_image.place(x=720, y=150)

    User.ad_root_homepage.mainloop()
