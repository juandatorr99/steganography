from PIL import Image
import binascii
import optparse

def rgb2hex(r,g,b):
    return '#{:02x}{:02x}{:02x}'.format(r,g,b)

def hex2rgb(hexcode):
    return tuple(map(ord, hexcode[1:].decode('hex')))

def str2bin(message):
    binary = bin(int(binascii.hexlify(message),16))
    # not storing the 0b
    return binary[2:]

def bin2str(binary):
    message = binascii.unhexlify('%x' %(int('0b' + binary, 2)))
    return message

def encode(hexcode, digit):
    if(hexcode[-1] in ('0','1','2','3','4','5')):
        hexcode = hexcode[:-1]+digit
        return hexcode
    else:
        return None

def decode (hexcode):
    if(hexcode[-1] in ('0','1')):
        return hexcode[-1]
    else:
        return None

def hideInfo(filename, message):
    img = Image.open(filename)
    binary = str2bin(message) + '1111111111111110'
    if img.mode in ('RGBA'):
        img = img.convert('RGBA')
        datas = img.getdata()
