import os
import requests

OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


class WeatherError(Exception):
    pass


def get_weather(city: str) -> dict:
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        raise WeatherError("Chave da API não configurada")

    params = {"q": city, "appid": api_key, "units": "metric", "lang": "pt_br"}

    try:
        response = requests.get(OPENWEATHER_URL, params=params, timeout=5)
    except requests.exceptions.RequestException:
        raise WeatherError("Não foi possível conectar à API do clima")

    if response.status_code == 404:
        raise WeatherError(f"Cidade '{city}' não encontrada")
    if response.status_code != 200:
        raise WeatherError("API do clima retornou um erro")

    data = response.json()
    return {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "temp_min": data["main"]["temp_min"],
        "temp_max": data["main"]["temp_max"],
    }
