import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = """ 
        Company Name: MisTech
        Contact No.: 02269569692
        Website : mistech.co.in
        Email: mistech.official02@gmail.com
        GSTIN : 27LQEPS0449C1ZO
        Address : Office Block B1, Near 
        Business Park, Airoli, Sector 12.
    """
  
# Generate QR code 
url = pyqrcode.create(s)
  
# Create and save the png file naming "myqr.png" 
url.svg("myqrcode.svg", scale = 2)
