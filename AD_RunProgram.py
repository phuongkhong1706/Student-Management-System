from tkinter import *

# Hàm chuyển đổi giữa các form
def switch_to_form(form, current_form_label):
    form.tkraise()  # Đưa form lên trên cùng
    current_form.set(current_form_label)  # Cập nhật nhãn của form hiện tại

# Hàm tạo form mới có giao diện giống form home
def create_new_form(master, form_name):
    frame = Frame(master)
    label = Label(frame, text=form_name, font=("Arial", 16))
    label.pack(pady=20)

    # Hiển thị giao diện button Form Home để quay lại trang chính
    button_home = Button(frame, text="Form Home", command=lambda: switch_to_form(form_home, "Form Home"))
    button_home.pack(pady=5)

    frame.grid(row=0, column=0, sticky='nsew')
    return frame

# Tạo cửa sổ chính
root = Tk()
root.title("Form Switching Example")
root.geometry("400x300")

# Biến lưu trạng thái form hiện tại
current_form = StringVar(value="Form Home")

# Tạo form chính (home)
form_home = Frame(root)
label_home = Label(form_home, textvariable=current_form, font=("Arial", 16))
label_home.pack(pady=20)

# Tạo Frame cho các nút Form 1
form1_frame = Frame(form_home)
button_form1 = Button(form1_frame, text="Form 1", command=lambda: switch_to_form(form1, "Form 1"))
button_form1.pack(side=LEFT, padx=10)
form1_frame.pack()

# Tạo Frame cho các nút Form 2
form2_frame = Frame(form_home)
button_form2 = Button(form2_frame, text="Form 2", command=lambda: switch_to_form(form2, "Form 2"))
button_form2.pack(side=LEFT, padx=10)
form2_frame.pack()

form_home.grid(row=0, column=0, sticky='nsew')

# Tạo các form 1 và 2
form1 = create_new_form(root, "Form 1")
button_form11 = Button(form1, text="Form 11", font=("Arial", 12, "bold"), command=lambda: update_menu(1, 11))
button_form11.pack(pady=5)

button_form12 = Button(form1, text="Form 12", command=lambda: update_menu(1, 12))
button_form12.pack(pady=5)

form2 = create_new_form(root, "Form 2")
button_form21 = Button(form2, text="Form 21", font=("Arial", 12, "bold"), command=lambda: update_menu(2, 21))
button_form21.pack(pady=5)

button_form22 = Button(form2, text="Form 22", command=lambda: update_menu(2, 22))
button_form22.pack(pady=5)

# Tạo các form con của Form 1 và Form 2
form11 = create_new_form(root, "Form 11")
form12 = create_new_form(root, "Form 12")
form21 = create_new_form(root, "Form 21")
form22 = create_new_form(root, "Form 22")

# Hiển thị form home đầu tiên
switch_to_form(form_home, "Form Home")

# Chạy vòng lặp chính của ứng dụng
root.mainloop()
