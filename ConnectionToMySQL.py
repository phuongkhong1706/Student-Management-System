import mysql
def connection_to_mysql():
    # Kết nối đến MySQL
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='dotrungquan183@',  # Đặt mật khẩu của bạn
        database='student_management'  # Tên database
    )
    return connection