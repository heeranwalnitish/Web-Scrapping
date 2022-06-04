from cgitb import html
from bs4 import BeautifulSoup
from matplotlib.pyplot import title
import pandas as pd
import csv
import requests
from sympy import re


#importing the dataset
df = pd.read_excel(r"D:\Pyhon_practice\Scrapping\Blackcoffer\Input.xlsx")
df.URL_ID = pd.to_numeric(df.URL_ID, downcast='integer')

# Getting our list
lst_URL = df['URL'].to_list()
lst_URL_ID = df['URL_ID'].to_list()

#URL ="https://insights.blackcoffer.com/how-is-login-logout-time-tracking-for-employees-in-office-done-by-ai/"


def scrapping_blog(url, url_id):
    try :
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}


        page = requests.get(url, headers=headers)
        htmlContent = page.content

        soup1 = BeautifulSoup(htmlContent, "html.parser")
        soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

        #Block to scrappe the Article Title.
        try :
            title = soup2.find("h1",attrs= {"class":'entry-title'}).text
            title = title.rstrip("\n")
            title = " ".join(title.split())

            c = []
            content = soup2.find("div", attrs = {"class":"td-post-content"})
            dat = '' 
            for dat in content.find_all("p"): 
                c.append(dat.get_text())

            result = ""
            for string in c:
                result += string + " "

            content = title + result
            
                
        
        except :
            print("Not able to access the title and content")


        

    except:
        print("Not able to access the page")

    else:
        file_name = f"{url_id}.txt"
        try:

            with open(file_name, 'w',encoding="utf8") as f:
                f.write(content)
        except FileNotFoundError:
            print("The 'docs' directory does not exist")



done = map(scrapping_blog,lst_URL,lst_URL_ID)

print(list(done))