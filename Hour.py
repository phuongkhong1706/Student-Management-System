import tkinter as tk
from tkcalendar import DateEntry

def get_selected_datetime():
    selected_date = date_entry.get()
    selected_hour = hour_spinbox.get()
    selected_minute = minute_spinbox.get()
    print(f"Ngày được chọn: {selected_date}, Giờ: {selected_hour}:{selected_minute}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chọn ngày và giờ")

# Widget chọn ngày
tk.Label(root, text="Chọn ngày:").pack(pady=5)
date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
date_entry.pack(pady=5)

# Widget chọn giờ (Spinbox)
tk.Label(root, text="Chọn giờ:").pack(pady=5)
frame_time = tk.Frame(root)
frame_time.pack(pady=5)

# Spinbox cho giờ và phút
hour_spinbox = tk.Spinbox(frame_time, from_=0, to=23, width=3, format='%02.0f')
minute_spinbox = tk.Spinbox(frame_time, from_=0, to=59, width=3, format='%02.0f')

hour_spinbox.pack(side='left', padx=(0, 10))
minute_spinbox.pack(side='left')

# Nút để in giá trị đã chọn
button = tk.Button(root, text="In ngày và giờ", command=get_selected_datetime)
button.pack(pady=20)

# Chạy chương trình
root.mainloop()
