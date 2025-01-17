
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import time
from config import usuario, senha, mensagem, links
import random  

def setup_driver():
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(2)
    return driver

def login(driver):
    
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')

    username_input.send_keys(usuario)
    password_input.send_keys(senha)
    password_input.send_keys(Keys.RETURN)
    time.sleep(4)

def enviar_mensagem(driver, link):
    print(f"Acessando o link: {link}")
    driver.get(link)
    time.sleep(random.uniform(3, 5))

    try:
        
        print("Clicando o botão de 'Message'...")
        message_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Message']"))
        )
        message_button.click()
        print("Clicou no botão de 'message'.")

        try:
            not_now_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))
            )
            not_now_button.click()
            print("Clicou no botão 'Not Now'.")
        except NoSuchElementException as e:
            print(f'Elemento não encontrado: {e}')
        except TimeoutException as e:
            print(f'Tempo de espera esgotado: {e}')
        except Exception as e:
            print(f'Erro inesperado: {e}')

        print("Aguardando a caixa de mensagem...")
        message_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Message']"))
        )
        message_box.click()  # Clica na caixa para ativá-la
        message_box.send_keys(mensagem)

        print("Aguardando o botão 'Send'...")
        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Send']"))
        )
        send_button.click()
        print(f'Mensagem enviada para {link}')

        time.sleep(random.uniform(3, 5))

    except NoSuchElementException as e:
        print(f'Elemento não encontrado: {e}')
    except TimeoutException as e:
        print(f'Tempo de espera esgotado: {e}')
    except Exception as e:
        print(f'Erro inesperado: {e}')


