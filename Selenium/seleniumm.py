# Importing necessary libraries
import re
from selenium import webdriver
import time
import pandas as pd

# Path is the geckodriver.exe, in this project it stored with this python file.
# Otherwise we have to use full path of the geckodriver.exe!
gecko_path = 'geckodriver'

# website of the our project
url = 'https://www.waterstones.com/'

options = webdriver.firefox.options.Options()
options.headless = False
driver = webdriver.Firefox(options = options, executable_path = gecko_path)

# It opens the website via Firefox and sleeps(waits) 1 sec
# we used time sleeps for get rid of the internet connection problems and banned from the website
driver.get(url)
time.sleep(1)

# This is the xpath of the bestsellers section of the website
#It has to click
bestsellers = driver.find_element_by_xpath('//a[@class="nav-item-bestsellers js-nav-item nav-item  "]')
bestsellers.click()
time.sleep(2)

# Below code creates empty data frame for the scraped data
data = pd.DataFrame({"Name of the Book" : [], "Name of the Author" : [], "Price of the Book" : []})

# This for loop extract the book's name, author name and the prices
# It clicks the books and then extract the price from that page
for i in range(len(driver.find_elements_by_xpath('//div[@class="title-wrap"]'))):
    try:
        name = driver.find_elements_by_xpath('//div[@class="title-wrap"]')[i].text
    except:
        name = ""

    try:
        author = driver.find_elements_by_xpath('//span[@class="author"]')[i].text
    except:
        author = ""

    try:
        link = driver.find_elements_by_xpath('//div[@class="image-wrap"]/a')[i].get_attribute('href')
        driver.execute_script('window.open('');')
        driver.switch_to.window(driver.window_handles[1])
        driver.get(link)
        time.sleep(0.4)
        regex = re.compile('([0-9]...)')
        price_xpath = driver.find_element_by_xpath('//b[@itemprop="price"]')
        price = re.findall(regex, price_xpath.text)[0]
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    except:
        price = ""

    # Below code writes the names and prices to a data frame and appends it to the data frame that we created above
    dataframe = {"Name of the Book" : name, "Name of the Author" : author, "Price of the Book" : price}
    data = data.append(dataframe, ignore_index=True)

# Below code writes the scraped data to the csv file
data.to_csv("data_selenium.csv", mode = "a", header = True, index = False, sep= ";")

# This closes the Firefox
driver.close()