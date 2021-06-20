import requests
url = 'https://pokemon.fandom.com/wiki/Bulbasaur'
r = requests.get(url)

#can get status code
#print(r.status_code)

#can get encoding 
#print(r.encoding)

#can get contents of web bage
print(r.text)

#can get response header
#print(r.headers)

