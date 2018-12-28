import requests 
from bs4 import BeautifulSoup

#download webpage
page = requests.get('https://www.askhargapedia.com/#download')

#parsing the webpage
soup = BeautifulSoup(page.content,  'html.parser')

#to find the link in the "As featured on" section and print the links available
for tag in soup.findAll('section', class_='padding', id="featured"):
    for link in tag.findAll('a'):
        print(link.get('href'))

#save the link extracted into text file
with open('AvailableLink.txt', 'w') as textFile:
    for link in tag.findAll('a'):
        textFile.write(link.get('href') + '\n')
                   

