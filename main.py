from bs4 import BeautifulSoup
import requests
import lxml
from filling_sheets import FillingForms


FIREFOX_WEBDRIVER = "/home/walter/Public/drivers/firefox-driver/geckodriver"
send_data = FillingForms(FIREFOX_WEBDRIVER)

ZILLOW_WEBPAGE_URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A37.811917679459086%2C%22south%22%3A37.73864807505057%2C%22east%22%3A-122.32758609179687%2C%22west%22%3A-122.53907290820312%7D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A618290%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%2C%22usersSearchTerm%22%3A%22San%20Francisco%20CA%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%7D%5D%2C%22category%22%3A%22cat1%22%7D"

headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(url=ZILLOW_WEBPAGE_URL, headers=headers)
zillow_rental_page = response.text

soup = BeautifulSoup(zillow_rental_page, "lxml")
link_elements = soup.find_all(name="a", class_="property-card-link")

rental_links = [link.get("href") for link in link_elements]

new_list_of_home_links = []

for link in rental_links:
    link_url = "https://www.zillow.com"
    if link_url not in link:
        combining = link_url + link
        new_list_of_home_links.append(combining)
    else:
        new_list_of_home_links.append(link)
        
print(new_list_of_home_links)

home_prices_element = soup.find_all(name="span", class_="vjmXt")
home_prices_text = [price.getText() for price in home_prices_element]
print(home_prices_text)

home_addresses_elements = soup.select(selector="#grid-search-results ul li a address")
home_addresses_texts = [address.get_text() for address in home_addresses_elements]
print(home_addresses_texts)

send_data.sending_data(home_addresses=home_addresses_texts, home_prices=home_prices_text, home_links=new_list_of_home_links)



            
   
    