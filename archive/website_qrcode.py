import qrcode
import PIL
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import CircleModuleDrawer

from  qrcode.image.styles.colormasks import ImageColorMask
from PIL import Image, ImageDraw

if not hasattr(PIL.Image, 'Resampling'):
    PIL.Image.Resampling = PIL.Image

# Now PIL.Image.Resampling.BICUBIC is always recognized. 

# Variables
input_url = 'https://rachelgugler.com/'
img_file = 'algea.png'

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data(input_url)


qr_img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=CircleModuleDrawer(),
    color_mask=ImageColorMask(color_mask_path=img_file),
)

qr_img.save('website_qrcode.png')