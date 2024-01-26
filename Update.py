# install QRCode_Generate C:\Users\admincjgmd\AppData\Local\Programs\Python\Python39\python.exe E:\HOATMX\Python\Service\QRCode_Gen\QRCode_Generate.py

from flask import Flask, send_file, request
import qrcode
import os
from urllib.parse import quote

app = Flask(__name__)

@app.route('/generate_qr', methods=['GET'])
def generate_qr():
    data = request.args.get('data', '')
    size = request.args.get('size', '')

    # Chuyển đổi giá trị size sang kiểu tuple (width, height)
    try:
        width, height = map(int, size.split('x'))
    except ValueError:
        # Sử dụng giá trị mặc định hoặc thông báo lỗi
        width, height = 330, 350

    # Mã hóa dữ liệu trước khi thêm vào URL
    encoded_data = quote(data)

    # Path cho file hình
    # cache_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'qrcode.png')
    cache_path = os.path.join("E:/HOATMX/Python/Service/QRCode_Gen", 'qrcode.png')

    # Tạo QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=0,  # loại bỏ margin/border
    )
    qr.add_data(encoded_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Điều chỉnh kích thước ảnh
    img = img.resize((width, height))

    # Lưu QR code
    img.save(cache_path, 'PNG')

    # Trả về QR code
    return send_file(cache_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
