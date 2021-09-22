import requests
from bs4 import BeautifulSoup
from playsound import playsound
from selenium import webdriver
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/87.0.4280.88 Safari/537.36'}
add_cart = True
wait_duration = 2


class Product:
    def __init__(self, url, selector, description, flag):
        self.url = url
        self.selector = selector
        self.description = description
        self.flag = flag


urlA = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum' \
       '-and-black/6429442.p?skuId=6429442 '
productA = Product(urlA, "button[data-sku-id='6429442']", 'FE 3070', True)

urlB = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and' \
       '-black/6429440.p?skuId=6429440 '
productB = Product(urlB, "button[data-sku-id='6429440']", 'FE 3080', True)

url1 = 'https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-ultra-gaming-8gb-gddr6-pci-express-4-0-graphics-card' \
       '-light-hash-rate/6479528.p?skuId=6479528 '
product1 = Product(url1, "button[data-sku-id='6479528']", 'EVGA 3070 KL', True)

url2 = 'https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-ultra-gaming-8gb-gddr6-pci-express-4-0-graphics-card' \
       '-light-hash-rate/6477077.p?skuId=6477077 '
product2 = Product(url2, "button[data-sku-id='6477077']", 'EVGA 3070 KH', True)

url3 = 'https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-ultra-gaming-8gb-gddr6-pci-express-4-0-graphics-card' \
       '/6439299.p?skuId=6439299 '
product3 = Product(url3, "button[data-sku-id='6439299']", 'EVGA 3070', True)

url4 = 'https://www.bestbuy.com/site/evga-rtx-3080-xc3-ultra-gaming-10g-p5-3885-kh-pci-express-4-0-lhr/6471615.p' \
       '?skuId=6471615 '
product4 = Product(url4, "button[data-sku-id='6471615']", 'EVGA 3080 KH', True)

url5 = 'https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6-pci-express-4-0-graphics-card' \
       '/6432400.p?skuId=6432400 '
product5 = Product(url5, "button[data-sku-id='6432400']", 'EVGA 3080', True)

products = [product1, product2, product3]
loop_count = 0


def check_product(product):
    print("Checking {0}".format(product.description))

    page = requests.get(product.url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    fulfillment_css_selector = 'div.fulfillment-fulfillment-summary'
    fulfillment = soup.select(fulfillment_css_selector)
    fulfillment_text = fulfillment[0].get_text()
    print("{0}: fulfillment: {1}".format(product.description, fulfillment_text))

    button_css_selector = product.selector
    button = soup.select(button_css_selector)
    button_text = button[0].get_text()
    print("{0}: button: {1}".format(product.description, button_text))

    if fulfillment_text != "Sold Out" or button_text != "Sold Out":
        if add_cart and button_text != "Sold Out":
            add_to_cart(product.url, button_css_selector)
            print("{0} In Stock?!!!".format(product.description))
            while True:
                playsound('Synthwave-CC0.wav')
        else:
            print("{0} In Stock?!!!".format(product.description))
            while True:
                playsound('Synthwave-CC0.wav')
    else:
        print("{0} Not In Stock... Sleeping...".format(product.description))
        time.sleep(wait_duration)


def add_to_cart(url, selector):
    driver = webdriver.Chrome()
    driver.get(url)
    element = driver.find_element_by_css_selector(selector)
    element.click()
    while True:
        playsound('Synthwave-CC0.wav')


while True:
    print(loop_count)

    for item in products:
        if item.flag:
            try:
                check_product(item)
            except requests.exceptions.ConnectionError as error:
                print("Request failed, for some reason", error)

    loop_count += 1
