#!/usr/bin/env python
# coding: utf-8

# # FINAL PROJECT: NETFLIX ~something~
# 

# # Index
# 
# [Netflix Titles csv](#Netflix-titles)
# 
# [Netflix TV Shows csv](#Netflix-TV-Shows)
# 
# [Movies Various Platforms](#Movies-on-platforms)

# ## Main Idea

# Create a Tabletop/Boardgame recommender that asks users a videogame they like.
# 
# Clustering VG and adding TTBG to the grouping. 
# 
# Not based just in theme/genre i.e Horror, Resource Management, Strategy, etc
# 
# 

# ### First problem to tackle

# 

# ## Imports
# 

# In[56]:


get_ipython().system('pip install nltk')


# In[497]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

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


# In[432]:


streamlit run Draft Anal. Netflix.ipynb


# In[556]:


get_ipython().system('jupyter nbconvert   --to script NetflixAnalysis.ipynb')
get_ipython().system("awk '!/ipython/' NetflixAnalysis.py >  temp.py && mv temp.py app.py && rm NetflixAnalysis.py")
get_ipython().system('streamlit run app.py ')


# ## CSVs

# In[58]:


tv_shows = pd.read_csv("../data/tv_shows.csv")

netflix_titles = pd.read_csv("../data/netflix_titles.csv")

movies_plat = pd.read_csv("../data/MoviesOnStreamingPlatforms_updated.csv")


# ### Netflix titles

# In[59]:


netflix_titles


# In[60]:


netflix_titles["type"].unique()


# In[61]:


netflix_titles["type"].value_counts()


# In[62]:


# Separating teflix_titles DF into tv show or movie

titles_net_film = netflix_titles[netflix_titles["type"] == "Movie"]

titles_net_show = netflix_titles[netflix_titles["type"] == "TV Show"]

titles_net_film

titles_net_show


# ### Netflix TV Shows

# In[63]:


tv_shows[tv_shows["Netflix"] == 1]


# ### Movies on platforms

# In[64]:


len(movies_plat)


# In[65]:


(len(movies_plat["IMDb"]) - movies_plat["IMDb"].isna().sum()) / 100


# In[66]:


net_movies_plat = movies_plat[movies_plat["Netflix"] == 1]


# ### Cleaning NaNs titles_net_show

# In[67]:


titles_net_show.isna().sum()


titles_net_show[titles_net_show["cast"].isna()].sample(5)

titles_net_show[titles_net_show["title"].str.contains("Cosmos")]


# In[68]:


titles_net_show.isna().sum()


# In[69]:


titles_net_show["country"] = titles_net_show["country"].fillna("Unknown / VV DD")


# In[70]:


titles_net_show[titles_net_show["rating"].isna()].sample(2)


# In[71]:


# Clean 2 ratings that have NAN 

drop_list = [2359,3660]

titles_net_show.drop(drop_list, inplace = True)


# In[72]:


# Cleaning the rest of NANs in columns - Filling NANs
titles_net_show["director"] = titles_net_show["director"].fillna("Unknown / VV DD")

titles_net_show["cast"] = titles_net_show["cast"].fillna("Anchors / Participants")

titles_net_show["country"] = titles_net_show["country"].fillna("Unknown")

titles_net_show["date_added"] = titles_net_show["date_added"].fillna("Misc")

titles_net_show.head()



# In[73]:


def find_show(search_title):
   
    checking_indf = titles_net_show["title"].str.find(search_title)

    index_search = np.where(checking_indf != -1)[0][0]

    show_found = titles_net_show.iloc[index_search]

    my_dict = dict(show_found)

    
    my_dict = { key:[value] for key, value in my_dict.items() }

    result = pd.DataFrame(my_dict)
    
    return result


find_show("pene")


# ### Cleaning NaNs titles_net_film

# In[74]:


titles_net_film.isna().sum()


# In[75]:


titles_net_film[titles_net_film["rating"].isna()].sample(5)


# In[76]:


titles_net_film["director"] = titles_net_film["director"].fillna("Unknown / VV DD")

titles_net_film["cast"] = titles_net_film["cast"].fillna("Anchors / Participants")

titles_net_film["country"] = titles_net_film["country"].fillna("Unknown")

