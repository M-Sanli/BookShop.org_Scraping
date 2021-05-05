import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.waterstones.com/books/bestsellers/sort/bestselling/format/17"
response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi, "html.parser")

d = pd.DataFrame({'Name' : [], 'Author' : [], 'Price' : []})

for i in range(len(soup.find_all("div", {"class" : "title-wrap"}))):
    try:
        name = soup.find_all("div", {"class" : "title-wrap"})[i].text.replace("\n", "")
    except:
        name = ""

    try:
        author = soup.find_all("span", {"class" : "author"})[i].text.replace("\n", "")
    except:
        author = ""

    try:
        price = soup.find_all("span", {"class" : "price"})[i].text.replace("\n", "")
    except:
        price = ""

    dataframe = {"Name" : name, "Author" : author, "Price" : price}
    d = d.append(dataframe, ignore_index=True)
print(d)

d.to_csv("data_bs.csv", mode = "a", header = True, index = False, sep= ";")