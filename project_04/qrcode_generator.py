# pip install qrcode
import qrcode

domains = ["google", "naver", "youtube", "netflix", "mdn"]

for d in domains:
    url = "www." + d + ".com"
    qr_img = qrcode.make(url)
    qr_img.save(url + ".png")
