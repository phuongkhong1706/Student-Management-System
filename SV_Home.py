from tkinter import *
from PIL import Image, ImageTk

# import AD_DeleteAccount
# import AD_History
# import AD_InforAccount
# import AD_PassWord
# import AD_CreateAccount
# import AD_ResetPassword
# import AD_AccessControl

# def sv_home():
sv_root_homepage = Tk()
sv_root_homepage.title("Trang chủ")
sv_root_homepage.state("zoomed")

# Tạo canvas và scrollbar
canvas = Canvas(sv_root_homepage, borderwidth=0)
scrollbar = Scrollbar(sv_root_homepage, orient=VERTICAL, command=canvas.yview)
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
image_home = create_image("./icon/home.png", 37, 37)
image_tk = create_image("./icon/user.png", 37, 37)
image_kqht = create_image("./icon/kqht.png", 37, 37)
image_hdnk = create_image("./icon/extraact.png", 37, 37)
image_kehoach = create_image("./icon/learning.png", 37, 37)
image_hocphi = create_image("./icon/tuitionfee.png", 37, 37)
image_logout = create_image("./icon/logout.png", 37, 37)
image_hethong = create_image("./icon/system.png", 37, 37)
image_meoquan = create_image("./icon/meoqan.jpg", 200, 200)

label_hp = Label(frame_hp, height=150, image=image_hp, anchor=CENTER,
                 borderwidth=0, bg="#34495E")
label_hp.pack()


def atv_sv_button_tk():
    sv_button_kqht.pack_forget()
    sv_button_kqht_bdcn.pack_forget()
    sv_button_kqht_pt.pack_forget()

    sv_button_hdnk.pack_forget()
    sv_button_hdnk_dkhd.pack_forget()
    sv_button_hdnk_mchd.pack_forget()
    sv_button_hdnk_cdrl.pack_forget()
    sv_button_hdnk_tckqrl.pack_forget()
    sv_button_hdnk_knhd.pack_forget()

    sv_button_khht.pack_forget()
    sv_button_khht_dkhp.pack_forget()
    sv_button_khht_dklhp.pack_forget()
    sv_button_khht_tkb.pack_forget()

    sv_button_hphi.pack_forget()
    sv_button_hphi_xhp.pack_forget()
    sv_button_hphi_dhp.pack_forget()

    sv_button_dx.pack_forget()
    sv_label_none.pack_forget()

    sv_button_tk_tttk.pack(anchor='w', padx=0, pady=5)
    sv_button_tk_dmk.pack(anchor='w', padx=0, pady=5)
    sv_button_kqht.pack(anchor='w', padx=0, pady=5)
    sv_button_hdnk.pack(anchor='w', padx=0, pady=5)
    sv_button_khht.pack(anchor='w', padx=0, pady=5)
    sv_button_hphi.pack(anchor='w', padx=0, pady=5)
    sv_button_dx.pack(anchor='w', padx=0, pady=5)
    sv_label_none.pack()


sv_button_home = Button(frame_hp, text="    Trang chủ", font=("Arial", 14, "bold"),
                        fg="white", bg="#34495E", borderwidth=0, compound="left",
                        image=image_home, width=290, height=50, anchor="w", padx=10)
sv_button_home.pack(anchor='w', padx=0, pady=5)

sv_button_tk = Button(frame_hp, text="    Tài khoản", font=("Arial", 14, "bold"),
                      fg="white", bg="#34495E", borderwidth=0, compound="left",
                      image=image_tk, width=290, height=50, anchor="w", padx=10,
                      command=atv_sv_button_tk)
sv_button_tk.pack(anchor='w', padx=0, pady=5)


def select_sv_button_tk_tttk():
    sv_root_homepage.destroy()
    # AD_InforAccount.sv_inforaccount()


sv_button_tk_tttk = Button(frame_hp, text="   Thông tin tài khoản", font=("Arial", 14, "bold"),
                           fg="white", bg="#34495E", borderwidth=0, compound="left",
                           width=290, height=1, anchor="w", padx=64, command=select_sv_button_tk_tttk)


def select_sv_button_tk_dmk():
    sv_root_homepage.destroy()
    # AD_PassWord.sv_password()


sv_button_tk_dmk = Button(frame_hp, text="   Đổi mật khẩu", font=("Arial", 14, "bold"),
                          fg="white", bg="#34495E", borderwidth=0, compound="left",
                          width=290, height=1, anchor="w", padx=64, command=select_sv_button_tk_dmk)


