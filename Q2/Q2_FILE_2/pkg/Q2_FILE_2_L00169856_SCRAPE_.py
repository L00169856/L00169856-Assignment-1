"""
# File             : Q2_FILE_2_L00169856_SCRAPE_.py
# Created          : 09/11/2021 20:39
# Author           : Patrick McGourty
# Version          : v1.0.0
# Licencing        : (c) 2021 Patrick McGourty
#                  Available under GNU public License (GPL)
# Description      : Code for scraping the Apache2 website
#

"""
from bs4 import BeautifulSoup
import requests

"Declaring url as the webserver url"
url = "http://192.168.225.132/"
"requesting to get the url and declaring it page"
page = requests.get(url)
"Creating variable soup declaring content for the above and letting beautifulsoup know its parsering html"
soup = BeautifulSoup(page.content, "html.parser")
"printing the html in easily readable format"
print(soup.prettify())