titles_net_film["rating"] = titles_net_film["rating"].fillna("Unknown")

titles_net_film


# In[77]:


titles_net_film["listed_in"].unique()

genres = ["LGBTQ Movies", "Documentaries", "Children & Family Movies", "Comedies", "Horror Movies", "Sci-Fi & Fantasy", "Thrillers", "Dramas", "Romantic Movies", """"""""]


# ## Movies Netflix Data

# In[78]:



def get_frequency_details(column):
    
    df_info = column.value_counts()

    my_info = dict(df_info)

    df_info_dict = { key:[value] for key, value in my_info.items() }

    print(f"This is the frequency of {column.name}")
    
    return df_info_dict


# #### Dictionary with movie catalogue and when they where released. 

# In[79]:


get_frequency_details(titles_net_film["release_year"])


# #### Dictionary with movie age rating. 

# In[80]:


get_frequency_details(titles_net_film["rating"])


# #### Dict with movies per country

# In[81]:


country_film_prod = get_frequency_details(titles_net_film["country"])

country_film_prod


# In[ ]:





# ## Tv Show Netflix Data

# In[82]:


titles_net_show


# In[83]:


titles_net_show.columns


# In[84]:


show_added_date = get_frequency_details(titles_net_show["date_added"])
show_added_date


# In[85]:


shows_age_rating = get_frequency_details(titles_net_show["rating"])

shows_age_rating


# In[86]:


get_frequency_details(titles_net_show["country"])


# In[87]:


not_order_release_freq_show = get_frequency_details(titles_net_show["release_year"])

not_order_release_freq_show


# In[88]:


from collections import OrderedDict
 

Ord_release_year = OrderedDict(sorted(not_order_release_freq_show.items()))
Ord_release_year


# In[89]:



Ord_show_added = OrderedDict(sorted(show_added_date.items()))
Ord_show_added


# ## Film Netflix Data

# In[90]:


titles_net_film.columns


# In[91]:


film_added_date = get_frequency_details(titles_net_film["date_added"])
film_added_date


# In[92]:


film_country_prod = get_frequency_details(titles_net_film["country"])
film_country_prod


# In[93]:


not_order_release_freq_film = get_frequency_details(titles_net_film["release_year"])

#not_order_release_freq_film

Ord_release_year_film = OrderedDict(sorted(not_order_release_freq_film.items()))
Ord_release_year_film


# In[94]:


film_age_rating = get_frequency_details(titles_net_film["rating"])
film_age_rating


# In[95]:


def tylen(x):
    x1 = len(x)
    x2 = type(x)
    result = (x1, x2)
    
    return result

tylen(not_order_release_freq_show)
    


# ## Graphs - TV Show

# In[96]:


#sns.pairplot(shows_age_rating, hue='species', size=2.5);


# 

# In[97]:


shows_age_rating.items()


# In[98]:


#keys = list(shows_age_rating.keys())

#vals = [float(shows_age_rating[k][0]) for k in keys]

#sns.barplot(x=keys, y=vals).set_title("Netflix shows by Age Rating");
#
#fig4, ax4 = plt.subplots(figsize = (12,8))

#ax4.set_title("Netflix shows by Age Rating", size='25', fontweight='bold')

#sns.barplot(x = keys,y = vals, ax = ax4);


# In[99]:


#g =sns.barplot(x=keys, y=vals).set_title("Netflix shows by Age Rating");

#for keys, values in shows_age_rating.items():
#    g.text(shows_age_rating.nam,"eme", values, color='black', ha="center")


# In[100]:


#plt.legend(labels=['legendEntry1', 'legendEntry2', 'legendEntry3'])


# 

# In[101]:


shows_age_rating.values()


# #### Barplot: Netflix TV Shows distributed by Age Rating

# In[122]:


keys = list(shows_age_rating.keys())

vals = [float(shows_age_rating[k][0]) for k in keys]

fig4, ax4 = plt.subplots(figsize = (12,8))

ax4.set_title("Netflix shows by Age Rating", size='16', fontweight='bold') ### ci = None (para quitar barrita) ci = None

sns.barplot(x = keys,y = vals, ax = ax4);


# #### Barplot: Netflix TV Shows added by release date

# In[121]:


plt.style.use("dark_background")

