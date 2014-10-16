from pip.backwardcompat import raw_input
import urllib5
from json import load 

url = "http://api.npr.org/query?apiKey="
key = "API_KEY"
url = url + key
url += "&numResults=3"
url += "&format=json"
url += "&id="
npr_id = raw_input("Which NPR ID do you want to query?")
url += npr_id

response = urlopen(url)
json_obj = load(response)

for story in json_obj['list']['story']:
    print (story['title']['$text'])