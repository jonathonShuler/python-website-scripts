
import requests
from bs4 import BeautifulSoup
from playsound import playsound
from selenium import webdriver
import time

url_ip = 'https://www.google.com/search?q=what+is+my+ip+address'
url_one = 'https://www.bestbuy.com/site/evga-rtx-3080-xc3-ultra-gaming-10g-p5-3885-kh-pci-express-4-0-lhr/6471615.p?skuId=6471615'
url_two = 'https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-ultra-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6439299.p?skuId=6439299'

flag_ip = False
flag_one = True
flag_two = True

add_cart = False

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

def check_ip():
    print("Checking ip")
    
    page = requests.get(url_ip, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    ip_div = soup.select('div.NEM4H')
    ip_address = ip_div[0].get_text()
    print(ip_address)

def check_one():
    print("Checking Item One")
    
    page = requests.get(url_one, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    fulfillment_css_selector = 'div.fulfillment-fulfillment-summary'
    fulfillment = soup.select(fulfillment_css_selector)
    fulfillment_text = fulfillment[0].get_text()
    print("fulfillment: " + fulfillment_text)

    button_css_selector = 'button[data-sku-id="6471615"]'
    button = soup.select(button_css_selector)
    button_text = button[0].get_text()
    print("button: " + button_text)
    
    if fulfillment_text != "Sold Out" or button_text != "Sold Out":
        if add_cart:
            add_to_cart(url_one, button_css_selector)
            print("Item One In Stock!!!")
            while True:
                playsound('Synthwave-CC0.wav')
        else:
            print("Item One In Stock?!!!")
            while True:
                playsound('Synthwave-CC0.wav')
    else:
        print("Item One Not In Stock... Sleeping...")
        time.sleep(4)

def check_two():
    print("Checking Item Two")
    
    page = requests.get(url_two, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    fulfillment_css_selector = 'div.fulfillment-fulfillment-summary'
    fulfillment = soup.select(fulfillment_css_selector)
    fulfillment_text = fulfillment[0].get_text()
    print("fulfillment: " + fulfillment_text)

    button_css_selector = 'button[data-sku-id="6439299"]'
    button = soup.select(button_css_selector)
    button_text = button[0].get_text()
    print("button: " + button_text)
    
    if fulfillment_text != "Sold Out" or button_text != "Sold Out":
        if add_cart:
            add_to_cart(url_two, button_css_selector)
            print("Item Two In Stock!!!")
            while True:
                playsound('Synthwave-CC0.wav')
        else:
            print("Item Two In Stock?!!!")
            while True:
                playsound('Synthwave-CC0.wav')
    else:
        print("Item Two Not In Stock... Sleeping...")
        time.sleep(4)
        
def add_to_cart(url, selector):
    driver = webdriver.Chrome()
    driver.get(url)
    element = driver.find_element_by_button_css_selector(selector)
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
