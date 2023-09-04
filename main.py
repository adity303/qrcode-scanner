import qrcode
import qrcode as qr

#simple 2 line code for qr code
#img= qr.make("https://github.com/adity303")
#img.save("ADITYA_GITHUB.png")

#advanced form of generating qr code
from PIL import Image

qr=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=20,border=4,)

qr.add_data("https://github.com/adity303")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("Aditya_github.png")



