import requests
from bs4 import BeautifulSoup
from playsound import playsound
import smtplib
import time

test_url = 'https://www.amazon.com/DualSense-Wireless-Controller-PlayStation-5/dp/B08FC6C75Y'

# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
headers = { 
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip', 
'DNT' : '1', # Do Not Track Request Header 
'Connection' : 'close'
}

page = requests.get(test_url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

stock = soup.find(id = "priceblock_ourprice").get_text()

print(stock)

