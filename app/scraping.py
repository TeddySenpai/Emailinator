import requests
from bs4 import BeautifulSoup

def scrape_leads(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    leads = []
    for item in soup.find_all('div', class_='lead-item'):
        lead = {
            'name': item.find('h2').text,
            'email': item.find('a', class_='email').text
        }
        leads.append(lead)
    return leads