keys = list(Ord_release_year.keys())

vals = [float(Ord_release_year[k][0]) for k in keys]

fig5, ax5 = plt.subplots(figsize = (16,8))

sns.barplot(x=keys, y=vals, ).set_title("Netflix TV Shows added by release date", size='16', fontweight='bold')

plt.xticks(rotation=45);


# In[ ]:





# In[ ]:





# ## Graphs - Movie

# #### Barplot: Netflix Movies distributed by Age Rating

# In[123]:


keys = list(film_age_rating.keys())

vals = [float(film_age_rating[k][0]) for k in keys]

fig6, ax6 = plt.subplots(figsize = (12,8))

ax6.set_title("Netflix Movies by Age Rating", size='16', fontweight='bold') ### ci = None (para quitar barrita) ci = None

sns.barplot(x = keys,y = vals, ax = ax6);


# In[ ]:





# #### Barplot: Netflix TV Shows added by release date

# In[124]:


keys = list(Ord_release_year_film.keys())

vals = [float(Ord_release_year_film[k][0]) for k in keys]

fig5, ax5 = plt.subplots(figsize = (18,8))

sns.barplot(x=keys, y=vals, ).set_title("Netflix Movies added by release date", size='16', fontweight='bold')

plt.xticks(rotation=45);


# In[ ]:





# In[125]:


keys = list(shows_age_rating.keys())

vals = [float(shows_age_rating[k][0]) for k in keys]

fig4, ax4 = plt.subplots(figsize = (12,8))

ax4.set_title("Netflix shows by Age Rating", size='16', fontweight='bold') ### ci = None (para quitar barrita) ci = None

sns.barplot(x = keys,y = vals, ax = ax4);


# In[ ]:





# In[ ]:





# In[ ]:





# ### Bag of words & Cleaning

# In[143]:


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('tagsets')
nltk.download('averaged_perceptron_tagger')


# In[144]:


nltk.download('stopwords')
stop_words = list(stopwords.words('english')) 
#lista = stop_words
#lista.append("test")

#lista


# ### Tokenizing words fro description

# In[145]:


titles_net_show["description"]


# In[146]:


reviews = ''

for review in titles_net_show["description"]:
    reviews += review



corpus = nltk.sent_tokenize(reviews)


# In[159]:


def create_corpus(data, column):
    """
    Input a data frame, and the a string of the name of the column you want to create the corpus
    It produces two outcomes:
    - the list_tokens as a list of tokens
    - the one_string_tokens as a string with all tokens
    """
 
    #create an empty string
    one_string_tokens = ''
    #we add every word in the 
    for review in data[column]:
        one_string_tokens += review
#     corpus = nltk.sent_tokenize(reviews)
    #list_tokens = word_tokenize(one_string_tokens)

    return one_string_tokens


# In[161]:


corpus = create_corpus(titles_net_show, "description")


# In[165]:


for i in range(len(corpus)):
    corpus[i] = corpus[i].lower()
    corpus[i] = re.sub(r'\W+',' ',corpus[i]) # Replace everything non-alpahnumeric by ' '
    corpus[i] = re.sub(r'\s+',' ',corpus[i]) # Replace one or more whitespaces by  ' '
    corpus[i] = re.sub(r'\d+',' ',corpus[i]) # Replace one or more digits by  ' '
    #corpus[i] = re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)'," ", corpus[i]) # Replace e-mails by ''
    # Replace urls by ''
    #corpus[i] = re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', ' ' , corpus[i]) 
    # Replace html tags by ''
    corpus[i] = BeautifulSoup(corpus[i], 'lxml').get_text().strip()


# In[166]:


corpus


# In[169]:


query = corpus
stopwords = ['what', 'who', 'is', 'a', 'at', 'is', 'he', "series", "one","two", "three", "four", "get", "take", "must"]
querywords = query.split()

resultwords  = [word for word in querywords if word.lower() not in stopwords]
result = ' '.join(resultwords)

print(result)


# In[149]:


wordfreq = {}
for sentence in corpus:
    words = sentence.split()
    #tokens = nltk.word_tokenize(sentence) # To get the words, it can be also done with sentence.split()
    for word in words:
        if ( word not in wordfreq.keys() ):
            wordfreq[word] = 1 # We initialize the corresponding counter
        else:
            wordfreq[word] += 1 # We increase the corresponding counter
    


