import hug
from client import Client
from data_adapter import DataAdapter

@hug.get(output=hug.output_format.png_image)
def temperaturePlot(cities: hug.types.delimited_list(",")):
    """Rysuje prognozę temperatury dla danych miast"""
    client = Client(cities)
    data = client.fetch()
    adapter = DataAdapter(data)
    data = adapter.adapt()
    citiesPlot = Plot(data).plot()
    return citiesPlot

@hug.get()
def pressurePlot():
    """Rysuje prognozę cisnienia dla danych miast"""
    return "<h1>Tu będzie obrazek cisnienia</h1>"
