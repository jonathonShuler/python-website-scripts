# Based on this tutorial: https://www.youtube.com/watch?v=X7hXR_1eA5c


import requests
from bs4 import BeautifulSoup
from playsound import playsound
import smtplib
import time

tumbler_url = 'https://www.rockshed.com/rock-shop/rock-tumblers-supplies/rock-tumblers/rotary-rock-tumblers/lortone-model-qt12-single-12lb-capacity-barrel/'
console_url = 'https://direct.playstation.com/en-us/consoles/console/playstation5-digital-edition-console.3005817'

tumbler_flag = True
console_flag = True

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

def check_tumbler():
    print("Checking Tumbler")
    
    page = requests.get(tumbler_url, headers=headers)
    bs = BeautifulSoup(page.content, 'html.parser')

    stock = bs.find(class_ = "stock out-of-stock").get_text()
    if(stock != "Out of stock"):
        send_email("QT12 In Stock!!!")
        playsound('Synthwave-CC0.wav')
        global tumbler_flag
        tumbler_flag = False
        print("QT12 In Stock!!!")

def check_console():
    print("Checking Console")

    page = requests.get(console_url, headers=headers)
    bs = BeautifulSoup(page.content, 'html.parser')

    stock = bs.find(class_ = "out-stock-wrpr").find(class_ = "sony-text-body-1").get_text()
    if(stock != "Out of Stock"):
        send_email("PS5 In Stock!!!")
        playsound('Synthwave-CC0.wav')
        global console_flag
        console_flag = False
        print("PS5 In Stock!!!")

def send_email(message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('from@email.com', 'google app password')

    server.sendmail('from@email.com','to@email.com', message)
    server.quit()

while tumbler_flag or console_flag:

    if tumbler_flag == True:
        check_tumbler()
        
    print("Sleeping")
    time.sleep(60)

    if console_flag == True:
        check_console()

    print("Sleeping")
    time.sleep(60)
