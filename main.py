from bs4 import BeautifulSoup
import requests


# TODO wrap in function
# def scrap():
# result list
goods = []

# read https://www.tanuki.ru/menu/
url = 'https://www.tanuki.ru/menu/'
# change headers to avoid blocking
headers = {
    'user-agent': 'Chrome/75.0.3770.142',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive'
}
r = requests.get(url, headers=headers)

# parse page to csv
text = r.text
soup = BeautifulSoup(text, features='lxml')
catalog = soup.find('div', {'class': 'catalog'})
product_items = catalog.find_all('div', {'class': 'product'})

for product_item in product_items:
    name = product_item.find('div', {'class': 'product__title'}).text
    price = product_item.find('div', {'class': 'product__price'}).text
    pic = product_item.find('img', {'class': 'product__image'})['src']
    item = [name, price, pic]
    goods.append(item)

print(goods)
