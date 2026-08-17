import qrcode

url = "https://TEN-GITHUB-CUA-BON.github.io/thu-gui-bo/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=4
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(
    fill_color="black",
    back_color="white"
)

img.save("QR_Thu_Gui_Bo.png")

print("✅ Đã tạo QR: QR_Thu_Gui_Bo.png")