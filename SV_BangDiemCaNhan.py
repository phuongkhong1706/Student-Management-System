from datetime import datetime
import random
import string
from tkinter import *
import mysql.connector
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkinter import ttk, messagebox

import ConnectionToMySQL

# import AD_DeleteAccount
# import AD_History
# import AD_InforAccount
# import AD_PassWord
# import AD_CreateAccount
# import AD_ResetPassword
# import AD_AccessControl

# def sv_bangdiemcanhan():
sv_root_bangdiemcanhan = Tk()
sv_root_bangdiemcanhan.title("Bảng điểm cá nhân")
sv_root_bangdiemcanhan.state("zoomed")

# Tạo canvas và scrollbar
canvas = Canvas(sv_root_bangdiemcanhan, borderwidth=0)
scrollbar = Scrollbar(sv_root_bangdiemcanhan, orient=VERTICAL, command=canvas.yview)
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
    sv_root_bangdiemcanhan.destroy()
    # AD_InforAccount.sv_inforaccount()

sv_button_tk_tttk = Button(frame_hp, text="   Thông tin tài khoản", font=("Arial", 14, "bold"),
                               fg="white", bg="#34495E", borderwidth=0, compound="left",
                               width=290, height=1, anchor="w", padx=64, command = select_sv_button_tk_tttk)

def select_sv_button_tk_dmk():
    sv_root_bangdiemcanhan.destroy()
    # AD_InforAccount.sv_inforaccount()
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

sv_button_kqht_bdcn = Button(frame_hp, text="   Bảng điểm cá nhân", font=("Arial", 14, "bold"),
                          fg="#34495E", bg="white", borderwidth=0, compound="left",
                          width=290, height=1, anchor="w", padx=64)
sv_button_kqht_bdcn.pack(anchor='w', padx=0, pady=5)

def select_sv_button_kqht_pt():
    sv_root_bangdiemcanhan.destroy()
    # AD_DeleteAccount.sv_deleteaccount()


sv_button_kqht_pt = Button(frame_hp, text="   Phúc tra", font=("Arial", 14, "bold"),
                          fg="white", bg="#34495E", borderwidth=0, compound="left",
                          width=290, height=1, anchor="w", padx=64, command=select_sv_button_kqht_pt)
sv_button_kqht_pt.pack(anchor='w', padx=0, pady=5)
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
    sv_root_bangdiemcanhan.destroy()
    # AD_CreateAccount.sv_createaccount()


sv_button_hdnk_dkhd = Button(frame_hp, text="   Đăng ký hoạt động", font=("Arial", 14, "bold"),
                          fg="white", bg="#34495E", borderwidth=0, compound="left",
                          width=290, height=1, anchor="w", padx=64, command=select_sv_button_hdnk_dkhd)


def select_sv_button_hdnk_mchd():
    sv_root_bangdiemcanhan.destroy()
    # AD_DeleteAccount.sv_deleteaccount()


sv_button_hdnk_mchd = Button(frame_hp, text="   Minh chứng", font=("Arial", 14, "bold"),
                          fg="white", bg="#34495E", borderwidth=0, compound="left",
                          width=290, height=1, anchor="w", padx=64, command=select_sv_button_hdnk_mchd)

def select_sv_button_hdnk_cdrl():
    sv_root_bangdiemcanhan.destroy()
    # AD_DeleteAccount.sv_deleteaccount()


sv_button_hdnk_cdrl = Button(frame_hp, text="   Chấm điểm rèn luyện", font=("Arial", 14, "bold"),
                          fg="white", bg="#34495E", borderwidth=0, compound="left",
                          width=290, height=1, anchor="w", padx=64, command=select_sv_button_hdnk_cdrl)

def select_sv_button_hdnk_tckqrl():
    sv_root_bangdiemcanhan.destroy()
    # AD_DeleteAccount.sv_deleteaccount()


