#import needed libraries
import requests
import json
import pandas as pd
import numpy as np
import praw
import datetime as dt
import requests


#initialize reddit connection
reddit = praw.Reddit(client_id='Lv9oSz3II4A1KQ',
                     client_secret='Fwzk-Ccdw9w3pB0lbt3R4ayDVlo',
                     user_agent='scrapey',
                     username='LoZ56',
                     password='onica12')



#function to scrape,   #input is starting url
def scrape_it(url, post_list):
    #initial conditions
    after = None
    after_list = []
    iteration = 0
    it_max = 200
    print("Scraping new list...")
    #loop through and continuously pull
    while iteration < it_max:
        if ((after==None) and (iteration>0)):
            break
        if after == None:
            now_url = url
        else:
            now_url = url  + '?after=' + after

        #open request connection
        res = requests.get(now_url, headers = {'User-agent': 'Z1.0'})
        reddit_dict = res.json()

        #extract the posts from the json and make list of dictionaries
        new_posts = [p['data'] for p in reddit_dict['data']['children']]

        #append new posts to master list
        post_list.extend(new_posts)

        #move to next set of posts
        after = reddit_dict['data']['after']
        after_list.append(after)
        iteration += 1


fake_posts = []
real_posts = []

scrape_it('https://www.reddit.com/r/AskWomen.json', real_posts)
scrape_it('https://www.reddit.com/user/AskWomen_SS.json', fake_posts)

scrape_it('https://www.reddit.com/r/AskWomen/top/.json?sort=top&t=all', real_posts)
scrape_it('https://www.reddit.com/user/AskWomen_SS.json?sort=top', fake_posts)


df_fake = pd.DataFrame(fake_posts)
df_real = pd.DataFrame(real_posts)


print("fake dims:", df_fake.shape)
print("real dims:", df_real.shape)

# make df and export data
df_fake.to_csv('./data/fake_posts.csv')
df_real.to_csv('./data/real_posts.csv')
