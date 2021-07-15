
import requests
from bs4 import BeautifulSoup
from playsound import playsound
import smtplib
import time

url_ip = 'https://www.google.com/search?q=what+is+my+ip+address'
url_nvidia = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442'
url_evga = 'https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6432400.p?skuId=6432400'

flag_ip = False
flag_nvidia = True
flag_evga = False

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

def check_ip():
    print("Checking ip")
    
    page = requests.get(url_ip, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    ip_div = soup.select('div.NEM4H')
    ip_address = ip_div[0].get_text()
    print(ip_address)

def check_nvidia():
    print("Checking 3070")
    
    page = requests.get(url_nvidia, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    button = soup.select('button[data-sku-id]')
    text = button[0].get_text();
    print(text)
    
    if(text != "Sold Out"):
        print("3070 In Stock!!!")
        while True:
            playsound('Synthwave-CC0.wav')
    else:
        print("3070 Not In Stock... Sleeping...")
        time.sleep(15)

def check_evga():
    print("Checking EVGA 3080")
    
    page = requests.get(url_evga, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    button = soup.select('button[data-sku-id]')
    text = button[0].get_text();
    print(text)
    
    if(text != "Sold Out"):
        print("EVGA 3080 In Stock!!!")
        while True:
            playsound('Synthwave-CC0.wav')
    else:
        print("EVGA 3080 Not In Stock... Sleeping...")
        time.sleep(15)

loop_count = 0
while flag_ip or flag_nvidia or flag_evga:
    print(loop_count)
    
    if flag_ip and (loop_count == 0 or loop_count % 30 == 0):
        check_ip()
    
    if flag_nvidia:
        check_nvidia()
        
    if flag_evga:
        check_evga()
        
    loop_count += 1
