# Importing necessary libraries
import scrapy
import re
import pandas as pd

class BestsellersSpider(scrapy.Spider):
    name = 'bestsellers'
    allowed_domains = ['www.waterstones.com']
    start_urls = ['https://www.waterstones.com/books/bestsellers/']

    def parse(self, response):
        # Below code is used for creating empty data frame
        data = pd.DataFrame({"Name of the Book": [], "Name of the Author": [], "Price of the Book": []})

        # Extract data using xpath
        titles = response.xpath('//div[@class="title-wrap"]/a/text()').extract()
        author = response.xpath('//span[@class="author"]/a/b/text()').extract()
        prices = response.xpath('//span[@class="price"]/text()').re(r"([0-9]...)")

        for item in zip(titles, author, prices):

            # Creating dictionary to store the scraped data, items means product in the list.
            scraped_data = {
                'Name of the Book': item[0],
                'Name of the Author': item[1],
                'Price of the Book': item[2],
            }

            # Appends scraped data to the empty data frame for get rid of punctuation in the csv file
            data = data.append(scraped_data, ignore_index=True)

            yield scraped_data

        # Below code writes the scraped data to the csv file
        data.to_csv("data_scrapy.csv", mode="a", header=True, index=False, sep=";")

