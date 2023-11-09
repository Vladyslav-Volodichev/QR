from unicodedata import name
import qrcode

def get_qrcode(url='Instagram.com', name='QR '):
    qr = qrcode.make(data=url)
    qr.save(stream=f'{name}.png')

    return f'QR code was created! Open the {name}.png'
#in url enter the link to creat QR code
def main():
    print(get_qrcode(url='+32486296520', name='instawhatssoup'))


if __name__ =='__main__':
    main()




