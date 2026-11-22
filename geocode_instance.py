import csv
import json
import time
import urllib.parse
import urllib.request


def geocode_address(query, user_agent="projekat_bih_student"):
    url = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode({
        "q": query,
        "format": "json",
        "limit": 1
    })
    req = urllib.request.Request(url, headers={"User-Agent": user_agent})

    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            data = json.loads(response.read().decode("utf-8"))
            if len(data) > 0:
                lat = float(data[0]["lat"])
                lon = float(data[0]["lon"])
                return lat, lon, "OK"
            else:
                return None, None, "NOT_FOUND"
    except Exception as e:
        return None, None, f"ERROR: {e}"


def get_row_id(row):
    return (row.get("id") or row.get("\ufeffid") or "").strip()


def process_csv(input_path, output_path):
    rows = []
    with open(input_path, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        base_fields = [col.lstrip("\ufeff") for col in (reader.fieldnames or [])]
        fieldnames = base_fields + ["lat", "lon", "geo_status"]

        for raw_row in reader:
            row = {k.lstrip("\ufeff"): v for k, v in raw_row.items()}
            row_id = get_row_id(row)
            naziv = (row.get("naziv") or "").strip()
            adresa = (row.get("adresa") or "").strip()
            grad = (row.get("grad") or "").strip()

            query_full = f"{adresa}, {grad}, Bosnia and Herzegovina"
            lat, lon, status = geocode_address(query_full)
            time.sleep(1.1)

            if status != "OK":
                cista_adresa = adresa.split("(")[0].replace("bb", "").strip(" ,-")
                query_fallback = f"{cista_adresa}, {grad}, Bosnia and Herzegovina"
                lat, lon, status = geocode_address(query_fallback)
                time.sleep(1.1)

            if status != "OK":
                query_city = f"{grad}, Bosnia and Herzegovina"
                lat, lon, status = geocode_address(query_city)
                if status == "OK":
                    status = "CITY_FALLBACK"
                time.sleep(1.1)

            row["lat"] = lat if lat is not None else ""
            row["lon"] = lon if lon is not None else ""
            row["geo_status"] = status
            rows.append(row)

            print(f"[{row_id}] {naziv} -> {status} ({lat}, {lon})")

    with open(output_path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for r in rows:
            writer.writerow(r)

    print(f"Gotovo! Sačuvano u: {output_path}\n")


if __name__ == "__main__":
    process_csv("data/instanca_mala_sarajevo.csv", "data/instanca_mala_sarajevo_geo.csv")
    process_csv("data/instanca_velika_bingo.csv", "data/instanca_velika_bingo_geo.csv")
