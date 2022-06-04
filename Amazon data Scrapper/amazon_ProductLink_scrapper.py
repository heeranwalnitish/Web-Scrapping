# Importing all the necessary libraries
from bs4 import BeautifulSoup
import requests

#Connect to the website and pull the data

URL = "https://www.amazon.in/s?k=laptop&ref=nb_sb_noss_2"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-61979db0-44fbfcaa2665c7de2c5d1195"}

page = requests.get(URL, headers = headers)

soup1 = BeautifulSoup(page.content,"html.parser")
soup2 = BeautifulSoup(soup1.prettify(),"html.parser")


#Fetch links as Listof Tag Objects
links = soup2.find_all("a",attrs={'class' : 'a-size-base a-link-normal a-text-normal'})


# Store the links
links_list = []
# Loop for extracting links from Tag Objects
for link in links:
    links_list.append(link.get("href"))

for i in links_list:
    print(i)
