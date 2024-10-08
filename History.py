from datetime import datetime
import mysql.connector
from ConnectionToMySQL import connection_to_mysql

def save_user(user_input, action):
    # Kết nối tới cơ sở dữ liệu
    connection = connection_to_mysql()

    cursor = connection.cursor()

    try:
        # Lấy thông tin từ bảng list_create theo MaSo
        query = "SELECT DoiTuongSuDung, HoVaTen FROM list_create WHERE MaSo = %s"
        cursor.execute(query, (user_input,))
        result = cursor.fetchone()

        if result is None:
            print(f"Không tìm thấy MaSo: {user_input}")
            return

        DoiTuongSuDung, HoVaTen = result

        # Lấy thời gian hiện tại và định dạng theo yêu cầu
        ThoiGian = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Thêm dữ liệu vào bảng list_history
        insert_query = """
        INSERT INTO list_history (MaSo, ThoiGian, DoiTuongSuDung, HoVaTen, HoatDong)
        VALUES (%s, %s, %s, %s, %s)
        """
        data_to_insert = (user_input, ThoiGian, DoiTuongSuDung, HoVaTen, action)
        cursor.execute(insert_query, data_to_insert)

        # Lưu thay đổi vào cơ sở dữ liệu
        connection.commit()
        print("Thông tin đã được lưu vào bảng list_history.")

    except mysql.connector.Error as error:
        print(f"Lỗi khi lưu dữ liệu: {error}")

    finally:
        cursor.close()
        connection.close()
