#!/usr/bin/env python
# coding: utf-8

# Required libraries:

import pandas as pd
import matplotlib.pyplot as pl


# Reading the data from csv file:

df = pd.read_csv('data_scrapy.csv', sep = ";")


# Mean of the book prices:

df["Price of the Book"].mean()


# Max price of the books:

df["Price of the Book"].max()


# Min price of the books:

df["Price of the Book"].min()


# First 4 lines of the data frame:

df["Price of the Book"].head(4)


# Visualization of the data that we scraped:

df['Price of the Book'].plot.hist()
pl.title("Histogram of Scraped Data")
pl.xlabel("Prices")
pl.ylabel("Number of Books")

