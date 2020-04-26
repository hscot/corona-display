import time
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from bs4 import BeautifulSoup
import requests
import sys
import math
#This is the following code from the Adafruit Learn Page for the ssd1306 display. I will leave the original code and comments here!
# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)
# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
# Clear display.
disp.fill(0)
disp.show()
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0
# Load default font.
font = ImageFont.load_default()




#Here is the updated code from the original LCD display, updated for use with the OLED display
while True:
    for i in range(5):

        # Insert your country URL here
        url_b = "https://corona.help/country/united-states"
        url_c = "https://corona.help/country/united-states"

        # Insert your country Population here
        population_c = "8173166"
        population_w = "7770173166" # World-population
        url_w ="https://corona.help/"
        # Your Country-Code
        cc = "US"

        page_b = requests.get(url_b)
        soup_b = BeautifulSoup(page_b.text, 'html.parser')
        page_c = requests.get(url_c)
        soup_c = BeautifulSoup(page_c.text, 'html.parser')
        page_w = requests.get(url_w)
        soup_w = BeautifulSoup(page_w.text, 'html.parser')

        #print (soup_c)ython

        country_b = soup_b.select('h2')[0].text.strip()
        infections_b = soup_b.select('h2')[1].text.strip()
        deaths_b = soup_b.select('h2')[3].text.strip()
        survived_b = soup_b.select('h2')[5].text.strip()
        today_b = soup_b.select('h2')[2].text.strip()

        first_b = country_b.rsplit(' ',1)[0]

        country_c = soup_c.select('h2')[0].text.strip()
        infections_c = soup_c.select('h2')[1].text.strip()
        deaths_c = soup_c.select('h2')[3].text.strip()
        survived_c = soup_c.select('h2')[5].text.strip()
        today_c = soup_c.select('h2')[2].text.strip()

        first_c = country_c.rsplit(' ',1)[0]
            
        infections_w = soup_w.select('h2')[1].text.strip()
        deaths_w = soup_w.select('h2')[3].text.strip()
        survived_w = soup_w.select('h2')[5].text.strip()
        today_w = soup_w.select('h2')[2].text.strip()

        #Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        time.sleep(1)

        #Begin display information
        draw.text((x, top + 0), (first_c), font=font, fill=255)
        draw.text((x, top + 8), "Infected " + (infections_c), font=font, fill=255)
        draw.text((x, top + 16), "Worldwide", font=font, fill=255)
        draw.text((x, top + 24), "Infected " + (infections_w), font=font, fill=255)
        disp.image(image)
        disp.show()
        time.sleep(5)

        #The same code as before, but this one is displaying death information
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x, top + 0), (first_c), font=font, fill=255)
        draw.text((x, top + 8), ("Deaths ") + (deaths_c), font=font, fill=255)
        draw.text((x, top + 16), "Worldwide", font=font, fill=255)
        draw.text((x, top + 24), ("Deaths ") + (deaths_w), font=font, fill=255)
        disp.image(image)
        disp.show()
        time.sleep(5)
        
        #Recoveries
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x, top + 0), (first_c), font=font, fill=255)
        draw.text((x, top + 8), "Recovered" + (survived_c), font=font, fill=255)
        draw.text((x, top + 16), "Worldwide", font=font, fill=255)
        draw.text((x, top + 24), (survived_w), font=font, fill=255)
        disp.image(image)
        disp.show()
        time.sleep(5)

        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x, top + 0), "COVID-19 Tracker", font=font, fill=255)
        draw.text((x, top + 8), "By Julain Bruegger", font=font, fill=255)
        draw.text((x, top + 16), "Adapted for OLED", font=font, fill=255)
        draw.text((x, top + 24), "By Harrison Thow", font=font, fill=255)
        disp.image(image)
        disp.show()
        print(i)    
        time.sleep(5)
    time.sleep(5)

        

