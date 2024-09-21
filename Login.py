from tkinter import *
from tkinter import ttk
import Homepage  # Import file homepage.py


def open_homepage():
    root_login.destroy()
    Homepage.homepage()


root_login = Tk()
root_login.title("Đăng nhập")

root_login.state('zoomed')

label_dn = Label(root_login, text="ĐĂNG NHẬP BẰNG TÀI KHOẢN", font=("Arial", 25, "bold"), fg="#34495E")
label_dn.place(relx=0.5, rely=0.16, anchor=CENTER)  # Đặt ở phía trên cửa sổ

frame = Frame(root_login, height=340, width=450, borderwidth=3, bg="white")
frame.place(relx=0.5, rely=0.5, anchor=CENTER)  # Đặt khung ở giữa màn hình

label_tentk = Label(frame, text="Tài khoản", font=("Arial", 12, "bold"), fg="#34495E", bg="white")
label_tentk.place(relx=0.1, rely=0.1)

text_tentk = Text(frame, width=44, height=1.5, borderwidth=1, relief=SOLID)
text_tentk.place(relx=0.1, rely=0.2)

label_mk = Label(frame, text="Mật khẩu", font=("Arial", 12, "bold"), fg="#34495E", bg="white")
label_mk.place(relx=0.1, rely=0.37)

text_mk = Text(frame, width=44, height=1.5, borderwidth=1, relief=SOLID)
text_mk.place(relx=0.1, rely=0.47)

button_quenmk = Button(frame, width=12, height=1, text="Quên mật khẩu?", fg="#34495E", bg="white", relief=FLAT)
button_quenmk.place(relx=0.693, rely=0.6)

button_dn = Button(frame, width=29, height=1, text="Đăng nhập", font=("Arial", 14, "bold"), bg="#34495E", fg="white",
                   command=open_homepage)
button_dn.place(relx=0.1, rely=0.74)

root_login.mainloop()