# In[150]:


wordfreq


# In[151]:


from nltk.corpus import stopwords

stop_words = list(stopwords.words('english')) 


# In[152]:


for i in range(len(stop_words)):
    stop_words[i] = re.sub(r"\s*'\s*\w*","",stop_words[i])

#stop_words = [word for word in list(np.unique(stop_words)) if len(word) > 1]


# In[ ]:





# In[153]:


add_stop_words = ["one","two", "three", "four", "get", "take", "must"]

for words in add_stop_words:
    stop_words.append(words)
    
stop_words


# In[154]:


corpus = [(wordfreq[key],key) for key in list(wordfreq.keys()) if key not in stop_words]


# In[155]:


corpus.sort(reverse = True)

# Here we keep only the 20 most frequent words but it can be changed to another bigger value
corpus_freq = [(word[1],word[0]) for word in corpus[:50]] 
corpus_freq = corpus_freq[1:]
corpus_freq


# In[172]:


word_cloud = WordCloud(collocations = False, background_color = 'white').generate(result)

ax = plt.figure(figsize=(15,10))
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.show()
    


# In[ ]:



wordcloud = WordCloud(width=900,height=500, max_words=50,relative_scaling=1,normalize_plurals=False).generate_from_frequencies(corpus_freq)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:


efe = corpus


# In[ ]:


for i in range(len(corpus)):
    corpus[i] = corpus[i].lower()
    corpus[i] = re.sub(r'\W+',' ',corpus[i]) # Replace everything non-alpahnumeric by ' '
    corpus[i] = re.sub(r'\s+',' ',corpus[i]) # Replace one or more whitespaces by  ' '
    #corpus[i] = re.sub(r'\d+',' ',corpus[i]) # Replace one or more digits by  ' '
    #corpus[i] = re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)'," ", corpus[i]) # Replace e-mails by ''
    # Replace urls by ''
    #corpus[i] = re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', ' ' , corpus[i]) 
    # Replace html tags by ''
    corpus[i] = BeautifulSoup(corpus[i], 'lxml').get_text().strip()


# In[ ]:


efe


# #### importing

# In[ ]:


