import pandas as pd
from bs4 import BeautifulSoup
import requests
import datetime
import csv

#Get the products Urls :
def get_urls(search_url,num_pages ):
    base_url = "https://www.amazon.fr"
    if "&page=" in search_url:
        search_url = search_url.split("&page=")[0]

    
    if search_url.endswith("&"):
        search_url_prefix = search_url + "page="
    else:
        search_url_prefix = search_url + "&page="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    product_links = [] 
    for page_num in range(1, num_pages+1): 
        url = search_url_prefix + str(page_num)
        print(f"Scraping page {page_num}: {url}") 

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser') 

        products = soup.find_all("div", {"data-component-type": "s-search-result"})

        for product in products:
            link_tag = product.find("a", class_="a-link-normal s-no-outline")
            if link_tag and "href" in link_tag.attrs:
                href = link_tag["href"]

                if "/dp/" in href:
                    clean_link = base_url + href.split("?")[0]
                    product_links.append(clean_link)

    return product_links 

#Scrap the price, name and link 
def scrap_infos(liens,file):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }   
    file=file+'.csv'
    with open(file, 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Price','link', 'Date'])
 
    for link in liens:
        page_prods = requests.get(link, headers=headers)
        soup2_prods = BeautifulSoup(page_prods.content, 'html.parser')

        # Get title safely
        title_tag = soup2_prods.find(id="productTitle")
        title = title_tag.get_text(strip=True) if title_tag else "No title found"

        # Get price safely
        whole_tag = soup2_prods.find('span', class_='a-price-whole')
        fraction_tag = soup2_prods.find('span', class_='a-price-fraction')

        if whole_tag and fraction_tag:
            price = whole_tag.get_text(strip=True) + ',' + fraction_tag.get_text(strip=True) + ' €'
        else:
            price = "Price not found"

        

        today = datetime.date.today()
        data = [title, price,link, today]

        # Append only the data, not the header every time
        with open(file, 'a+', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(data)
    return file

#Preview of the data

def preview_data():
    df=pd.read_csv(file)
    print(df.head(10))