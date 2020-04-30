import png
import pyqrcode

def main():
    """ Main entry point of the app """
    Wifi_Name = 'xxxxx'
    Wifi_Protocol = 'WPA/WPA2'
    Wifi_Password = 'xxxxx'
    QRCode = pyqrcode.create(F'WIFI:S:{Wifi_Name};T:{Wifi_Protocol};P:{Wifi_Password};;')
    QRCode.svg('QRCode.svg', scale=8)
    QRCode.eps('QRCode.eps', scale=2)
    print(QRCode.terminal(quiet_zone=1))
    QRCode.png('abc.png', scale=8)
    print('QR Code Generated..')

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
