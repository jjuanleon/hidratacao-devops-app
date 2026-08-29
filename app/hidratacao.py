def calculo_hidratacao(peso_kg: float, temperatura_c: float) -> float:
    if peso_kg <= 0:
        raise ValueError("Peso precisa ser maior que zero")

    base_ml = peso_kg * 35

    if temperatura_c >= 30:
        base_ml += 700
    elif temperatura_c >= 25:
        base_ml += 350

    return round(base_ml / 1000, 2)
