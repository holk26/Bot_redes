import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def abrir_navegador():
    # Crear una instancia del navegador Chrome
    driver = webdriver.Chrome()

    # Navegar a la página de inicio de sesión de Instagram
    driver.get("https://www.instagram.com/accounts/login/")

    # Esperar hasta que aparezca el campo de entrada de usuario
    campo_usuario = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    # Escribir el nombre de usuario en el campo de entrada
    campo_usuario.send_keys("oh.vida.mia")

    # Esperar hasta que aparezca el campo de entrada de contraseña
    campo_contrasena = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

    # Escribir la contraseña en el campo de entrada
    campo_contrasena.send_keys("Vida#2023@1.")

    # Presionar la tecla Enter para enviar el formulario de inicio de sesión
    campo_contrasena.send_keys(Keys.RETURN)

    # Esperar a que se cargue la página de inicio de Instagram
    WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/accounts/edit/')]"))
    )

    driver.get("https://www.instagram.com/instagram/")

    # Esperar a que aparezca el botón "Seguir" en la página
    boton_seguir = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Seguir']"))
    )

    # Imprimir un mensaje de confirmación
    print("Inicio de sesión exitoso")

# Crear una ventana
ventana = tk.Tk()

ventana.title("Robot instagram")

# Definir el tamaño de la ventana
ventana.geometry("400x300")

# Agregar un botón a la ventana
boton = tk.Button(ventana, text="Abrir Navegador", command=abrir_navegador)
boton.pack()

# Mostrar la ventana
ventana.mainloop()
