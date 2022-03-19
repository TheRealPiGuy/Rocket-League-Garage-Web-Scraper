import requests
#import tkinter as tk
import re

from bs4 import BeautifulSoup, NavigableString, Tag
#from tkinter import *

def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))

URL = 'https://rocket-league.com/items/shop' # Set variable to the main URL

#URL = 'https://rocket-league.com/items/shop/2021-08-26'


page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

item_containers = soup.find_all(class_= 'rlg-item-shop') # Search for all items in the shop

featured_containers = soup.find_all(class_= 'rlg-item-shop__featured') # Featured items

daily_containers = soup.find_all(class_= 'rlg-item-shop__daily') # Daily items



for featured_item_container in item_containers: # Loop through featured items
    featured_elem = featured_item_container.find('div', class_='rlg-item-shop__featured')


for daily_item_container in item_containers: # Loop through daily items
    daily_elem = daily_item_container.find('div', class_='rlg-item-shop__daily')



for bad_featured_item in soup.findAll("div", {'class': 'rlg-item-shop__meta'}): # Loop through again to remove price and votes from featured items
    if isinstance(bad_featured_item, NavigableString):
        continue
    if isinstance(bad_featured_item, Tag):
        bad_featured_item.decompose()

for bad_daily_item in soup.findAll("div", {'class': 'rlg-item-shop__meta --daily'}): # Loop through again to remove price and votes from dailt items
    if isinstance(bad_daily_item, NavigableString):
        continue
    if isinstance(bad_daily_item, Tag):
        bad_daily_item.decompose()



print("\n") # Line between console and program output
print("FEATURED ITEMS")
print("--------------")


newFeaturedString = featured_elem.text.replace('\n\n\n\n\n\n\n\n','').replace('\n\n','') # Replace extra white space in the HTML

res_list = [] # Make new list
res_list = re.findall('[A-Z][^A-Z]*', newFeaturedString) # Set to a regular expression to space out words
newFeaturedString = re.sub(' +', ' ', listToString(res_list)) # Feed into function that converts a list to string
otherString = newFeaturedString.replace('\n ', '\n') # Remove final spaces and print featured items

checkBool = False
if(otherString.count('\n') <= 1):
    checkBool = True
print(otherString)
if(checkBool):
    print('')
    #print(otherString.count('\n'))

#print(featured_elem.text.replace('\n\n\n\n\n\n\n\n','').replace('\n\n','')) # Print featured items

print('\n')
print('DAILY ITEMS')
print('-----------')


print(daily_elem.text.replace('\n\n\n\n\n\n\n\n','').replace('\n\n','').replace("  "," ")) # Print daily items

print('----------------------')