sv_button_hdnk_tckqrl = Button(frame_hp, text="   Tra cứu KQRL", font=("Arial", 14, "bold"),
                          fg="white", bg="#34495E", borderwidth=0, compound="left",
                          width=290, height=1, anchor="w", padx=64, command=select_sv_button_hdnk_tckqrl)

def select_sv_button_hdnk_knhd():
    sv_root_bangdiemcanhan.destroy()
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
    sv_root_bangdiemcanhan.destroy()
    # AD_CreateAccount.sv_createaccount()


sv_button_khht_dkhp = Button(frame_hp, text="   Đăng ký học phần", font=("Arial", 14, "bold"),
                             fg="white", bg="#34495E", borderwidth=0, compound="left",
                             width=290, height=1, anchor="w", padx=64, command=select_sv_button_khht_dkhp)


def select_sv_button_khht_dklhp():
    sv_root_bangdiemcanhan.destroy()
    # AD_DeleteAccount.sv_deleteaccount()


sv_button_khht_dklhp = Button(frame_hp, text="   Đăng ký lớp học phần", font=("Arial", 14, "bold"),
                             fg="white", bg="#34495E", borderwidth=0, compound="left",
                             width=290, height=1, anchor="w", padx=64, command=select_sv_button_khht_dklhp)


def select_sv_button_khht_tkb():
    sv_root_bangdiemcanhan.destroy()
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
    sv_root_bangdiemcanhan.destroy()
    # AD_CreateAccount.sv_createaccount()


sv_button_hphi_xhp = Button(frame_hp, text="   Xem học phí", font=("Arial", 14, "bold"),
                             fg="white", bg="#34495E", borderwidth=0, compound="left",
                             width=290, height=1, anchor="w", padx=64, command=select_sv_button_hphi_xhp)


def select_sv_button_hphi_dhp():
    sv_root_bangdiemcanhan.destroy()
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

sv_label = Label(sv_root_bangdiemcanhan, text="   Bảng điểm cá nhân", fg="#34495E", font=("Arial", 16, "bold"),
                 borderwidth=0, relief=RAISED, width=81, height=2, anchor='w', bg="#DEE3EB")
sv_label.place(x=292, y=0)

#code giao diện ở đây
sv_label_find = Label(sv_root_bangdiemcanhan, text="Tra cứu", font=("Arial", 14, "bold"),
                      fg="black", borderwidth=0)
sv_label_find.place(x=310, y=60)

sv_frame_find = Frame(sv_root_bangdiemcanhan, width=1025, height=100, borderwidth=2, relief=RAISED)
sv_frame_find.place(x=310, y=90)

sv_label_semester = Label(sv_root_bangdiemcanhan, text="Học kỳ: ", font=("Arial", 12, "bold"),
                      fg="black", borderwidth=0)
sv_label_semester.place(x=320, y=110)

# Tạo combo box đối tượng sử dụng
sv_combobox_find_semester = ["20231", "20232",
                                 "20233", "20241", "20242"]
sv_combobox_find_semester = Combobox(sv_root_bangdiemcanhan,
                                 values=sv_combobox_find_semester, width=20, state="readonly")
sv_combobox_find_semester.set("Chọn học kỳ")

sv_combobox_find_semester.place(x=400, y=110)

sv_label_find_student = Label(sv_root_bangdiemcanhan, text="Mã học phần / Tên học phần: ", font=("Arial", 12, "bold"),
                              fg="black", borderwidth=0)
sv_label_find_student.place(x=570, y=110)

sv_text_find_student = Text(sv_root_bangdiemcanhan, width=29, height=1)
sv_text_find_student.place(x=810, y=110)

sv_label_grade = Label(sv_root_bangdiemcanhan, text="Thang điểm: ", font=("Arial", 12, "bold"),
                      fg="black", borderwidth=0)
sv_label_grade.place(x=1070, y=110)
# Tạo combo box đối tượng sử dụng
sv_combobox_find_grade = ["A+", "A", "B+", "B", "C+", "C", "D+", "D", "F"]
sv_combobox_find_grade = Combobox(sv_root_bangdiemcanhan,
                                 values=sv_combobox_find_grade, width=20, state="readonly")
