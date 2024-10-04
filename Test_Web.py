import tkinter as tk
from tkinter import messagebox
import webbrowser


# Hàm mở trang web chuyển tiền
def open_transfer_page():
    amount = entry_amount.get()
    recipient = entry_recipient.get()

    if not amount or not recipient:
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
        return

    try:
        # Chuyển số tiền sang dạng số để kiểm tra
        amount = float(amount)
        if amount <= 0:
            raise ValueError

        # Mở trình duyệt với trang web chuyển tiền (URL giả định)
        webbrowser.open(f"https://www.examplebank.com/transfer?amount={amount}&recipient={recipient}")

        # Hiển thị thông báo thành công
        messagebox.showinfo("Thành công", "Chuyển tiền thành công!")
    except ValueError:
        messagebox.showerror("Lỗi", "Số tiền không hợp lệ!")


# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chuyển tiền")
root.geometry("400x250")

# Tiêu đề
label_title = tk.Label(root, text="Giao diện Chuyển tiền", font=("Arial", 16))
label_title.pack(pady=10)

# Nhập số tiền
label_amount = tk.Label(root, text="Số tiền:")
label_amount.pack()
entry_amount = tk.Entry(root)
entry_amount.pack(pady=5)

# Nhập người nhận
label_recipient = tk.Label(root, text="Người nhận:")
label_recipient.pack()
entry_recipient = tk.Entry(root)
entry_recipient.pack(pady=5)

# Nút chuyển tiền
button_transfer = tk.Button(root, text="Chuyển tiền", command=open_transfer_page)
button_transfer.pack(pady=20)

# Chạy giao diện
root.mainloop()
