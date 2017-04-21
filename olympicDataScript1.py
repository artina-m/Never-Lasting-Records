
# coding: utf-8

# In[1]:

import requests
from bs4 import BeautifulSoup

# https://www.dataquest.io/blog/web-scraping-tutorial-python/

track = requests.get("https://www.olympic.org/athletics/100m-men");
trackW = requests.get("https://www.olympic.org/athletics/100m-women");

swim = requests.get("https://www.olympic.org/swimming/200m-butterfly-men");
swimW = requests.get("https://www.olympic.org/swimming/200m-butterfly-women");

throw = requests.get("https://www.olympic.org/athletics/discus-throw-men");
throwW = requests.get("https://www.olympic.org/athletics/discus-throw-women");


# In[21]:

dataFile = [['Game','Year', "Medal", 'Result','Country','Athlete']];

# Get data from HTML elements
# Get year of Olympic Game
# Get medal result of game
# Get athlete
# Get Country
def dataScrape(game, table, header):
    i = 1;
    for t in table:
        getYear = header[i].get_text().strip();
        year = getYear[-4:];
        i += 1;
        
        #Gold Medal
        goldMedal = t.select("tr")[1];
        
        gResult = goldMedal.find(class_="txt");
        if isinstance(gResult, type(None)): gResult = "";
        else: gResult = gResult.get_text();
            
        gAthlete = goldMedal.find(class_="name");
        if isinstance(gAthlete, type(None)): gAthlete = "";
        else: gAthlete = gAthlete.get_text();
        
        gCountry = goldMedal.find(class_="profile-row").get_text().strip();
        
        goldData = [game, year,"gold",gResult, gCountry, gAthlete];
        dataFile.append(goldData);
        
        #Silver Medal
        silverMedal = t.select("tr")[2];
        
        sResult = silverMedal.find(class_="txt")
        if isinstance(sResult, type(None)): sResult = "";
        else: sResult = sResult.get_text();
            
        sAthlete = silverMedal.find(class_="name");
        if isinstance(sAthlete, type(None)): sAthlete = "";
        else: sAthlete = sAthlete.get_text();
            
        sCountry = silverMedal.find(class_="profile-row").get_text().strip();
        
        silverData = [game, year,"silver",sResult,sCountry, sAthlete];
        dataFile.append(silverData);
        
        #Bronze Medal
        if (len(t.select("tr")) == 4):
            bronzeMedal = t.select("tr")[3];

            bResult = bronzeMedal.find(class_="txt")
            if isinstance(bResult, type(None)): bResult = "";
            else: bResult = bResult.get_text();

            bAthlete = bronzeMedal.find(class_="name");
            if isinstance(bAthlete, type(None)): bAthlete = "";
            else: bAthlete = bAthlete.get_text();

            bCountry = bronzeMedal.find(class_="profile-row").get_text().strip();

            bronzeData = [game, year,"bronze",bResult,bCountry, bAthlete];
            dataFile.append(bronzeData);


# In[22]:

# Data-Scrape 100M Men from 1896-2016
trackSoup = BeautifulSoup(track.content, 'html.parser')
trackTables =  trackSoup.find_all(class_ ="table3 alt");
trackHeaders = trackSoup.find_all("h2");

dataScrape("100M Men", trackTables, trackHeaders);


# In[23]:

# Data-Scrape 100M Women from 1928-2016
trackSoupW = BeautifulSoup(trackW.content, 'html.parser')
trackTablesW =  trackSoupW.find_all(class_ ="table3 alt");
trackHeadersW = trackSoupW.find_all("h2");

dataScrape("100M Women", trackTablesW, trackHeadersW);


# In[24]:

# Data-Scrape 200M Butterfly Men from 1960-2016
swimSoup = BeautifulSoup(swim.content, 'html.parser')
swimTables =  swimSoup.find_all(class_ ="table3 alt");
swimHeaders = swimSoup.find_all("h2");

dataScrape("200M Butterfly Men", swimTables, swimHeaders);


# In[25]:

# Data-Scrape 200M Butterfly Women from 1968-2016
swimSoupW = BeautifulSoup(swimW.content, 'html.parser')
swimTablesW =  swimSoupW.find_all(class_ ="table3 alt");
swimHeadersW = swimSoupW.find_all("h2");

dataScrape("200M Butterfly Women", swimTablesW, swimHeadersW);


# In[26]:

# Data-Scrape Discus Throw Women from 1908-2016
throwSoupW = BeautifulSoup(throwW.content, 'html.parser')
throwTablesW =  throwSoupW.find_all(class_ ="table3 alt");
throwHeadersW = throwSoupW.find_all("h2");

dataScrape("Discus Throw Women", throwTablesW, throwHeadersW);


# In[27]:

# Data-Scrape Discus Throw Men from 1928-2016
throwSoup = BeautifulSoup(throw.content, 'html.parser')
throwTables =  throwSoup.find_all(class_ ="table3 alt");
throwHeaders = throwSoup.find_all("h2");

dataScrape("Discus Throw Women", throwTablesW, throwHeadersW);


# In[28]:

import csv
def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "wt") as csv_file:
        writer = csv.writer(csv_file, delimiter=',');
        for line in data:
            writer.writerow(line);


# In[29]:

f= open('oplympicData.csv', 'wt')
writer = csv_writer(dataFile,'oplympicData.csv' );
f.close()

