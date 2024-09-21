from tkinter import *
from PIL import Image, ImageTk

def homepage2():
    root_homepage = Tk()
    root_homepage.title("Trang chủ")
    root_homepage.state("zoom")

    # Tạo canvas và scrollbar
    canvas = Canvas(root_homepage, borderwidth=0)
    scrollbar = Scrollbar(root_homepage, orient=VERTICAL, command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Tạo một frame bên trong canvas
    frame_hp = Frame(canvas, width=300, borderwidth=3, bg="#4682B4")
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


    image_hp = create_image("C://Users//ASUS//Desktop//python-logo.png", 100, 100)
    image_bt = create_image("C://Users//ASUS//Desktop//python-logo.png", 50, 50)

    label_hp = Label(frame_hp, height=150, image=image_hp, anchor=CENTER,
                     borderwidth=0, bg="#4682B4")
    label_hp.pack()


    def button_ht_atv():
        button_kqht.pack_forget()
        button_hdnk.pack_forget()
        button_khht.pack_forget()
        button_hocphi.pack_forget()
        button_dx.pack_forget()
        button_bctk.pack_forget()
        label_none.pack_forget()
        button_ht_ctk.pack(anchor='w', padx=10, pady=5)
        button_kqht.pack(anchor='w', padx=10, pady=5)
        button_hdnk.pack(anchor='w', padx=10, pady=5)
        button_khht.pack(anchor='w', padx=10, pady=5)
        button_hocphi.pack(anchor='w', padx=10, pady=5)
        button_bctk.pack(anchor='w', padx=10, pady=5)
        button_dx.pack(anchor='w', padx=10, pady=5)
        label_none.pack()


    button_ht = Button(frame_hp, text="    Hệ thống", font=("Arial", 14, "bold"),
                       fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt, command=button_ht_atv)
    button_ht.pack(anchor='w', padx=10, pady=5)

    button_ht_ctk = Button(frame_hp, text="    Cấp tài khoản", font=("Arial", 14, "bold"),
                           fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)

    button_ht_xtk = Button(frame_hp, text="    Xóa tài khoản", font=("Arial", 14, "bold"),
                           fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)

    button_ht_clmk = Button(frame_hp, text="    Cấp lại mật khẩu", font=("Arial", 14, "bold"),
                           fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)

    button_ht_xlshd = Button(frame_hp, text="    Xem lịch sử hoạt động", font=("Arial", 14, "bold"),
                           fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)

    button_ht_pq = Button(frame_hp, text="    Phân quyền", font=("Arial", 14, "bold"),
                           fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)

    button_dm = Button(frame_hp, text="    Danh mục", font=("Arial", 14, "bold"),
                         fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)
    button_dm.pack(anchor='w', padx=10, pady=5)

    button_dm_cngv = Button(frame_hp, text="    Cập nhật Giảng viên", font=("Arial", 14, "bold"),
                         fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)
    button_dm_cngv.pack(anchor='w', padx=10, pady=5)

    button_dm_cnhp = Button(frame_hp, text="    Cập nhật Học phần", font=("Arial", 14, "bold"),
                         fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)
    button_dm_cnhp.pack(anchor='w', padx=10, pady=5)

    button_dm_cnlhp = Button(frame_hp, text="    Cập nhật Lớp HP", font=("Arial", 14, "bold"),
                         fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)
    button_dm_cnlhp.pack(anchor='w', padx=10, pady=5)

    button_dm_cnsv = Button(frame_hp, text="    Cập nhật Sinh viên", font=("Arial", 14, "bold"),
                         fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)
    button_dm_cnsv.pack(anchor='w', padx=10, pady=5)

    button_dm_cnn = Button(frame_hp, text="    Cập nhật Ngành", font=("Arial", 14, "bold"),
                         fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)
    button_dm_cnn.pack(anchor='w', padx=10, pady=5)

    button_kqht = Button(frame_hp, text="    Kết quả học tập", font=("Arial", 14, "bold"),
                         fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)
    button_kqht.pack(anchor='w', padx=10, pady=5)

    button_hdnk = Button(frame_hp, text="    Hoạt động ngoại khóa", font=("Arial", 14, "bold"),
                         fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)
    button_hdnk.pack(anchor='w', padx=10, pady=5)

    button_khht = Button(frame_hp, text="    Kế hoạch học tập", font=("Arial", 14, "bold"),
                         fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)
    button_khht.pack(anchor='w', padx=10, pady=5)

    button_hocphi = Button(frame_hp, text="    Học phí", font=("Arial", 14, "bold"),
                           fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)
    button_hocphi.pack(anchor='w', padx=10, pady=5)

    button_dx = Button(frame_hp, text="    Đăng xuất", font=("Arial", 14, "bold"),
                       fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)
    button_dx.pack(anchor='w', padx=10, pady=5)

    button_bctk = Button(frame_hp, text="    Thống kê", font=("Arial", 14, "bold"),
                       fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)
    button_bctk.pack(anchor='w', padx=10, pady=5)

    label_none = Label(frame_hp, bg="#4682B4", borderwidth=0, height=500)
    label_none.pack()

    label = Label(root_homepage, text="   Trang chủ", fg="white", font=("Arial", 14, "bold"),
                  borderwidth=2, relief=RAISED, width=86, height=2, anchor='w', bg="#4682B4")
    label.place(x=306, y=0)

    label_content = Label(root_homepage, text="  XIN CHÀO, ĐÂY NÀ PHẦN MỀM CUTI CỦA CHÚNG TA ĐỂ VIẾT ZÔ CI ZI",
                          fg="blue", font=("Arial", 16, "bold"),
                          borderwidth=2, relief=RAISED, width=79, height=30, anchor=CENTER)
    label_content.place(x=311, y=50)

    root_homepage.mainloop()
