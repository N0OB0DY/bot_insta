# bot.py
from scraper import setup_driver, login, enviar_mensagem
from config import links
import time

def main():
    driver = setup_driver()
    login(driver)

    for link in links:
        enviar_mensagem(driver, link)
        time.sleep(5)
        
    driver.quit()

if __name__ == '__main__':
    main()
