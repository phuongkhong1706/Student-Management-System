import cv2
from deepface import DeepFace

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

# Hàm so sánh khuôn mặt
def compare_faces(image1_path, image2_path):
    result = DeepFace.verify(image1_path, image2_path)

    if result["verified"]:
        print("Khuôn mặt khớp với nhau!")
    else:
        print("Khuôn mặt không khớp!")

# Chụp ảnh từ camera và lưu lại
captured_image_path = "C://Users//DO TRUNG QUAN//Desktop//Itsempe.jpg"

# Đường dẫn tới ảnh có sẵn để so sánh
pre_existing_image_path = "C://Users//DO TRUNG QUAN//Desktop//Itsempe.jpg"

# So sánh khuôn mặt vừa chụp với ảnh có sẵn
compare_faces(captured_image_path, pre_existing_image_path)
