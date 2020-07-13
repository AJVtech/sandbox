from bs4 import BeautifulSoup 
import requests 
import geopy

geolocator = geopy.Nominatim(user_agent='my-application')

zipcode = input('Enter Zip Code: ')
location = geolocator.geocode(zipcode) 
latitude = location.latitude 
longitude = location.longitude

site = f'https://forecast.weather.gov/MapClick.php?lat={latitude}&lon={longitude}' 
source = requests.get(site).text 
soup = BeautifulSoup(source, 'lxml')

try:
    location = soup.find('h2', class_='panel-title').text 
    forecast = soup.find('p', class_='myforecast-current').text 
    temp = soup.find('p', class_='myforecast-current-lrg').text

    print(f'Weather for {location}')
    print(forecast)
    print(temp)
except AttributeError:
    print('Invalid Location')

