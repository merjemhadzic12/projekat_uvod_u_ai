# Dnevnik rada na projektu

### 2026-11-20 — Inicijalizacija repozitorija i radnog okruženja
    * Kreiran lokalni projektni folder `projekat_bih` odvojen od materijala sa vježbi.
    * Postavljen i povezan udaljeni GitHub repozitorij (`projekat_uvod_u_ai`).
    * Kreirano Python virtuelno okruženje (`projekat_bih`), instalirani paketi `numpy` i `matplotlib` te generisani `.gitignore` i `requirements.txt`.
    * Kreirani početni dokumenti projekta (`README.md`, `DNEVNIK.md`, `AI_IZJAVA.md`).

## 2026-11-21 - Priprema i čišćenje ulaznih instanci (CSV)

- Kreirani i popunjeni ulazni fajlovi u folderu `data/` sa strukturom kolona `id,lanac,naziv,adresa,grad`.
- **Velika instanca (`data/instanca_velika_bingo.csv`):** prikupljeno ukupno 110 Bingo poslovnica širom Bosne i Hercegovine, izvršena provjera i uklanjanje duplikata/preklapanja (Ciljuge/Živinice-Tuzla, dupli unosi u Tuzli i Zenici), izvršena prenumeracija ID-jeva, te je zadržano **106 čistih lokacija** (ID `1`–`106`).
- **Mala instanca (`data/instanca_mala_sarajevo.csv`):** prikupljeno i objedinjeno **28 lokacija** na području Sarajeva iz više trgovačkih lanaca: Amko Komerc (10), Konzum (8), Mercator (3) i Hoše Komerc (7), sa ID-jevima `1`–`28`.
- Izvršena provjera ispravnosti zapisa i broja redova u oba CSV fajla putem terminala.

## Izvori podataka
- **Bingo:** zvanična web stranica Bingo d.o.o. Tuzla (pregled poslovnica i adresa širom BiH).
- **Amko Komerc:** zvanična web stranica Amko Komerc d.o.o. (pregled poslovnica i adresa u Sarajevu).
- **Konzum:** zvanična web stranica Konzum d.o.o. Sarajevo (pregled prodajnih jedinica i adresa).
- **Mercator:** zvanična web stranica Mercator BH d.o.o. (pregled centara/supermarketa i adresa).
- **Hoše Komerc:** zvanična web stranica Hoše Komerc d.o.o. (pregled marketa i adresa u Kantonu Sarajevo).

### 2026-11-22 - Udaljenost i vremena voznje

# 1. Cilj i značaj preciznih koordinata za modeliranje logistike (VRP)
- U okviru pripreme podataka za problem rutiranja vozila (VRP) i proračun matrica cestovnih udaljenosti i vremena vožnje (OSRM) te zračnih udaljenosti (Haversine formula), svaka lokacija (skladište/depou i maloprodajni objekti) mora imati što tačnije geografske koordinate (`lat` i `lon`).
- Kada lokacija ostane na nivou rezervnog geokodiranja (`CITY_FALLBACK`, tj. centar grada), više različitih prodavnica u istom gradu dobija identične ili približne koordinate centra grada. To u daljem modeliranju može dovesti do nerealnih (skoro nultih) distanci unutar grada, pogrešnog redoslijeda posjeta i iskrivljenih vremena vožnje.
- Zbog toga je sprovedena sistematska verifikacija svih `CITY_FALLBACK` lokacija u obje instance i njihovo unapređenje na provjerene koordinate objekata uz oznaku `MANUAL`.

# 2. Automatsko geokodiranje (Nominatim / OpenStreetMap) i početni rezultati
- Za inicijalno geokodiranje korišten je Nominatim servis (OpenStreetMap) kroz modularni postupak pretrage sa rezervnom logikom:
  1. Puna adresa, naziv objekta i grad,
  2. Pojednostavljena adresa bez dodataka i oznaka `bb`,
  3. Rezervna koordinata centra grada (`CITY_FALLBACK`) kada precizna adresa/objekat nije prepoznat.
- Dobijeni rezultati su sačuvani u dvije radne datoteke:
  - `data/instanca_mala_sarajevo_geo.csv` (ukupno 28 lokacija na području Sarajeva),
  - `data/instanca_velika_bingo_geo.csv` (ukupno 106 lokacija maloprodajne mreže Bingo širom Bosne i Hercegovine).
- Prije ručnih korekcija, stanje je bilo sljedeće:
  - **Mala instanca (`instanca_mala_sarajevo_geo.csv`):** 23 lokacije sa statusom `OK` i 5 lokacija sa statusom `CITY_FALLBACK` (ID-jevi: `7`, `9`, `12`, `20`, `25`).
  - **Velika instanca (`instanca_velika_bingo_geo.csv`):** 82 lokacije sa statusom `OK` i 24 lokacije sa statusom `CITY_FALLBACK`.

# 3. Ručna verifikacija putem Google Maps-a i rad u grupama
- Za sve lokacije koje su imale status `CITY_FALLBACK` pronađene su tačne koordinate (`lat`, `lon`) na Google Maps-u na nivou samog objekta ili najbliže tačke na pripadajućoj ulici/naselju.
- **Mala instanca (Sarajevo — 5 lokacija):**
  - `7` — Amko PJ 12 (`Doglodi do br. 7`)
  - `9` — Amko PJ 15 (`Oprkanj-Brodac bb`)
  - `12` — Konzum PJ 0003 (`Senada Mandića Dende 5`)
  - `20` — Mercator Centar Dobrinja (`Bulevar Mimar Sinana 1`)
  - `25` — Hoše Market Koševo (`Patriotske lige / Braće Begić 1`)
