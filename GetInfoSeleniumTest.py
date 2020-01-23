#first selenium code in python
#recognize food type using caloriemama.ai

from selenium import webdriver
import time
browser = webdriver.Firefox() #my browser is firefox there's different things for other browsers
browser.get('https://www.caloriemama.ai/api')

upload = browser.find_element_by_class_name('file-upload')
upload.send_keys('/media/lucifer/New Volume/PRABA/Code/python/pizza.jpeg') #enter your image file location here

time.sleep(5) #i add this because when i write this code i had poor network
get = browser.find_elements_by_class_name('group-name')

for got in get:
	print(got.text,"\n") #first result is  high accuracy one

#if need only one result, remove for loop and change 'find_elements_by_class_name' to 'find_element_by_class_name' 
#print get.text