def atv_sv_button_kqht():
    sv_button_tk_tttk.pack_forget()
    sv_button_tk_dmk.pack_forget()

    sv_button_hdnk.pack_forget()
    sv_button_hdnk_dkhd.pack_forget()
    sv_button_hdnk_mchd.pack_forget()
    sv_button_hdnk_cdrl.pack_forget()
    sv_button_hdnk_tckqrl.pack_forget()
    sv_button_hdnk_knhd.pack_forget()

    sv_button_khht.pack_forget()
    sv_button_khht_dkhp.pack_forget()
    sv_button_khht_dklhp.pack_forget()
    sv_button_khht_tkb.pack_forget()

    sv_button_hphi.pack_forget()
    sv_button_hphi_xhp.pack_forget()
    sv_button_hphi_dhp.pack_forget()

    sv_button_dx.pack_forget()
    sv_label_none.pack_forget()

    sv_button_kqht_bdcn.pack(anchor='w', padx=0, pady=5)
    sv_button_kqht_pt.pack(anchor='w', padx=0, pady=5)

    sv_button_hdnk.pack(anchor='w', padx=0, pady=5)
    sv_button_khht.pack(anchor='w', padx=0, pady=5)
    sv_button_hphi.pack(anchor='w', padx=0, pady=5)
    sv_button_dx.pack(anchor='w', padx=0, pady=5)
    sv_label_none.pack()


sv_button_kqht = Button(frame_hp, text="    Kết quả học tập", font=("Arial", 14, "bold"),
                      fg="white", bg="#34495E", borderwidth=0, compound="left", image=image_kqht,
                      width=290, height=50, anchor="w", padx=10, command=atv_sv_button_kqht)
sv_button_kqht.pack(anchor='w', padx=0, pady=5)


def select_sv_button_kqht_bdcn():
    sv_root_homepage.destroy()
    # AD_CreateAccount.sv_createaccount()


sv_button_kqht_bdcn = Button(frame_hp, text="   Bảng điểm cá nhân", font=("Arial", 14, "bold"),
                          fg="white", bg="#34495E", borderwidth=0, compound="left",
                          width=290, height=1, anchor="w", padx=64, command=select_sv_button_kqht_bdcn)


def select_sv_button_kqht_pt():
    sv_root_homepage.destroy()
    # AD_DeleteAccount.sv_deleteaccount()


sv_button_kqht_pt = Button(frame_hp, text="   Phúc tra", font=("Arial", 14, "bold"),
                          fg="white", bg="#34495E", borderwidth=0, compound="left",
                          width=290, height=1, anchor="w", padx=64, command=select_sv_button_kqht_pt)

def atv_sv_button_hdnk():
    sv_button_tk_tttk.pack_forget()
    sv_button_tk_dmk.pack_forget()
    sv_button_kqht_bdcn.pack_forget()
    sv_button_kqht_pt.pack_forget()

    sv_button_khht.pack_forget()
    sv_button_khht_dkhp.pack_forget()
    sv_button_khht_dklhp.pack_forget()
    sv_button_khht_tkb.pack_forget()

    sv_button_hphi.pack_forget()
    sv_button_hphi_xhp.pack_forget()
    sv_button_hphi_dhp.pack_forget()

    sv_button_dx.pack_forget()
    sv_label_none.pack_forget()

    sv_button_hdnk_dkhd.pack(anchor='w', padx=0, pady=5)
    sv_button_hdnk_mchd.pack(anchor='w', padx=0, pady=5)
    sv_button_hdnk_cdrl.pack(anchor='w', padx=0, pady=5)
    sv_button_hdnk_tckqrl.pack(anchor='w', padx=0, pady=5)
    sv_button_hdnk_knhd.pack(anchor='w', padx=0, pady=5)

    sv_button_khht.pack(anchor='w', padx=0, pady=5)
    sv_button_hphi.pack(anchor='w', padx=0, pady=5)
    sv_button_dx.pack(anchor='w', padx=0, pady=5)
    sv_label_none.pack()

sv_button_hdnk = Button(frame_hp, text="    Hoạt động ngoại khóa", font=("Arial", 14, "bold"),
                      fg="white", bg="#34495E", borderwidth=0, compound="left", image=image_hdnk,
                      width=290, height=50, anchor="w", padx=10, command=atv_sv_button_hdnk)
