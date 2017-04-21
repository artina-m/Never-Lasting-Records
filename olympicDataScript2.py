
# coding: utf-8

# In[14]:

import requests
from bs4 import BeautifulSoup


# In[15]:

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


# In[16]:

longJumpM = requests.get("https://www.olympic.org/athletics/long-jump-men");
longJumpW = requests.get("https://www.olympic.org/athletics/long-jump-women");

hammerThrowM = requests.get("https://www.olympic.org/athletics/hammer-throw-men");
hammerThrowW = requests.get("https://www.olympic.org/athletics/hammer-throw-women");

freestyleSwimM = requests.get("https://www.olympic.org/swimming/400m-freestyle-men");
freestyleSwimW = requests.get("https://www.olympic.org/swimming/400m-freestyle-women");

hurdlesM = requests.get("https://www.olympic.org/athletics/400m-hurdles-men");
hurdlesW = requests.get("https://www.olympic.org/athletics/400m-hurdles-women"); #400

shotPutM =  requests.get("https://www.olympic.org/athletics/shot-put-men");
shotPutW =  requests.get("https://www.olympic.org/athletics/shot-put-women");

tripleJumpM =  requests.get("https://www.olympic.org/athletics/triple-jump-men");
tripleJumpW =  requests.get("https://www.olympic.org/athletics/triple-jump-women");

trackM = requests.get("https://www.olympic.org/athletics/100m-men");
trackW = requests.get("https://www.olympic.org/athletics/100m-women");

swimM = requests.get("https://www.olympic.org/swimming/200m-butterfly-men");
swimW = requests.get("https://www.olympic.org/swimming/200m-butterfly-women");

throwM = requests.get("https://www.olympic.org/athletics/discus-throw-men");
throwW = requests.get("https://www.olympic.org/athletics/discus-throw-women");

highJumpM = requests.get("https://www.olympic.org/athletics/high-jump-men");
highJumpW = requests.get("https://www.olympic.org/athletics/high-jump-women");



# In[17]:

def connectData(request, title):
    soup = BeautifulSoup(request.content, 'html.parser')
    tables =  soup.find_all(class_ ="table3 alt");
    headers = soup.find_all("h2");

    dataScrape(title, tables, headers);


# In[18]:

connectData(longJumpM,"Long Jump Mens");
connectData(longJumpW,"Long Jump Womens");

connectData(hammerThrowM,"Hammer Throw Mens");
connectData(hammerThrowW,"Hammer Throw Womens");

connectData(freestyleSwimM,"400m Freestyle Mens");
connectData(freestyleSwimW,"400m Freestyle Womens");


connectData(hurdlesM,"Hurdles Mens");
connectData(hurdlesW,"Hurdles Womens");

connectData(shotPutM,"Shot Put Mens");
connectData(shotPutW,"Shot Put Womens");

connectData(tripleJumpM,"Triple Jump Mens");
connectData(tripleJumpW,"Triple Jump Womens");

connectData(trackM,"100m Mens");
connectData(trackW,"100m Womens");

connectData(swimM,"200m Butterfly Mens");
connectData(swimW,"200m Butterfly Womens");

connectData(throwM,"Discus Throw Mens");
connectData(throwW,"Discus Throw Womens");

connectData(highJumpM,"High Jump Mens");
connectData(highJumpW,"High Jump Womens");







# In[ ]:




# In[19]:

import csv
def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "wt") as csv_file:
        writer = csv.writer(csv_file, delimiter=',');
        for line in data:
            writer.writerow(line);


# In[20]:

f= open('OplympicRegression.csv', 'wt')
writer = csv_writer(dataFile,'OplympicRegression.csv' );
f.close()


# In[ ]:



