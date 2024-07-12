import qrcode
# a library to generate QR codes
# pip install qrcode
# pip install pillow for processing the qr image

image = qrcode.make('https://127.0.0.1:8000')
# makes a qrcode image linking to the above url

image.save('qr.png')
# saves the image with a file name