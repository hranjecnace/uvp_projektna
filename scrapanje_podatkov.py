import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.imo-official.org/results/individual/year/"
leto = 1959
vsi_podatki = []

def obstaja(element):
    if element is None:
        return None
    else:
        return element.get_text(strip=True)


while leto < 2027:
    response = requests.get(url + str(leto))
    soup = BeautifulSoup(response.text, "html.parser")

    if response.status_code == 404:
        leto += 1
        continue

    kraj = soup.select_one(".results-page__subtitle").get_text(strip=True).split(",")[0]
    drzava_tekmovanja = soup.select_one(".results-page__subtitle").get_text(strip=True).split(",")[1].split("·")[0].strip()
    stevilo_tekmovalcev = soup.select_one(".results-page__subtitle").get_text(strip=True).split(",")[1].split("·")[1].strip().split(" ")[0].strip()

    vrstice = soup.select("tbody tr")

    
    for vrstica in vrstice:
        span = vrstica.select_one("span[data-person-name], span[data-results-anomaly-name]")
        if span:
            ime = span.get("data-name")
            priimek = span.get("data-surname")
        else:
            ime = None
            priimek = None

        narodnost = obstaja(vrstica.select_one(".data-table__country-full"))
        mesto = obstaja(vrstica.select_one(".data-table__section-start"))
        medalja = obstaja(vrstica.select_one(".data-table__medal-char"))
        skupne_tocke = obstaja(vrstica.select_one(".data-table__total-cell"))
        naloge = vrstica.select("td.data-table__num:not(.data-table__total-cell):not([data-value])")
        tocke = [td.text.strip() if td.text else None for td in naloge][1:]
        

        vsi_podatki.append({
            "kraj" : kraj,
            "drzava" : drzava_tekmovanja,
            "ime" : ime,
            "priimek" : priimek,
            "narodnost" : narodnost,
            "mesto" : mesto,
            "medalja" : medalja,
            "skupne tocke" : skupne_tocke,
            "tocke" : tocke
        })
    leto +=1

df = pd.DataFrame(vsi_podatki)
df.to_csv("rezultati.csv", index=False, encoding="utf8")