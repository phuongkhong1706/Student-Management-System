import cv2
import face_recognition

# Hàm chụp ảnh từ camera
def capture_image():
    cap = cv2.VideoCapture(0)  # Mở camera
    while True:
        ret, frame = cap.read()  # Đọc frame từ camera
        if not ret:
            break

        # Hiển thị frame trên cửa sổ
        cv2.imshow("Press Space to Capture", frame)

        # Chờ người dùng nhấn phím Space để chụp ảnh
        if cv2.waitKey(1) & 0xFF == ord(' '):
            # Lưu ảnh chụp lại
            image_path = "captured_image.jpg"
            cv2.imwrite(image_path, frame)
            print(f"Image saved as {image_path}")
            break

    cap.release()
    cv2.destroyAllWindows()
    return image_path

# Hàm so sánh khuôn mặt giữa ảnh chụp và ảnh có sẵn
def compare_faces(image1_path, image2_path):
    # Load ảnh và tìm mã nhận diện khuôn mặt
    img1 = face_recognition.load_image_file(image1_path)
    img2 = face_recognition.load_image_file(image2_path)

    # Tìm mã nhận diện khuôn mặt (encoding) từ ảnh
    encodings_img1 = face_recognition.face_encodings(img1)
    encodings_img2 = face_recognition.face_encodings(img2)

    # Kiểm tra nếu không tìm thấy khuôn mặt trong một trong hai ảnh
    if len(encodings_img1) == 0 or len(encodings_img2) == 0:
        print("Không phát hiện được khuôn mặt trong một trong hai ảnh.")
        return

    # Lấy mã nhận diện khuôn mặt đầu tiên
    encoding1 = encodings_img1[0]
    encoding2 = encodings_img2[0]

    # So sánh mã nhận diện khuôn mặt
    results = face_recognition.compare_faces([encoding1], encoding2)
    if results[0]:
        print("Khuôn mặt khớp với nhau!")
    else:
        print("Khuôn mặt không khớp!")

# Chụp ảnh từ camera
captured_image_path = capture_image()

# Đường dẫn tới ảnh có sẵn để so sánh
pre_existing_image_path = "D://HUST//testKTHP.jpg"

# So sánh hai khuôn mặt
compare_faces(captured_image_path, pre_existing_image_path)
