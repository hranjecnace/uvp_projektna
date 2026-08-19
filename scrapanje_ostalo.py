import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def obstaja(element):
    if element is None:
        return None
    else:
        return element.get_text(strip=True)


def poberi_tekmovalce(tekmovanje, prvo_leto, zadnje_leto):
    url = f"https://moresults.org/competitions/{tekmovanje}-"
    podatki = []
    leto = prvo_leto

    print(tekmovanje.upper())

    while leto < zadnje_leto + 1:
        driver = webdriver.Chrome()
        driver.get(url + str(leto))

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "a[href^='/contestants/']")
                )
            )

        except TimeoutException:
            print(f"Leto {leto} ne obstaja")
            driver.quit()
            leto += 1
            continue

        html = driver.page_source
        driver.quit()

        soup = BeautifulSoup(html, "html.parser")
        vrstice = soup.find_all("tr")

        for vrstica in vrstice:
            ime = obstaja(vrstica.select_one("a[href^='/contestants/']"))
            drzava = obstaja(
                vrstica.select_one("a[href^='/countries/individual/'] div")
            )

            if ime and drzava:
                podatki.append((tekmovanje.upper(), drzava[2:], ime))

        print(f"Leto {leto} obdelano")
        leto += 1

    df = pd.DataFrame(podatki, columns=["Tekmvanje", "Država", "Tekmovalec"])
    df.to_csv(f"csv_datoteke/{tekmovanje}.csv", index=False, encoding="utf-8")