sv_combobox_find_grade.set("Chọn thang điểm")
sv_combobox_find_grade.place(x=1185, y=110)

###################################################################################################
sv_label_list_bangdiemhocphan = Label(sv_root_bangdiemcanhan, text="Bảng điểm học phần",
                             font=("Arial", 14, "bold"),
                             fg="black", borderwidth=0)
sv_label_list_bangdiemhocphan.place(x=310, y=200)


# Hàm kết nối đến MySQL và lấy dữ liệu
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


# Khởi tạo style
style = ttk.Style()
style.theme_use('clam')
style.configure("Treeview.Heading", font=("Arial", 12, "bold"),
                background="#34495E", foreground="white")
style.configure("Treeview", font=("Arial", 12), rowheight=50)
style.configure("Treeview", highlightthickness=0, bd=0, font=('Arial', 12))
style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

query = "SELECT * from list_bangdiemcanhan"
data = fetch_data_from_mysql(query)

# Tạo widget Treeview
tree = ttk.Treeview(sv_root_bangdiemcanhan,
                    columns=("Học kỳ", "Mã học phần", "Tên học phần", "Điểm quá trình", "Điểm cuối kỳ", "Điểm chữ"),
                    show="headings")

# Đặt tên tiêu đề cho các cột
tree.heading("Học kỳ", text="Học kỳ")
tree.heading("Mã học phần", text="Mã học phần")
tree.heading("Tên học phần", text="Tên học phần")
tree.heading("Điểm quá trình", text="Điểm quá trình")
tree.heading("Điểm cuối kỳ", text="Điểm cuối kỳ")
tree.heading("Điểm chữ", text="Điểm chữ")

# Căn và tùy chỉnh kích thước cho từng cột
tree.column("Học kỳ", anchor="w", width=100)
tree.column("Mã học phần", anchor="w", width=150)
tree.column("Tên học phần", anchor="w", width=310)
tree.column("Điểm quá trình", anchor="w", width=150)
tree.column("Điểm cuối kỳ", anchor="w", width=150)
tree.column("Điểm chữ", anchor="w", width=150)

# Thêm dữ liệu vào Treeview
for row in data:
    tree.insert("", "end", values=row)

# Tạo thanh cuộn dọc
tree_scroll_vertical = Scrollbar(sv_root_bangdiemcanhan, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=tree_scroll_vertical.set)

# Đặt vị trí Treeview và các thanh cuộn
tree.place(x=310, y=230, height=200)  # Đặt chiều cao tối đa cho Treeview là 200 (4 dòng * 50 pixel)
tree_scroll_vertical.place(x=1320, y=230, height=200)
#######################################################################################################

###################################################################################################
sv_label_list_bangdiemnienkhoa = Label(sv_root_bangdiemcanhan, text="Bảng điểm niên khóa",
                             font=("Arial", 14, "bold"),
                             fg="black", borderwidth=0)
sv_label_list_bangdiemnienkhoa.place(x=310, y=450)

# Khởi tạo style
style = ttk.Style()
style.theme_use('clam')
style.configure("Treeview.Heading", font=("Arial", 12, "bold"),
                background="#34495E", foreground="white")
style.configure("Treeview", font=("Arial", 12), rowheight=50)
style.configure("Treeview", highlightthickness=0, bd=0, font=('Arial', 12))
style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

query = "SELECT * from list_bangdiemcanhan"
data = fetch_data_from_mysql(query)

# Tạo widget Treeview
tree = ttk.Treeview(sv_root_bangdiemcanhan,
                    columns=("Học kỳ", "GPA", "CPA",
                             "TC qua", "TC nợ", "TC ĐK", "Trình độ", "CTĐT"),
                    show="headings")

