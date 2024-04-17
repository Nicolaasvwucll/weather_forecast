import urllib.request
import json
from urllib.error import HTTPError

def main():
    print("Hallo welkom op onze weer-cli")
    #weather_json = request_weather(request_location())
    while True:
        location = request_location()
        try:
            weather_json = request_weather(location)
            if weather_json:
                break  # Exit the loop if weather data is successfully retrieved
            else:
                print("Error: Could not retrieve weather data. Please try again.")
        except HTTPError as e:
                print(f"HTTP Error: {e.code} - {e.reason}")

    
    temp_celsius = round(weather_json.get("temp") - 273.15) # Alle temperaturen van Kelvin naar Celsius omzetten
    temp_celsius_max = round(weather_json.get("temp_max") - 273.15)
    temp_celsius_min = round(weather_json.get("temp_min") - 273.15)
    wind_speed = f"{weather_json.get('wind').get('speed')} m/s"
    wind_degree = weather_json.get('wind').get('deg')
    
    #Wind degrees omzetten naar windrichting 
    if wind_degree >= 350 or wind_degree <= 10:
        wind_direction = "N"
    elif 20 <= wind_degree <= 30:
        wind_direction = "N/NE"
    elif 40 <= wind_degree <= 50:
        wind_direction = "NE"
    elif 60 <= wind_degree <= 70:
        wind_direction = "E/NE"
    elif 80 <= wind_degree <= 100:
        wind_direction = "E"
    elif 110 <= wind_degree <= 120:
        wind_direction = "E/SE"
    elif 130 <= wind_degree <= 140:
        wind_direction = "SE"
    elif 150 <= wind_degree <= 160:
        wind_direction = "S/SE"
    elif 170 <= wind_degree <= 190:
        wind_direction = "S"
    elif 200 <= wind_degree <= 210:
        wind_direction = "S/SW"
    elif 220 <= wind_degree <= 230:
        wind_direction = "SW"
    elif 240 <= wind_degree <= 250:
        wind_direction = "W/SW"
    elif 260 <= wind_degree <= 280:
        wind_direction = "W"
    elif 290 <= wind_degree <= 300:
        wind_direction = "W/NW"
    elif 310 <= wind_degree <= 320:
        wind_direction = "NW"
    elif 330 <= wind_degree <= 340:
        wind_direction = "N/NW"
    else:
        wind_direction = "In between" #Momenteel zo ingesteld , waarden volgen nog niet mooi op elkaar dus er zijn waarden die buiten de ranges van windrichtingen liggen
        
      
    print(f"\nWeersomschrijving: {weather_json.get('desc')}\nTemperatuur: {temp_celsius} graden Celsius \nMax temperatuur: {temp_celsius_max} graden Celsius\nMin temperatuur: {temp_celsius_min} graden Celsius\nWind: {wind_speed} {wind_direction}\n")
 
def request_location():
    location = input('Voer een postcode of plaatsnaam in: ')
   
    if location.isdigit():
        PostalCode = location
        print(PostalCode)
    else:
        City = location
        print(City)
   
    return location
 
def request_weather(location):
    api_key = "a63d18c496d1634e8b62e88c148e8f90"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    
    response = urllib.request.urlopen(url)
     
    if response.status == 200:
        response_json = response.read()
        parsed_json = json.loads(response_json)   #json omzetten
        
        weather_dict = {}   #Dictionary om nodige info in te bewaren
            
        #Data aan weather_dict toevoegen met bepaalde key , value komt uit het parsed_json obj
        weather_dict["temp"]= parsed_json.get("main").get("temp")
        weather_dict["temp_min"]= parsed_json.get("main").get("temp_min")
        weather_dict["temp_max"]= parsed_json.get("main").get("temp_max")
        weather_dict["desc"]= parsed_json.get("weather")[0].get("description")
        weather_dict["wind"]= parsed_json.get("wind")
    else: 
        print(f"Error: {response.status} - {response.reason}")
    return weather_dict

main() 