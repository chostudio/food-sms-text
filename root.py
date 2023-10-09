from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
from datetime import date
import os

SECRET_API_KEY = os.environ["SECRET_API_KEY"]

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

#get today's date
today = date.today()

# Numerical day
d2 = today.strftime("%d")

# example: 30, 01, 05


# multiple big for loops?
# inner while loop?
# how to accurately insert text in a string?
# maybe write a method for ease of readability?

# find the div that contains the h6 title tag
titleText = ""
menuTitleList = []

titleList = soup.find_all('h1', class_ = 'zone')

# This works for inner restaurant webpage food and when
menuTitleList = soup2.find_all('div', class_ = 'section')[:3]

menuTitleText = ""
for i in menuTitleList:
        menuTitleText += i.getText() + "\n"

print(menuTitleText)
# restaurantList = soup.find_all('a', class_ = 'concept')
# timeList = soup.find_all('div', class_ = 'time')

# foodList = soup.find_all('div', class_ = 'concept')
# for data in foodList:
#     titleText += data.findChildren()
# print(titleText)

# splice [start:end]
# [6:10] for main dining hall titles
finalTitleList = []
for data in titleList[6:10]:
        # Remove tags
        finalTitleList.append(data.get_text())
print(finalTitleList)
# print(soup.find_all('div', class_ = 'pure_g').contents)



textMessageBody = ""
# textMessageBody += soup.something



# #Twilio texting part

# figure out how to hide the api key in hosting dashboard

# Your Account SID and Auth Token from console.twilio.com
# account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# auth_token  = "your_auth_token"

# client = Client(account_sid, auth_token)

# # for i in range(len(phoneNumbers)):

# for sms in client.messages.list():
#   print(sms.to)

# message = client.messages.create(
#     to = phoneNumbers[i], #this is the phone number that is recieving texts
#     from_="+15017250604",
#     body = textMessageBody )

# print(message.sid)