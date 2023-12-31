import requests
from bs4 import BeautifulSoup

endereco = 'https://realpython.github.io/fake-jobs/'

resposta = requests.get(endereco)
soup = BeautifulSoup(resposta.text, 'html.parser')

for cartao in soup.find_all('div', class_='card'):
    titulo = cartao.find('h2', class_='title').text.strip()
    empresa = cartao.find('h3', class_='subtitle').text.strip()
    localizacao = cartao.find('p', class_='location').text.strip()

    print(f"Título: {titulo}\nEmpresa: {empresa}\nLocalização: {localizacao}\n{'-' * 30}")
