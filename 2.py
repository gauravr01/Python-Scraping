import requests
from bs4 import BeautifulSoup
import csv
import time
import random

# base_url = 'https://www.amazon.in/s?k=Apple&i=electronics&rh=n%3A1389401031&page={}&ref=sr_pg_{}'
base_url = 'https://www.amazon.in/s?k=Apple&i=electronics&rh=n%3A1389401031&page={}'

# Function to extract product titles and prices from a page
def extract_product_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36',
    }

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    product_titles = [title.text.strip() for title in soup.find_all('span', class_="a-size-base-plus a-color-base a-text-normal")]
    product_prices = [price.text.strip() for price in soup.find_all('span', class_='a-price-whole')]
    
    product_info = dict(zip(product_titles, product_prices))
    
    return product_info


# Number of pages to scrape
num_pages = 3

# Initialize an empty dictionary to store the product info
product_info_dict = {}

# Loop through the pages and extract product info
for page_num in range(1, num_pages + 1):
    url = base_url.format(page_num)
    print(url)
    product_info = extract_product_info(url)

    product_info_dict.update(product_info)
    # Add a delay between requests (e.g., random delay between 2 to 5 seconds)
    delay = random.uniform(2, 5)
    time.sleep(delay)


# Print the dictionary containing product titles and prices
for title, price in product_info_dict.items():
    print(f"Title: {title}")
    print(f"Price: {price}")
    print("\n")

print(product_info_dict)