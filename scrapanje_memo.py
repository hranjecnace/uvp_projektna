from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd


def obstaja(element):
    if element is None:
        return None
    else:
        return element.get_text(strip=True)


url = "https://moresults.org/competitions/memo-"
podatki = []
leto = 2007


while leto < 2026:
    driver = webdriver.Chrome()
    driver.get(url + str(leto))

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[href^='/contestants/']"))
    )

    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, "html.parser")
    vrstice = soup.find_all("tr")
    
    for vrstica in vrstice:
        ime = obstaja(vrstica.select_one("a[href^='/contestants/']"))
        drzava = obstaja(vrstica.select_one("a[href^='/countries/individual/'] div"))

        if ime and drzava:
            podatki.append((drzava[2:], ime))

    print(f"Leto {leto} obdelano")
    leto += 1

df = pd.DataFrame(podatki, columns=["Država", "Tekmovalec"])
df.to_csv("memo.csv", index=False, encoding="utf-8")