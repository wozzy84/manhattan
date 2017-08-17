from datetime import datetime
from client import Client

class DataAdapter(object):
    """DataAdapter adaptuje surowe dane z open weather map api do formatu ktory umozliwia wyswietlenie danych korzystajac z biblioteki matplotlib"""
    
    def __init__(self, data):
        self.data = data

    def adapt(self):
        adapted_data = list(map(self.adapt_item, self.data))

        return adapted_data

    def adapt_item(self, city_forecast):
        return {
            'title': city_forecast['city']['name'],
            'xs': {
                'label': 'Data i godzina',
                'values': self.x_values(city_forecast)
            },
            'ys': {
                'label': 'Temperatura',
                'values': self.y_values(city_forecast)
            }
        }

    def x_values(self, city_forecast):
        forecasts = city_forecast['list']
        return list(map(lambda forecast: datetime.strptime(forecast['dt_txt'], "%Y-%m-%d %H:%M:%S"), forecasts))

    def y_values(self, city_forecast):
        forecasts = city_forecast['list']
        return list(map(lambda forecast: self.to_c(forecast['main']['temp']), forecasts))
    
    def to_c(self, temp):
        return round(temp - 273.15, 2)

if __name__ == '__main__':
    cities = ['Danzig', 'Breslau']
    client = Client(cities)
    data = client.fetch()
    adapter = DataAdapter(data)
    data = adapter.adapt()
    print(data)