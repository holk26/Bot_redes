import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BrowserController import BrowserControllerX


def abrir_navegador():
    bc = BrowserControllerX()
    bc.navigate('https://www.instagram.com/accounts/login/')
    bc.fill_input('/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input', 'oh.vida.mia')
    bc.fill_input('/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input','Vida#2023@1.')
    bc.wait_and_click('/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button')
    bc.wait_and_click('/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a')

    bc.click_name('toystyleofficial')

    bc.wait_and_click(
        '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a')

    for i in range(1, 4):
        button_xpath = f"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div[3]/button/div/div"
        bc.wait_and_click(button_xpath)

    #bc.quit()

    # Esperar hasta que aparezca el campo de entrada de usuario
    #campo_usuario = WebDriverWait(driver, 10).until(
     #   EC.presence_of_element_located((By.NAME, "username"))
    #)

    # Escribir el nombre de usuario en el campo de entrada
    #campo_usuario.send_keys("oh.vida.mia")

    # Esperar hasta que aparezca el campo de entrada de contraseña
    #campo_contrasena = WebDriverWait(driver, 10).until(
     #   EC.presence_of_element_located((By.NAME, "password"))
    #)

    # Escribir la contraseña en el campo de entrada
    #campo_contrasena.send_keys("Vida#2023@1.")

    # Presionar la tecla Enter para enviar el formulario de inicio de sesión
    #campo_contrasena.send_keys(Keys.RETURN)

    # Esperar a que se cargue la página de inicio de Instagram
    #WebDriverWait(driver, 50).until(
     #   EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/accounts/edit/')]"))
    #)

    #driver.get("https://www.instagram.com/instagram/")

    # Esperar a que aparezca el botón "Seguir" en la página
    #boton_seguir = WebDriverWait(driver, 10).until(
     #   EC.presence_of_element_located((By.XPATH, "//button[text()='Seguir']"))
    #)

    # Imprimir un mensaje de confirmación
    print("Inicio de sesión exitoso")
    breakpoint()

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
