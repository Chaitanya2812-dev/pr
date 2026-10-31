import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://books.toscrape.com/"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all products
products = soup.find_all("article", class_="product_pod")

# Extract product information
for product in products:

    # Product name
    name = product.h3.a["title"]

    # Price
    price = product.find("p", class_="price_color").text

    # Product link
    link = product.h3.a["href"]

    print("Product:", name)
    print("Price:", price)
    print("Link:", link)
    print("-" * 50)