from flask import Blueprint, render_template, request

from app.hidratacao import calculo_hidratacao
from app.weather import WeatherError, get_weather

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    erro = None

    if request.method == "POST":
        cidade = request.form.get("city", "").strip()
        peso_raw = request.form.get("weight", "")

        try:
            peso = float(peso_raw)
            clima = get_weather(cidade)
            litros = calculo_hidratacao(peso, clima["temp"])
            resultado = {**clima, "water_liters": litros}
        except (WeatherError, ValueError) as e:
            erro = str(e)

    return render_template("index.html", result=resultado, error=erro)