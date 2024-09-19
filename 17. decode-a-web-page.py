import requests
from bs4 import BeautifulSoup


url = 'https://www.nytimes.com/';
r = requests.get(url);
soup = BeautifulSoup(r.text, "html.parser");

# Gives error, needs to downgrade to an older version so going to skip for now
for heading in soup.find("css-xdandi"):
    print(heading);
