from tkinter import *
from PIL import Image, ImageTk


# def homepage():
root_homepage = Tk()
root_homepage.title("Trang chủ")
root_homepage.state("zoomed")

# Tạo canvas và scrollbar
canvas = Canvas(root_homepage, borderwidth=0)
scrollbar = Scrollbar(root_homepage, orient=VERTICAL, command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Tạo một frame bên trong canvas
frame_hp = Frame(canvas, width=270, borderwidth=0, bg="#34495E")
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


image_hp = create_image("C://Users//FUJITSU//PycharmProjects//StuManagement//icon//icons8-scaler-academy-144.png",
                        120, 120)
image_trangchu = create_image("C://Users//FUJITSU//PycharmProjects//StuManagement//icon//homepage.png", 50, 50)
image_tk = create_image("C://Users//FUJITSU//PycharmProjects//StuManagement//icon//account.png", 45, 45)
image_kqht = create_image("C://Users//FUJITSU//PycharmProjects//StuManagement//icon//kqht.png", 45, 45)
image_hdnk = create_image("C://Users//FUJITSU//PycharmProjects//StuManagement//icon//extraact.png", 45, 45)
image_kehoach = create_image("C://Users//FUJITSU//PycharmProjects//StuManagement//icon//learning.png", 45, 45)
image_hocphi = create_image("C://Users//FUJITSU//PycharmProjects//StuManagement//icon//tuitionfee.png", 45, 45)
image_logout = create_image("C://Users//FUJITSU//PycharmProjects//StuManagement//icon//logout.png", 45, 45)

label_hp = Label(frame_hp, height=150, image=image_hp, anchor=CENTER,
                 borderwidth=0, bg="#34495E")
label_hp.pack()

button_trangchu = Button(frame_hp, text="    Trang chủ", font=("Arial", 14, "bold"),
                   fg="white", bg="#34495E", borderwidth=0, compound="left", image=image_trangchu)
button_trangchu.pack(anchor='w', padx=10, pady=5)

button_tk = Button(frame_hp, text="    Tài khoản", font=("Arial", 14, "bold"),
                   fg="white", bg="#34495E", borderwidth=0, compound="left", image=image_tk)
button_tk.pack(anchor='w', padx=10, pady=5)

button_kqht = Button(frame_hp, text="    Kết quả học tập", font=("Arial", 14, "bold"),
                     fg="white", bg="#34495E", borderwidth=0, compound="left", image=image_kqht)
button_kqht.pack(anchor='w', padx=10, pady=5)

button_hdnk = Button(frame_hp, text="    Hoạt động ngoại khóa", font=("Arial", 14, "bold"),
                     fg="white", bg="#34495E", borderwidth=0, compound="left", image=image_hdnk)
button_hdnk.pack(anchor='w', padx=10, pady=5)

button_khht = Button(frame_hp, text="    Kế hoạch học tập", font=("Arial", 14, "bold"),
                     fg="white", bg="#34495E", borderwidth=0, compound="left", image=image_kehoach)
button_khht.pack(anchor='w', padx=10, pady=5)

button_hocphi = Button(frame_hp, text="    Học phí", font=("Arial", 14, "bold"),
                       fg="white", bg="#34495E", borderwidth=0, compound="left", image=image_hocphi)
button_hocphi.pack(anchor='w', padx=10, pady=5)

button_dx = Button(frame_hp, text="    Đăng xuất", font=("Arial", 14, "bold"),
                   fg="white", bg="#34495E", borderwidth=0, compound="left", image=image_logout)
button_dx.pack(anchor='w', padx=10, pady=5)

label_none = Label(frame_hp, bg="#34495E", borderwidth=0, height=500)
label_none.pack()

label = Label(root_homepage, text="   Trang chủ", fg="white", font=("Arial", 14, "bold"),
              borderwidth=2, relief=RAISED, width=86, height=2, anchor='w', bg="#34495E")
label.place(x=306, y=0)

label_content = Label(root_homepage, text="  XIN CHÀO, ĐÂY NÀ PHẦN MỀM CUTI CỦA CHÚNG TA ĐỂ VIẾT ZÔ CI ZI",
                      fg="blue", font=("Arial", 16, "bold"),
                      borderwidth=2, relief=RAISED, width=79, height=30, anchor=CENTER)
label_content.place(x=311, y=50)

root_homepage.mainloop()
