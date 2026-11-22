## 20.11.2026.
Tokom izrade ovog projekta koristim AI asistenta (**Gemini**) kao podršku u radu.

# Svrha korištenja
* Pomoć pri konfiguraciji Git repozitorija i Python virtuelnog okruženja.
* Konsultacije oko organizacije strukture projekta, dokumentacije i konceptualnih pojašnjenja algoritama optimizacije.

## 2026-11-21 - Korištenje AI alata u pripremi podataka

- AI asistent je korišten kao podrška pri razvrstavanju prikupljenih poslovnica po lancima i gradovima, ujednačavanju formata zapisa u CSV fajlove (`data/instanca_velika_bingo.csv` i `data/instanca_mala_sarajevo.csv`) te provjeri eventualnih duplikata i preklapanja lokacija.
- Spiskovi poslovnica i adresa prikupljeni su sa zvaničnih web stranica odgovarajućih trgovačkih lanaca, a konačan izbor i ispravnost unesenih lokacija su pregledani i potvrđeni.

## 2026-11-22 - Nalazenje koordinata 

# Korištenje AI alata u izradi i objašnjavanju koda
- U izradi i doradi dijela koda za geokodiranje i obradu koordinata korišten je AI asistent (Gemini) uz naknadnu provjeru i verifikaciju rezultata:
  - **Skripta za geokodiranje (`geocode_instance`):** kod/logika za automatsko pretraživanje adresa, primjenu rezervnog nivoa (`CITY_FALLBACK`) i označavanje statusa lokacija (`OK` / `CITY_FALLBACK`) u CSV datotekama.
  - **Skripta za ručne koordinate (`src/apply_manual_coords.py`):** skripta generisana uz pomoć AI asistenta koja učitava geokodirane CSV datoteke, upisuje ručno pronađene koordinate (`lat`, `lon`, i po potrebi `grad`) za zadane `id` vrijednosti, postavlja status `MANUAL` i ispisuje sažetak provjere podataka.
- Sve ručno unijete koordinate su provjerene na Google Maps-u, a generisani kod je pregledan i testiran u okviru projekta.