# Analiza IMO

Naloga je projektno delo pri predmetu Uvod v programiranje v 1. letniku študija matematike na Fakulteti za matematiko in fiziko Univerze v Ljubljani.

## Uvod
Mednarodna matematična olimpijada (IMO) je najprestižnejže matematično tekmovanje za dijake na svetu. Vsako leto se na njej pomerijo dijaki iz preko 100 držav sveta.

## Struktura
Analizirali bomo naslednje stvari:
* Najuspešnejše države in tekmovalce
* Zmagovalne države
* Rezultati gostiteljev
* Število sodelujočih
* Leto pridružitve držav
* Uspeh Slovenije
* Težavnost nalog
* Število enakih tekmovalcev
* Primerjava z MEMO
* Primerjava z ostalimi tekmovanji

## Dokumenti
Projekt vključuje naslednje dokumente:

```text
uvp_projektna
├── README.md
├── main.py
├── scrapanje_ostalo.py
├── scrapanje_podatkov.py
├── .gitignore
├── analiza_podatkov.ipynb
└── csv_datoteke
    ├── egmo.csv
    ├── imo.csv
    ├── jbmo.csv
    └── memo.csv
```

## Uporaba
Uporabnik mora imeti naložene knjižnice zapisane v razdelku [Knjižnice](#knjižnice). Datoteko uporabnik odpre v VS Code in požene main.py, lahko pa tak korak izpusti in uporabi že naložene podatke v csv datotekah. Analizo si lahko ogleda v datoteki analiza_podatkov.ipynb.

## Knjižnice
Potrebno si je namestiti:
* [Pandas](https://pandas.pydata.org/docs/getting_started/install.html)
* [Jupyter Notebook](https://pypi.org/project/jupyter/)
* [Matplotlib](https://matplotlib.org/stable/install/index.html)
* [Requests](https://pypi.org/project/requests/)
* [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
* [Selenium](https://www.selenium.dev/documentation/webdriver/getting_started/install_library/)
* [IPython](https://ipython.org/install/)