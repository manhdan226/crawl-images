# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
from GoogleImageScrapper import GoogleImageScraper
import os
import pandas as pd
#list_file = 'D:\Data_Vietnamese\Google-Image-Scraper-master\data.csv'
data = pd.read_csv('data.csv')
webdriver_path = os.getcwd()+"\\webdriver\\chromedriver.exe"
image_path = os.getcwd()+"\\photos"
#add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
search_keys = data['Tên'].values.tolist()
print(search_keys[100])
gender = data['Giới tính'].values.tolist()
number_of_images = 10
headless = False
#min_resolution = (width,height)
min_resolution=(0,0)
#max_resolution = (width,height)
max_resolution=(10000,10000)
for x in range(len(search_keys)):
	img_path = os.path.join(image_path,gender[x],str(x)+'.jpg')
	image_scrapper = GoogleImageScraper(webdriver_path,img_path,search_keys[x],number_of_images,headless,min_resolution,max_resolution)
	image_urls = image_scrapper.find_image_urls()
	image_scrapper.save_images(image_urls)
