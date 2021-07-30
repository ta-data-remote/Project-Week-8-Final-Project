import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import re
from wordcloud import WordCloud

import streamlit as st

from PIL import Image
from io import BytesIO
from matplotlib.pyplot import imshow
import requests



tv_shows = pd.read_csv("../data/tv_shows.csv")

netflix_titles = pd.read_csv("../data/netflix_titles.csv")

movies_plat = pd.read_csv("../data/MoviesOnStreamingPlatforms_updated.csv")


titles_net_film = netflix_titles[netflix_titles["type"] == "Movie"]

titles_net_show = netflix_titles[netflix_titles["type"] == "TV Show"]

net_movies_plat = movies_plat[movies_plat["Netflix"] == 1]

titles_net_show["country"] = titles_net_show["country"].fillna("Unknown / VV DD")

drop_list = [2359,3660]

titles_net_show.drop(drop_list, inplace = True)

titles_net_show["director"] = titles_net_show["director"].fillna("Unknown / VV DD")

titles_net_show["cast"] = titles_net_show["cast"].fillna("Anchors / Participants")

titles_net_show["country"] = titles_net_show["country"].fillna("Unknown")

titles_net_show["date_added"] = titles_net_show["date_added"].fillna("Misc")

titles_net_film["director"] = titles_net_film["director"].fillna("Unknown / VV DD")

titles_net_film["cast"] = titles_net_film["cast"].fillna("Anchors / Participants")

titles_net_film["country"] = titles_net_film["country"].fillna("Unknown")

titles_net_film["rating"] = titles_net_film["rating"].fillna("Unknown")

def get_frequency_details(column):
    
    df_info = column.value_counts()

    my_info = dict(df_info)

    df_info_dict = { key:[value] for key, value in my_info.items() }

    print(f"This is the frequency of {column.name}")
    
    return df_info_dict

country_film_prod = get_frequency_details(titles_net_film["country"])

show_added_date = get_frequency_details(titles_net_show["date_added"])

shows_age_rating = get_frequency_details(titles_net_show["rating"])

not_order_release_freq_show = get_frequency_details(titles_net_show["release_year"])


from collections import OrderedDict
 
Ord_release_year = OrderedDict(sorted(not_order_release_freq_show.items()))

Ord_show_added = OrderedDict(sorted(show_added_date.items()))

film_added_date = get_frequency_details(titles_net_film["date_added"])

film_country_prod = get_frequency_details(titles_net_film["country"])

not_order_release_freq_film = get_frequency_details(titles_net_film["release_year"])

Ord_release_year_film = OrderedDict(sorted(not_order_release_freq_film.items()))

film_age_rating = get_frequency_details(titles_net_film["rating"])

import requests


import random

import pandas as pd

from bs4 import BeautifulSoup

from selenium import webdriver

from time import sleep

from selenium.webdriver.common.keys import Keys

import time



