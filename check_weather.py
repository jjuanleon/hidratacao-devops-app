from dotenv import load_dotenv
load_dotenv()

from app.weather import get_weather, WeatherError
try:
    get_weather('CidadeTesteABC')
except WeatherError as e:
    print('Erro esperado', e)
