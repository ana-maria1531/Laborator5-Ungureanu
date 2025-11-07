from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setarea căii către ChromeDriver
driver_path = r"C:\Users\user\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Deschide Google
    driver.get("https://www.google.com")
    time.sleep(2)

    # Verifică dacă bara de căutare există
    search_box = driver.find_element(By.NAME, "q")
    if search_box.is_displayed():
        print("Testul a trecut: Bara de căutare Google este afișată")

        # Introduce "computer" în bara de căutare și apasă Enter
        search_box.send_keys("computer")
        search_box.send_keys(Keys.RETURN)
        print("Căutarea 'computer' a fost efectuată")
    else:
        print("Testul a eșuat: Bara de căutare Google nu este afișată")

    # Pauză mică ca să vedem browserul
    time.sleep(3)

finally:
    driver.quit()