def recommending_input(testinput):    
    url = "https://www.imdb.com/"
    options = webdriver.ChromeOptions()
    options.add_argument('--lang=en')
    #options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    browser = webdriver.Chrome('../data/chromedriver', chrome_options=options)
    #browser = webdriver.Chrome('../data/chromedriver') 
    browser.get(url)
    search=browser.find_element_by_xpath("//*[@id='suggestion-search']")
    search.send_keys(testinput)
    search.send_keys(Keys.RETURN)
    time.sleep(3)
    browser.find_element_by_xpath("//*[@id='main']/div/div[2]/table/tbody/tr[1]/td[2]/a").click() #//*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[2]/a
    #print(browser.page_source)

    source = browser.page_source    
    soup = BeautifulSoup(source,"html.parser")

    #print(type(soup))
    #recomm_list = soup.find_all("div", {"class": "ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--nowrap ipc-shoveler__grid"})
    recomm_list = soup.find_all("div", {"class", "ipc-poster-card ipc-poster-card--base ipc-poster-card--dynamic-width TitleCard-sc-1e5jqmp-0 egRGeD has-action-icons ipc-sub-grid-item ipc-sub-grid-item--span-2"})

   
    recom_data = {"titles":[], "rating": [], "link": []}
    for elem in recomm_list:
            # Getting rating
            rat = elem.find_all("span" , {"class", "ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb"})
            #ratings.append(rat[0].get_text())
            recom_data["rating"].append(rat[0].get_text())

            # Getting image
            img_recom = elem.find_all("div" , {"class", "ipc-media ipc-media--poster ipc-image-media-ratio--poster ipc-media--base ipc-media--poster-m ipc-poster__poster-image ipc-media__img"})
            text = "https" + str(img_recom[0]).split(", https")[-1]
            recom_data["link"].append(text.split()[0])

            # Get title
            tit = elem.find_all("span", attrs={"data-testid":"title"})
            rating_tag = elem.find_all("span", {"class" : "ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb"})
            if ( len(tit) > 0 ):
                for e in tit:
                        #titulos.append(e.get_text())
                        recom_data["titles"].append(e.get_text())

            #recom_data["titles"].append(e.get_text())           
            #e = [s for s in sub if sub['data-testid']== "title"]
            #print(e)

            #recom_data["titles"].append(e.get_text())
            #t = (rat[0].get_text(),e.get_text())
            #datos.append(t)
    recom_data_df = pd.DataFrame(recom_data)
    return  recom_data_df

#recommending_input(testinput)

import urllib.request
from PIL import Image

def get_df(testinput):
    recomm_df_info = recommending_input(testinput)
    return recomm_df_info


def imdb_is_great(x, df):
    print("Wait a moment please, my audiovisual-lover, loading recommendations!")
    title = df.iloc[x-1][0]
    rating = df.iloc[x-1][1]
    img = show_img(df.iloc[x-1][2])
    
    if len(netflix_titles[netflix_titles["title"] == title]) != 0:
        platform = "Netflix"
    else:
        platform = "Not in Netflix"
    #check_plat = movies_plat[movies_plat["Title"] == title].index.to_list()
    #if (movies_plat["Netflix"].iloc[check_plat] == 1).any():
    #    platform = "Netflix"
    #elif (movies_plat["Prime Video"].iloc[check_plat] == 1).any():
    #    platform = "Prime Video"    
    #elif (movies_plat["Hulu"].iloc[check_plat] == 1).any():
    #    platform = "Hulu"
    #elif (movies_plat["Disney+"].iloc[check_plat] == 1).any():
    #    platform = "Disney+"    
    return title, rating, img, platform



#x = len(df)
#for i in range(0,x):
#    title, rating, img = imdb_is_great(i, df)
#    print(title)
#    print(rating)
#    display(img)
    
def ask_user():
    testinput = input("Please enter a Netflix media content you like!")
    imdb_is_great(testinput)
    
    return

#df = get_df(testinput)

def show_img(x):                 
    response = requests.get(x)
    img = Image.open(BytesIO(response.content))
    return img

#show_img(recom_info_link)

def ask_user(testinput):
       
    print("Wait a moment please, my audiovisual-lover, loading recommendations!")
    df = get_df(testinput)
    x = len(df)
    #imdb_is_great(x, df)
    #print("Wait a moment please, my audiovisual-lover, loading recommendations!")
    for i in range(0,x):
        title, rating, img, platform= imdb_is_great(i, df) #, platform
        #print(title)
        #print(rating)
        #display(img)
        st.write(title)
        st.write(platform)
        st.write(rating)
        st.image(img)
        

    return 

#ask_user()
st.title("Netflix & IMDB Recommendator")
user_input = st.text_input("Please enter the streaming media content you like!\n")
search = st.button("Get Recommendations")
if search:
    with st.spinner("Wait a moment please, my audiovisual-lover, loading recommendations!"):
        ask_user(user_input)
        #st.write(ask_user(user_input))
        st.balloons()
#st.write(movies_plat)
        