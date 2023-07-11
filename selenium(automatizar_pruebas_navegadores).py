from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

#Abrir una nueva pestaña en el navegador sin que se cierre
# options =webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# browser = webdriver.Chrome(options=options)

#Abrir una sola pestaña en el navegador  
browser = webdriver.Chrome()

# Genera un tiempo de espera para que la página web cargue toda su información
browser.implicitly_wait(10)
browser.get("https://github.com/login")

#Hacer click en un botón de la página web  
# link1 = browser.find_element(By.LINK_TEXT, "Sign up")
# link1.click()

#Buscar elementos HTML dentro de la página web
user_input = browser.find_element(By.ID, "login_field")
pass_input = browser.find_element(By.ID, "password")

#Colocar un texto dentro de las casillas 
user_input.send_keys(os.environ.get("user"))
pass_input.send_keys(os.environ.get("pass"))

#Hacer un enter 
pass_input.send_keys(Keys.RETURN)

#Las clases hay que separarlas por "." en vez de ","
profile = browser.find_element(
    By.CLASS_NAME,
    "css-truncate.css-truncate-target.ml-1"
)

label = profile.get_attribute("innerHTML")
assert "Fabianjimenez2021" in label 

#Para utilizar quit() hay que utilizar una sola pestaña 
browser.quit()