sv_button_hdnk.pack(anchor='w', padx=0, pady=5)


def select_sv_button_hdnk_dkhd():
    sv_root_homepage.destroy()
    # AD_CreateAccount.sv_createaccount()


sv_button_hdnk_dkhd = Button(frame_hp, text="   Đăng ký hoạt động", font=("Arial", 14, "bold"),
                          fg="white", bg="#34495E", borderwidth=0, compound="left",
                          width=290, height=1, anchor="w", padx=64, command=select_sv_button_hdnk_dkhd)


def select_sv_button_hdnk_mchd():
    sv_root_homepage.destroy()
    # AD_DeleteAccount.sv_deleteaccount()


sv_button_hdnk_mchd = Button(frame_hp, text="   Minh chứng", font=("Arial", 14, "bold"),
                          fg="white", bg="#34495E", borderwidth=0, compound="left",
                          width=290, height=1, anchor="w", padx=64, command=select_sv_button_hdnk_mchd)

def select_sv_button_hdnk_cdrl():
    sv_root_homepage.destroy()
    # AD_DeleteAccount.sv_deleteaccount()


sv_button_hdnk_cdrl = Button(frame_hp, text="   Chấm điểm rèn luyện", font=("Arial", 14, "bold"),
                          fg="white", bg="#34495E", borderwidth=0, compound="left",
                          width=290, height=1, anchor="w", padx=64, command=select_sv_button_hdnk_cdrl)

def select_sv_button_hdnk_tckqrl():
    sv_root_homepage.destroy()
    # AD_DeleteAccount.sv_deleteaccount()


sv_button_hdnk_tckqrl = Button(frame_hp, text="   Tra cứu KQRL", font=("Arial", 14, "bold"),
                          fg="white", bg="#34495E", borderwidth=0, compound="left",
                          width=290, height=1, anchor="w", padx=64, command=select_sv_button_hdnk_tckqrl)

def select_sv_button_hdnk_knhd():
    sv_root_homepage.destroy()
    # AD_DeleteAccount.sv_deleteaccount()


sv_button_hdnk_knhd = Button(frame_hp, text="   Khiếu nại hoạt động", font=("Arial", 14, "bold"),
                          fg="white", bg="#34495E", borderwidth=0, compound="left",
                          width=290, height=1, anchor="w", padx=64, command=select_sv_button_hdnk_knhd)

def atv_sv_button_khht():
    sv_button_tk_tttk.pack_forget()
    sv_button_tk_dmk.pack_forget()
    sv_button_kqht_bdcn.pack_forget()
    sv_button_kqht_pt.pack_forget()
    sv_button_hdnk_dkhd.pack_forget()
    sv_button_hdnk_mchd.pack_forget()
    sv_button_hdnk_cdrl.pack_forget()
    sv_button_hdnk_tckqrl.pack_forget()
    sv_button_hdnk_knhd.pack_forget()

    sv_button_hphi.pack_forget()
    sv_button_hphi_xhp.pack_forget()
    sv_button_hphi_dhp.pack_forget()

    sv_button_dx.pack_forget()
    sv_label_none.pack_forget()

    sv_button_khht_dkhp.pack(anchor='w', padx=0, pady=5)
    sv_button_khht_dklhp.pack(anchor='w', padx=0, pady=5)
    sv_button_khht_tkb.pack(anchor='w', padx=0, pady=5)

    sv_button_hphi.pack(anchor='w', padx=0, pady=5)
    sv_button_dx.pack(anchor='w', padx=0, pady=5)
    sv_label_none.pack()


sv_button_khht = Button(frame_hp, text="    Kế hoạch học tập", font=("Arial", 14, "bold"),
                        fg="white", bg="#34495E", borderwidth=0, compound="left", image=image_kehoach,
                        width=290, height=50, anchor="w", padx=10, command=atv_sv_button_khht)
sv_button_khht.pack(anchor='w', padx=0, pady=5)


def select_sv_button_khht_dkhp():
    sv_root_homepage.destroy()
    # AD_CreateAccount.sv_createaccount()


sv_button_khht_dkhp = Button(frame_hp, text="   Đăng ký học phần", font=("Arial", 14, "bold"),
                             fg="white", bg="#34495E", borderwidth=0, compound="left",
                             width=290, height=1, anchor="w", padx=64, command=select_sv_button_khht_dkhp)


