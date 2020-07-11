import requests 
from bs4 import BeautifulSoup

import time
import random as rand 

import csv

class X():
    pass

def none2null(x):
    if x is None:
        x = X()
        x.text = ""
        return x
    return x

with open("reviews.csv", mode="wb") as f:
    writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    datapages = list(range(0, 642))
    rand.shuffle(datapages)
    it = 0;
    
    for page in datapages: #Remember to update the number of pages 
        url = 'https://www.metacritic.com/game/playstation-4/the-last-of-us-part-ii/user-reviews?sort-by=date&num_items=100&page='+str(page)
        user_agent = {'User-agent': 'Mozilla/5.0'}
        response  = requests.get(url, headers = user_agent)
        time.sleep(rand.randint(1,5)) 
        soup = BeautifulSoup(response.text, 'html.parser')
        
        print "Processing page " + str(page) + ", total " + str(it)
        it += 1
        
        for review in soup.find_all('div', class_='review_content'):
            if review.find('div', class_='name') == None:
                           break 
            r =  {'name':None, 'date':None, 'rating':None, 'review':None}
            
            r['name'] = review.find('div', class_='name').find('a').text
            r['date'] = review.find('div', class_='date').text
            r['rating'] = review.find('div', class_='review_grade').find_all('div')[0].text
            if review.find('span', class_='blurb blurb_expanded'):
                r['review'] = none2null(review.find('span', class_='blurb blurb_expanded')).text
            else:
                r['review'] = none2null(review.find('div', class_='review_body').find('span')).text
                
            writer.writerow([r['name'].encode('utf-8'), r['date'].encode('utf-8'), r['rating'].encode('utf-8'), r['review'].encode('utf-8')])
