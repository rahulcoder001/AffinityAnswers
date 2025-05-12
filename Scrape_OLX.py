
import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.olx.in/items/q-car-cover"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

listings = soup.find_all("div", {"class": "_2tD1M"})  # Update class if needed

with open("olx_car_covers.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Location", "Link"])
    for item in listings:
        title = item.find("span", {"class": "_2poNJ"}).text.strip()
        price = item.find("span", {"class": "_2Ks63"}).text.strip()
        location = item.find("span", {"class": "_2VQu4"}).text.strip()
        link = item.find("a")["href"]
        writer.writerow([title, price, location, f"https://www.olx.in{link}"])
