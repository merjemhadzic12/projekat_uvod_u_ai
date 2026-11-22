import csv
from pathlib import Path

MANUAL_BY_DATASET = {
    Path("data/instanca_mala_sarajevo_geo.csv"): {
        "7": ("43.85159425162504", "18.30217889553255", None),
        "9": ("43.859431779695356", "18.43258268871922", None),
        "12": ("43.84338431168865", "18.341061620464274", None),
        "20": ("43.82849755849104", "18.344928356853565", None),
        "25": ("43.86987892838569", "18.40675159553376", None),
    },
    Path("data/instanca_velika_bingo_geo.csv"): {
        # Grupa 1: Tuzla i okolina
        "23": ("44.536438061340164", "18.69768136859372", None),
        "24": ("44.52994089117091", "18.69468665140042", None),
        "25": ("44.53100295389847", "18.692814722564375", None),
        "36": ("44.565798495625025", "18.604032422567304", None),
        "38": ("44.53666728418732", "18.68523376489334", None),
        "39": ("44.538558847598615", "18.69675527186771", None),
        "41": ("44.55249343515612", "18.692319810923046", None),
        "42": ("44.5565239141726", "18.69110977994496", None),
        "49": ("44.51388483487349", "18.58434239985757", "Tuzla"),
        # Grupa 2: Mostar, Visoko, Bihać, Travnik, Janja/Bijeljina
        "50": ("43.36527876538334", "17.82336068015692", None),
        "54": ("44.000301359404844", "18.16217182437833", None),
        "70": ("44.822851552432844", "15.86411834545895", None),
        "75": ("44.82659463546834", "15.879372207373024", None),
        "80": ("44.226226688192504", "17.648135014773178", None),
        "81": ("44.24108246885328", "17.577984210901686", None),
        "86": ("44.66457056307968", "19.249451835086695", None),
        # Grupa 3: Mostar, Živinice, Bugojno, Goražde
        "52": ("43.391527125816694", "17.83164332760306", None),
        "94": ("44.45802077384057", "18.641920949012853", None),
        "95": ("44.45736555881022", "18.642264271765722", None),
        "99": ("44.43696381060834", "18.650159242793876", None),
        "101": ("44.05490716926729", "17.435894853686495", None),
        "102": ("44.05649355203929", "17.44915543097774", None),
        "103": ("43.65964307536029", "18.97544843913107", None),
        "104": ("43.66457452715435", "18.975917093534434", None),
    },
}


def apply_manual_to_file(csv_path: Path, manual_map: dict[str, tuple[str, str, str | None]]) -> None:
    if not csv_path.exists():
        print(f"[UPOZORENJE] Fajl nije pronađen: {csv_path}")
        return

    rows: list[dict[str, str]] = []
    updated_ids: list[str] = []

    with open(csv_path, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = [c.lstrip("\ufeff") for c in (reader.fieldnames or [])]
        for raw in reader:
            row = {k.lstrip("\ufeff"): (v or "") for k, v in raw.items()}
            rid = row.get("id", "").strip()
            if rid in manual_map:
                lat, lon, new_city = manual_map[rid]
                row["lat"] = lat
                row["lon"] = lon
                row["geo_status"] = "MANUAL"
                if new_city and "grad" in row:
                    row["grad"] = new_city
                updated_ids.append(rid)
            rows.append(row)

    with open(csv_path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    total = len(rows)
    ok_cnt = sum(1 for r in rows if r.get("geo_status") == "OK")
    manual_cnt = sum(1 for r in rows if r.get("geo_status") == "MANUAL")
    fallback_cnt = sum(1 for r in rows if r.get("geo_status") == "CITY_FALLBACK")

    print(f"=== {csv_path} ===")
    print(f"Ažurirano ({len(updated_ids)}): {updated_ids}")
    print(f"Ukupno: {total} | OK: {ok_cnt} | MANUAL: {manual_cnt} | CITY_FALLBACK: {fallback_cnt}\n")


def main() -> None:
    for csv_path, manual_map in MANUAL_BY_DATASET.items():
        apply_manual_to_file(csv_path, manual_map)


if __name__ == "__main__":
    main()
