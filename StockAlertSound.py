
import requests
from bs4 import BeautifulSoup
from playsound import playsound
import smtplib
import time

url_ip = 'https://www.google.com/search?q=what+is+my+ip+address'
url_3080 = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440'

flag_ip = True
flag_3080 = True

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

def check_ip():
    print("Checking ip")
    
    page = requests.get(url_ip, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    ip_div = soup.select('div.NEM4H')
    ip_address = ip_div[0].get_text()
    print(ip_address)

def check_3080():
    print("Checking 3080")
    
    page = requests.get(url_3080, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    button = soup.select('button[data-sku-id]')
    text = button[0].get_text();
    print(text)
    
    if(text != "Sold Out"):
        print("3080 In Stock!!!")
        while True:
            playsound('Synthwave-CC0.wav')
    else:
        print("3080 Not In Stock... Sleeping...")
        time.sleep(30)
        
loop_count = 0
while flag_ip or flag_3080:
    print(loop_count)
    
    if flag_ip and loop_count == 0 or loop_count % 10 == 0:
        check_ip()
    
    if flag_3080:
        check_3080()
        
    loop_count += 1
