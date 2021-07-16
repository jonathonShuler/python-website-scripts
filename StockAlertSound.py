
import requests
from bs4 import BeautifulSoup
from playsound import playsound
from selenium import webdriver
import smtplib
import time

url_ip = 'https://www.google.com/search?q=what+is+my+ip+address'
url_one = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442'
url_two = 'https://www.bestbuy.com/site/corsair-vengeance-lpx-32gb-2-x-16gb-3-2-ghz-ddr4-c16-desktop-memory/6448611.p?skuId=6448611'

flag_ip = False
flag_one = True
flag_two = False

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

def check_ip():
    print("Checking ip")
    
    page = requests.get(url_ip, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    ip_div = soup.select('div.NEM4H')
    ip_address = ip_div[0].get_text()
    print(ip_address)

def check_one():
    print("Checking 3070")
    
    page = requests.get(url_one, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    css_selector = 'button[data-sku-id="6429442"]'
    button = soup.select(css_selector)
    text = button[0].get_text();
    print(text)
    
    if(text != "Sold Out"):
        add_to_cart(url_one, css_selector);
        print("3070 In Stock!!!")
        while True:
            playsound('Synthwave-CC0.wav')
    else:
        print("3070 Not In Stock... Sleeping...")
        time.sleep(15)

def check_two():
    print("Checking Memory")
    
    page = requests.get(url_two, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    css_selector = 'button[data-sku-id="6448611"]'
    button = soup.select(css_selector)
    text = button[0].get_text();
    print(text)
    
    if(text != "Sold Out"):
        add_to_cart(url_two, css_selector);
        print("Memory In Stock!!!")
        while True:
            playsound('Synthwave-CC0.wav')
    else:
        print("Memory Not In Stock... Sleeping...")
        time.sleep(15)
        
def add_to_cart(url, selector):
    driver = webdriver.Chrome();
    driver.get(url);
    element = driver.find_element_by_css_selector(selector);
    element.click()
    while(True):
       playsound('Synthwave-CC0.wav')

loop_count = 0
while flag_ip or flag_one or flag_two:
    print(loop_count)
    
    if flag_ip and (loop_count == 0 or loop_count % 30 == 0):
        check_ip()
    
    if flag_one:
        check_one()
        
    if flag_two:
        check_two()
        
    loop_count += 1
