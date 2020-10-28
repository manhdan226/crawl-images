# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
from GoogleImageScrapper import GoogleImageScraper
import os

webdriver_path = os.getcwd()+"\\webdriver\\chromedriver.exe"
image_path = os.getcwd()+"\\photos"
#add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
search_keys= ["ChiPu", "Lê Công Vinh", "Binz"]
number_of_images = 10
headless = False
#min_resolution = (width,height)
min_resolution=(0,0)
#max_resolution = (width,height)
max_resolution=(10000,10000)
# for search_key in search_keys:
# 	image_path = os.path.join(image_path,search_key) 
#     image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,headless,min_resolution,max_resolution)
#     image_urls = image_scrapper.find_image_urls()
#     image_scrapper.save_images(image_urls)
