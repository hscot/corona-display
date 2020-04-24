from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!

disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear display.

disp.fill(0)
disp.show()