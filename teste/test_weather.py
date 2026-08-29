import os

import pytest
import requests_mock

os.environ.setdefault("OPENWEATHER_API_KEY", "chave-fake-para-teste")

from app.weather import WeatherError, get_weather

def test_clima_sucesso(): 
    with requests_mock.Mocker() as m:
        m.get(
            "https://api.openweathermap.org/data/2.5/weather",
            json={
                "name": "Belo Horizonte",
                "main": {"temp": 24, "temp_min": 20, "temp_max": 27}, 
            },
        )
        dados = get_weather("Belo Horizonte")
        assert dados["temp"] == 24
        assert dados["city"] == "Belo Horizonte"

def test_cidade_nao_encontrada():
    with requests_mock.Mocker() as m:
        m.get("https://api.openweathermap.org/data/2.5/weather", status_code=404)
        with pytest.raises(WeatherError):
            get_weather("CidadeQueNaoExiste")
        
def test_erro_generico_da_api():
    with requests_mock.Mocker() as m:
        m.get("https://api.openweathermap.org/data/2.5/weather", status_code=500)
        with pytest.raises(WeatherError): 
            get_weather("Belo Horizonte")