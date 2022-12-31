import qrcode

myqr = qrcode.QRCode(
    version=5,
    box_size=10,
    border=1
)

myqr.add_data("address")

img = myqr.make_image()
img.save("Name.png")