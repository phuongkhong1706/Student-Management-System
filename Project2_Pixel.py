import cv2

# Đọc hình ảnh
image = cv2.imread("C://Users//DO TRUNG QUAN//Desktop//Test_Image.png")

# Hàm xử lý sự kiện chuột
def show_pixel_value(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        # Kiểm tra nếu tọa độ nằm trong phạm vi của hình ảnh
        if x < image.shape[1] and y < image.shape[0]:
            pixel_value = image[y, x]
            # Hiển thị giá trị pixel (BGR)
            print(f"Pixel tại ({x}, {y}) - Giá trị BGR: {pixel_value}")

# Tạo một cửa sổ để hiển thị hình ảnh
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', show_pixel_value)

while True:
    # Hiển thị hình ảnh
    cv2.imshow('Image', image)

    # Nhấn phím ESC để thoát
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Đóng tất cả các cửa sổ
cv2.destroyAllWindows()
