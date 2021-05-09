# Importing necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# url is the website of the scraping data
url = "https://www.waterstones.com/books/bestsellers/sort/bestselling/format/17"
response = requests.get(url)

html_icerigi = response.content

# Scraped the specified page and assigned it to soup variable
soup = BeautifulSoup(html_icerigi, "html.parser")

# Below code creates empty data frame for the scraped data
d = pd.DataFrame({'Name of the Book' : [], 'Name of the Author' : [], 'Price of the Book(£)' : []})

# This for loop extract the book's name, author name and the prices
for i in range(len(soup.find_all("div", {"class" : "title-wrap"}))):

    # For try and except: If it does not get the data, it will extract blank
    try:
        name = soup.find_all("div", {"class" : "title-wrap"})[i].text.replace("\n", "")
    except:
        name = ""

    try:
        author = soup.find_all("span", {"class" : "author"})[i].text.replace("\n", "")
    except:
        author = ""

    try:
        price = soup.find_all("span", {"class" : "price"})[i].text.strip().replace("£","")
    except:
        price = ""

    # Below code writes the names and prices to a data frame and appends it to the data frame that we created above
    dataframe = {"Name of the Book" : name, "Name of the Author" : author, "Price of the Book(£)" : price}
    d = d.append(dataframe, ignore_index=True)

# Below code writes the scraped data to the csv file
d.to_csv("data_bs.csv", mode = "a", header = True, index = False, sep= ";")