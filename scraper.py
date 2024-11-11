import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ai_learning_db"]

def scrape_content():
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.get_text()

    # Store content in MongoDB
    db.content.insert_one({"url": url, "content": content})

