from bs4 import BeautifulSoup
import requests

response = requests.get('https://en.wikipedia.org/wiki/Stoicism')
response1 = requests.get('https://en.wikipedia.org/wiki/Hedonism')
response2 = requests.get('https://en.wikipedia.org/wiki/Existentialism')
response3 = requests.get('https://en.wikipedia.org/wiki/Epicureanism')
response4 = requests.get('https://en.wikipedia.org/wiki/Nihilism')


soup = BeautifulSoup(response.text, 'lxml')
soup1 = BeautifulSoup(response1.text, 'lxml')
soup2 = BeautifulSoup(response2.text, 'lxml')
soup3 = BeautifulSoup(response3.text, 'lxml')
soup4 = BeautifulSoup(response4.text, 'lxml')

with open('stoic.html','w',encoding='UTF-8') as f:
    f.write(soup.prettify())

with open('hedonist.html','w',encoding='UTF-8') as f:
    f.write(soup1.prettify())

with open('Existentialism.html','w',encoding='UTF-8') as f:
    f.write(soup2.prettify())

with open('Epicureanism.html','w',encoding='UTF-8') as f:
    f.write(soup3.prettify())

with open('Nihilism.html','w',encoding='UTF-8') as f:
    f.write(soup4.prettify())


