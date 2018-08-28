from twython import Twython
import requests

 
# api-endpoint
URL = "https://api.scratch.mit.edu/projects/count/all"
r = requests.get(url = URL)
data = r.json()
numofprojects= data['count'][0]
twitter = Twython(APP_KEY, APP_SECRET
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
tweet= 'As of today, '+numofprojects+ 'Scratch projects are shared on Scratch website! Check out Scratch today-> https://scratch.mit.edu/'
twitter.update_status(status=tweet)