add_stop_words = ["one","two", "three", "on", "is", "when", "and", "this", "they", "a", """""""""""""]


# In[ ]:


def filter_review(x):
    text = efe
    tags = nltk.pos_tag(text)
    words = []
    for tag in tags:
        # Include the type of words that you want to consider.
        # It will be also better 
        if ( tag[1] in ['JJ','NN','VB'] ):
            words.extend(tag[0])
    return "".join(words)

filter_review(corpus)


# In[ ]:





# In[ ]:





# In[ ]:


# API

import requests


import random
import pandas as pd
from bs4 import BeautifulSoup

#SELENIUM


# In[ ]:


pip install twitchAPI


# ### Web Scraping for IMDB Recommendations
# 

# In[206]:



from selenium import webdriver

from time import sleep

from selenium.webdriver.common.keys import Keys

import time


# In[178]:


url = "https://www.imdb.com/"
    
url


# In[180]:


user_choice = input("Please enter a Netflix media content you like:")


# In[ ]:


review_id_list= []
scores_over50_list= []
dates_list = []
titles_list=[]
reviews_list = []

for url in list_urls:
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome('Users/Emanuele/Desktop/IRONHACK/BOOTCAMPO/PROJECTS/FINAL PROJECT/data') 
    print("Current session is {}".format(browser.session_id))
    browser.get(url)
    time.sleep(3)
    browser.find_element_by_xpath("//*[@id='suggestion-search']").click()
    time.sleep(3)
    browser.find_element_by_xpath("//*[@id='main']/div/div[2]/table/tbody/tr[1]/td[2]/a").click()
    print(url)
    time.sleep(3)
    source = browser.page_source    
    soup = BeautifulSoup(source, features = "lxml")
    browser.close()
    for tag in soup.select("#taplc_location_reviews_list_resp_rr_resp_0 > div >div > div > div > div  "):
        if tag.get('data-reviewid') != None:
            review_id_list.append(tag.get('data-reviewid'))
        for date in tag.find_all(class_="ratingDate"):
            dates_list.append(date.get('title'))
        for title in tag.find_all(class_="noQuotes"):
            titles_list.append(title.text)
        for review in tag.find_all(class_="partial_entry"):
            reviews_list.append(review.text.replace("\n", ""))
        for score in tag.find_all("span",attrs={'class': re.compile('ui_bubble_rating bubble_')}):
            indiv_score= score.get('class')[1].split("_")[1]
            scores_over50_list.append(indiv_score)


# In[191]:


options = webdriver.ChromeOptions()
browser = webdriver.Chrome('../data/chromedriver') 
#print("Current session is {}".format(browser.session_id))
browser.get(url)
time.sleep(3)
browser.find_element_by_xpath("//*[@id='suggestion-search']").click()
time.sleep(3)
browser.find_element_by_xpath("//*[@id='main']/div/div[2]/table/tbody/tr[1]/td[2]/a").click()
time.sleep(3)


# In[ ]:


options = webdriver.ChromeOptions()
browser = webdriver.Chrome('Users/Emanuele/Desktop/IRONHACK/BOOTCAMPO/PROJECTS/FINAL PROJECT/data') 
print("Current session is {}".format(browser.session_id))
browser.get(url)
time.sleep(3)
browser.find_element_by_xpath("//*[@id='suggestion-search']").click()
time.sleep(3)
browser.find_element_by_xpath("//*[@id='main']/div/div[2]/table/tbody/tr[1]/td[2]/a").click()
print(url)
time.sleep(3)
source = browser.page_source    
soup = BeautifulSoup(source, features = "lxml")
browser.close()
for tag in soup.select("#taplc_location_reviews_list_resp_rr_resp_0 > div >div > div > div > div  "):
    if tag.get('data-reviewid') != None:
        review_id_list.append(tag.get('data-reviewid'))
    for date in tag.find_all(class_="ratingDate"):
        dates_list.append(date.get('title'))
    for title in tag.find_all(class_="noQuotes"):
        titles_list.append(title.text)
    for review in tag.find_all(class_="partial_entry"):
        reviews_list.append(review.text.replace("\n", ""))
    for score in tag.find_all("span",attrs={'class': re.compile('ui_bubble_rating bubble_')}):
        indiv_score= score.get('class')[1].split("_")[1]
        scores_over50_list.append(indiv_score)


# In[ ]:


inputElement = browser.find_element_by_id("")
inputElement.send_keys('1234')


# In[237]:


options = webdriver.ChromeOptions()
browser = webdriver.Chrome('../data/chromedriver') 


# In[486]:


url = "https://www.imdb.com/"
    
url


# In[531]:


testinput = input("ejemplo:")


# In[529]:


#search.clear()
def recommending_input(testinput):    
    url = "https://www.imdb.com/"
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome('../data/chromedriver') 
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
                        titulos.append(e.get_text())

            recom_data["titles"].append(e.get_text())           
            #e = [s for s in sub if sub['data-testid']== "title"]
            #print(e)

            #recom_data["titles"].append(e.get_text())
            #t = (rat[0].get_text(),e.get_text())
            #datos.append(t)
    recom_data_df = pd.DataFrame(recom_data)
    return  recom_data_df

recommending_input("invincible")


# #### Image printing with Title and Rating

# In[433]:


import urllib.request
from PIL import Image


# In[489]:


for link in recom_data["link"]:
    print(link)


# In[440]:


for link in recom_data["link"]:
    urllib.request.urlretrieve(link, "gfg.png")
    img = Image.open("gfg.png")
    


# In[535]:


recomm_df_info = recommending_input(testinput)

for i in range(0, (int(recomm_df_info.size / 3) - 1)):
    for e in range(0,3):
        recom_info = recomm_df_info.iloc[int(i)][e]

        if "https" in recom_info:
            display(show_img(recomm_df_info.iloc[int(i)][e]))
        else:
            print(recom_info)


# In[536]:


len(recomm_df_info)


# In[ ]:


def imb_test(testinput):
    
    df  = recommending_input(testinput)
    links = df["links"]
    name = df["titles"]
    rating = df["rating"]
    for i in range(len(recom_df_info)):
        for e in range(0,3):
                
    
            
imb_test(testinput)


# In[542]:


def get_df(testinput):
    recomm_df_info = recommending_input(testinput)
    return recomm_df_info


# In[547]:



def imdb_is_great(x, df):
    print("Wait a moment please, my audiovisual-lover, loading recommendations!")
    title = df.iloc[x-1][0]
    rating = df.iloc[x-1][1]
    img = show_img(df.iloc[x-1][2])
    return title, rating, img

    
    


# In[ ]:


df = get_df(testinput)


# In[554]:



x = len(df)
for i in range(0,x):
    title, rating, img = imdb_is_great(i, df)
    print(title)
    print(rating)
    display(img)


# In[540]:


def ask_user():
    testinput = input("Please enter a Netflix media content you like!")
    imdb_is_great(testinput)
    
    return

ask_user()


# In[520]:


recom_info_link = recomm_df_info.iloc[int(0)][2]

if "https" in recom_info_link:
    display(show_img(recom_info_link))
else:
    print("pasa cabron")


# In[517]:


#response = requests.get(testimg)
#img = Image.open(BytesIO(response.content)
def show_img(x):                 
    response = requests.get(x)
    img = Image.open(BytesIO(response.content))
    return img
show_img(recom_info_link)


# In[495]:


testimg = "https://m.media-amazon.com/images/M/MV5BN2ZmYjg1YmItNWQ4OC00YWM0LWE0ZDktYThjOTZiZjhhN2Q2XkEyXkFqcGdeQXVyNjgxNTQ3Mjk@._V1_QL75_UX280_CR0,0,280,414_.jpg"



basewidth = 300
img = Image.open(BytesIO(testimg))
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)


