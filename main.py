from bs4 import BeautifulSoup
import requests


# format float numbers
def format_float(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num


# result list
goods = []

# read url
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

# number for img naming
num = 0

for product_item in product_items:
    name = product_item.find('div', {'class': 'product__title'}).text
    price = product_item.find('div', {'class': 'product__price'}).text[0:-4]
    sale_price = format_float(int(price) * 0.9)
    pic = product_item.find('img', {'class': 'product__image'})['src']

    num += 1

    # write to csv
    with open('tanuki_dataset.csv', 'a', encoding='utf-8') as f:
        f.write(f'{name},{price} ₽,{sale_price} ₽,{num}.jpg\n')

    # save pics from links
    with open(f'{num}.jpg', 'wb') as f:
        f.write(requests.get(pic).content)
