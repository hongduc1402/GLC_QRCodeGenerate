<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generate QR Code</title>
    <!-- Thêm thư viện jQuery -->
    <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
</head>
<body>

<script>
    // Hàm để mã hóa dữ liệu và tạo QR code
    function generateQRFromURL() {
        // Lấy dữ liệu từ URL
        var urlParams = new URLSearchParams(window.location.search);
        var data = urlParams.get('data');
        var size = urlParams.get('size');

        // Nếu có dữ liệu và size, thực hiện tạo QR code
        if (data && size) {
            // Mã hóa ký tự "#" thành "%23"
            var encodedData = encodeURIComponent(data);

            // Tạo URL với dữ liệu đã mã hóa và size
            var qrCodeURL = "http://127.0.0.1:8000/generate_qr?data=" + encodedData + "&size=" + size;

            // Gửi yêu cầu đến máy chủ để tạo QR code
            $.ajax({
                url: qrCodeURL,
                method: "GET",
                success: function () {
                    // Xử lý khi yêu cầu thành công
                    console.log("QR code generated successfully");
                },
                error: function () {
                    // Xử lý khi có lỗi xảy ra
                    console.error("Failed to generate QR code");
                }
            });
        }
    }

    // Gọi hàm khi trang web được tải
    $(document).ready(function () {
        generateQRFromURL();
    });

</script>

</body>
</html>
