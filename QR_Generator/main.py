'''
we are going  to us a python library like qr code and convert url to qr

'''
import qrcode
url =input("Enter your url: ")
filename=(input("filename you wanna save it as : "))
if not (filename.endswith(".png")):

    filename=filename + ".png"
img = qrcode.make(url)
img.save(filename)