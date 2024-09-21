import cv2

# Tải mô hình phát hiện khuôn mặt từ OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Mở camera
cap = cv2.VideoCapture(0)

# Kiểm tra camera có mở thành công không
if not cap.isOpened():
    print("Không thể mở camera")
    exit()

while True:
    # Đọc khung hình từ camera
    ret, frame = cap.read()

    if not ret:
        print("Không thể nhận khung hình từ camera")
        break

    # Chuyển khung hình sang xám để phát hiện khuôn mặt
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Phát hiện các khuôn mặt
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Vẽ khung hình chữ nhật xung quanh mỗi khuôn mặt
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Tự động chụp ảnh khi phát hiện khuôn mặt
        if len(faces) > 0:
            cv2.imwrite('face_capture.png', frame)
            print("Đã chụp ảnh khuôn mặt!")
            break

    # Hiển thị khung hình
    cv2.imshow('Camera', frame)

    # Nhấn phím 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên và đóng cửa sổ
cap.release()
cv2.destroyAllWindows()