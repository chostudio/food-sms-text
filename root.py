from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
import os

# BeautifulSoup part
url = "https://my.uhds.oregonstate.edu/api/drupal/hours"

urlDictionary = {
"urlWestSideGrill" : "https://my.uhds.oregonstate.edu/api/dining/weeklymenu/15",
"urlClubhouseDeli" : "https://my.uhds.oregonstate.edu/api/dining/weeklymenu/09",
"urlCoopersCreek" : "https://my.uhds.oregonstate.edu/api/dining/weeklymenu/10",
"urlRingOfFire" : "https://my.uhds.oregonstate.edu/api/dining/weeklymenu/12",
"urlTomassitosItalianCafe" : "https://my.uhds.oregonstate.edu/api/dining/weeklymenu/14",
"urlSerranos" : "https://my.uhds.oregonstate.edu/api/dining/weeklymenu/13",

"urlEastSideEats" : "https://my.uhds.oregonstate.edu/api/dining/weeklymenu/17",
"urlCalabaloos" : "https://my.uhds.oregonstate.edu/api/dining/weeklymenu/16",
"urlFiveFourOne" : "https://my.uhds.oregonstate.edu/api/dining/weeklymenu/12",
"urlLaCalle" : "https://my.uhds.oregonstate.edu/api/dining/weeklymenu/19",

"urlEastSideEats" : "https://my.uhds.oregonstate.edu/api/dining/weeklymenu/17",
"urlCalabaloos" : "https://my.uhds.oregonstate.edu/api/dining/weeklymenu/16",
"urlFiveFourOne" : "https://my.uhds.oregonstate.edu/api/dining/weeklymenu/12",
"urlLaCalle" : "https://my.uhds.oregonstate.edu/api/dining/weeklymenu/19"
}

html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

html2 = requests.get(urlDictionary["urlWestSideGrill"])
soup2 = BeautifulSoup(html2.content, "html.parser")

# multiple big for loops?
# inner while loop?
# how to accurately insert text in a string?
# maybe write a method for ease of readability?

# find the div that contains the h6 title tag
titleText = ""
menuTitleList = []

diningHallList = soup.find_all('h1', class_ = 'zone')
restaurantList = soup.find_all('div', class_ = 'pure-g')

# This works for inner restaurant webpage food and when
# menuTitleList = soup2.find_all('div', class_ = 'section')[:3]

# menuTitleText = ""
# for i in menuTitleList:
#         menuTitleText += i.getText() + "\n"

# print(menuTitleText)
# restaurantList = soup.find_all('a', class_ = 'concept')
# timeList = soup.find_all('div', class_ = 'time')

# foodList = soup.find_all('div', class_ = 'concept')
# for data in foodList:
#     titleText += data.findChildren()
# print(titleText)

# Twilio texting part
# Your Account SID and Auth Token from console.twilio.com
ACCOUNT_SID = os.environ["ACCOUNT_SID"]
AUTH_TOKEN = os.environ["AUTH_TOKEN"]
NUMBER = os.environ["NUMBER"]

client = Client(ACCOUNT_SID, AUTH_TOKEN)

textMessageBody = "\n"
for i in range(7, 10, 2):
        textMessageBody += diningHallList[i-1].get_text()
        textMessageBody += restaurantList[i].get_text()
        message = client.messages.create(
                from_="+18556429708", # the phone number that is sending texts
                body = textMessageBody,
                to = NUMBER # the phone number that is recieving texts
        )
        textMessageBody = textMessageBody.replace("More Hours >>", "")
        textMessageBody = textMessageBody.replace("\n\n", "\n")
        print(textMessageBody)
textMessageBody = ""