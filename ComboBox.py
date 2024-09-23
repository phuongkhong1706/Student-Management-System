from tkinter import *
from tkinter.ttk import Combobox

# Khởi tạo cửa sổ chính
ad_root_createaccount = Tk()
ad_root_createaccount.geometry("400x200")

# Tạo nhãn cho ComboBox
ad_label_find_moment = Label(ad_root_createaccount, text="Chọn một mục", font=("Arial", 10, "bold"),
                             fg="black", borderwidth=0)
ad_label_find_moment.place(x=50, y=50)

# Tạo danh sách lựa chọn cho ComboBox
options = ["A", "B", "C"]

# Tạo ComboBox
combo_box = Combobox(ad_root_createaccount, values=options, width=10, state="readonly")

# Đặt giá trị mặc định
combo_box.set("A")

# Đặt vị trí cho ComboBox
combo_box.place(x=200, y=50)

# Chạy giao diện
ad_root_createaccount.mainloop()
