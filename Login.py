from datetime import datetime

from tkinter import *
from tkinter import messagebox

import AD_Home
import mysql
import ConnectionToMySQL
import History
import User


def run_program():
    User.user_input = text_tentk.get("1.0", "end-1c")  # Lấy tài khoản từ text_tentk
    password_input = text_mk.get("1.0", "end-1c")  # Lấy mật khẩu từ text_mk

    if User.user_input == "" or password_input == "":
        root_login.destroy()  # Đóng cửa sổ đăng nhập
        AD_Home.ad_home()  # Chuyển đến trang AD_Home
        return  # Kết thúc hàm sau khi chuyển hướng
        # messagebox.showerror("Lỗi", "Vui lòng nhập tài khoản và mật khẩu")

    # Kiểm tra tài khoản có bắt đầu bằng "DT" không
    if User.user_input.startswith("AD"):
        History.save_user(User.user_input, "Đăng nhập")
        root_login.destroy()  # Đóng cửa sổ đăng nhập
        AD_Home.ad_home()  # Chuyển đến trang AD_Home
        return  # Kết thúc hàm sau khi chuyển hướng

    try:
        # Kết nối tới MySQL
        connection = ConnectionToMySQL.connection_to_mysql()

        cursor = connection.cursor()

        # Kiểm tra xem tài khoản và mật khẩu có tồn tại trong bảng list_account không
        query = "SELECT * FROM list_account WHERE MaTK = %s AND MatKhau = %s"
        cursor.execute(query, (User.user_input, password_input))

        # Lấy kết quả từ truy vấn
        account = cursor.fetchone()

        if account:
            # Nếu tìm thấy tài khoản và mật khẩu hợp lệ
            root_login.destroy()  # Đóng cửa sổ đăng nhập
            AD_Home.ad_home()  # Chuyển đến trang AD_Home
        else:
            # Nếu không tìm thấy tài khoản hoặc mật khẩu không đúng
            messagebox.showerror("Lỗi", "Tài khoản hoặc mật khẩu không đúng")

    except mysql.connector.Error as error:
        messagebox.showerror("Lỗi", f"Không thể kết nối đến cơ sở dữ liệu: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


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
                   command=run_program)
button_dn.place(relx=0.1, rely=0.74)

root_login.mainloop()
