from bs4 import BeautifulSoup
import requests
from twilio.rest import Client

#BeautifulSoup part
url = "https://my.uhds.oregonstate.edu/api/drupal/hours"
url = "https://uhds.oregonstate.edu/restaurants/clubhouse-deli"
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")
print(soup)

# print(soup.find_all('a', class_ = 'content'))


# #Twilio texting part

# # Your Account SID and Auth Token from console.twilio.com
# account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# auth_token  = "your_auth_token"

# client = Client(account_sid, auth_token)

# message = client.messages.create(
#     to="+15558675309",
#     from_="+15017250604",
#     body="Hello from Python!")

# print(message.sid)