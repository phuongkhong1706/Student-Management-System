import cv2

# Đọc hình ảnh
image = cv2.imread("C://Users//DO TRUNG QUAN//Desktop//Test_Image.png")

# Kiểm tra nếu hình ảnh không được tải thành công
if image is None:
    print("Không thể đọc hình ảnh. Vui lòng kiểm tra đường dẫn.")
    exit()

# Chuyển đổi hình ảnh sang mức xám
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Hàm xử lý sự kiện chuột
def show_pixel_value(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        # Kiểm tra nếu tọa độ nằm trong phạm vi của hình ảnh
        if x < gray_image.shape[1] and y < gray_image.shape[0]:
            pixel_value = gray_image[y, x]
            # Hiển thị giá trị mức xám
            print(f"Pixel tại ({x}, {y}) - Mức xám: {pixel_value}")

# Tạo một cửa sổ để hiển thị hình ảnh
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', show_pixel_value)

while True:
    # Hiển thị hình ảnh mức xám
    cv2.imshow('Image', gray_image)

    # Nhấn phím ESC để thoát
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Đóng tất cả các cửa sổ
cv2.destroyAllWindows()
