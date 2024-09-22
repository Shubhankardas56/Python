import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image


qr=pyqrcode.create('http://mywebprojectt20premierleague.herokuapp.com')
qr.png('MyT20League.png',scale=8)

d=decode(Image.open('MyT20League.png'))
print(d)
