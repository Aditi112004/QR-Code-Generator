import qrcode
from PIL import Image
upi_link = "upi://pay?pa=yourupi@upi&pn=YourName&mc=0000&tid=000000000000&tr=1234567890&tn=Payment%20for%20services&am=10.00&cu=INR&url="

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=50,border=10,)
qr.add_data("aditikurkote@okaxis")
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save("upi.png")