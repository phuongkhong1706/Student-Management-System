from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Trang chủ với giao diện chuyển tiền
@app.route('/')
def index():
    return render_template('index.html')


# Xử lý chuyển tiền sau khi người dùng nhấn nút
@app.route('/transfer', methods=['POST'])
def transfer():
    amount = request.form['amount']
    recipient = request.form['recipient']

    if not amount or not recipient:
        return "Vui lòng nhập đầy đủ thông tin!", 400

    try:
        # Kiểm tra tính hợp lệ của số tiền
        amount = float(amount)
        if amount <= 0:
            return "Số tiền không hợp lệ!", 400

        # Giả lập chuyển tiền
        return f"Chuyển {amount} cho {recipient} thành công!"
    except ValueError:
        return "Số tiền không hợp lệ!", 400


if __name__ == '__main__':
    app.run(debug=True)
