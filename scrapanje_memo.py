import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup, NavigableString
import pandas as pd

url = "https://moresults.org/competitions/memo-"
pari = []

leto = 2007
while leto < 2026:
    driver = webdriver.Chrome()
    driver.get(url + str(leto))

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[href^='/contestants/']"))
    )

    zadnja_visina = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1.0)
        nova_visina = driver.execute_script("return document.body.scrollHeight")
        if nova_visina == zadnja_visina:
            break
        zadnja_visina = nova_visina

    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, "html.parser")
    vrstice = soup.find_all("tr")

    for vrstica in vrstice:
        ime_element = vrstica.select_one("a[href^='/contestants/']")
        ime = ime_element.get_text(strip=True) if ime_element else None

        drzava_div = vrstica.select_one("a[href^='/countries/individual/'] div")
        drzava = None
        if drzava_div:
            for del_besedila in drzava_div.contents:
                if isinstance(del_besedila, NavigableString):
                    kandidat = del_besedila.strip()
                    if kandidat:
                        drzava = kandidat
                        break

        if ime and drzava:
            pari.append((drzava, ime))

    print(f"Leto {leto} obdelano")
    leto += 1
    
pari_unikatni = sorted(set(pari))

df_pari = pd.DataFrame(pari_unikatni, columns=["Država", "Tekmovalec"])
df_pari.to_csv("memo.csv", index=False, encoding="utf-8")