def select_sv_button_khht_dklhp():
    sv_root_homepage.destroy()
    # AD_DeleteAccount.sv_deleteaccount()


sv_button_khht_dklhp = Button(frame_hp, text="   Đăng ký lớp học phần", font=("Arial", 14, "bold"),
                             fg="white", bg="#34495E", borderwidth=0, compound="left",
                             width=290, height=1, anchor="w", padx=64, command=select_sv_button_khht_dklhp)


def select_sv_button_khht_tkb():
    sv_root_homepage.destroy()
    # AD_DeleteAccount.sv_deleteaccount()


sv_button_khht_tkb = Button(frame_hp, text="   Thời khóa biểu", font=("Arial", 14, "bold"),
                             fg="white", bg="#34495E", borderwidth=0, compound="left",
                             width=290, height=1, anchor="w", padx=64, command=select_sv_button_khht_tkb)

def atv_sv_button_hphi():
    sv_button_tk_tttk.pack_forget()
    sv_button_tk_dmk.pack_forget()
    sv_button_kqht_bdcn.pack_forget()
    sv_button_kqht_pt.pack_forget()
    sv_button_hdnk_dkhd.pack_forget()
    sv_button_hdnk_mchd.pack_forget()
    sv_button_hdnk_cdrl.pack_forget()
    sv_button_hdnk_tckqrl.pack_forget()
    sv_button_hdnk_knhd.pack_forget()
    sv_button_khht_dkhp.pack_forget()
    sv_button_khht_dklhp.pack_forget()
    sv_button_khht_tkb.pack_forget()


    sv_button_dx.pack_forget()
    sv_label_none.pack_forget()

    sv_button_hphi_xhp.pack(anchor='w', padx=0, pady=5)
    sv_button_hphi_dhp.pack(anchor='w', padx=0, pady=5)
    sv_button_dx.pack(anchor='w', padx=0, pady=5)
    sv_label_none.pack()


sv_button_hphi = Button(frame_hp, text="    Học phí", font=("Arial", 14, "bold"),
                        fg="white", bg="#34495E", borderwidth=0, compound="left", image=image_hocphi,
                        width=290, height=50, anchor="w", padx=10, command=atv_sv_button_hphi)
sv_button_hphi.pack(anchor='w', padx=0, pady=5)


def select_sv_button_hphi_xhp():
    sv_root_homepage.destroy()
    # AD_CreateAccount.sv_createaccount()


sv_button_hphi_xhp = Button(frame_hp, text="   Xem học phí", font=("Arial", 14, "bold"),
                             fg="white", bg="#34495E", borderwidth=0, compound="left",
                             width=290, height=1, anchor="w", padx=64, command=select_sv_button_hphi_xhp)


def select_sv_button_hphi_dhp():
    sv_root_homepage.destroy()
    # AD_DeleteAccount.sv_deleteaccount()


sv_button_hphi_dhp = Button(frame_hp, text="   Đăng ký lớp học phần", font=("Arial", 14, "bold"),
                              fg="white", bg="#34495E", borderwidth=0, compound="left",
                              width=290, height=1, anchor="w", padx=64, command=select_sv_button_hphi_dhp)


sv_button_dx = Button(frame_hp, text="    Đăng xuất", font=("Arial", 14, "bold"),
                      fg="white", bg="#34495E", borderwidth=0, compound="left", image=image_logout,
                      width=290, height=50, anchor="w", padx=10)
sv_button_dx.pack(anchor='w', padx=0, pady=5)

sv_label_none = Label(frame_hp, bg="#34495E", borderwidth=0, height=1000)
sv_label_none.pack()

sv_label = Label(sv_root_homepage, text="   Trang chủ", fg="#34495E", font=("Arial", 16, "bold"),
                 borderwidth=0, relief=RAISED, width=81, height=2, anchor='w', bg="#DEE3EB")
sv_label.place(x=290, y=0)

sv_label_content = Label(sv_root_homepage, text="  Tổ hợp cuti meo qăn của sin ziên",
                         fg="blue", font=("Arial", 16, "bold"),
                         borderwidth=0, relief=RAISED, width=81, height=30, anchor=CENTER)
sv_label_content.place(x=290, y=50)

sv_image = Label(sv_root_homepage, image=image_meoquan)
sv_image.place(x=720, y=150)

sv_root_homepage.mainloop()