- **Velika instanca (Bingo — 24 lokacije, podijeljene u 3 grupe radi lakše kontrole):**
  - **Grupa 1 (Tuzla i okolina — 9 lokacija):** ID-jevi `23`, `24`, `25`, `36`, `38`, `39`, `41`, `42` i `49` (Bingo PJ 035 Kiseljak kod Tuzle, uz usklađivanje naziva grada na `Tuzla`).
  - **Grupa 2 (Mostar, Visoko, Bihać, Travnik, Janja/Bijeljina — 7 ažuriranih lokacija u ovom koraku):** ID-jevi `50`, `54`, `70`, `75`, `80`, `81` i `86` (uz dodatnu provjeru i ispravku lokacije ID `52` u Mostaru nakon što je uočena koordinata iz Sarajeva).
  - **Grupa 3 (Mostar, Živinice, Bugojno, Goražde — 8 lokacija):** ID-jevi `52`, `94`, `95`, `99`, `101`, `102`, `103` i `104`.

# 4. Korištenje namjenskih Python skripti umjesto ručnog uređivanja CSV fajlova
- Umjesto direktnog ručnog mijenjanja CSV datoteka u tekstualnom editoru ili tabelarnom programu, korekcije su sprovedene izvršavanjem namjenskih Python skripti (`apply_sarajevo_manual.py`, `update_bingo_g1.py`, `update_bingo_g2.py` i `update_bingo_g3.py`).
- Ovakav pristup je obezbijedio:
  - očuvanje ispravne CSV strukture, zaglavlja i UTF-8 kodiranja (`utf-8-sig` pri čitanju, `utf-8` pri pisanju),
  - precizno ažuriranje kolona `lat`, `lon` (i po potrebi `grad`) isključivo za ciljane `id` vrijednosti,
  - postavljanje statusa `geo_status = "MANUAL"` za ručno verifikovane redove,
  - automatsku kontrolu nakon svakog koraka (ispis ažuriranih ID-jeva i provjeru preostalog broja `CITY_FALLBACK` redova).

# 5. Razlika između `OK` i `MANUAL` statusa i uticaj na dalji razvoj koda
- **`OK`** označava lokacije čije su koordinate automatski pronađene i potvrđene kroz Nominatim/OSM pretragu na osnovu adrese/objekta.
- **`MANUAL`** označava lokacije kod kojih automatska pretraga nije dala preciznu tačku (`CITY_FALLBACK`), pa su koordinate ručno očitane sa Google Maps-a i upisane u dataset.
- **Uticaj na dalji razvoj koda:** Skripte za proračun matrica udaljenosti i vremena vožnje koriste `lat` i `lon` nezavisno od toga da li je status `OK` ili `MANUAL`, dok postojanje oznake `MANUAL` omogućava da se ručno verifikovane koordinate zaštite od slučajnog prepisivanja prilikom eventualnog ponovnog pokretanja automatskog geokodiranja i olakšava reviziju kvaliteta podataka.

# 6. Završno stanje obje instance
- `data/instanca_mala_sarajevo_geo.csv`: **23 `OK` + 5 `MANUAL` = 28/28** lokacija (`0` preostalih `CITY_FALLBACK`).
- `data/instanca_velika_bingo_geo.csv`: **82 `OK` + 24 `MANUAL` = 106/106** lokacija (`0` preostalih `CITY_FALLBACK`).

# 7. Refaktorisanje i objedinjavanje skripti za ručne korekcije (`src/apply_manual_coords.py`)
- Nakon što su sve ručne korekcije uspješno sprovedene po grupama kroz pojedinačne radne skripte (`apply_sarajevo_manual.py`, `update_bingo_g1.py`, `update_bingo_g2.py` i `update_bingo_g3.py`), izvršeno je čišćenje i organizacija koda u projektu.
- Sve ručno verifikovane koordinate za obje instance objedinjene su u jednu centralizovanu i ponovljivu Python skriptu `src/apply_manual_coords.py`, dok su privremene pomoćne skripte uklonjene iz glavnog direktorijuma projekta.
- **Prednosti ovakve organizacije koda:**
  - **Jedinstven izvor istine (Single Source of Truth):** Sve ručne ispravke za obje instance (`instanca_mala_sarajevo_geo.csv` i `instanca_velika_bingo_geo.csv`) nalaze se na jednom preglednom mjestu unutar strukture `MANUAL_BY_DATASET`, organizovane po datotekama i grupama gradova.
  - **Idempotentnost i ponovljivost:** Skripta `src/apply_manual_coords.py` može se pokrenuti proizvoljan broj puta (npr. nakon ponovnog automatskog geokodiranja) i uvijek će konzistentno primijeniti sve provjerene koordinate, postaviti status `MANUAL` i ispisati kontrolni izvještaj (`OK`, `MANUAL`, `CITY_FALLBACK`).
  - **Uredna struktura repozitorijuma:** Sav izvršni kod je smješten u direktorijum `src/`, dok glavni direktorijum projekta ostaje čist i pregledan.
