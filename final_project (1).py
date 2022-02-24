#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:40:55 2019

@author: melaneymoffitt
"""

import nltk
from selenium import webdriver

driver = webdriver.Chrome('/Applications/chromedriver')

urls = ['https://www.naturalhairrules.com/my-superpower/', 'https://www.naturalhairrules.com/grow-long/', 'https://www.naturalhairrules.com/box-braids-wash/', 'https://www.naturalhairrules.com/hair-breakage/', 'https://www.naturalhairrules.com/4c-hair/', 'https://www.naturalhairrules.com/oil-rinse/']
threeurls = ['https://www.afrobella.com/2019/12/08/mariah-carey-vahdam-tea/', 'https://www.afrobella.com/2019/11/26/pumpkin-beauty-skincare/', 'https://www.afrobella.com/2019/11/25/kitchen-gifts-that-should-last-at-least-a-decade/', 'https://www.afrobella.com/2019/11/06/leota/', 'https://www.afrobella.com/2019/10/17/kegels-kegelbell/', 'https://www.afrobella.com/2019/08/13/mented-helped-me-find-my-nude-makeup-groove/', 'https://www.afrobella.com/2019/07/30/my-easy-trader-joes-charcuterie-board-how-to-make-the-cheese-board-of-your-dreams/']
  
#access each blog post through css selector and image link
url_elements = driver.find_elements_by_css_selector('a[class="entry-image-link"]')
url_elements3 = driver.find_elements_by_css_selector('a[class="entry-image-link"]')

for element in url_elements:
    urls.append(element.get_attribute("href"))
    
for element3 in url_elements3:
    threeurls.append(element3.get_attribute("href"))


for url in urls:
    driver.get(url)
    
    #gets the text from htmls
    el = driver.find_elements_by_class_name('content')

    #translates the text to english not html
    elp = [elem.text for elem in el]

    #write the text to a file
    with open('web.txt', 'a') as file:
        for line in elp:
            file.write("%s\n" % line)
          
for e in threeurls:
    driver.get(e)
    #gets the text from the html
    el3 = driver.find_elements_by_tag_name('p')

    #translates the text to english not html
    elp3 = [elem3.text for elem3 in el3]

    #write the text to a file
    with open('web.txt', 'a') as file:
        for i in elp3:
            file.write("%s\n" %i) 

def postag(f):
    document = []
    #Open the file to read so it can tag the words
    with open(f,'r') as f:
        for line in f:
            #split the words into a list in the document to tag parts of speech
            document = f.read().split()
            tagged = nltk.pos_tag(document)  
    return(tagged)

f = "web.txt"
print(postag(f))
driver.close()
f.close()