# Đặt tên tiêu đề cho các cột
tree.heading("Học kỳ", text="Học kỳ")
tree.heading("GPA", text="GPA")
tree.heading("CPA", text="CPA")
tree.heading("TC qua", text="TC qua")
tree.heading("TC nợ", text="TC nợ")
tree.heading("TC ĐK", text="TC ĐK")
tree.heading("Trình độ", text="Trình độ")
tree.heading("CTĐT", text="CTĐT")

# Căn và tùy chỉnh kích thước cho từng cột
tree.column("Học kỳ", anchor="w", width=100)
tree.column("GPA", anchor="w", width=100)
tree.column("CPA", anchor="w", width=100)
tree.column("TC qua", anchor="w", width=100)
tree.column("TC nợ", anchor="w", width=100)
tree.column("TC ĐK", anchor="w", width=100)
tree.column("Trình độ", anchor="w", width=150)
tree.column("CTĐT", anchor="w", width=260)

# Thêm dữ liệu vào Treeview
for row in data:
    tree.insert("", "end", values=row)

# Tạo thanh cuộn dọc
tree_scroll_vertical = Scrollbar(sv_root_bangdiemcanhan, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=tree_scroll_vertical.set)

# Đặt vị trí Treeview và các thanh cuộn
tree.place(x=310, y=480, height=200)  # Đặt chiều cao tối đa cho Treeview là 200 (4 dòng * 50 pixel)
tree_scroll_vertical.place(x=1320, y=480, height=200)
#######################################################################################################


def sv_query():
    # Lấy dữ liệu từ các widget
    date = sv_text_find_date.get()  # Lấy ngày từ DateEntry
    hour = hour_spinbox.get()  # Lấy giờ từ Spinbox
    minute = minute_spinbox.get()  # Lấy phút từ Spinbox
    second = second_spinbox.get()  # Lấy giây từ Spinbox

    # Chuyển đổi định dạng ngày từ mm/dd/yy sang mm-dd-yyyy
    date_obj = datetime.strptime(date, "%m/%d/%y")  # Sử dụng %y cho năm 2 chữ số
    formatted_date = date_obj.strftime("%Y-%m-%d")  # Định dạng lại thành mm-dd-yyyy

    # Tạo chuỗi datetime
    datetime_str = f"{formatted_date} {hour}:{minute}:{second}"  # Tạo chuỗi datetime

    user_type = sv_combobox_find_user.get()  # Lấy đối tượng sử dụng từ Combobox
    student_info = sv_text_find_student.get("1.0", "end-1c").strip()  # Lấy MSSV/họ tên từ Text widget

    query = """
               SELECT MaSo, ThoiGian, DoiTuongSuDung, HoVaTen 
               FROM list_bangdiemcanhan 
               WHERE ThoiGian = %s AND DoiTuongSuDung = %s AND (MaSo = %s OR HoVaTen LIKE %s)
               """
    params = (datetime_str, user_type, student_info, f"%{student_info}%")  # Cập nhật tham số cho truy vấn
    data = fetch_data_from_mysql(query, params)  # Giả định rằng hàm này nhận params

    # Xóa tất cả các mục hiện tại trong Treeview
    for item in tree.get_children():
        tree.delete(item)

    # Thêm dữ liệu mới vào Treeview
    for row in data:
        tree.insert("", "end", values=row)

    # Điều chỉnh kích thước Treeview
    max_visible_rows = 6  # Số dòng tối đa mà bạn muốn hiển thị
    row_count = len(data)  # Đếm số dòng trả về

    # Đặt chiều cao của Treeview tương ứng với số dòng trả về
    tree.config(height=min(max_visible_rows, row_count))  # Giữ chiều cao tối đa là 4 dòng


sv_button_find = Button(sv_root_bangdiemcanhan, text="Tìm kiếm", font=("Arial", 12, "bold"),
                        fg="white", bg="#34495E", command=sv_query)
sv_button_find.place(x=1251, y=155)

sv_root_bangdiemcanhan.mainloop()
