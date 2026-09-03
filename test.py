import requests

url = "https://hidratacao-app.calmfield-923b4e88.eastus.azurecontainerapps.io"
dados = {
    "city": "São Paulo",
    "weight": "70"
}

resposta = requests.post(url, data=dados)

print("Status Code:", resposta.status_code)
print("Conteúdo da Resposta (HTML):")
print(resposta.text)