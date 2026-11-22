# Dnevnik rada na projektu

## 2026-11-20 — Inicijalizacija repozitorija i radnog okruženja
    * Kreiran lokalni projektni folder `projekat_bih` odvojen od materijala sa vježbi.
    * Postavljen i povezan udaljeni GitHub repozitorij (`projekat_uvod_u_ai`).
    * Kreirano Python virtuelno okruženje (`projekat_bih`), instalirani paketi `numpy` i `matplotlib` te generisani `.gitignore` i `requirements.txt`.
    * Kreirani početni dokumenti projekta (`README.md`, `DNEVNIK.md`, `AI_IZJAVA.md`).

## 2026-11-21 - Priprema i čišćenje ulaznih instanci (CSV)

- Kreirani i popunjeni ulazni fajlovi u folderu `data/` sa strukturom kolona `id,lanac,naziv,adresa,grad`.
- **Velika instanca (`data/instanca_velika_bingo.csv`):** prikupljeno ukupno 110 Bingo poslovnica širom Bosne i Hercegovine, izvršena provjera i uklanjanje duplikata/preklapanja (Ciljuge/Živinice-Tuzla, dupli unosi u Tuzli i Zenici), izvršena prenumeracija ID-jeva, te je zadržano **106 čistih lokacija** (ID `1`–`106`).
- **Mala instanca (`data/instanca_mala_sarajevo.csv`):** prikupljeno i objedinjeno **28 lokacija** na području Sarajeva iz više trgovačkih lanaca: Amko Komerc (10), Konzum (8), Mercator (3) i Hoše Komerc (7), sa ID-jevima `1`–`28`.
- Izvršena provjera ispravnosti zapisa i broja redova u oba CSV fajla putem terminala.

### Izvori podataka
- **Bingo:** zvanična web stranica Bingo d.o.o. Tuzla (pregled poslovnica i adresa širom BiH).
- **Amko Komerc:** zvanična web stranica Amko Komerc d.o.o. (pregled poslovnica i adresa u Sarajevu).
- **Konzum:** zvanična web stranica Konzum d.o.o. Sarajevo (pregled prodajnih jedinica i adresa).
- **Mercator:** zvanična web stranica Mercator BH d.o.o. (pregled centara/supermarketa i adresa).
- **Hoše Komerc:** zvanična web stranica Hoše Komerc d.o.o. (pregled marketa i adresa u Kantonu Sarajevo).
