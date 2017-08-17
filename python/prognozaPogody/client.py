import requests, json

class Client(object):
    """Client sluzy do pobierania danych z open weather map client i z zwracania 
       danych w postaci slownikowej przy pomocy metody #fetch()"""
      
    def __init__(self, cities):
        self.openweather_url = "http://api.openweathermap.org/data/2.5/forecast"
        self.api_key =  "823afac09c34370d779296d434aea0e9"
        self.cities = cities

    def fetch(self):
        weather_data = list(map(self.fetch_one_city, self.cities))
        return weather_data
    
    def fetch_one_city(self, city_name):
        params = { "appid": self.api_key, "q": city_name }
        response = requests.get("http://api.openweathermap.org/data/2.5/forecast", params = params)
        return json.loads(response.text)
    
if __name__ == "__main__":
    import numpy as np
    client = Client(["Danzig", "Warsaw", "Breslau"])
    data = client.fetch()
    listy_zjawisk = list(map(lambda miasto: miasto['list'], data))
    temperatury = []
    
    for prognoza_w_miescie in listy_zjawisk:
        temperatury.append(list(map(lambda obserwacja: obserwacja['main']['temp'], prognoza_w_miescie)))
        
    dates = np.arange(len(temperatury[0]))
   
    import matplotlib.pyplot as plt
    
    _fig, axs = plt.subplots(1, 3, figsize=(30, 10))
    
    for i, ax in enumerate(axs):
        ax.plot(dates, temperatury[i])
    plt.show()