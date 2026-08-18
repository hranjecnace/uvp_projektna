import requests
from bs4 import BeautifulSoup
import pandas as pd

def imo_scrape(zacetno_leto, koncno_leto):

    url = "https://www.imo-official.org/results/individual/year/"
    leto = zacetno_leto
    vsi_podatki = []

    def obstaja(element):
        if element is None:
            return None
        else:
            return element.get_text(strip=True)

    print("IMO")

    while leto < koncno_leto + 1:
        response = requests.get(url + str(leto))
        soup = BeautifulSoup(response.text, "html.parser")

        if response.status_code != 200:
            print(f"Leto {leto} ne obstaja")
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

            drzava = obstaja(vrstica.select_one(".data-table__country-full"))
            mesto = obstaja(vrstica.select_one(".data-table__section-start"))
            medalja = obstaja(vrstica.select_one(".data-table__award-circle"))
            skupne_tocke = obstaja(vrstica.select_one(".data-table__total-cell"))
            naloge = vrstica.select("td.data-table__num:not(.data-table__total-cell):not([data-value])")
            tocke = [int(td.text.strip()) if td.text else None for td in naloge][1:]


            vsi_podatki.append({
                "Leto" : leto,
                "Kraj" : kraj,
                "Število tekmovalcev" : stevilo_tekmovalcev,
                "Gostiteljica" : drzava_tekmovanja,
                "Ime" : ime,
                "Priimek" : priimek,
                "Država" : drzava,
                "Mesto" : mesto,
                "Medalja" : medalja,
                "Skupno" : skupne_tocke,
                "Točke" : tocke
            })

        print(f"Leto {leto} obdelano")
        leto +=1

    df = pd.DataFrame(vsi_podatki)
    df.to_csv("csv_datoteke/imo.csv", index=False, encoding="utf8")