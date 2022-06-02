import qrcode

link = input('Enter link : ')

img = qrcode.make(link)

img.save("qr.png",'PNG')
