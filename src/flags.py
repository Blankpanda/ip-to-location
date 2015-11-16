import urllib, urllib.request
from bs4 import BeautifulSoup

def get_flag_image(country):
    country = country.lower()
    url = "http://www.geonames.org/flags/x/" + country + ".gif"
    file_name = country + ".gif"
    urllib.request.urlretrieve(url, file_name)

    return file_name

def get_country_full_name(abbrev):

    url = "http://sustainablesources.com/resources/country-abbreviations/"
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    matches = soup.find_all("td")

    for match in matches:
        try:
            if match.get_text() == abbrev.lower():
                return matches[matches.index(match) + 1].contents[0]
        except Exception as e:
            print("couldn't encode country name.")
