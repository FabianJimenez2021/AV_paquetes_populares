# #Análisis de paginas web 
import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"
respuesta = requests.get(url)
texto = respuesta.text
soup = BeautifulSoup(texto, "html.parser")

#Para seleccionar un id hay que utilizar un # antes de este 
#Para seleccionar una clase se debe utilizar un .
preguntas = soup.select(".s-post-summary")
print(preguntas[0]["data-post-id"])

#O
# for pregunta in preguntas:
#     print(pregunta)
#     pass

for pregunta in preguntas:
    titulo = pregunta.select_one(".s-link").get_text()
    usuario = pregunta.select_one(".s-user-card--link").get_text()
    # print(f"{usuario} -- titulo: {titulo}")
