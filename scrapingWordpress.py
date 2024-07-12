import json
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re
import datetime
import unidecode
import sys
import json


# Function to clean and format the price
def clean_price(price):
    price_numeric = re.findall(r"\d+[\.,]?\d*", price.replace(",", "."))
    try:
        return float(price_numeric[0]) if price_numeric else None
    except ValueError:
        return None


# Function to clean and normalize text
def clean_text(text):
    text = text.lower()
    text = unidecode.unidecode(text)
    text = re.sub(r"[^a-zA-Z0-9 ]", "", text)
    return text.replace(" ", "-")


# Function to extract product details
def extract_product_details(
    url,
    store_title,
    store_logo,
    store_url,
    title_tag,
    title_class,
    title_content,
    price_tag,
    price_class,
    price_content,
    availability_tag,
    availability_class,
    availability_content,
    sku_tag,
    sku_class,
    sku_content,
    ratings_tag,
    ratings_class,
    ratings_content,
    nbr_rating_tag,
    nbr_rating_class,
    nbr_rating_content,
    delivery_price,
    offre,
):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        title_element = soup.find(title_tag, {title_class: title_content})
        title = (
            title_element.get_text().strip() if title_element else "Titre non trouvé"
        )

        price_element = soup.find(price_tag, {price_class: price_content})
        price_text = (
            price_element.find("bdi").get_text().strip()
            if price_element
            else "Prix non trouvé"
        )
        price_numeric = clean_price(price_text)

        availability_element = soup.find(
            availability_tag, {availability_class: availability_content}
        )
        if availability_element:
            availability_text = (
                availability_element.get_text()
                .strip()
                .replace("Status:", "")
                .strip()
                .lower()
            )
            availability = (
                "Disponible" if "in stock" in availability_text else "Indisponible"
            )
        else:
            availability = "Indisponible"

        sku_element = soup.find(sku_tag, {sku_class: sku_content})
        product_id = sku_element.get_text().strip() if sku_element else "SKU non trouvé"

        offer = offre

        scraping_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        store_titlee = store_title
        store_slug = clean_text(store_title)
        store_logoo = store_logo
        store_urll = store_url

        # Extracting ratings and number of ratings
        rating_element = soup.find(ratings_tag, {ratings_class: ratings_content})
        rating = float(rating_element.get_text().strip()) if rating_element else 0.0

        nbr_ratings_element = soup.find(
            nbr_rating_tag, {nbr_rating_class: nbr_rating_content}
        )
        nbr_ratings = (
            int(nbr_ratings_element.get_text().strip()) if nbr_ratings_element else 0
        )

        delivery_pricee = int(delivery_price)  # Ajout de la colonne delivery_price

        return {
            "title": title,
            "value": f"{price_numeric:.1f}" if price_numeric is not None else None,
            "product_url": url,
            "availability": availability,
            "rating": rating,
            "nbr_rating": nbr_ratings,
            "delivery_price": delivery_pricee,
            "delivery_time": "48 heures après la commande",
            "offer": offer,
            "scraping_time": scraping_time,
            "store_title": store_titlee,
            "store_slug": store_slug,
            "store_logo": store_logoo,
            "store_url": store_urll,
            "product_id": product_id,
        }

    except requests.exceptions.RequestException as e:
        print(f"Une erreur est survenue lors de la récupération de l'URL : {url} - {e}")
        return None