# In[446]:


for data in recom_data["titles"]:
    print(data)
    
    #print(recom_data["rating"])


# In[ ]:



input_img = Image.open(BytesIO(response.content))

basewidth = 300
img = Image.open(BytesIO(response.content))
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
#img.save('somepic.jpg')
print('Thanks! Check if this is the boardgame you selected.')
print("If the image is not enough, please check the following link:", try_1["games"][0]["url"])


# In[423]:


test_df = {"link" : []}
for elem in recomm_list:
        # Getting rating
        img_recom = elem.find_all("div" , {"class", "ipc-media ipc-media--poster ipc-image-media-ratio--poster ipc-media--base ipc-media--poster-m ipc-poster__poster-image ipc-media__img"})
        text = "https" + str(img_recom[0]).split(", https")[-1]
        test_df["link"].append(text.split()[0])
        #print(img_recom)
        
pd.DataFrame(test_df)        


# In[419]:


test_df = {"link" : []}

for elem in recomm_list:
        # Getting rating
        img_recom = elem.find_all("div" , {"class", "ipc-media ipc-media--poster ipc-image-media-ratio--poster ipc-media--base ipc-media--poster-m ipc-poster__poster-image ipc-media__img"})
        text = "https" + str(img_recom[0]).split(", https")[-1]
        datos["titulo"].append(e.get_text())
        text.split()[0]
        #print([image_link.attrs["src"] for image_link in img_recom])
        
        pd.DataFrame(test_df)


# In[422]:


#text = str(img_recom[0])
#new_text = "https" + text.split(", https")[-1]
#new_text.split()[0]
text = "https" + str(img_recom[0]).split(", https")[-1]
text.split()[0]


# In[197]:


#div.ipc-sub-grid.ipc-sub-grid--page-span-2.ipc-sub-grid--nowrap.ipc-shoveler__grid


# In[ ]:


#__next > main > div > section.ipc-page-background.ipc-page-background--base.TitlePage__StyledPageBackground-wzlr49-0.dDUGgO > div > section > div > div.TitleMainBelowTheFoldGroup__TitleMainPrimaryGroup-sc-1vpywau-1.btXiqv.ipc-page-grid__item.ipc-page-grid__item--span-2 > section:nth-child(23) > div.ipc-shoveler > div.ipc-sub-grid.ipc-sub-grid--page-span-2.ipc-sub-grid--nowrap.ipc-shoveler__grid > div:nth-child(1) > a > span


# ##### X-Path to click search bar & To click first result

# In[ ]:


(/*[@id="suggestion-search"])


(/*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[2]/a)

