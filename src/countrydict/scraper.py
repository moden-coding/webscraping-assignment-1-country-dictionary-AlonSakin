import requests
from bs4 import BeautifulSoup

def build_country_dict(soup):
    countries = soup.find_all("div", class_ = "country")
    country_names = list(map(lambda country: country.find('h3', class_ = "country-name").get_text(strip = True), countries))
    country_capitals = list(map(lambda country: country.find('span', class_ = "country-capital").get_text(strip = True), countries))
    country_areas = list(map(lambda country: float(country.find('span', class_ = "country-area").get_text(strip = True)), countries))
    country_populations = list(map(lambda country: int(country.find('span', class_ = "country-population").get_text(strip = True)), countries))

    zipped = zip(country_names, country_capitals, country_areas, country_populations)

    return {name: {"Population": population, "Area": area, "Capital": capital} for name,capital,area,population in zipped}


if __name__ == "__main__":
    url = "https://www.scrapethissite.com/pages/simple/"
    resp = requests.get(url, timeout=20)
    soup = BeautifulSoup(resp.text, "html.parser")
    
    
    # build_country_dict(soup)
    data = build_country_dict(soup)
    
    
    if len(data) != 250:
        print(f'''You should have found 250 countries, you found {len(data)}''')
    
    if int(data["Angola"]["Population"]) != 13068161:
        print(f'''Angola's population should be 13068161 you said it was {data["Angola"]["Population"]}''')
        
    if float(data["Israel"]["Area"]) != 20770.0:
        print(f'''Israel should have an area of 20770.0 you said it was {data["Israel"]["Area"]}''')
        
    if data["Venezuela"]["Capital"] != "Caracas":
        print(f'''Venezuela's capital should be Caracas, it was {data["Venezuela"]["Capital"]}''')

    