# Get the title from command line arguments
store_title = sys.argv[1] if len(sys.argv) > 1 else None
store_logo = sys.argv[2] if len(sys.argv) > 2 else None
store_url = sys.argv[3] if len(sys.argv) > 3 else None
title_tag = sys.argv[4] if len(sys.argv) > 4 else None
title_class = sys.argv[5] if len(sys.argv) > 5 else None
title_content = sys.argv[6] if len(sys.argv) > 6 else None
price_tag = sys.argv[7] if len(sys.argv) > 7 else None
price_class = sys.argv[8] if len(sys.argv) > 8 else None
price_content = sys.argv[9] if len(sys.argv) > 9 else None
availability_tag = sys.argv[10] if len(sys.argv) > 10 else None
availability_class = sys.argv[11] if len(sys.argv) > 11 else None
availability_content = sys.argv[12] if len(sys.argv) > 12 else None
sku_tag = sys.argv[13] if len(sys.argv) > 13 else None
sku_class = sys.argv[14] if len(sys.argv) > 14 else None
sku_content = sys.argv[15] if len(sys.argv) > 15 else None
ratings_tag = sys.argv[16] if len(sys.argv) > 16 else None
ratings_class = sys.argv[17] if len(sys.argv) > 17 else None
ratings_content = sys.argv[18] if len(sys.argv) > 18 else None
nbr_rating_tag = sys.argv[19] if len(sys.argv) > 19 else None
nbr_rating_class = sys.argv[20] if len(sys.argv) > 20 else None
nbr_rating_content = sys.argv[21] if len(sys.argv) > 21 else None
delivery_price = sys.argv[22] if len(sys.argv) > 22 else None
offre = sys.argv[23] if len(sys.argv) > 23 else None
sitemap = sys.argv[24] if len(sys.argv) > 24 else None

# List of sitemap URLs


# Function to extract URLs from sitemap and scrape product details
def extract_urls_from_sitemap(sitemap_url):
    products = []

    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()

        tree = ET.fromstring(response.content)
        loc_elements = tree.findall(
            ".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"
        )

        for loc_element in loc_elements[:10]:  # Limiting to first 5 products
            url = loc_element.text
            product_data = extract_product_details(
                url,
                store_title,
                store_logo,
                store_url,
                title_tag,
                title_class,
                title_content,
                price_tag,
                price_class,
                price_content,
                availability_tag,
                availability_class,
                availability_content,
                sku_tag,
                sku_class,
                sku_content,
                ratings_tag,
                ratings_class,
                ratings_content,
                nbr_rating_tag,
                nbr_rating_class,
                nbr_rating_content,
                delivery_price,
                offre,
            )
            if product_data:
                products.append(product_data)

    except (requests.exceptions.RequestException, ET.ParseError) as e:
        print(
            f"Une erreur est survenue lors de l'extraction des URL du sitemap : {sitemap_url} - {e}"
        )

    return products


# Extracting all products from sitemaps
sitemap_urls_string = str(sitemap)
all_products = []
sitemap_urls = [url.strip() for url in sitemap_urls_string.split(",")]
for sitemap_url in sitemap_urls:
    products = extract_urls_from_sitemap(sitemap_url)
    all_products.extend(products)

# Exporting data to a JSON file with specific order
formatted_products = []
store_slug = ""
scraping_time = ""
for product in all_products:
    formatted_product = {
        "title": product["title"],
        "value": float(product["value"]),
        "product_url": product["product_url"],
        "availability": product["availability"],
        "rating": product["rating"],
        "nbr_rating": product["nbr_rating"],
        "delivery_price": product["delivery_price"],
        "delivery_time": product["delivery_time"],
        "offer": product["offer"],
        "scraping_time": product["scraping_time"],
        "store_title": product["store_title"],
        "store_slug": product["store_slug"],
        "store_logo": product["store_logo"],
        "store_url": product["store_url"],
        "product_id": product["product_id"],
    }
    store_slug = formatted_product["store_slug"]
    scraping_time = formatted_product["scraping_time"][:10]
    formatted_products.append(formatted_product)

# Exporting data to a JSON file
with open(
    store_slug + "_" + scraping_time + ".json",
    "w",
    encoding="utf-8",
) as json_file:
    json.dump(formatted_products, json_file, ensure_ascii=False, indent=4)

print("Les données ont été exportées avec succès au format JSON ")
