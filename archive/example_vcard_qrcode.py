import qrcode
import PIL
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

from  qrcode.image.styles.colormasks import ImageColorMask
from PIL import Image, ImageDraw

if not hasattr(PIL.Image, 'Resampling'):
    PIL.Image.Resampling = PIL.Image

# Now PIL.Image.Resampling.BICUBIC is always recognized. 

# Variables
img_file = 'oil.png'
card_data = '''
BEGIN:VCARD
VERSION:4.0
FN:Rachel Gugler
TEL;TYPE=mobile:+1 234-567-8910
EMAIL:name@email.com
END:VCARD
'''

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data(card_data)


qr_img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=ImageColorMask(color_mask_path=img_file),
)

qr_img.save('vcard_qrcode.png')