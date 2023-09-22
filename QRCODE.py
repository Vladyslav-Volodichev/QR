from unicodedata import name
import qrcode

def get_qrcode(url='Instagram.com', name='QR '):
    qr = qrcode.make(data=url)
    qr.save(stream=f'{name}.png')

    return f'QR code was created! Open the {name}.png'
#в url вставить ссылку по которой будет создан QR код 
def main():
    print(get_qrcode(url='', name='instawhatssoup'))


if __name__ =='__main__':
    main()




